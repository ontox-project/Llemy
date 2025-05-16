from ontox_client import ontox_map_data_retriever
import logging

# Ensure logging from ontox_client is visible
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    print("--- Testing Ontox API Client (Full Map Data Retrieval with Reaction Refs) ---")
    
    # Invoke the tool. The question argument is optional for ontox_map_data_retriever.
    result = ontox_map_data_retriever.invoke({}) 
    
    print(f"\nStatus: {result.get('status', 'N/A')}") # Use .get for safety
    
    if result.get('status') == 'success':
        data = result.get('data', '')
        print(f"\nFirst 1500 characters of formatted data:\n{data[:1500]}...")
    elif result.get('error_message'):
        print(f"\nError: {result.get('error_message')}")
    elif result.get('data'): # For no_data_found status
        print(f"\nData: {result.get('data')}")
    else:
        print("\nNo specific data or error message returned.")
