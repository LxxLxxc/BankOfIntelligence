from flask import Blueprint, request, jsonify

intelli_bp = Blueprint('intelli_agent', __name__)

@intelli_bp.route('/api/intelli_agent', methods=['POST'])
def handle_prompt():
    data = request.get_json()
    prompt = data.get('message', '')

    # رد تجريبي — يمكن ربطه لاحقًا بـ bi_agent أو nlp_parser
    response = f"تم استلام فكرتك: '{prompt}' — سيتم تنفيذها قريبًا."

    return jsonify({"response": response})
