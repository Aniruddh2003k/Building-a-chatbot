import os
import openai
from dotenv import load_dotenv

# Load API key from .env file (recommended)
load_dotenv()
client = openai(api_key=os.getenv("OPENAI_API_KEY"))

# function that takes in string argument as parameter
# PROMPT: what the user types (their message/question).
# MaxToken: maximum length of the response (default = 50 words-ish).
# outputs: how many different replies you want at once (default = 3).
def comp(PROMPT, MaxToken=50, outputs=3):
    # using OpenAI's Completion module that helps execute 
    # any tasks involving text 
    response = client.chat.completions.create(
        # model name used here is text-davinci-003
        # there are many other models available under the 
        # umbrella of GPT-3
        model="gpt-4.1-nano",
        # passing the user input 
        messages=[{"role": "user", "content": PROMPT}],
        # generated output can have "max_tokens" number of tokens 
        max_tokens=MaxToken,
        # number of outputs generated in one call
        n=outputs
    )
    # creating a list to store all the outputs
    output = list()
    for choice in response.choices:
        output.append(choice.message.content.strip())
    return output

# Example usage
if __name__ == "__main__":
    replies = comp("Hello, how are you?")
    for i, reply in enumerate(replies, 1):
        print(f"Response {i}: {reply}")

