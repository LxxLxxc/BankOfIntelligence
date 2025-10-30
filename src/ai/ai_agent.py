# ai_agent.py – المحرك التنفيذي للأوامر الذكية

from flask import Flask, request, jsonify
from src.ai.nlp_parser import parse_command
from src.ai.project_builder import build_project

app = Flask(__name__)

@app.route('/src/ai/ai_agent.py', methods=['POST'])
def execute_prompt():
    data = request.get_json()
    prompt = data.get('prompt', '')

    if not prompt:
        return jsonify({"error": "لم يتم إرسال أي أمر."}), 400

    try:
        command = parse_command(prompt)
        result = build_project(command)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
