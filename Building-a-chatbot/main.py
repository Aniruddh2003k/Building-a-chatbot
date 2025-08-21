import os
from openai import OpenAI
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

PROMPT = """Write a story to inspire greatness, take the antagonist as a Rabbit and protagnist as turtle. 
Let antagonist and protagnist compete against each other for a common goal. 
Story should atmost have 3 lines."""

def comp(PROMPT, MaxToken=500, outputs=3):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": PROMPT}],
        max_tokens=MaxToken,
        n=outputs
    )

    output = list()
    for choice in response.choices:
        output.append(choice.message.content.strip())
    return output


if __name__ == "__main__":
    replies = comp("Hello, how are you?")
    for i, reply in enumerate(replies, 1):
        print(f"Response {i}: {reply}")
