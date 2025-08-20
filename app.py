# SPDX-License-Identifier: Apache-2.0
# Copyright 2025 Ivo Djidrovski, Marie Corradi

"""
Streamlit UI 

This module provides a user interface for interacting with the Assistant,
allowing users to ask questions about physiological maps and view comprehensive answers.
"""

import streamlit as st
from datetime import datetime, timedelta
import time

# --- Constants
EXPIRATION_MINUTES = 20
EXPIRATION_DELTA = timedelta(minutes=EXPIRATION_MINUTES)

# --- Utility: Expiration check
def is_key_expired(timestamp):
    return not timestamp or (datetime.now() - timestamp > EXPIRATION_DELTA)

# --- Utility: Logout
def clear_keys():
    for key in ["api_key_oai", "api_key_oai_time", "api_key_pplx", "api_key_pplx_time"]:
        st.session_state.pop(key, None)
    st.success("🔓 Logged out successfully!")

# --- UI Layout: Title and logout button in one row
col1, col2 = st.columns([12, 1])
with col1:
    st.title("🔐 API Keys Login")
with col2:
    if st.button("Logout"):
        clear_keys()
        st.rerun()

# --- Initialize missing session keys
for key in ["api_key_oai", "api_key_oai_time", "api_key_pplx", "api_key_pplx_time"]:
    if key not in st.session_state:
        st.session_state[key] = None

# --- Expire if keys too old
if is_key_expired(st.session_state.api_key_oai_time):
    st.session_state.api_key_oai = None
    st.session_state.api_key_oai_time = None

if is_key_expired(st.session_state.api_key_pplx_time):
    st.session_state.api_key_pplx = None
    st.session_state.api_key_pplx_time = None

# --- Prompt for OpenAI key if needed
if not st.session_state.api_key_oai:
    api_key_oai = st.text_input("Enter your OpenAI API key", type="password")
    if api_key_oai:
        st.session_state.api_key_oai = api_key_oai
        st.session_state.api_key_oai_time = datetime.now()
        st.success("✅ OpenAI API key set")
    else:
        st.warning("Please enter your OpenAI API key to continue.")
        st.stop()
else:
    st.success("✅ OpenAI API key is already set")

# --- Prompt for Perplexity key if needed
if not st.session_state.api_key_pplx:
    api_key_pplx = st.text_input("Enter your Perplexity API key", type="password")
    if api_key_pplx:
        st.session_state.api_key_pplx = api_key_pplx
        st.session_state.api_key_pplx_time = datetime.now()
        st.success("✅ Perplexity API key set")
    else:
        st.warning("Please enter your Perplexity API key to continue.")
        st.stop()
else:
    st.success("✅ Perplexity API key is already set")



# Lazy import to avoid api key issues
from workflow import assistant_chain, MODEL_NAME
from minerva_client import MinervaClient, PROJECT_ID as DEFAULT_PROJECT_ID
from minerva_utils import get_available_projects 

