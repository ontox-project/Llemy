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
        #self._authenticate()

    #def _authenticate(self):
    #    # enot needed for anonymous login
    #   
    #    login_payload = f"login=anonymous&password="
    #    login_headers = {"Content-Type": "application/x-www-form-urlencoded"}

    #    try:
    #        response = self.post("/doLogin", content=login_payload.encode("utf-8"), headers=login_headers)
    #        response.raise_for_status()
    #        log.info("MINERVA Client: Anonymous login successful.")
    #    except httpx.HTTPStatusError as e:
    #        log.error(f"MINERVA Client: Anonymous login failed ({e.response.status_code}).")
    #        raise ValueError("MINERVA authentication failed. Anonymous login rejected.") from e
    #    except Exception as e:
    #        log.error(f"MINERVA Client: Unexpected error during authentication: {str(e)}")
    #        raise

    #@tenacity.retry(
    #    wait=tenacity.wait_random_exponential(min=2, max=30),
    #    stop=tenacity.stop_after_attempt(3),
    #    retry=tenacity.retry_if_exception_type((httpx.HTTPError, httpx.ConnectError, httpx.TimeoutException)),
    #    reraise=True
    #)
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

        if "application/json" in response.headers.get("content-type", ""):
            return response.json()
        log.warning(f"Non-JSON response from {path}. Content-Type: {response.headers.get('content-type')}")
        return response.text

    def get_all_elements(self) -> List[Dict[str, Any]]:
        """Fetches all elements from the specified project map."""
        elements_path = f"/projects/{self.project_id}/models/{MAP_ID}/bioEntities/elements/"
        log.info(f"Fetching all elements from: {elements_path}")
        elements_data = self._call_api("GET", elements_path)
        return elements_data if isinstance(elements_data, list) else []

    def get_all_reactions(self) -> List[Dict[str, Any]]:
        """Fetches all reactions from the specified project map."""
        reactions_path = f"/projects/{self.project_id}/models/{MAP_ID}/bioEntities/reactions/"
        log.info(f"Fetching all reactions from: {reactions_path}")
        reactions_data = self._call_api("GET", reactions_path)
        return reactions_data if isinstance(reactions_data, list) else []

# --- Helper Functions for Formatting ---

def simplify_element_description(element_id: int, elements_df: pd.DataFrame) -> str:
    """Creates a simplified description for an element, inspired by R code."""
    if elements_df.empty or 'id' not in elements_df.columns:
        return f"Element_ID_{element_id}"
    
    # Use .loc for potentially faster lookup if 'id' is index, or boolean indexing otherwise
    element_rows = elements_df[elements_df['id'] == element_id]
    if element_rows.empty:
        return f"Element_ID_{element_id}_NotFound"
    
    element_series = element_rows.iloc[0]

    name = element_series.get('name', 'UnknownName')
    
    # Handle potential non-list or None values gracefully
    former_symbols_list = element_series.get('formerSymbols', [])
    former_symbols = ",".join(str(s) for s in former_symbols_list if s) if isinstance(former_symbols_list, list) else ""
    
    references_list = element_series.get('references', [])
    annotations = ""
    if isinstance(references_list, list) and references_list:
        ref_strings = []
        for ref in references_list:
             # Check if ref is a dict and has the required keys
             if isinstance(ref, dict) and ref.get('type') and ref.get('resource'):
                 ref_strings.append(f"{ref['type']}:{ref['resource']}")
        if ref_strings:
            annotations = ",".join(ref_strings)

    desc = f"name: {name}"
    if former_symbols:
        desc += f" (formerSymbols: {former_symbols})"
    if annotations:
        desc += f" (annotations: {annotations})"
    return desc

