# SPDX-License-Identifier: Apache-2.0
# Copyright 2025 Ivo Djidrovski - Marek Ostaszewski - Marie Corradi

"""
MINERVA API Client (Refactored for Full Map Data Retrieval)

This module provides a client for interacting with the MINERVA API.
It fetches all elements and reactions from a specified project map and formats
them into a descriptive text for LLM processing, including reaction references.
Handles authentication via anonymous login with fallback to a pre-saved token.
"""

#import os
import httpx
import tenacity
#import functools
from typing import Dict, List, Any, Optional
from dotenv import load_dotenv
from langchain.tools import tool
import logging
import requests
import pandas as pd
from minerva_utils import *
import json

# Setup logging
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


# API Constants
BASE_URL = "https://ontox.elixir-luxembourg.org/minerva/"
PROJECT_ID = "Liver_Lipid_Metabolism_Physiological_Map_August_2024"
MAP_ID = "*" # Search across all maps in the chosen project


class MinervaClient(httpx.Client):
    def __init__(self, base_url: str = BASE_URL, project_id: str = PROJECT_ID, *args, **kwargs):
        self.base_url = base_url.rstrip("/")+ "/api"
        self.project_id = project_id
        super().__init__(*args, base_url=self.base_url, follow_redirects=True, timeout=60, **kwargs)

    def _call_api(self, method: str, path: str, **kwargs) -> Any:
        log.debug(f"Calling MINERVA API: {method} {path} with params {kwargs.get('params')}")
        params = kwargs.pop("params", {})

        # Optionally inject project ID
        if self.project_id and 'projectId' not in path and 'projectId' not in params:
            if path.startswith(("/projects/", "/models/", "/bioEntities/")) or "/models/" in path:
                pass  # Do not auto-inject
            elif path.startswith(("/elements", "/reactions")):
                params["projectId"] = self.project_id

        response = self.request(method, path, params=params, **kwargs)
        response.raise_for_status()
        return response

    def get_all_elements(self) -> List[Dict[str, Any]]:
        """Fetches all elements from the specified project map."""
        elements_path = f"{self.base_url}/projects/{self.project_id}/models/{MAP_ID}/bioEntities/elements/"
        log.info(f"Fetching all elements from: {elements_path}")
        elements_data = requests.get(elements_path, cookies={"MINERVA_AUTH_TOKEN": ''})
        elements= elements_data.text
        return json.loads(elements)

    def get_all_reactions(self) -> List[Dict[str, Any]]:
        """Fetches all reactions from the specified project map."""
        reactions_path = f"{self.base_url}/projects/{self.project_id}/models/{MAP_ID}/bioEntities/reactions/"
        log.info(f"Fetching all reactions from: {reactions_path}")
        reactions_data = requests.get(reactions_path, cookies={"MINERVA_AUTH_TOKEN": ''})
        reactions = reactions_data.text
        return json.loads(reactions)


### Helper functions to transform MINERVA map data (elements and reactions) into a knowledge graph
def simple_minerva_query_kg(elements_data, reactions_data, e_props=None, r_props=None):
    def select_parameters_from_list(source_list, parameters_to_select):
        ret = {}
        for param_id in parameters_to_select:
            if source_list[param_id]:
               ret[param_id] = source_list[param_id]

        if ret.get("references"):
            ret["references"] = [{"database": ref["type"],
                                  "database_id": ref["resource"]} for ref in ret["references"]]

        return ret

    reduced_element_data = elements_data
    if e_props is not None:
        reduced_element_data = [select_parameters_from_list(el, e_props) for el in elements_data]

    reduced_reaction_data = reactions_data
    if r_props is not None:
        reduced_reaction_data = [select_parameters_from_list(rc, r_props) for rc in reactions_data]

    def redefine_reaction(r):
        r["reactants"] = [{"node_id": reactant["aliasId"]} for reactant in r["reactants"]]
        r["sources"] = r.pop("reactants")
        r["products"] = [{"node_id": product["aliasId"]} for product in r["products"]]
        r["targets"] = r.pop("products")
        if r.get("modifiers"):
            r["modifiers"] = [{"node_id": modifier["aliasId"],
                               "modification_type": modifier["type"]} for modifier in r["modifiers"]]
        return r

    reduced_reaction_data = [redefine_reaction(r) for r in reduced_reaction_data]

    return reduced_element_data, reduced_reaction_data





@tool("minerva_map_data_retriever")
def minerva_map_data_retriever(question: Optional[str] = None, project_id: Optional[str] = PROJECT_ID, machine_url: Optional[str] = BASE_URL) -> Dict[str, Any]:
    """
    Fetches all elements and reactions from the specified MINERVA project map
    and formats them into a comprehensive text description including reaction references.
    This tool provides the full context of the map for LLM reasoning.
    
    Args:
        question: (Optional) The user's question, currently not used for filtering.
        project_id: (Optional) The ID of the MINERVA project to fetch data from. Defaults to PROJECT_ID constant.
        
    Returns:
        Dictionary with status ('success', 'error', 'no_data_found'),
        data (formatted string of all reactions or None), and error_message (string or None).
    #TODO: add filter based on query to limit context passed to synthesizer
    """
    try:
        client = MinervaClient(base_url=machine_url, project_id=project_id)
        effective_project_id = client.project_id if project_id else PROJECT_ID
        log.info(f"Fetching all elements for project ID: {effective_project_id}...")
        all_elements = client.get_all_elements()
        if not all_elements:
            log.warning(f"No elements retrieved from the map for project ID: {effective_project_id}.")
            client.close()
            return {"status": "no_data_found", "data": f"No elements found in the map for project ID: {effective_project_id}.", "error_message": None}

        log.info(f"Fetched {len(all_elements)} elements. Fetching all reactions for project ID: {effective_project_id}...")
        all_reactions = client.get_all_reactions()
        if not all_reactions:
            log.warning(f"No reactions retrieved from the map for project ID: {effective_project_id}.")
            client.close()
            return {"status": "no_data_found", "data": f"No reactions found in the map for project ID: {effective_project_id} (though elements were found).", "error_message": None}

        log.info(f"Fetched {len(all_reactions)} reactions. JSON Formatting for LLM...")
        formatted_data = simple_minerva_query_kg(all_elements, all_reactions,
                                   e_props=["id", "name", "synonyms", "type", "references"],
                                   r_props=["id", "type", "reactants", "products", "modifiers", "references"])
        client.close()
        
        return {"status": "success", "data": formatted_data, "error_message": None}
    except Exception as e:
        log.exception(f"Critical error during Minerva map data retrieval")
        # Ensure client is closed even if error occurs after instantiation
        try:
            client.close()
        except NameError: 
            pass 
        except Exception as close_e:
            log.error(f"Error closing MinervaClient after exception: {close_e}")
            
        return {"status": "error", "data": None, "error_message": f"Failed to retrieve/process Minerva map data: {str(e)}"}

if __name__ == "__main__":
    print("--- Testing Minerva API Client (Full Map Data Retrieval with Reaction Refs) ---")

    result = minerva_map_data_retriever.invoke({}) 
    
    print(f"\nStatus: {result['status']}")
    if result['status'] == 'success':
        print(f"\nFirst 1500 characters of formatted data:\n{result['data'][:1500]}...")
    elif result['error_message']:
        print(f"\nError: {result['error_message']}")
    else:
        print(f"\nData: {result['data']}")
    
    log.info("Test finished. Check logs for MINERVA Client authentication messages.")
