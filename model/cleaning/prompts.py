cleaning_prompt = """
Task:
You are provided with a file extracted from the web. This file contains a combination of text, images, tables, and links arranged in proper order. However, the file also includes noise such as sidebar menus, irrelevant initial or concluding content, advertisements, and unnecessary links, images, or tables. Your task is to clean this content based on the following guidelines and steps.

Instructions:
  Initial Cleanup (Top of the File):
    Remove any irrelevant or unnecessary introductory text, images, tables, or links at the top of the document.
    Irrelevant content includes:
    Navigation menus or sidebar text.
    Repetitive headings or summaries unrelated to the main content.
  
  Content Review (Middle of the File):
    Carefully analyze the images, tables, and links in the middle of the document.
      Keep if:
        The image is directly referenced in the text or is critical for explaining a concept.
        The table provides valuable information supporting the content.
        The link adds meaningful context or directs to a source essential to understanding the material.
      Remove if:
        The image is an advertisement, logo, or unrelated photo of an individual.
        The table or link does not contribute to the topic or appears promotional in nature.
  
  Final Cleanup (Bottom of the File):
    Remove any irrelevant or unnecessary concluding text, images, tables, or links at the end of the document.
    Examples of irrelevant content include:
    Footer menus, "Contact Us," or subscription-related links.
    Advertisements or logos.

  Structured Output for Relevant Images and Links:
    If an image is determined to be relevant to the content:
      Return the image in the following format:
        <img src="source"> text </img>
        Replace source with the actual image source URL.
        Replace text with any accompanying explanation or description provided in the file.
    If a link is determined to be relevant to the content:
      Return the link in the following format:
        <a href="URL">link text</a>
        Replace URL with the link destination.
        Replace link text with the associated text in the document, if applicable.
  
  Chain of Thought (Review and Justification):
    For each item (text, image, table, or link) that you choose to remove, ensure to assess its relevance based on its context within the content.
    When in doubt:
      Check if the image, link, or table is referenced in the surrounding text or contributes to the explanation.
      Evaluate if the image appears generic, unrelated, or promotional, and act accordingly.

  Output:
    Provide a cleaned version of the document with all irrelevant elements removed.
    Ensure the remaining content maintains logical flow and clarity.

  
  Note:
    Use basic reasoning to evaluate images and links. For instance:
    Logos or generic pictures of people are typically not relevant unless explicitly described in the text.
    Links to unrelated external sites or promotional pages should be removed unless they are cited as a reference or essential for the explanation.
  
  The final document should look clean, professional, and focused on delivering the primary content without unnecessary distractions.

Text:   
"""
