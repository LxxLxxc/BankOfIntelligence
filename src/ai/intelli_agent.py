from flask import Blueprint, request, jsonify

intelli_bp = Blueprint('intelli_agent', __name__)

@intelli_bp.route('/api/intelli_agent', methods=['POST'])
def handle_prompt():
    try:
        data = request.get_json(force=True)
        prompt = data.get('message', '').strip()

        if not prompt:
            return jsonify({"response": "يرجى إدخال فكرة واضحة."}), 400

        # رد تجريبي — جاهز للربط مع bi_agent أو nlp_parser
        response = f"✅ تم استلام فكرتك: «{prompt}» — سيتم تنفيذها قريبًا."

        return jsonify({"response": response})

    except Exception as e:
        return jsonify({"response": f"❌ حدث خطأ أثناء المعالجة: {str(e)}"}), 500
