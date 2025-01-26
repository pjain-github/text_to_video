

from openai import OpenAI

class OpenAIUtil:
    def __init__(self, open_ai_api_key):
        self.openai = OpenAI()
        self.async_openai = AsyncOpenAI()
        self.openai.api_key = open_ai_api_key

