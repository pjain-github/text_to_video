from data.google_search import GoogleSearch
import os
from dotenv import load_dotenv
from utils.search_util import process_google_search
from ai.gemini_util import Gemini
from model.blog.blog import Blog
from model.query_modification.query_modification import QueryModification
from datetime import datetime, timedelta
import logging
# Configure logging to print INFO level messages to the console
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize the GoogleSearch object with your API key and CSE ID
# Load environment variables from .env file
load_dotenv()

# Get the API key and CSE ID from environment variables
google_api_key = os.getenv('GOOGLE_SEARCH_API_KEY')
google_cse_id = os.getenv('GOOGLE_SEARCH_CSE_ID')
gemini_api_key = os.getenv('GEMINI_API_KEY')

def simple_search(query: str, start_date: str=None, end_date: str=None, region: str='in', num:int=10):

    # Gemini model
    llm = Gemini(api_key=gemini_api_key)

    # Query Modification model
    query_mod = QueryModification(llm)
    search_queries = query_mod.blog_search(query)

    return search_queries

    # Create a GoogleSearch object
    google_search = GoogleSearch(google_api_key, google_cse_id)

    query_params = {
                'num': num,
                'start': 1,
                'lr': 'en',
                'gl': region,
                'safe': 'off',
            }
    
    logging.info(f"Querying Google Search API with query: {query} and query parameters: {query_params}")
    search_results = google_search.search(query, **query_params)
    logging.info(f"Received {len(search_results)} search results from Google Search API")

    # Processing Search Results
    processed_results = []

    logging.info(f"Processing search results")
    for search_result in search_results:
        metadata = process_google_search(search_result)
        processed_results.append(metadata)
    logging.info(f"Processed {len(processed_results)} search results")

    # Gemini model
    llm = Gemini(api_key=gemini_api_key)

    blog_class = Blog(llm)

    logging.info(f"Creating blog on: {query} using search results")
    answer = blog_class.answer_question(query, processed_results)
    logging.info(f"Blog generated")

    return answer

if __name__ == "__main__":
    print(simple_search("Shopify"))