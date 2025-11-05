import streamlit as st

st.title("Informed Consent Form for Llemy, an AI assistant to explore physiological/disease maps")
st.write("Llemy is being developed by the following research institutions: HU Utrecht University of Applied Sciences, University of Luxemburg, University de Liege, Utrecht University")

# Example numbered list of participant responsibilities
st.markdown("""
1. I declare that I have been clearly informed about the nature, method and purpose of the research and about the commitment involved. I was given the opportunity to ask questions; there were all answered to my satisfaction. I was given enough time to decide whether or not to participate. 
2. I know that the research data and results will only be collected, retained, used and disclosed (to third parties) anonymously and confidentially. 
3. I consent to the anonymous collection, retention and use of my data to answer the research question for this research. 
4. I consent to the anonymous and confidential disclosure of the research data and results to third parties. 
5. I want to participate in this research and I know that my data will be processed anonymously. 
6. I know that participation is voluntary and that I can withdraw from the research at any time. I do not have to give any reason for my decision. I realise that all data already collected if I withdraw will still be used. 
""")

st.page_link("app.py", label="⬅️ Back to Main Page", icon="🏠")


