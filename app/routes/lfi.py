from flask import Blueprint, request, render_template

lfi_bp = Blueprint('lfi', __name__)

@lfi_bp.route('/lfi/')
def lfi():
    page = request.args.get('page', 'welcome.txt')
    if 'flag' in page.lower():
        return "<h3>File Contents of flag.txt:</h3><pre>CTF{lfi_path_tr4v3rs4l_m4st3r_2026}</pre>"
    elif page == 'welcome.txt':
        content = "Welcome to System Compliance Log Viewer. Select a log file to view."
    else:
        content = f"Log File: {page} loaded successfully."
    return render_template('portal.html', lfi_content=content)
