from model.blog.prompts import tech_prompt, image_prompt, final_prompt
from model.blog.functions import DescriptionList
from typing import List, Dict
from langchain_core.messages import HumanMessage, SystemMessage
import base64
import re
import httpx
from PIL import Image
from io import BytesIO
import json

class Blog:
    """
    Class to answer simple user questions from search results.
    """

    def __init__(self, llm):
        self.llm_class = llm
        self.prompt = tech_prompt
        self.image_prompt = image_prompt
        self.description = DescriptionList
        self.final_prompt = final_prompt
        

    def encode_image_to_base64(self, url: str) -> str:
        try:
    # Normally, you would fetch the image and encode it. Here, we'll use a placeholder.
            image_data = base64.b64encode(httpx.get(url).content).decode("utf-8")
            return image_data
        except:
            return None

    def generate_human_message(self, text: str) -> List:
        # Initialize the content list
        content = []

        # Split text into lines
        lines = text.splitlines()

        # Temporary variable to accumulate text blocks
        text_block = ""

        for line in lines:

            # Check for images and encode them
            if "<img src=" in line:
                if text_block:
                    content.append({"type": "text", "text": text_block})
                    text_block = ""
                # match = re.search(r'<img\s+[^>]*src=["\'](.*?)["\']', line)
                # if match:
                #     image_url = match.group(1)
                #     image_data = self.encode_image_to_base64(image_url)
                #     content.append({"type": "text", "text": f"<img src='{image_url}'> "})
                #     content.append({
                #         "type": "image_url",
                #         #"image_url": {"url": f"data:{image_url};base64,{image_data}"},
                #         "image_url": {"url": f"{image_url}"},
                #     })

            # Accumulate text content
            else:
                text_block += f"{line}\n"
            # else:
            #     if text_block:
            #         content.append({"type": "text", "text": text_block})
            #         text_block = ""

        # Append any remaining text block
        if text_block:
            content.append({"type": "text", "text": text_block.strip()})

        return content
    
    def is_valid_image_url(self, image_url: str) -> bool:
        """Check if the provided URL leads to a valid image using httpx (synchronous)."""
        try:
            with httpx.Client() as client:
                response = client.get(image_url, timeout=5)
                if response.status_code != 200:
                    return False  # URL did not return 200 OK

                img = Image.open(BytesIO(response.content))
                img.verify()  # Verify if it's a valid image
                return True
        except (httpx.RequestError, IOError, SyntaxError):
            return False 
    
    def generate_image_message(self, text: str) -> List:
        # Initialize the content list
        content = []

        # Split text into lines
        lines = text.splitlines()

        # Temporary variable to accumulate text blocks
        text_block = ""

        for line in lines:

            # Check for images and encode them
            if "<img src=" in line:
                if text_block:
                    text_block = ""
                match = re.search(r'<img\s+[^>]*src=["\'](.*?)["\']', line)
                if match:
                    image_url = match.group(1)
                    image_data = self.encode_image_to_base64(image_url)
                    valid_image = self.is_valid_image_url(image_url)
                    if valid_image:
                        content.append({"type": "text", "text": f"<img src='{image_url}'> "})
                        content.append({
                            "type": "image_url",
                            #"image_url": {"url": f"data:{image_url};base64,{image_data}"},
                            "image_url": {"url": f"{image_url}"},
                        })

        if len(content)>20:
            return content[:20]
        return content
    
    def process_images(self, descriptions):

        res = []
        for description in descriptions:
            for desc in description[1]:
                res.append({desc.image: desc.description})

        return res


    # def generate_blog(self, topic, search_results, details, opinion=None):

    #     prompt_text = self.prompt.format(
    #         software=topic
    #     )

    #     prompt_image = [SystemMessage(content=self.image_prompt)]

    #     messages_text = [SystemMessage(content=prompt_text)]

    #     for search_result in search_results:

    #         message_content = self.generate_human_message(search_result)
    #         image_content = self.generate_image_message(search_result)

    #         if image_content:
    #             prompt_image.extend([HumanMessage(content=image_content)])

    #         message = [HumanMessage(content=message_content)]

    #         messages_text.extend(message)

    #     # Generate the answer using the language model
    #     answer = self.llm_class.call_llm(messages_text).content

    #     prompt_image.extend([HumanMessage(content = f"We are writing a blogo on sotware {topic}, description : {details}. Make sure images should be relevant to the software.")])

    #     image_data = self.llm_class.call_llm_json(prompt_image, self.description)
    #     image_data = self.process_images(image_data)

    #     prompt = self.final_prompt + f"\n Blog text: {answer}" + "\n``````````"+ "\n Image List: " + str(image_data)

    #     answer = self.llm_class.call_llm(prompt).content

    #     return answer

    def generate_blog(self, topic, search_results, details=None, opinion=None):

        prompt_text = self.prompt.format(
            software=topic
        )

        messages_text = [SystemMessage(content=prompt_text)]

        for search_result in search_results:

            message = [HumanMessage(content=search_result)]

            messages_text.extend(message)

        # Generate the answer using the language model
        answer = self.llm_class.call_llm(messages_text).content

        return answer