# Set up the Streamlit page
st.set_page_config(
    page_title="LLMapperino",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for UX
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #2E86C1;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #5D6D7E;
    }
    .stAlert {
        background-color: #F8F9F9;
        border-color: #D5D8DC;
    }
    .info-box {
        background-color: #EBF5FB;
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    .stChatMessage {
        background-color: #F4F6F7;
        padding: 0.5rem;
        border-radius: 0.5rem;
        margin-bottom: 0.5rem;
    }
    [data-testid="stTooltipContent"] {
        font-size: 14px !important;
        color: white !important;
        background: #333 !important;
        border-radius: 6px !important;
        padding: 8px !important;
    }
</style>
""", unsafe_allow_html=True)

# Application header
st.markdown("<h1 class='main-header'>LLMapperino</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='sub-header'>A Multi-Agent System for MINERVA Map Exploration</h3>", unsafe_allow_html=True)

# Sidebar for settings and info
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2021/2021815.png", width=100)
    st.markdown("## About")
    
    st.markdown("""
    This application helps researchers explore questions about physiological maps available via the MINERVA API.
    
    It combines:
    - Structured data from a user-selected MINERVA project map
    - Web research from Perplexity
    - AI synthesis for comprehensive answers
    """)
    
    st.markdown("---")
    st.markdown("## MINERVA Project Selection")

    # Fetch and cache available projects
    if "minerva_projects" not in st.session_state:
        try:
            st.session_state.minerva_projects = get_available_projects()
        except Exception as e:
            st.error(f"Failed to fetch MINERVA projects: {str(e)}")
            st.session_state.minerva_projects = []

    # UI: project selection
    if st.session_state.minerva_projects:
        project_options = [p['project'] for p in st.session_state.minerva_projects]

        # Default selection logic
        default_index = 0
        if DEFAULT_PROJECT_ID in project_options:
            default_index = project_options.index(DEFAULT_PROJECT_ID)

        selected_project_name = st.selectbox(
            "Select MINERVA Project:",
            options=project_options,
            index=default_index,
            key="selected_minerva_project_name"
        )

        st.session_state.selected_minerva_project_id = selected_project_name
        st.session_state.selected_machine_url = next((p["machine_url"] for p in st.session_state.minerva_projects if p["project"] == selected_project_name), None)

    elif "minerva_projects" in st.session_state:
        st.warning("No MINERVA projects available or failed to load.")


    @st.cache_resource
    def get_minerva_client(base_url: str) -> MinervaClient:
        return MinervaClient(base_url=base_url)
    
    st.markdown("---")
    st.markdown("## Example Questions")
    
    #TODO: more general example questions
    example_questions = [
        "List three specific inhibitors of CD36 and tell me which general molecular processes would be mainly impaired",
        "Tell me an alternative to FATP2 if I want to test for the functionality of bile canalicular efflux",
        "What protein or protein combinations should I measure if I want to assess HDL secretion?",
        "In what organelle are fatty acids mainly stored in a cell system not expressing FABP1?",
        "What are the differential molecular processes inhibited when PPAR alpha and PPAR gamma are inhibited?",
        "Is PPAR alpha involved in the uptake of fatty acids?",
        "How is BSEP related to fatty acid beta oxidation?",
        "How does FATP1 inhibition in the liver affect the homeostasis of cholesterol?",
        "Which cell types should I include in an in vitro model of steatohepatitis?",
        "What is the abundance of FATP transporters in the liver?",
        "Is valproic acid inhibitor of OTG2?"
    ]

    def set_prompt(example_text):
        st.session_state.query = example_text

    def shorten_text(text, max_chars=50):
        return text if len(text) <= max_chars else text[:max_chars-3] + "..."
    
    for q in example_questions:
        st.button(
            label=shorten_text(q),
            help=q, 
            on_click=set_prompt,
            args=(q,)
        )

    
    st.markdown("---")
    st.markdown("### Performance Metrics")
    if "response_time" in st.session_state:
        st.metric("Last Response Time", f"{st.session_state.response_time:.2f}s")


# Initialize session state for chat history
if "history" not in st.session_state:
    st.session_state.history = []

if "query" not in st.session_state:
    st.session_state.query = ""

# Function to process the query
def process_query(query):
    start_time = time.time()
    
    api_status_details = None
    web_status_details = None
    
    # Get the selected project ID from session state
    selected_project_id = st.session_state.get("selected_minerva_project_id")
    if not selected_project_id:
        st.error("No MINERVA project selected.")
        return "Error: No MINERVA project selected.", None, None
    # Get the smachine url from session state
    selected_machine_url = st.session_state.get("selected_machine_url")
    if not selected_machine_url:
        st.error("No machine URL associated to project.")
        return "Error: No machine URL associated to project.", None, None

    with st.spinner(f"Retrieving knowledge from MINERVA project '{selected_project_id}' and performing web research..."):
        try:
            # Pass the selected project_id to the assistant_chain
            result = assistant_chain.invoke({"question": query, "project_id": selected_project_id, "machine_url":selected_machine_url})
            answer = result.get("final_answer", "Error: No response generated.")
            api_status_details = result.get("api_status_details")
            web_status_details = result.get("web_status_details")
        except Exception as e:
            answer = f"Error processing your query: {str(e)}"
            # Ensure status details are initialized even on error to prevent NoneType issues later
            api_status_details = {"status": "error", "error_message": str(e)}
            web_status_details = {"status": "error", "error_message": str(e)}

    end_time = time.time()
    st.session_state.response_time = end_time - start_time
    
    return answer, api_status_details, web_status_details

# Main chat interface
query = st.chat_input("Ask about biology, transporters, or metabolism...", key="chat_input")

# Process query from session state (if set by example button)
if st.session_state.query and not query:
    query = st.session_state.query
    st.session_state.query = ""  # Clear it after use

if query:
    # Add user query to history
    st.session_state.history.append({"role": "user", "content": query, "api_status": None, "web_status": None, "minerva_data": None})
    
    # Process the query
    answer, api_status, web_status = process_query(query)
    
    # Extract Minerva raw data if available from the result
    minerva_data = api_status.get("data") if api_status and api_status.get("status") == "success" else None

    # Add assistant response to history
    st.session_state.history.append({
        "role": "assistant", 
        "content": answer, 
        "api_status": api_status, 
        "web_status": web_status,
        "minerva_data": minerva_data # Store the raw Minerva data
    })

# Display chat history
for message in st.session_state.history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        # Display Minerva raw data if available for assistant messages
        if message["role"] == "assistant" and message.get("minerva_data"):
             with st.expander("Minerva API Data Retrieved", expanded=False):
                 st.text_area("Raw Data:", value=message["minerva_data"], height=200, disabled=True)
        
        # Display API Call Status
        if message["role"] == "assistant" and message.get("api_status"):
            with st.expander("API Call Status Details", expanded=False):
                st.markdown("##### Minerva API")
                minerva_status = message["api_status"]
                if minerva_status["status"] == "success":
                    st.success(f"Status: {minerva_status['status']}")
                    # st.text_area("Data Snippet:", value=str(minerva_status.get('data', ''))[:200]+"...", height=100, disabled=True)
                elif minerva_status["status"] == "no_data_found":
                    st.warning(f"Status: {minerva_status['status']}")
                    st.caption(f"Details: {minerva_status.get('data', 'No specific message.')}")
                else: # error
                    st.error(f"Status: {minerva_status['status']}")
                    st.caption(f"Error: {minerva_status.get('error_message', 'Unknown error')}")

                st.markdown("##### Perplexity API")
                perplexity_status = message["web_status"]
                if perplexity_status["status"] == "success":
                    st.success(f"Status: {perplexity_status['status']}")
                    # st.text_area("Data Snippet:", value=str(perplexity_status.get('data', ''))[:200]+"...", height=100, disabled=True)
                else: # error
                    st.error(f"Status: {perplexity_status['status']}")
                    st.caption(f"Error: {perplexity_status.get('error_message', 'Unknown error')}")


# Display a getting started message if history is empty
if not st.session_state.history:
    st.info("""
    ## Welcome to LLMapperino!
    
    Ask questions about the selected MINERVA project map.
    
    You can:
    - Type your own question in the input box below
    - Try one of the example questions from the sidebar
    
    The system will combine information from the MINERVA API and web research to provide comprehensive answers.
    """)

# Footer
st.markdown("---")

st.markdown(f"""
<small>This is a prototype application for research purposes only.  
Developped with Streamlit, LangChain, OpenAI ({MODEL_NAME}) and Perplexity. License Apache 2.0.</small>""", unsafe_allow_html=True)

if __name__ == "__main__":
    # This will only execute when the script is run directly
    pass
