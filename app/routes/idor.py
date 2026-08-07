from flask import Blueprint, render_template, request

idor_bp = Blueprint('idor', __name__, template_folder='../templates/idor', url_prefix='/idor')

USERS_DB = {
    "101": {"name": "Bob Marley", "email": "bob@company.local", "role": "User", "note": "Standard employee profile."},
    "102": {"name": "Alice Smith", "email": "alice@company.local", "role": "User", "note": "Welcome to DevPortal! Currently logged in as User #102."},
    "100": {"name": "System Administrator", "email": "admin@company.local", "role": "Administrator", "note": "CONFIDENTIAL FLAG: CTF{1d0r_pr1v1l3g3_3sc4l4710n_2026}"}
}

@idor_bp.route('/')
def index():
    user_id = request.args.get('user_id', '102')
    user_info = USERS_DB.get(user_id)

    if not user_info:
        user_info = {"name": "Unknown User", "email": "N/A", "role": "N/A", "note": "User account ID not found."}

    return render_template('idor/profile.html', user_id=user_id, user=user_info)
