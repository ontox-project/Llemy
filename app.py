# SPDX-License-Identifier: Apache-2.0
# Copyright 2025 Marie Corradi

"""
Streamlit UI for Llemy

This module provides a user interface for interacting with Llemy,
allowing users to ask questions about lipid biology and view comprehensive answers.
"""

import streamlit as st
from datetime import datetime, timedelta
import time
import uuid
import hashlib

# Constants
EXPIRATION_MINUTES = 60
EXPIRATION_DELTA = timedelta(minutes=EXPIRATION_MINUTES)

# Utility: Expiration check
def is_key_expired(timestamp):
    return not timestamp or (datetime.now() - timestamp > EXPIRATION_DELTA)

# Utility: Logout
def clear_keys():
    for key in ["api_key_oai", "api_key_oai_time", "hash"]:
        st.session_state.pop(key, None)
    st.success("🔓 Logged out successfully!")


col1, col2 = st.columns([12, 1])
with col1:
    st.title("🔐 API Key Login")
with col2:
    if st.button("Logout"):
        clear_keys()
        st.rerun()

# Initialize missing session keys
for key in ["api_key_oai", "api_key_oai_time", "hash"]:
    if key not in st.session_state:
        st.session_state[key] = None

# Expire if keys are too old
if is_key_expired(st.session_state.api_key_oai_time):
    st.session_state.api_key_oai = None
    st.session_state.api_key_oai_time = None
    st.session_state.hash = None

# Prompt for OpenAI key if needed
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


# Prompt for unique hash
if not st.session_state.hash:
    pwd = st.text_input("Enter a password to received a unique identifier. This will not be stored. Please remember your password for future sessions, or make sure to write down all IDs in the questionnaire.", type="password")
    if pwd:
        hash_pwd = pwd + st.session_state.api_key_oai
        hash = hashlib.sha1(hash_pwd.encode("UTF-8")).hexdigest()
        st.success(f"✅ Identifier set: {hash}. Please write it down for the survey.")
        st.session_state.hash = hash
    else:
        st.warning("Please enter a password to continue")
        st.stop()
else:
    st.success(f"✅ Unique identifier is already set: {st.session_state.hash}. Please write it down for the survey.")

# Consent with resized checkbox
st.markdown("""
<style>

div[data-testid="stCheckbox"] input[type="checkbox"] {
    width: 25px;
    height: 25px;
}

div[data-testid="stCheckbox"] label {
    font-size: 22px;
}

</style>
""", unsafe_allow_html=True)

if "consent_once" not in st.session_state:
    st.session_state.consent_once = False
if "consent" not in st.session_state:
    st.session_state.consent = None
options=["Yes", "No"]
consent = st.radio(
    "I have read and agree to the informed consent information and I want to participate in the Llemy user research.",
    options,
    index=options.index(st.session_state.consent) if st.session_state.consent else None,
    horizontal=True
)
st.page_link("pages/Consent.py", label="View informed consent details", icon="📝")

st.session_state.consent = consent
if consent is not None and not st.session_state.consent_once:
    st.session_state.consent_once = True

# --- Gate content until first answer is made ---
if not st.session_state.consent_once:
    st.warning("Please answer the consent question to continue.")
    st.stop()


# Lazy import to avoid api key issues
from workflow import api_chain, MODEL_NAME
from minerva_client import MinervaClient, PROJECT_ID as DEFAULT_PROJECT_ID
from minerva_utils import * 
import json
from streamlit_extras.bottom_container import bottom
from codecarbon import EmissionsTracker

