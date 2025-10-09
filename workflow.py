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
from langchain.schema import SystemMessage, HumanMessage
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableParallel, RunnablePassthrough, RunnableLambda

# Import our custom tools
from minerva_client import minerva_map_data_retriever
#from perplexity_client import perplexity_web
from web_search import web_call
from config import get_openai_api_key


MODEL_NAME="gpt-4.1-nano" 
model_name=MODEL_NAME

def get_llm():
    return ChatOpenAI(model_name=model_name, temperature=0, api_key=get_openai_api_key()) #gpt5-nano only supports temperature of 1

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

def search_agent(question: str) -> Dict[str, Any]:
    """
    Agent that performs web research using Perplexity.
    
    Args:
        question: The user's question about physiological maps
        
    Returns:
        Dictionary with web research status and data/error
    """
    return web_call(question) # returns a dict with status, data, error_message

# Create a parallel retrieval component that runs both agents concurrently
# This part remains the same, but the output of api_agent and search_agent is now structured
#parallel_retrieval = RunnableParallel(
#    api_result=api_agent, # Renamed to avoid conflict with 'api' key in synth_agent
#    web_result=search_agent  # Renamed to avoid conflict with 'web' key in synth_agent
#)



# System prompt for the synthesis agent
#TODO: make prompt more general
SYNTH_SYSTEM_PROMPT = """
You are a senior biomedical scientist specializing in hepatic lipid metabolism.
Your task is to synthesize information from various sources to answer the user's QUESTION:
1.  **MINERVA Map Data**: This is a comprehensive dump of all reactions and elements from a specific metabolic map. It describes reactions, their participants (reactants, products, modifiers), and details about these elements (names, symbols, annotations). You will need to parse this information to find what's relevant to the QUESTION. Clearly label information derived from this source as "(Source: Minerva Map Data)". If the provided map data doesn't seem to contain information relevant to the QUESTION, state that. If there was an error retrieving this map data, that will be indicated.
2.  **Perplexity Web Research**: Provides broader scientific context and citations from web searches. Clearly label information from this source as "(Source: Perplexity Web Research)" and include any provided citations. If there was an error or no data was found from Perplexity, state that.

Based on the user's QUESTION, analyze both the detailed Minerva Map Data and the Perplexity Web Research (if included).
Create a comprehensive, scientifically rigorous answer.
If the sources provide conflicting information, prioritize peer-reviewed research and explain the discrepancy, clearly stating which source supports which claim.
Your answer should:
- Directly address the user's QUESTION.
- Be accurate and factual.
- Explain complex concepts clearly.
- Highlight areas of scientific consensus and ongoing research questions relevant to the QUESTION.
- Present information in a well-structured format with appropriate headings.
- Explicitly state the source of each piece of information or the status of the data retrieval.

Highlight first the evidence coming from the MINERVA map, then evidence coming from any other source if relevant. Do not perform web search if that is not specifically asked, restrict yourself to the context provided. 
Do not ask the user if they would like further steps in your answer, restrict yourself to providing information only.

After each statement, give a structured list of pertinent references with hyperlinks.

Remember to maintain scientific integrity and acknowledge any limitations in the available information.
"""

# Human prompt template for synthesis
SYNTH_HUMAN_TEMPLATE = """
USER QUESTION:
{question}

CONTEXT FROM MINERVA MAP DATA:
Status: {api_status}
Full Map Data (Reaction and Element Descriptions):
{api_content}
Error (if any): {api_error}

CONTEXT FROM PERPLEXITY WEB RESEARCH:
Status: {web_status}
Web Research Content:
{web_content}
Error (if any): {web_error}

Please synthesize a comprehensive answer to the USER QUESTION based on the available data from all sources, clearly attributing information and noting any retrieval issues as instructed in the system prompt. Focus on finding information within the Minerva Map Data that is relevant to the USER QUESTION. Present information from the Minerva map data first.
"""

# Create prompt template for synthesis
synth_prompt = ChatPromptTemplate.from_messages([
    ("system", SYNTH_SYSTEM_PROMPT),
    ("human", SYNTH_HUMAN_TEMPLATE),
])

