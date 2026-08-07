import base64
import pickle
from flask import Blueprint, render_template, request, make_response, redirect, url_for

pickle_bp = Blueprint('pickle_rce', __name__, template_folder='../templates/pickle_rce', url_prefix='/pickle_rce')

class UserProfile:
    def __init__(self, username, role="guest"):
        self.username = username
        self.role = role

@pickle_bp.route('/')
def index():
    session_cookie = request.cookies.get('pickle_session')
    
    if not session_cookie:
        default_obj = UserProfile("guest", "guest")
        serialized = base64.b64encode(pickle.dumps(default_obj)).decode('utf-8')
        resp = make_response(redirect(url_for('pickle_rce.index')))
        resp.set_cookie('pickle_session', serialized)
        return resp

    user_obj = None
    error = None
    
    try:
        raw_bytes = base64.b64decode(session_cookie)
        # Vulnerable Python Pickle Deserialization
        user_obj = pickle.loads(raw_bytes)
    except Exception as e:
        error = f"Deserialization Error: {str(e)}"

    return render_template('pickle_rce/index.html', user_obj=user_obj, session_cookie=session_cookie, error=error)
