from data.google_search import GoogleSearch
import os
from dotenv import load_dotenv

# Initialize the GoogleSearch object with your API key and CSE ID
# Load environment variables from .env file
load_dotenv()

# Get the API key and CSE ID from environment variables
api_key = os.getenv('GOOGLE_SEARCH_API_KEY')
cse_id = os.getenv('GOOGLE_SEARCH_CSE_ID')

# Initialize the GoogleSearch object with your API key and CSE ID
google_search = GoogleSearch(api_key, cse_id)

