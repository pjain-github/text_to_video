import requests
import json
import httpx


class GoogleSearch:
    """
    A class to interact with Google's Custom Search JSON API.
    It allows performing search queries and retrieving results based on specified criteria.
    """

    def __init__(self, api_key, cse_id):
        """
        Initializes the GoogleSearch object with an API key and Custom Search Engine (CSE) ID.

        Parameters:
        - api_key (str): The API key for accessing Google's Custom Search JSON API.
        - cse_id (str): The Custom Search Engine ID that identifies the specific search engine configuration.
        """
        self.api_key = api_key
        self.cse_id = cse_id

    def search(self, query, **kwargs):
        """
        Performs a search query using Google's Custom Search JSON API.

        Parameters:
        - query (str): The search query string.
        - **kwargs (dict): Additional optional parameters for customizing the search:
            - searchType (str): Specifies the type of search (e.g., 'image' for an image search).
            - num (int): Number of search results to return (up to 10).
            - start (int): Index of the first search result to return (for pagination).
            - fileType (str): Restricts the search to files of a specific type (e.g., 'pdf').
            - lr (str): Limits the search to a specific language (e.g., 'en' for English).
            - gl (str): Sets the geographic region for the search (e.g., 'in' for India).
            - safe (str): Specifies the SafeSearch level (e.g., 'off', 'medium', 'high').
            - dateRestrict (str): Restricts the search to results published within a specific date range, in the format 'YYYY-MM-DD:YYYY-MM-DD'.
            - sites (list): A list of websites to restrict the search to.

        Returns:
        - results (list): A list of search result items, each containing information such as the title, link, snippet, and other metadata.

        Sample Kwargs:
        kwargs = params = {
            'searchType': 'image',
            'num': 10,
            'start': 1,
            'fileType': 'pdf',
            'lr': 'en',
            'gl': 'in',
            'safe': 'off',
            'dateRestrict': '2024-01-01:2024-08-01'
            'sites': ['hindustantimes.com', 'https://www.thehindu.com']
        }
        """
        url = "https://www.googleapis.com/customsearch/v1"

        # If a list of websites is provided, include them in the query using the 'site:' operator
        if 'sites' in kwargs.keys():
            sites = kwargs.pop('sites')
            sites_query = " OR ".join([f"site:{site}" for site in sites])
            query = f"{query} ({sites_query})"

        print(kwargs.keys())

        if 'num' in kwargs.keys():
            print("nums")
            kwargs['num'] = min(kwargs['num'], 10)

        params = {
            'q': query,
            'key': self.api_key,
            'cx': self.cse_id,
            **kwargs
        }

        # Send a GET request to the Google Custom Search API with the provided parameters
        response = requests.get(url, params=params)

        # Parse the JSON response to extract the search results
        results = response.json().get('items', [])

        return results

    async def async_search(self, query, **kwargs):
        """
        Asynchronously performs a search query using Google's Custom Search JSON API and streams the results.

        Parameters:
        - query (str): The search query string.
        - **kwargs (dict): Additional optional parameters for customizing the search:
            - searchType (str): Specifies the type of search (e.g., 'image' for an image search).
            - num (int): Number of search results to return (up to 10).
            - start (int): Index of the first search result to return (for pagination).
            - fileType (str): Restricts the search to files of a specific type (e.g., 'pdf').
            - lr (str): Limits the search to a specific language (e.g., 'en' for English).
            - gl (str): Sets the geographic region for the search (e.g., 'in' for India).
            - safe (str): Specifies the SafeSearch level (e.g., 'off', 'medium', 'high').
            - dateRestrict (str): Restricts the search to results published within a specific date range, in the format 'YYYY-MM-DD:YYYY-MM-DD'.
            - sites (list): A list of websites to restrict the search to.

        Yields:
        - result (dict): A search result item containing information such as the title, link, snippet, and other metadata.
        """
        url = "https://www.googleapis.com/customsearch/v1"
        params = {
            'q': query,
            'key': self.api_key,
            'cx': self.cse_id,
            **kwargs
        }

        # Use httpx for async requests
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)

            # Check if the response was successful
            response.raise_for_status()

            # Parse the JSON response to extract the search results
            results = response.json().get('items', [])

            # Stream each result
            for result in results:
                yield result

    def available_gl(self):
        """
        Retrieves a list of available geographic regions for the search.
        """

        with open('/content/google-countries.json', 'r') as file:
            countries_list = json.load(file)

        countries_dict = {country['country_name']: country['country_code'] for country in countries_list}

        return countries_dict
       
    def __str__(self):
        return f"GoogleSearch API Key: ***************, CSE ID: #####"
    
    def __repr__(self):
        return f"GoogleSearch(api_key= '***************', cse_id='######')"