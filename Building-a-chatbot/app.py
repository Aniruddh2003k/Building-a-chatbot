from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import os
from main import comp  # import chatbot logic

load_dotenv()
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message")
    replies = comp(user_msg, outputs=1)
    return jsonify({"reply": replies[0]})

if __name__ == "__main__":
    app.run(debug=True)
