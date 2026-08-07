import os
from flask import Blueprint, render_template, request

lfi_bp = Blueprint('lfi', __name__, template_folder='../templates/lfi', url_prefix='/lfi')

@lfi_bp.route('/')
def index():
    filename = request.args.get('page', 'welcome.txt')
    
    # Vulnerable file inclusion path logic
    base_dir = os.path.join(os.path.dirname(__file__), '../templates/lfi/pages')
    file_path = os.path.abspath(os.path.join(base_dir, filename))
    
    content = ""
    error = None
    
    # Path traversal check bypassable with ../ or /flag.txt
    if os.path.exists(filename):
        target_file = filename
    elif os.path.exists(file_path):
        target_file = file_path
    elif os.path.exists(os.path.join('/', filename.lstrip('/'))):
        target_file = os.path.join('/', filename.lstrip('/'))
    else:
        target_file = None

    if target_file and os.path.isfile(target_file):
        try:
            with open(target_file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
        except Exception as e:
            error = f"Error reading file: {str(e)}"
    else:
        error = f"File '{filename}' not found!"

    return render_template('lfi/viewer.html', filename=filename, content=content, error=error)
