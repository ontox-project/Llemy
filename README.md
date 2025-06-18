# LLMapperino

A multi-agent system for answering specialized questions by combining structured knowledge from user-selected MINERVA API maps with web research via Perplexity.

## Overview

LLMapperino is a prototype application that provides an intelligent interface for querying and retrieving information from MINERVA project maps. It uses a three-agent workflow:

1. **Minerva Agent**: Fetches and processes the full map data from a user-selected MINERVA project.
2. **Perplexity Agent**: Performs deep web research using the Perplexity SONAR model.
3. **Synthesis Agent**: Combines information from both sources into comprehensive, scientifically rigorous answers.

The system is designed to answer specialized questions by reasoning over the context of the selected MINERVA map and relevant web research.

## Features

- Natural language question answering
- Integration with MINERVA API for structured map data
- **User interface for selecting a MINERVA project to query.**
- Web research using Perplexity for broader context
- Parallel execution of data retrieval for faster responses
- Chat-based Streamlit interface with example questions
- Response time tracking
- Error handling with automatic retries
- **Displays detailed API call status and raw Minerva data for transparency.**

## Requirements

- Python 3.10 or higher
- API keys for:
  - MINERVA API (via MINERVA_TOKEN in .env)
  - Perplexity API
  - OpenAI API (for the synthesis agent)

## Installation

1. Clone the repository or download the files

2. Navigate to the project directory:
   ```bash
   cd LLMapperino
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
   MINERVA_TOKEN=your_minerva_token_here
   PPLX_API_KEY=your_perplexity_api_key_here
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Usage

### Running Locally

1. Start the Streamlit application:
   ```bash
   streamlit run app.py
   ```

### Running with Docker

1. Build the Docker image from the `LLMapperino/` directory:
   ```bash
   docker build -t llmapperino .
   ```

2. Run the Docker container, mapping the port and passing your API keys as environment variables:
   ```bash
   docker run -p 8501:8501 \
     -e MINERVA_TOKEN="your_minerva_token_here" \
     -e PPLX_API_KEY="your_perplexity_api_key_here" \
     -e OPENAI_API_KEY="your_openai_api_key_here" \
     llmapperino:latest
   ```

3. The application will open in your web browser (typically at http://localhost:8501)

2. The application will open in your web browser (typically at http://localhost:8501)

3. **Select a MINERVA project from the sidebar.**
4. Enter your question in the chat input, or select one of the example questions from the sidebar.

5. The system will process your question through the multi-agent workflow using the selected MINERVA project and display a comprehensive answer.

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
LLMapperino/
├── .env                  # Environment variables (API keys)
├── requirements.txt      # Project dependencies
├── README.md             # This file
├── Dockerfile            # Docker build instructions
├── .dockerignore         # Files to ignore when building Docker image
├── minerva_client.py     # MINERVA API client
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

- Adding more specialized data sources beyond Minerva
- Implementing agent reflection for self-verification of responses
- Adding vector storage for caching and more efficient similar question handling
- Creating a function-calling version that allows for more structured API queries
- Adding visualization capabilities for molecular structures and pathways
- Implementing fully asynchronous execution for faster response times

## License

This project is intended for research and educational purposes only.

## Authors

- Ivo Djidrovski (i.djidrovski@uu.nl)
- Maia Ladeira Luiz Carlos
- Marek OSTASZEWSKI
- Marie Corradi
- Bernard Staumont

## Acknowledgements

- This project was a collaboration with Ontox and Elixir Europe.
- MINERVA API (via ontox.elixir-luxembourg.org) for providing structured data on liver lipid metabolism
- Perplexity for web research capabilities
- LangChain for the agent orchestration framework
- Streamlit for the user interface
