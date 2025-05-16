"""
Perplexity SONAR API Client

This module provides a client for interacting with the Perplexity API,
specifically focused on performing web research for lipid biology questions.
"""

import os
import httpx
import tenacity
from typing import Dict, Any
from dotenv import load_dotenv
from langchain.tools import tool

# Load environment variables from .env file
load_dotenv()

# API Constants
API_URL = "https://api.perplexity.ai/chat/completions"
API_KEY = os.environ.get("PPLX_API_KEY", "")

@tenacity.retry(
    wait=tenacity.wait_random_exponential(min=1, max=20),
    stop=tenacity.stop_after_attempt(3),
    retry=tenacity.retry_if_exception_type((httpx.HTTPError, httpx.ConnectError, httpx.TimeoutException)),
    reraise=True
)
def pplx_call(prompt: str, model="sonar-pro", temperature=0.2) -> str:
    """
    Make a request to the Perplexity SONAR API.
    
    Args:
        prompt: The prompt to send to Perplexity
        model: The model to use (default: sonar-medium-online)
        temperature: The temperature parameter (default: 0.2)
        
    Returns:
        The text response from Perplexity
        
    Raises:
        httpx.HTTPError: If the HTTP request fails
    """
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": temperature,
        "top_p": 1,
        "stream": False
    }
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    with httpx.Client(timeout=40) as client:
        response = client.post(
            API_URL,
            headers=headers,
            json=payload
        )
        response.raise_for_status()
        result = response.json()
        
        content = result["choices"][0]["message"]["content"]
        citations = result.get("citations", [])
        
        if citations:
            formatted_citations = "\n\n**Sources:**\n" + "\n".join([f"- {cit}" for cit in citations])
            content += formatted_citations
            
        return content

def enhance_query(question: str) -> str:
    """
    Enhance the original question to get better research results.
    
    Args:
        question: Original question about lipid biology
        
    Returns:
        Enhanced query for better research results
    """
    scientific_context = (
        "Conduct a thorough scientific literature search on this topic. "
        "Focus on peer-reviewed sources in biochemistry, hepatology, and lipid metabolism. "
        "Include both established knowledge and recent advances. "
        "Provide a comprehensive, scientifically accurate answer with references."
    )
    
    # Enhance certain terms with domain-specific modifiers
    enhancements = {
        "cd36": "CD36 fatty acid translocase",
        "fatp": "FATP fatty acid transport protein",
        "ppar": "PPAR peroxisome proliferator-activated receptor",
        "fatty acid": "fatty acid metabolism liver",
        "lipid": "lipid metabolism hepatic",
        "bile": "bile acid transport liver",
    }
    
    enhanced_question = question
    for term, expansion in enhancements.items():
        if term in question.lower() and term != expansion:
            enhanced_question = enhanced_question.replace(term, expansion)
    
    # Combine the question with scientific context
    return f"{enhanced_question}\n\n{scientific_context}"

@tool("perplexity_web", return_direct=True)
def perplexity_web(question: str) -> str:
    """
    Perform deep web research on lipid biology questions using Perplexity's SONAR model.
    Returns citation-rich answers based on current scientific literature.
    
    Args:
        question: A question about lipid biology, transporters, or metabolism
        
    Returns:
        Comprehensive web research results with citations
    """
    try:
        enhanced_query = enhance_query(question)
        data = pplx_call(enhanced_query)
        
        # Add a header to clarify this is from web research
        formatted_data = f"## Web Research Results (Perplexity API)\n\n{data}"
        return {"status": "success", "data": formatted_data, "error_message": None}
    except httpx.HTTPStatusError as e:
        return {"status": "error", "data": None, "error_message": f"Perplexity API request failed: {e.response.status_code} - {e.response.text}"}
    except httpx.RequestError as e:
        return {"status": "error", "data": None, "error_message": f"Perplexity API request error: {str(e)}"}
    except Exception as e:
        return {"status": "error", "data": None, "error_message": f"Error performing web research: {str(e)}"}

if __name__ == "__main__":
    # Example usage
    # Ensure your .env file has PPLX_API_KEY
    result = perplexity_web("What is the role of CD36 in fatty acid uptake?")
    print(result)
