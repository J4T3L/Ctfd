import hashlib
from flask import Blueprint, render_template, request, flash, redirect, url_for

hash_bp = Blueprint('weak_hash', __name__, template_folder='../templates/weak_hash', url_prefix='/weak_hash')

# MD5 hash of password 'password123'
ADMIN_PASSWORD_MD5 = hashlib.md5(b"password123").hexdigest()

@hash_bp.route('/')
def index():
    return render_template('weak_hash/login.html')

@hash_bp.route('/login', methods=['POST'])
def login():
    password = request.form.get('password', '')
    user_hash = hashlib.md5(password.encode('utf-8')).hexdigest()
    
    if user_hash == ADMIN_PASSWORD_MD5:
        flag = "CTF{md5_w34k_h4sh_cr4ck3d_2026}"
        return render_template('weak_hash/dashboard.html', flag=flag, hash=user_hash)
    else:
        flash(f"Invalid Password! Generated Hash: {user_hash}", "error")
        return redirect(url_for('weak_hash.index'))
