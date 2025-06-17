import httpx
import json
import os
from pathlib import Path # For more robust path handling
from dotenv import load_dotenv

def list_maps_in_project(base_api_url: str, project_id: str, auth_token: str | None):
    """
    Lists all (sub)maps in a given project using the Minerva API.
    base_api_url should be like 'https://minerva-service.lcsb.uni.lu/minerva/api/'
    """
    try:
        # Ensure the base URL ends with a slash
        if not base_api_url.endswith('/'):
            base_api_url += '/'
        
        url = f"{base_api_url}projects/{project_id}/models/"
        print(f"Fetching maps for project '{project_id}' from: {url}")
        
        cookies = {}
        if auth_token:
            cookies["MINERVA_AUTH_TOKEN"] = auth_token
            # Provide some feedback that a token is being used without exposing it.
            token_preview = f"starts with '{auth_token[:3]}', ends with '{auth_token[-3:]}'" if len(auth_token) >= 6 else "is present"
            print(f"Using MINERVA_AUTH_TOKEN ({token_preview}) for authentication via cookie.")
        else:
            # This case should ideally be caught before calling, but as a fallback:
            print("Warning: MINERVA_AUTH_TOKEN not provided to function. Request might fail if authentication is required.")

        response = httpx.get(url, cookies=cookies, timeout=30.0)
        response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
        
        maps_data = response.json()
        
        if isinstance(maps_data, list):
            print(f"\nFound {len(maps_data)} map(s) in project '{project_id}':")
            if not maps_data:
                print("  No maps found or the list is empty.")
            for map_item in maps_data:
                map_id = map_item.get('idObject', 'N/A')
                # The sample response shows 'name' can be null, provide a default.
                map_name = map_item.get('name') if map_item.get('name') is not None else 'Unnamed Map'
                map_desc = map_item.get('description') if map_item.get('description') is not None else 'No description'
                print(f"  - Map ID: {map_id}, Name: {map_name}")
                print(f"    Description: {map_desc}")
                # You can uncomment the line below for full details of each map
                # print(f"    Full details: {json.dumps(map_item, indent=2)}")
            return maps_data
        else:
            print("Unexpected response format. Expected a list of maps.")
            print(f"Raw response data type: {type(maps_data)}")
            print(f"Raw response content: {maps_data}")
            return None

    except httpx.HTTPStatusError as e:
        print(f"HTTP error occurred: {e.response.status_code} - {e.response.reason_phrase}")
        print(f"URL: {e.request.url}")
        try:
            print(f"Response content: {e.response.text}")
        except Exception:
            print("Could not retrieve response content for HTTPStatusError.")
        return None
    except httpx.RequestError as e:
        print(f"Request error occurred: {e}")
        if hasattr(e, 'request') and e.request is not None:
             print(f"URL: {e.request.url}")
        return None
    except json.JSONDecodeError:
        print("Failed to decode JSON response.")
        if 'response' in locals() and hasattr(response, 'text'):
            print(f"Response content: {response.text}")
        else:
            print("Could not retrieve response text for JSONDecodeError.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {type(e).__name__} - {e}")
        return None

if __name__ == "__main__":
    # Construct the path to the .env file relative to this script's location
    # Assumes .env is in the same directory as this script (fatty-acid-assistant)
    script_dir = Path(__file__).resolve().parent
    dotenv_path = script_dir / ".env"

    if dotenv_path.exists():
        print(f"Loading .env file from: {dotenv_path}")
        load_dotenv(dotenv_path=dotenv_path)
    else:
        print(f"Warning: .env file not found at {dotenv_path}. Attempting to load from default locations (e.g., current working directory).")
        load_dotenv() # Fallback to default behavior
    
    minerva_auth_token = os.getenv("MINERVA_TOKEN")

    if not minerva_auth_token:
        print("Error: MINERVA_TOKEN not found in environment variables after attempting to load .env.")
        print("Please ensure MINERVA_TOKEN is set in your .env file located at:", dotenv_path.parent / ".env" if dotenv_path else "your .env file path")
        exit(1) # Exit if no token is found, as it's required.
    else:
        print(f"MINERVA_TOKEN loaded successfully from .env file.")

    # Base URL from the CURL samples provided in the documentation
    api_base_url = "https://minerva-service.lcsb.uni.lu/minerva/api/"
    
    # Prompt user for the project ID
    project_to_query_raw = input(f"Enter project ID to list maps for (e.g., 'empty', 'test_project' from docs): ")
    # Clean the input: strip whitespace and common quote characters from start/end
    project_to_query = project_to_query_raw.strip().strip("'\"")
    
    if not project_to_query: # Check after stripping
        print("No valid project ID entered (after stripping whitespace/quotes). Exiting.")
    else:
        print(f"\nAttempting to list maps for project: '{project_to_query}' using API base: {api_base_url}")
        maps_list = list_maps_in_project(api_base_url, project_to_query, minerva_auth_token)
        
        if maps_list is not None:
            # The function already prints details, so just a success message here.
            print(f"\nSuccessfully processed map listing request for project '{project_to_query}'.")
        else:
            print(f"\nFailed to retrieve or process maps for project '{project_to_query}'.")
