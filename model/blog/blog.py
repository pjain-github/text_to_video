from model.blog.prompts import tech_prompt

class Blog:
    """
    Class to answer simple user questions from search results.
    """

    def __init__(self, llm):
        self.llm_class = llm
        self.prompt = tech_prompt

    def answer_question(self, topic, search_results, opinion=None):

        # Generate the prompt with the user question and search results
        prompt = self.prompt.format(topic=topic, articles=search_results, opinion=opinion)

        # Generate the answer using the language model
        answer = self.llm_class.call_llm(messages = prompt)

        return answer




