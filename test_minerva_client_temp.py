import httpx
import json

def simple_request_projects(mnv_api_base_url: str):
    """
    Fetches a list of publicly visible projects from the Minerva API.
    """
    try:
        # Ensure the base URL ends with a slash if it doesn't already
        if not mnv_api_base_url.endswith('/'):
            mnv_api_base_url += '/'
        
        url = f"{mnv_api_base_url}projects/"
        print(f"Fetching projects from: {url}")
        
        # Make the GET request
        response = httpx.get(url, timeout=30.0) # Added a timeout
        response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
        
        # Parse the JSON response
        projects_data = response.json()
        
        if isinstance(projects_data, list):
            print("\nAvailable Projects:")
            project_ids = []
            if not projects_data:
                print("  No projects found or the list is empty.")
            for project in projects_data:
                project_id = project.get('id') # Common field name for ID, or 'projectId'
                project_name = project.get('name', 'N/A') # Assuming 'name' field exists
                
                # The R script uses 'projectId'. Let's check for that first.
                if project_id is None: # If 'id' is not found or is None
                    project_id = project.get('projectId', 'N/A')

                print(f"  ID: {project_id}, Name: {project_name}")
                if project_id != 'N/A':
                    project_ids.append(project_id)
            return project_ids
        else:
            print("Unexpected response format. Expected a list of projects.")
            print("Raw response data type:", type(projects_data))
            print("Raw response content:", projects_data)
            return []

    except httpx.HTTPStatusError as e:
        print(f"HTTP error occurred: {e.response.status_code} - {e.response.reason_phrase}")
        print(f"URL: {e.request.url}")
        try:
            print(f"Response content: {e.response.text}")
        except Exception:
            print("Could not retrieve response content for HTTPStatusError.")
        return []
    except httpx.RequestError as e:
        print(f"Request error occurred: {e}")
        print(f"URL: {e.request.url}")
        return []
    except json.JSONDecodeError:
        print("Failed to decode JSON response.")
        if 'response' in locals() and hasattr(response, 'text'):
            print(f"Response content: {response.text}")
        else:
            print("Could not retrieve response text for JSONDecodeError.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

if __name__ == "__main__":
    # The API base URL provided in the R script example
    minerva_api_base = "https://ontox.elixir-luxembourg.org/minerva/api/"
    
    print("Attempting to fetch projects from Minerva API...")
    project_ids_list = simple_request_projects(minerva_api_base)
    
    if project_ids_list:
        print(f"\nSuccessfully retrieved list of Project IDs: {project_ids_list}")
    else:
        print("\nNo project IDs found or an error occurred during fetching.")
