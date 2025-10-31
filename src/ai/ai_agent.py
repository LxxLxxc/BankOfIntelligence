from flask import Blueprint, request, jsonify
from src.ai.nlp_parser import parse_command
from src.ai.project_builder import build_project

ai_bp = Blueprint('ai_agent', __name__)

@ai_bp.route('/api/ai_agent', methods=['POST'])
def execute_prompt():
    try:
        data = request.get_json(force=True)
        prompt = data.get('prompt', '').strip()

        if not prompt:
            return jsonify({"error": "لم يتم إرسال أي أمر."}), 400

        command = parse_command(prompt)
        result = build_project(command)

        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
