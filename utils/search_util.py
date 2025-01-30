from data.web_scrapping import WebScraper

def process_google_search(search_json):
    """
    Processes a JSON object from a Google search result, extracting relevant metadata.

    Parameters:
    - search_json (dict): A dictionary containing search result data.
    Returns:
    - metadata (dict): A dictionary containing the extracted metadata.
    """

    # Extracting relevant metadata using dictionary comprehension
    keys_of_interest = ["link"]

    metadata = {}

    for key in keys_of_interest:
        if key in search_json:
            metadata[key] = search_json[key]

    # Fetch the article's title and text if a link is present
    if 'link' in metadata:
        metadata['title'], metadata['text'] = WebScraper.get_article(metadata['link'])

    return metadata


async def async_process_google_search(search_json):
    """
    Processes a JSON object from a Google search result, extracting relevant metadata.

    Parameters:
    - search_json (dict): A dictionary containing search result data.

    Returns:
    - metadata (dict): A dictionary containing the extracted metadata.
    """

    # Extracting relevant metadata using dictionary comprehension
    keys_of_interest = ["link"]

    metadata = {key: search_json.get(key) for key in keys_of_interest if key in search_json}

    # Fetch the article's title and text if a link is present
    if 'link' in metadata:
        metadata['title'], metadata['text'] = await WebScraper.async_get_article(metadata['link'])

    return metadata
    

def process_google_search_blog(search_json):
    """
    Processes a JSON object from a Google search result, extracting relevant metadata.

    Parameters:
    - search_json (dict): A dictionary containing search result data.
    Returns:
    - metadata (dict): A dictionary containing the extracted metadata.
    """

    # Extracting relevant metadata using dictionary comprehension
    keys_of_interest = ["link"]

    metadata = {}

    for key in keys_of_interest:
        if key in search_json:
            metadata[key] = search_json[key]

    # Fetch the article's title and text if a link is present
    if 'link' in metadata:
        metadata['text'] = WebScraper.extract_content_with_sequence(metadata['link'])

    return metadata