import subprocess
from flask import Blueprint, render_template, request

rce_bp = Blueprint('rce_ping', __name__, template_folder='../templates/rce_ping', url_prefix='/rce_ping')

@rce_bp.route('/', methods=['GET', 'POST'])
def index():
    output = ""
    target_ip = ""
    
    if request.method == 'POST':
        target_ip = request.form.get('ip', '127.0.0.1')
        
        # Vulnerable Command Injection (Executing shell command directly)
        cmd = f"ping -c 2 {target_ip}"
        try:
            output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, timeout=5).decode('utf-8', errors='ignore')
        except subprocess.CalledProcessError as e:
            output = e.output.decode('utf-8', errors='ignore')
        except Exception as e:
            output = f"Execution error: {str(e)}"
            
    return render_template('rce_ping/index.html', output=output, target_ip=target_ip)
