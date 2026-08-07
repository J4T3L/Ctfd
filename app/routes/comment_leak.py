from flask import Blueprint, render_template

comment_bp = Blueprint('comment_leak', __name__, template_folder='../templates/comment_leak', url_prefix='/hidden_comment')

@comment_bp.route('/')
def index():
    return render_template('comment_leak/index.html')

@comment_bp.route('/secret_admin_dashboard_99')
def secret_admin():
    flag = "CTF{h7ml_c0mm3n7_l34k_d1sc0v3r3d_2026}"
    return render_template('comment_leak/admin.html', flag=flag)
