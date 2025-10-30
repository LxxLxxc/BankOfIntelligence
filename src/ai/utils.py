# utils.py – أدوات مساعدة للذكاء الاصطناعي والتنفيذ

import datetime

def get_timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def sanitize_input(text):
    return text.strip().replace("<", "&lt;").replace(">", "&gt;")

def log_activity(action, detail):
    timestamp = get_timestamp()
    return f"[{timestamp}] {action}: {detail}"
