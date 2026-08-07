from flask import Blueprint, render_template, request

xss_bp = Blueprint('xss_reflected', __name__, template_folder='../templates/xss_reflected', url_prefix='/xss_reflected')

@xss_bp.route('/')
def index():
    query = request.args.get('q', '')
    flag = None
    
    # Flag revealed if XSS payload detected or specific query parameter
    if '<script>' in query.lower() or 'alert(' in query.lower() or 'onerror' in query.lower():
        flag = "CTF{xss_r3fl3c73d_s3cr37_l34k_2026}"

    return render_template('xss_reflected/index.html', query=query, flag=flag)
