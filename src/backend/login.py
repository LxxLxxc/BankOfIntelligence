from flask import Blueprint, request, redirect, render_template

login_bp = Blueprint('login', __name__)

# بيانات دخول تجريبية (يمكن ربطها بقاعدة بيانات لاحقًا)
USERS = {
    "admin": "1234",
    "taha": "intelligence"
}

@login_bp.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username in USERS and USERS[username] == password:
        return redirect('/index.html')
    else:
        return "بيانات الدخول غير صحيحة", 401
