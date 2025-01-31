from data.google_search import GoogleSearch
import os
from dotenv import load_dotenv
from utils.search_util import process_google_search_blog
from ai.gemini_util import Gemini
from model.blog.blog import Blog
from model.cleaning.clean import Clean
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

def blog_generator(query: str, details:str=None, sites: list=[], num: int=5):

    # Gemini model 
    llm = Gemini(api_key=gemini_api_key)

    if sites:
        logging.info("Sites provided in the list")
        search_results = [{'link': site} for site in sites]
        logging.info(f"Received {len(search_results)} search results from User")

    else:

        # Create a GoogleSearch object
        google_search = GoogleSearch(google_api_key, google_cse_id)

        search_query = f"Reviews on {query}"

        query_params = {
                    'num': num,
                    'start': 1,
                    'lr': 'en',
                    'safe': 'off',
                }

        logging.info(f"Querying Google Search API with query: {search_query} and query parameters: {query_params}")
        search_results = google_search.search(query, **query_params)
        logging.info(f"Received {len(search_results)} search results from Google Search API")

    # Processing Search Results
    processed_results = []

    cln = Clean(llm)

    logging.info(f"Processing search results")
    for search_result in search_results:
        metadata = process_google_search_blog(search_result)
        # metadata['text'] = cln.clean_article(metadata['text'])
        processed_results.append(metadata['text'])
    logging.info(f"Processed {len(processed_results)} search results")

    blog_class = Blog(llm)

    logging.info(f"Creating blog on: {query} using search results")
    answer = blog_class.generate_blog(query, processed_results, details)
    logging.info(f"Blog generated")

    return answer

if __name__ == "__main__":
    print(blog_generator("Shopify"))