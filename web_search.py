from openai import OpenAI
import httpx
import tenacity
from typing import Dict, Any
from langchain.tools import tool
from config import get_openai_api_key
from openai import OpenAI


def web_client(prompt, model="gpt-5",reasoning_effort="low", temperature =0.2):
    client = OpenAI(api_key=get_openai_api_key())

    response = client.responses.create(
        model=model,
        reasoning={"effort": reasoning_effort},
        tools=[
            {
            "type": "web_search",
            "filters": {
                "allowed_domains": [
                "pubmed.ncbi.nlm.nih.gov",
                "clinicaltrials.gov",
                "www.who.int",
                "www.cdc.gov",
                "www.fda.gov",
                "pubchem.ncbi.nlm.nih.gov",
                "pmc.ncbi.nlm.nih.gov"
                ]
                }
            }
        ],
        tool_choice="auto",
        include=["web_search_call.action.sources"],
        input=prompt
        )
    return response


def enhance_query(question: str) -> str:
    """
    Enhance the original question to get better research results.
    
    Args:
        question: Original question
        
    Returns:
        Enhanced query for better research results
    """
    enhanced_question = (
        f"""Conduct a thorough scientific literature search on this topic: {question}. 
        Focus on peer-reviewed sources in biochemistry, biomedicine and toxicology. 
        Include both established knowledge and recent advances. 
        Provide a comprehensive, scientifically accurate answer with references."""
    )

    return enhanced_question

@tool("web_call", return_direct=True)
def web_call(question: str) -> str:
    """
    Perform web research on physiological maps questions to complete maps answers
    Limited to reliable sources.
    """
    try:
        enhanced_query = enhance_query(question)
        data = web_client(enhanced_query)
        
        # Add a header to clarify this is from web research
        formatted_data = f"## Web Research Results (GPT-5)\n\n{data.output_text}"
        return {"status": "success", "data": formatted_data, "error_message": None}
    except httpx.HTTPStatusError as e:
        return {"status": "error", "data": None, "error_message": f"OpenAI API request failed: {e.response.status_code} - {e.response.text}"}
    except httpx.RequestError as e:
        return {"status": "error", "data": None, "error_message": f"OpenAI API request error: {str(e)}"}
    except Exception as e:
        return {"status": "error", "data": None, "error_message": f"Error performing web research: {str(e)}"}

if __name__ == "__main__":
    # Example usage
    result = web_search("What is the role of CD36 in fatty acid uptake?")
    print(result)