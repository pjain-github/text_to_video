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
        
        try:
            response = requests.get(url, timeout=15)

            text = ''
            if response.status_code == 200:
                # Parse the HTML content of the webpage
                soup = BeautifulSoup(response.content, 'html.parser')
    
                # Getting title of the page
                title = soup.title.string if soup.title else "No title found"
    
                text = ''
    
                # Getting text from webpage            
                text_content = [p.get_text(strip=True) for p in soup.find_all('p')]
                for text_part in text_content:
                    text = text + text_part + '\n'

            else:
                print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
                title = ''

        except Exception as e:
            print("Failed to get text")
            # Extract all the text from the webpage
            return None, None

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
    
    @staticmethod
    def extract_content_with_sequence(url):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            # List to store extracted content
            content_list = []

            # Iterate over all elements in the body
            for element in soup.body.descendants:
                if element.name == 'p':  # Paragraph text
                    content = element.get_text(strip=True)
                    if content:
                        content_list.append({'type': 'text', 'content': content})

                elif element.name == 'img':  # Images
                    img_src = element.get('src')
                    if img_src:
                        full_url = requests.compat.urljoin(url, img_src)
                        content_list.append({'type': 'image', 'content': full_url})

                elif element.name == 'table':  # Tables
                    table_html = str(element)
                    content_list.append({'type': 'table', 'content': table_html})

                elif element.name == 'a':  # Links
                    link_href = element.get('href')
                    link_text = element.get_text(strip=True)
                    if link_href:
                        full_url = requests.compat.urljoin(url, link_href)
                        content_list.append({'type': 'link', 'content': {'url': full_url, 'text': link_text}})

            text = ""

            # Stringigy the extracted content
            for item in content_list:
                if item['type'] == 'text':
                    text += f"Text: {item['content']}\n"
                elif item['type'] == 'image':
                     text += f"Image URL: {item['content']}\n"
                elif item['type'] == 'table':
                     text += f"Table HTML: {item['content']}\n"
                elif item['type'] == 'link':
                     text += f"Link: {item['content']['url']} (Text: {item['content']['text']})\n"
            
            return text
        
        except:
            return None
