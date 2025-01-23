import requests
from bs4 import BeautifulSoup
import httpx

# Send a GET request to the URL
class WebScraper:
    """
    A class to scrape the title and text content of a webpage.
    Asynchronous and synchronous methods are provided for fetching the webpage content.
    """
    
    @staticmethod
    def get_article(url):
        """
        Sends a GET request to the given URL and retrieves the title and text content of the webpage.

        Parameters:
        - url (str): The URL of the webpage to scrape.

        Returns:
        - title (str): The title of the webpage.
        - text (str): The text content of the webpage.
        """

        response = requests.get(url)

        text = ''
        if response.status_code == 200:
            # Parse the HTML content of the webpage
            soup = BeautifulSoup(response.content, 'html.parser')

            # Getting title of the page
            title = soup.title.string if soup.title else "No title found"

            text = ''

            # Getting text from webpage
            try:
                text_content = [p.get_text(strip=True) for p in soup.find_all('p')]
                for text_part in text_content:
                    text = text + text_part + '\n'

            except Exception as e:
                print("Failed to get text")
                # Extract all the text from the webpage
                text = text + soup.get_text()

        else:
            print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
            title = ''

        return title, text

    @staticmethod
    async def async_get_article(url):
        """
        Asynchronously sends a GET request to the given URL and retrieves the title and text content of the webpage.

        Parameters:
        - url (str): The URL of the webpage to scrape.

        Returns:
        - title (str): The title of the webpage.
        - text (str): The text content of the webpage.
        """
        async with httpx.AsyncClient() as client:
            response = await client.get(url)

        title = ''
        text = ''

        if response.status_code == 200:
            # Parse the HTML content of the webpage
            soup = BeautifulSoup(response.content, 'html.parser')

            # Getting title of the page
            title = soup.title.string if soup.title else "No title found"

            # Getting text from webpage
            try:
                text_content = [p.get_text(strip=True) for p in soup.find_all('p')]
                text = '\n'.join(text_content)
            except Exception as e:
                print("Failed to get text")
                text = soup.get_text()
        else:
            print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

        return title, text
