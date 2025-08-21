import os
from openai import OpenAI
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def comp(PROMPT, MaxToken=50, outputs=3):
    response = client.chat.completions.create(
        model="gpt-4.1-nano",
        messages=[{"role": "user", "content": PROMPT}],
        max_tokens=MaxToken,
        n=outputs
    )

    output = []
    for choice in response.choices:
        output.append(choice.message.content.strip())
    return output


if __name__ == "__main__":
    replies = comp("Hello, how are you?")
    for i, reply in enumerate(replies, 1):
        print(f"Response {i}: {reply}")
