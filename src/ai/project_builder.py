# project_builder.py – تنفيذ التعليمات وإنشاء ملفات المشروع

import os

def build_project(command):
    if command["type"] == "create":
        target = command["target"]

        if target == "chat_interface":
            return create_chat_interface(command["features"])

        elif target == "login_page":
            return create_login_page(command["fields"])

        elif target == "homepage":
            return create_homepage(command["sections"])

        else:
            return "تعليمات غير مدعومة حاليًا."

    elif command["type"] == "unknown":
        return command["message"]

    else:
        return "نوع الأمر غير معروف."

def create_chat_interface(features):
    content = "<!-- واجهة دردشة -->\n<div class='chat-box'>\n"
    for feature in features:
        if feature == "text_input":
            content += "<textarea placeholder='اكتب هنا...'></textarea>\n"
        elif feature == "response_box":
            content += "<div id='responseBox'></div>\n"
        elif feature == "send_button":
            content += "<button onclick='sendPrompt()'>إرسال</button>\n"
    content += "</div>\n"
    return content

def create_login_page(fields):
    content = "<!-- صفحة تسجيل دخول -->\n<form>\n"
    for field in fields:
        if field == "username":
            content += "<input type='text' placeholder='اسم المستخدم'>\n"
        elif field == "password":
            content += "<input type='password' placeholder='كلمة المرور'>\n"
        elif field == "submit":
            content += "<button type='submit'>دخول</button>\n"
    content += "</form>\n"
    return content

def create_homepage(sections):
    content = "<!-- الصفحة الرئيسية -->\n"
    for section in sections:
        if section == "header":
            content += "<header><h1>BankOfIntelligence</h1></header>\n"
        elif section == "welcome":
            content += "<section><p>مرحبًا بك في بنك الذكاء</p></section>\n"
        elif section == "features":
            content += "<section><ul><li>دردشة ذكية</li><li>تنفيذ أوامر</li></ul></section>\n"
        elif section == "footer":
            content += "<footer><p>© 2025 جميع الحقوق محفوظة</p></footer>\n"
    return content