def synth_agent_adapter(inputs: Dict[str, Any]) -> Dict[str, Any]:
    """
    Adapts API and Web agent outputs for synthesis with synth_agent.
    Handles API only, Web only, or combined API + Web.

    Args:
        inputs: Dictionary containing:
            - 'question': str
            - 'api_result': dict with keys 'status', 'data', 'error_message' (optional)
            - 'web_result': dict with keys 'status', 'data', 'error_message' (optional)

    Returns:
        Dictionary with:
            - 'final_answer': synthesized answer from LLM
            - 'api_status_details': original api_result dict
            - 'web_status_details': original web_result dict
            - 'minerva_raw_data': raw API data if available
    """
    question = inputs.get("question", "No question provided.")

    # --- Normalize API result ---
    api_result = inputs.get("api_result") or {
        "status": "skipped",
        "data": None,
        "error_message": None
    }

    # --- Normalize Web result ---
    web_result = inputs.get("web_result") or {
        "status": "skipped",
        "data": None,
        "error_message": None
    }

    # --- Format API content ---
    api_content = api_result.get("data") or ""
    if api_result.get("status") == "success" and api_content and not api_content.startswith("## Minerva API Results"):
        api_content = f"## Minerva API Results\n\n{api_content}"
    elif api_result.get("status") == "error":
        api_content = "Error retrieving data from Minerva API."
    elif api_result.get("status") == "no_data_found":
        api_content = f"No specific data found in Minerva API: {api_result.get('data', '')}"
    elif api_result.get("status") == "skipped":
        api_content = ""

    # --- Format Web content ---
    web_content = web_result.get("data") or ""
    if web_result.get("status") == "error":
        web_content = "Error retrieving data from Web Research."
    elif web_result.get("status") == "skipped":
        web_content = ""

    # --- Prepare prompt for synthesis ---
    prompt_data = {
        "question": question,
        "api_status": api_result.get("status", "unknown"),
        "api_content": api_content,
        "api_error": api_result.get("error_message", "None"),
        "web_status": web_result.get("status", "unknown"),
        "web_content": web_content,
        "web_error": web_result.get("error_message", "None"),
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
        "web_status_details": web_result,
        "minerva_raw_data": minerva_raw_data
    }

# Define the complete workflow
# First run MINERVA API
# Then ask if the user want to perform a web search
# --- Stage 1: API only ---
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

def web_search(x):
    try:
        return search_agent(x["question"])
    except Exception as e:
        return {"status": "error", "data": None, "error_message": str(e)}
    
# Web enrichment ---
#def combine_api_and_web(x):
#    return {
#        "question": x["question"],
#        "api_result": x["api_result"],          
#        "web_result": search_agent(x["question"])
#    }

web_chain = RunnableLambda(web_search)

if __name__ == "__main__":
    # Example usage
    test_question = "What is the role of CD36 in fatty acid uptake?"
    print(f"Testing with question: {test_question}\n")
    
    # Example invocation with a specific project_id for testing
    # Replace 'Liver_Lipid_Metabolism_Physiological_Map_August_2024' with a project ID from the list
    # result = assistant_chain.invoke({"question": test_question, "project_id": "Liver_Lipid_Metabolism_Physiological_Map_August_2024"})
    
    # Default invocation without specifying project_id
    result = assistant_chain.invoke({"question": test_question})
    
    print("\n--- API Status (Minerva) ---")
    print(f"Status: {result['api_status_details']['status']}")
    if result['api_status_details']['error_message']:
        print(f"Error: {result['api_status_details']['error_message']}")
    else:
        print(f"Data: {result['api_status_details']['data'][:200]}...") # Print snippet

    print("\n--- Web Research Status (Perplexity) ---")
    print(f"Status: {result['web_status_details']['status']}")
    if result['web_status_details']['error_message']:
        print(f"Error: {result['web_status_details']['error_message']}")
    else:
        print(f"Data: {result['web_status_details']['data'][:200]}...") # Print snippet

    print("\n--- Synthesized Answer ---")
    print(result["final_answer"])
