# Fatty Acid Assistant

A multi-agent system for answering specialized questions about hepatic lipid biology by combining structured knowledge from the Ontox/MINERVA API with web research via Perplexity.

## Overview

Fatty Acid Assistant is a prototype application that provides an intelligent interface for querying and retrieving information about liver lipid metabolism. It uses a three-agent workflow:

1. **Ontox Agent**: Queries the MINERVA API for structured data about proteins, genes, and chemicals involved in lipid metabolism
2. **Perplexity Agent**: Performs deep web research using the Perplexity SONAR model
3. **Synthesis Agent**: Combines information from both sources into comprehensive, scientifically rigorous answers

The system is designed to answer specialized questions about lipid transporters, nuclear receptors, and metabolic processes in the liver.

## Features

- Natural language question answering about lipid biology
- Integration with specialized Ontox MINERVA API for structured data
- Web research using Perplexity for broader context
- Parallel execution of data retrieval for faster responses
- Chat-based Streamlit interface with example questions
- Response time tracking
- Error handling with automatic retries

## Requirements

- Python 3.10 or higher
- API keys for:
  - Ontox MINERVA API
  - Perplexity API
  - OpenAI API (for the synthesis agent)

## Installation

1. Clone the repository or download the files

2. Navigate to the project directory:
   ```bash
   cd fatty-acid-assistant
   ```

3. Set up a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Create a `.env` file with your API keys:
   ```
   ONTOX_TOKEN=your_ontox_token_here
   PPLX_API_KEY=your_perplexity_api_key_here
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Usage

1. Start the Streamlit application:
   ```bash
   streamlit run app.py
   ```

2. The application will open in your web browser (typically at http://localhost:8501)

3. Enter your question in the chat input, or select one of the example questions from the sidebar

4. The system will process your question through the multi-agent workflow and display a comprehensive answer

## Example Questions

- List three specific inhibitors of CD36 and tell me which general molecular processes would be mainly impaired
- Tell me an alternative to FATP2 if I want to test for the functionality of bile canalicular efflux
- What protein or protein combinations should I measure if I want to assess HDL secretion?
- In what organelle are fatty acids mainly stored in a cell system not expressing FABP1?
- What are the differential molecular processes inhibited when PPAR alpha and PPAR gamma are inhibited?
- Is PPAR alpha involved in the uptake of fatty acids?
- How is BSEP related to fatty acid beta oxidation?
- How does FATP1 inhibition in the liver affect the homeostasis of cholesterol?
- Which cell types should I include in an in vitro model of steatohepatitis?
- What is the abundance of FATP transporters in the liver?
- Is valproic acid inhibitor of OTG2?

## Project Structure

```
fatty-acid-assistant/
├── .env                  # Environment variables (API keys)
├── requirements.txt      # Project dependencies
├── README.md             # This file
├── ontox_client.py       # Ontox MINERVA API client
├── perplexity_client.py  # Perplexity API client
├── workflow.py           # LangChain agent workflow
└── app.py                # Streamlit UI application
```

## Troubleshooting

- **Missing API Keys**: Ensure all API keys are correctly set in the `.env` file
- **Module Import Errors**: Verify that all dependencies are installed correctly
- **API Timeouts**: The application includes retry logic for API calls, but persistent timeouts may indicate API service issues
- **Memory Issues**: For complex queries, ensure your system has sufficient memory

## Future Improvements

- Adding more specialized data sources beyond Ontox
- Implementing agent reflection for self-verification of responses
- Adding vector storage for caching and more efficient similar question handling
- Creating a function-calling version that allows for more structured API queries
- Adding visualization capabilities for molecular structures and pathways
- Implementing fully asynchronous execution for faster response times

## License

This project is intended for research and educational purposes only.

## Acknowledgements

- Ontox MINERVA API for providing structured data on liver lipid metabolism
- Perplexity for web research capabilities
- LangChain for the agent orchestration framework
- Streamlit for the user interface
