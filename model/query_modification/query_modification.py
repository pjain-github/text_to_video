from model.query_modification.prompts import query_modification_prompt, blog_prompt

class QueryModification:
    """
    Class to answer simple user questions from search results.
    """

    def __init__(self, llm):
        self.llm_class = llm
        self.answer_prompt = query_modification_prompt
        self.blog_prompt = blog_prompt

    def answer_question(self, question):

        # Generate the prompt with the user question and search results
        prompt = self.answer_prompt.format(user_query=question)

        # Generate the answer using the language model
        answer = self.llm_class.call_llm(messages = prompt)

        return answer
    
    def blog_search(self, query, software_description=None):
        # Generate the prompt with the user question and search results
        prompt = self.blog_prompt.format(query=query, software_description=software_description)

        # Generate the answer using the language model
        answer = self.llm_class.call_llm(messages = prompt)

        return answer
    