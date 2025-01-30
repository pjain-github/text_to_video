from model.cleaning.prompts import cleaning_prompt

class Clean:
    """
    Class to answer simple user questions from search results.
    """

    def __init__(self, llm):
        self.llm_class = llm
        self.cleaning_prompt = cleaning_prompt

    def clean_article(self, article):

        # Generate the prompt with the user question and search results
        prompt = self.cleaning_prompt + article

        # Generate the answer using the language model
        answer = self.llm_class.call_llm(messages = prompt)

        return answer.content