def format_reactions_for_llm(reactions_list: List[Dict[str, Any]], elements_df: pd.DataFrame) -> str:
    """Formats reactions into a detailed text blob for LLM processing, including reaction references."""
    if not reactions_list:
        return "No reactions found in the map."

    reaction_descriptions = []
    for reaction in reactions_list:
        reaction_id = reaction.get('id', 'UnknownReactionID')
        reaction_type = reaction.get('type', 'UnknownType')
        name = reaction.get('name', '')
        
        # Build description line by line
        lines = [f"Reaction ID {reaction_id} (Name: '{name}', Type: {reaction_type}):"]

        # Format Participants
        for participant_type in ["reactants", "products", "modifiers"]:
            participants = reaction.get(participant_type, [])
            participant_descs = []
            if participants: # Ensure participants is a list and not empty
                for p_info in participants:
                    # Check if p_info is a dict and has 'aliasId'
                    if isinstance(p_info, dict) and 'aliasId' in p_info:
                         # Ensure aliasId is an integer before lookup
                         try:
                             alias_id = int(p_info['aliasId'])
                             participant_descs.append(simplify_element_description(alias_id, elements_df))
                         except (ValueError, TypeError):
                             log.warning(f"Invalid aliasId format in reaction {reaction_id}, participant: {p_info}")
                             participant_descs.append("InvalidElementID")
                    # Fallback if participant is just an int ID (less likely based on R code)
                    elif isinstance(p_info, int): 
                        participant_descs.append(simplify_element_description(p_info, elements_df))
                    else:
                         log.warning(f"Unexpected participant format in reaction {reaction_id}: {p_info}")
                         participant_descs.append("UnknownParticipantFormat")

            if participant_descs:
                 lines.append(f"  {participant_type.capitalize()}: {'; '.join(participant_descs)}")
            else:
                lines.append(f"  {participant_type.capitalize()}: None")

        # Format Reaction-Level References (inspired by R code)
        reaction_refs_list = reaction.get('references', [])
        reaction_ref_strings = []
        if isinstance(reaction_refs_list, list) and reaction_refs_list:
            for ref in reaction_refs_list:
                if isinstance(ref, dict) and ref.get('type') and ref.get('resource'):
                    reaction_ref_strings.append(f"{ref['type']}:{ref['resource']}")
        
        # Append reference string if references were found
        if reaction_ref_strings:
            # Use " and " as separator like R code's paste(collapse = " and ") might imply
            ref_text = " and ".join(reaction_ref_strings)
            # Use slightly different phrasing for clarity and to ensure it's appended
            lines.append(f"  (References: {ref_text})") 
            
        reaction_descriptions.append("\n".join(lines)) # Join lines for this reaction description
    
    return "\n---\n".join(reaction_descriptions) # Join all reaction descriptions



def format_link(base_url, project_id, reactions_list):
    reactions_string = "%3B".join(map(str, reactions_list))
    return f"{base_url}/minerva/index.html?id={project_id}&perfectMatch=true&searchValue={reactions_string}"


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
        
        # Convert elements to DataFrame for efficient lookup
        elements_df = pd.DataFrame(all_elements)
        if 'id' not in elements_df.columns:
             log.error("Element data missing 'id' column.")
             client.close()
             return {"status": "error", "data": None, "error_message": "Element data format error: missing 'id'."}
        elements_df['id'] = elements_df['id'].astype(int) # Ensure ID is integer for matching

        log.info(f"Fetched {len(all_elements)} elements. Fetching all reactions for project ID: {effective_project_id}...")
        all_reactions = client.get_all_reactions()
        if not all_reactions:
            log.warning(f"No reactions retrieved from the map for project ID: {effective_project_id}.")
            client.close()
            return {"status": "no_data_found", "data": f"No reactions found in the map for project ID: {effective_project_id} (though elements were found).", "error_message": None}

        log.info(f"Fetched {len(all_reactions)} reactions. Formatting for LLM...")
        formatted_data = format_reactions_for_llm(all_reactions, elements_df)
        client.close()
        
        return {"status": "success", "data": formatted_data, "error_message": None}
    except Exception as e:
        log.exception(f"Critical error during Minerva map data retrieval")
        # Ensure client is closed even if error occurs after instantiation
        try:
            client.close()
        except NameError: # client might not be defined if error happened early
            pass 
        except Exception as close_e:
            log.error(f"Error closing MinervaClient after exception: {close_e}")
            
        return {"status": "error", "data": None, "error_message": f"Failed to retrieve/process Minerva map data: {str(e)}"}

if __name__ == "__main__":
    print("--- Testing Minerva API Client (Full Map Data Retrieval with Reaction Refs) ---")
    
    # Example of how to invoke with a specific project ID for testing
    # Replace 'your_test_project_id' with an actual project ID from the list
    # result = minerva_map_data_retriever.invoke({"project_id": "Liver_Lipid_Metabolism_Physiological_Map_August_2024"})
    
    # Default invocation without specifying project_id (uses PROJECT_ID constant)
    result = minerva_map_data_retriever.invoke({}) 
    
    print(f"\nStatus: {result['status']}")
    if result['status'] == 'success':
        print(f"\nFirst 1500 characters of formatted data:\n{result['data'][:1500]}...") # Show more data
    elif result['error_message']:
        print(f"\nError: {result['error_message']}")
    else:
        print(f"\nData: {result['data']}")
    
    log.info("Test finished. Check logs for MINERVA Client authentication messages.")
