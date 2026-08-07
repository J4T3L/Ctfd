from flask import Blueprint, render_template, Response

robots_bp = Blueprint('robots_secret', __name__, template_folder='../templates/robots_secret', url_prefix='/robots_secret')

@robots_bp.route('/')
def index():
    return render_template('robots_secret/index.html')

@robots_bp.route('/robots.txt')
def robots_txt():
    content = """User-agent: *
Disallow: /robots_secret/hidden_staging_backup_2026/
"""
    return Response(content, mimetype='text/plain')

@robots_bp.route('/hidden_staging_backup_2026/')
def hidden_staging():
    flag = "CTF{r0b07s_7x7_d1sc0v3ry_m4s73r_2026}"
    return render_template('robots_secret/staging.html', flag=flag)
