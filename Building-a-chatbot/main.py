import os
from openai import OpenAI
from dotenv import load_dotenv

# Load API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def comp(prompt, MaxToken=500, outputs=1):
    """Generate chatbot replies for a given prompt"""
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=MaxToken,
        n=outputs
    )

    output = [choice.message.content.strip() for choice in response.choices]
    return output