# Set up the Streamlit page
st.set_page_config(
    page_title="Llemy",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS 
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
</style>
""", unsafe_allow_html=True)

# Application header
st.markdown("<h1 class='main-header'>Llemy</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='sub-header'>An Agentic System for MINERVA Map Exploration</h3>", unsafe_allow_html=True)

# Sidebar for settings and info
with st.sidebar:
    st.image("https://static.vecteezy.com/system/resources/previews/016/314/451/large_2x/current-location-logo-world-map-location-logo-sign-map-graphic-free-png.png", width=100)
    st.page_link("app.py", label="Home", icon="🏠")
    st.page_link("pages/Consent.py", label="Informed consent form", icon="📝")
    st.page_link("pages/Instructions.py", label="Instructions", icon="📖")
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
        project_options = [p['name'] for p in st.session_state.minerva_projects]

        # Default selection logic
        default_index = 0
        if DEFAULT_PROJECT_ID in [p['project'] for p in st.session_state.minerva_projects]:
            default_index = project_options.index(
                next(p['name'] for p in st.session_state.minerva_projects if p['project'] == DEFAULT_PROJECT_ID)
            )

        selected_project_name = st.selectbox(
            "Select MINERVA Project:",
            options=project_options,
            index=default_index,
            key="selected_minerva_project_name"
        )

        selected_project = next((p for p in st.session_state.minerva_projects if p["name"] == selected_project_name),None)

        st.session_state.selected_minerva_project_id = selected_project["project"] if selected_project else None
        st.session_state.selected_machine_url = selected_project["machine_url"] if selected_project else None

    elif "minerva_projects" in st.session_state:
        st.warning("No MINERVA projects available or failed to load.")

    st.page_link(f"{st.session_state.selected_machine_url}index.html?id={st.session_state.selected_minerva_project_id}", label="View selected map", icon="🔎")


    @st.cache_resource
    def get_minerva_client(base_url: str) -> MinervaClient:
        return MinervaClient(base_url=base_url)
    
    st.markdown("---")
    st.markdown("## Example Questions")
    
    example_questions = [
        "What is the scope of this map? Give me a brief summary of the biology represented.",
        "What is the overall scope of the disease map (molecular, cellular, tissue, or organism-level)?",
        "What are the inputs, regulators, and phenotypic outputs of this system?",
        "Which triggers initiate the possible pathological response represented by this map, and which drivers maintain it?",
        "Which regulatory checkpoints limit over-activation of the pathways leading to pathological phenotypes?",
        "How does the microenvironment (inflammatory and metabolic) modulate core pathways?",
        "Are there any inter-organelle interactions (nucleus, mitochondria, membrane, ER) mapped?",
        "Which stress pathways (DNA damage, ER stress, oxidative stress, unfolded protein response) are represented in the map?",
        "Which sentinel nodes serve as proxies for system state?",
        "Does the map capture temporal aspects (e.g. early vs late disease stages)?",
        "Is the mapped system tissue- or cell-type specific? Or are there multiple tissues or cell-types represented?"
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
    
# Initialize session state for chat history
if "history" not in st.session_state:
    st.session_state.history = []

if "query" not in st.session_state:
    st.session_state.query = ""

if "feedback_log" not in st.session_state:
    st.session_state.feedback_log = []

if "page" not in st.session_state:
    st.session_state.page = "main"

if "emissions" not in st.session_state:
    st.session_state.emissions = ""

# Navigation function
def go_to(page_name):
    st.session_state.page = page_name

# Feedback function
def log_feedback(map,question, answer, feedback, response_time, emissions, hash):
    """Append feedback entry to session state and write to JSON file."""
    entry = {
        "timestamp": datetime.now().isoformat(),
        "map": map,
        "question": question,
        "answer": answer,
        "feedback": feedback,
        "response_time": response_time,
        "emissions": emissions,
        "user_hash": hash
    }
    st.session_state.feedback_log.append(entry)

    # Save feedback to JSON file
    with open("logs/feedback_log.json", "a", encoding="utf-8") as f:
        json.dump(st.session_state.feedback_log, f, ensure_ascii=False, indent=2)
        f.write("\n")


# Function to process the query
def process_query(query):
    tracker = EmissionsTracker()
    tracker.start()
    start_time = time.time()
    
    api_status_details = None
    
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

    with st.spinner(f"Retrieving knowledge from MINERVA project '{selected_project_id}' ..."):
        try:
            # Pass the selected project_id to the assistant_chain
            result = api_chain.invoke({"question": query, "project_id": selected_project_id, "machine_url":selected_machine_url})
            answer = result.get("final_answer", "Error: No response generated.")
            # Add links to MINERVA map in answer
            answer = append_reaction_links(answer, selected_machine_url, selected_project_id)
            api_status_details = result.get("api_status_details")
        except Exception as e:
            answer = f"Error processing your query: {str(e)}"
            # Ensure status details are initialized even on error to prevent NoneType issues later
            api_status_details = {"status": "error", "error_message": str(e)}

    end_time = time.time()
    response_time = end_time - start_time
    emissions = tracker.stop()
    
    return answer, api_status_details, response_time, emissions

# Main chat interface

query = st.chat_input("Ask about biology, transporters, or metabolism...", key="chat_input")

# Process query from session state (if set by example button)
if st.session_state.query and not query:
    query = st.session_state.query
    st.session_state.query = "" 

if query:
    # Add user query to history
    st.session_state.history.append({"id": str(uuid.uuid4()),"role": "user", "content": query, "api_status": None, "minerva_data": None})
    
    # Process the query
    answer, api_status, response_time, emissions = process_query(query)
    
    # Extract Minerva raw data if available from the result
    minerva_data = api_status.get("data") if api_status and api_status.get("status") == "success" else None

    # Add assistant response to history
    st.session_state.history.append({
        "id": str(uuid.uuid4()),
        "role": "assistant", 
        "content": answer, 
        "api_status": api_status, 
        "minerva_data": minerva_data,
        "response_time": response_time,
        "emissions": emissions
    })

# Display chat history
for i,message in enumerate(st.session_state.history):
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if message["role"] == "assistant":
            # Display feedback questionnaire if user consent
            if st.session_state.consent == "Yes":
                st.markdown("## 💭 Please give feedback on this answer")
                st.markdown("### Accuracy")
                accuracy_score = st.radio(
                    "Score (1 = Not Accurate at all - 5 = Very accurate):",
                    options=[1, 2, 3, 4, 5],
                    index=2,
                    key=f"accuracy_score_{i}",
                    horizontal=True
                )
                accuracy_comment = st.text_area(
                    "Comment on accuracy:",
                    placeholder="What was inaccurate?",
                    key=f"accuracy_comment_{i}"
                )

                st.markdown("### Conciseness")
                concise_score = st.radio(
                    "Score (1 = Very verbose - 5 = Very concise):",
                    options=[1, 2, 3, 4, 5],
                    index=2,
                    key=f"concise_score_{i}",
                    horizontal=True
                )

                st.markdown("### Reliability")

                reliability_score = st.radio(
                    "Score (1 = Not reliable at all - 5 = Very reliable):",
                    options=[1, 2, 3, 4, 5],
                    index=2,
                    key=f"reliability_score_{i}",
                    horizontal=True
                )
                reliability_comment = st.text_area(
                    "Comment on reliability:",
                    placeholder="How many references were unreliable?",
                    key=f"reliability_comment_{i}"
                )

                if st.button("Submit Feedback", key=f"submit_{i}"):
                    question = st.session_state.history[i - 1]["content"]
                    answer = message["content"]
                    response_time = message["response_time"]
                    emissions = message["emissions"]

                    feedback = {
                        "accuracy": {
                            "score": accuracy_score,
                            "comment": accuracy_comment.strip() or None
                        },
                        "conciseness": {
                            "score": concise_score
                        },
                        "reliability": {
                            "score": reliability_score,
                            "comment": reliability_comment.strip() or None
                        },
                    }
                    hash = st.session_state.hash
                    map = st.session_state.selected_minerva_project_id

                    log_feedback(map,question, answer, feedback, response_time, emissions,hash)
                    st.success("✅ Feedback saved, thank you!")

            # Display Minerva raw data if available for assistant messages
            if message.get("minerva_data"):
                with st.expander("Minerva API Data Retrieved", expanded=False):
                    st.text_area("Raw Data:", value=message["minerva_data"], height=200, disabled=True, key=message["id"])
            
            # Display API Call Status
            if message.get("api_status"):
                with st.expander("API Call Status Details", expanded=False):
                    st.markdown("##### Minerva API")
                    minerva_status = message["api_status"]
                    if minerva_status["status"] == "success":
                        st.success(f"Status: {minerva_status['status']}")
                    elif minerva_status["status"] == "no_data_found":
                        st.warning(f"Status: {minerva_status['status']}")
                        st.caption(f"Details: {minerva_status.get('data', 'No specific message.')}")
                    else: # error
                        st.error(f"Status: {minerva_status['status']}")
                        st.caption(f"Error: {minerva_status.get('error_message', 'Unknown error')}")


# Display a getting started message if history is empty
if not st.session_state.history:
    st.info("""
    Select a MINERVA map in the drop-down menu on the left, and ask questions about it.
    
    You can:
    - Type your own question in the input box below
    - Try one of the example questions from the sidebar
    All questions are independant from each other, Llemy uses only the data from the selected map to answer your question.
    """)

with bottom():
    st.markdown("---")

    st.markdown(f"""
    <small>This is a prototype application for research purposes only.   
    This work was developed in the context of the ONTOX project and VHP4Safety project.  
    Developped with Streamlit, LangChain and OpenAI ({MODEL_NAME}). License Apache 2.0.</small>""", unsafe_allow_html=True)

if __name__ == "__main__":
    # This will only execute when the script is run directly
    pass