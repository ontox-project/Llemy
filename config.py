# SPDX-License-Identifier: Apache-2.0
# Copyright 2025 Marie Corradi

import streamlit as st

def get_openai_api_key():
    try:
        return st.session_state.api_key_oai
    except KeyError:
        raise ValueError("OpenAI API key not set in session.")

def get_perplexity_api_key():
    try:
        return st.session_state.api_key_pplx
    except KeyError:
        raise ValueError("Perplexity API key not set in session.")
