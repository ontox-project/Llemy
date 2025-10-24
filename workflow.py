# SPDX-License-Identifier: Apache-2.0
# Copyright 2025 Ivo Djidrovski, Marie Corradi

"""
#TODO: more general description
Workflow Module 

This module defines the LangChain workflow that orchestrates the multi-agent system
for answering physiological maps questions using the MINERVA API and Perplexity web research.
"""

from typing import Dict, Any
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnablePassthrough

# Import our custom tools
from minerva_client import minerva_map_data_retriever
from minerva_utils import *
from config import get_openai_api_key


MODEL_NAME="gpt-4.1-nano" 
model_name=MODEL_NAME

def get_llm():
    return ChatOpenAI(model_name=model_name, temperature=0, api_key=get_openai_api_key())

def api_agent(inputs: Dict[str, Any]) -> Dict[str, str]:
    """
    Agent that queries the Minerva API for information.
    
    Args:
        inputs: Dictionary containing the user's question and selected project_id.
                Expected keys: 'question', 'project_id', 'machine_url'.
        
    Returns:
        Dictionary with API response status and data/error
    """
    question = inputs.get("question")
    project_id = inputs.get("project_id")
    machine_url = inputs.get("machine_url")
    return minerva_map_data_retriever.invoke({"question": question, "project_id": project_id, "machine_url": machine_url})


# System prompt for the synthesis agent
#TODO: make prompt more general
SYNTH_SYSTEM_PROMPT = """
You are a senior biomedical scientist specializing in hepatic lipid metabolism.
Your task is to synthesize information from MINERVA Map data to answer the user's QUESTION.
**MINERVA Map Data** is a comprehensive dump of all reactions and elements from a specific metabolic map. It describes reactions, their participants (reactants, products, modifiers), and details about these elements (names, symbols, annotations). You will need to parse this information to find what's relevant to the QUESTION. Clearly label information derived from this source as "(Source: Minerva Map Data)". If the provided map data doesn't seem to contain information relevant to the QUESTION, state that. If there was an error retrieving this map data, that will be indicated.

Based on the user's QUESTION, analyze the detailed Minerva Map Data.
Create a comprehensive, scientifically rigorous answer.
Your answer should:
- Directly address the user's QUESTION.
- Be accurate and factual.
- Explain complex concepts clearly.
- Present information in a well-structured format with appropriate headings and clear separations between sections.
- Explicitly state the source of each piece of information or the status of the data retrieval.

Do not perform web search, restrict yourself to the context provided. 
Do not ask the user if they would like further steps in your answer, restrict yourself to providing information only.

After each statement, give a structured list of pertinent reaction references from the map.
"""

# Human prompt template for synthesis
SYNTH_HUMAN_TEMPLATE = """
USER QUESTION:
{question}

CONTEXT FROM MINERVA MAP DATA:
Status: {api_status}
Relevant Map Data (Reaction and Element Descriptions in text blob format):
{api_content}
Error (if any): {api_error}

Please synthesize a comprehensive answer to the USER QUESTION based on the available data from the map and noting any retrieval issues as instructed in the system prompt. Do not search the web for additional information.
"""

# Create prompt template for synthesis
synth_prompt = ChatPromptTemplate.from_messages([
    ("system", SYNTH_SYSTEM_PROMPT),
    ("human", SYNTH_HUMAN_TEMPLATE),
])

def synth_agent_adapter(inputs: Dict[str, Any]) -> Dict[str, Any]:
    """
    Adapts API output for synthesis with synth_agent.

    Args:
        inputs: Dictionary containing:
            - 'question': str
            - 'api_result': dict with keys 'status', 'data', 'error_message' (optional)

    Returns:
        Dictionary with:
            - 'final_answer': synthesized answer from LLM
            - 'api_status_details': original api_result dict
            - 'minerva_raw_data': raw API data if available
    """
    question = inputs.get("question", "No question provided.")

    # --- Normalize API result ---
    api_result = inputs.get("api_result") or {
        "status": "skipped",
        "data": None,
        "error_message": None
    }


    # --- Format API content ---
    api_content = api_result.get("data") or ""
    if api_result.get("status") == "success" and api_content :
        api_content = f"## Minerva API Results\n\n{api_content}"
    elif api_result.get("status") == "error":
        api_content = "Error retrieving data from Minerva API."
    elif api_result.get("status") == "no_data_found":
        api_content = f"No specific data found in Minerva API: {api_result.get('data', '')}"
    elif api_result.get("status") == "skipped":
        api_content = ""


    # --- Prepare prompt for synthesis ---
    prompt_data = {
        "question": question,
        "api_status": api_result.get("status", "unknown"),
        "api_content": api_content,
        "api_error": api_result.get("error_message", "None")
    }

    # --- Generate the synthesis ---
    llm = get_llm()
    response_chain = synth_prompt | llm
    synthesis_result = response_chain.invoke(prompt_data)

    # --- Extract raw API data if available ---
    minerva_raw_data = api_result.get("data") if api_result.get("status") == "success" else None

    # --- Return consistent dict ---
    return {
        "final_answer": synthesis_result.content,
        "api_status_details": api_result,
        "minerva_raw_data": minerva_raw_data
    }

# Define the complete workflow, API only
base = RunnablePassthrough.assign(
    question=lambda x: x.get("question"),
    project_id=lambda x: x.get("project_id"),
    machine_url=lambda x: x.get("machine_url"),
)

with_api = base.assign(
    api_result=lambda x: api_agent({
        "question": x.get("question"),
        "project_id": x.get("project_id"),
        "machine_url": x.get("machine_url"),
    })
)

api_chain = with_api | synth_agent_adapter

if __name__ == "__main__":
    result = assistant_chain.invoke({"question": test_question})
    
    print("\n--- API Status (Minerva) ---")
    print(f"Status: {result['api_status_details']['status']}")
    if result['api_status_details']['error_message']:
        print(f"Error: {result['api_status_details']['error_message']}")
    else:
        print(f"Data: {result['api_status_details']['data'][:200]}...") 

    print("\n--- Synthesized Answer ---")
    print(result["final_answer"])
