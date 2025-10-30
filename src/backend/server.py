# server.py – تشغيل السيرفر وربط الواجهة بالذكاء الاصطناعي

from flask import Flask, request, jsonify
from src.ai.ai_agent import execute_prompt

app = Flask(__name__)

@app.route('/run', methods=['POST'])
def run_agent():
    return execute_prompt()

@app.route('/', methods=['GET'])
def home():
    return "<h1>BankOfIntelligence Server Running</h1>"

if __name__ == '__main__':
    app.run(debug=True)
