# nlp_parser.py – تحليل أوامر المستخدم وتحويلها إلى تعليمات تنفيذية

def parse_command(prompt):
    prompt = prompt.strip().lower()

    if "موقع دردشة" in prompt or "chat site" in prompt:
        return {
            "type": "create",
            "target": "chat_interface",
            "features": ["text_input", "response_box", "send_button"]
        }

    elif "صفحة تسجيل دخول" in prompt or "login page" in prompt:
        return {
            "type": "create",
            "target": "login_page",
            "fields": ["username", "password", "submit"]
        }

    elif "صفحة رئيسية" in prompt or "homepage" in prompt:
        return {
            "type": "create",
            "target": "homepage",
            "sections": ["header", "welcome", "features", "footer"]
        }

    else:
        return {
            "type": "unknown",
            "message": "لم يتم التعرف على الأمر. يرجى إعادة الصياغة."
        }
