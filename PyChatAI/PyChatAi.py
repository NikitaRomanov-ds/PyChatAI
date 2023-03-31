import openai
from api_keys import gpt_api_key

class GPT:
    
    __version__ = '0.0.1'
    
    def __init__(self, api_key):
        openai.api_key = gpt_api_key
        
    def generate_answer(self, question):
        """
        Sends a request to the OpenAI GPT-3 language model with the given question, and returns a generated answer.

        Parameters:
            question (str): The question to ask the language model.

        Returns:
            None. Prints the generated answer to the console.

        Example Usage:
            INPUT:  gpt.generate_answer("surname of Shaquille basketball player?")
            OUTPUT: "The surname of Shaquille O'Neal, the retired American professional basketball player, is "O'Neal"."
        """
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"{question}\nAI:",
            max_tokens=4000,
            n=1,
            stop=None,
            temperature=0.5,
        )
        answer = response.choices[0].text.strip()
        print(answer)