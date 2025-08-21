from flask import Flask, request, jsonify, render_template
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ✅ Define the class
class ChatResponse:
    def __init__(self, user_message, bot_reply):
        self.user_message = user_message
        self.bot_reply = bot_reply

    def to_dict(self):
        return {
            "user_message": self.user_message,
            "bot_reply": self.bot_reply
        }

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message")
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": user_msg}]
    )
    reply = response.choices[0].message.content.strip()

    # ✅ Use ChatResponse
    res = ChatResponse(user_message=user_msg, bot_reply=reply)
    return jsonify(res.to_dict())

if __name__ == "__main__":
    app.run(debug=True)
