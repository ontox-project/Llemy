import streamlit as st

st.title("Instructions")

st.subheader("Instructions")
st.markdown("""
1. Select the map of interest in the side panel. You can only select a publicly available map.
2. If you agree with our informed consent, please tick the box and record your feedback on the response provided. Make sure to tick the box before launching the chatbot, or once you have obtained an answer (not while the chatbot is processing).
3. Enter your question in the chatbot. You can select a question from the sidebar, be aware that it will immediately be sent to the chatbot.
4. The chatbot will retrieve the map data from the MINERVA API, synthetize a response and return it in the main page. Be patient, it can take a couple of minutes!
5. If you wish, ask another question. 
6. Do not forget to also fill in the general questionnaire when you are done with testing. For that purpose, make sure to record your automatically-generated ID.         
""")

st.subheader("Limitations")
st.markdown("""
- Be aware that all questions are independant: the answers will not build upon answers to previous questions.
- For optimal viewing, please disable dark mode in your browser and in the app.
""")

st.subheader("Contact details")
st.markdown("""
If you experience any technical issue please contact marie.corradi@hu.nl            
""")

st.page_link("app.py", label="⬅️ Back to Main Page", icon="🏠")