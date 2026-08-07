import base64
from flask import Blueprint, render_template, request, make_response, redirect, url_for

cookie_bp = Blueprint('cookie_lab', __name__, template_folder='../templates/cookie_lab', url_prefix='/cookie_lab')

@cookie_bp.route('/')
def index():
    user_cookie = request.cookies.get('user_session')
    
    if not user_cookie:
        # Default unprivileged user cookie: user:guest (base64 encoded)
        default_cookie = base64.b64encode(b"role=guest").decode('utf-8')
        resp = make_response(redirect(url_for('cookie_lab.index')))
        resp.set_cookie('user_session', default_cookie)
        return resp

    try:
        decoded = base64.b64decode(user_cookie).decode('utf-8')
    except Exception:
        decoded = "role=guest"

    is_admin = "role=admin" in decoded
    flag = "CTF{c00k13_m4n1pul4710n_m4s73r_2026}" if is_admin else None

    return render_template('cookie_lab/index.html', decoded=decoded, is_admin=is_admin, flag=flag)

@cookie_bp.route('/reset')
def reset():
    default_cookie = base64.b64encode(b"role=guest").decode('utf-8')
    resp = make_response(redirect(url_for('cookie_lab.index')))
    resp.set_cookie('user_session', default_cookie)
    return resp
