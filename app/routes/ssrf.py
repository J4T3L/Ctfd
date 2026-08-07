import urllib.request
from flask import Blueprint, render_template, request

ssrf_bp = Blueprint('ssrf', __name__, template_folder='../templates/ssrf', url_prefix='/ssrf')

@ssrf_bp.route('/', methods=['GET', 'POST'])
def index():
    fetched_content = ""
    target_url = ""
    error = None
    
    if request.method == 'POST':
        target_url = request.form.get('url', 'http://httpbin.org/get')
        try:
            req = urllib.request.Request(target_url, headers={'User-Agent': 'CyberVault-Fetcher/1.0'})
            with urllib.request.urlopen(req, timeout=4) as res:
                fetched_content = res.read().decode('utf-8', errors='ignore')
        except Exception as e:
            error = f"Fetch Error: {str(e)}"
            
    return render_template('ssrf/index.html', fetched_content=fetched_content, target_url=target_url, error=error)

@ssrf_bp.route('/internal/admin/secret')
def internal_secret():
    # Only accessible via SSRF loopback request
    return "SECRET SYSTEM SERVICE ONLINE: CTF{ssrf_1n73rn4l_n37w0rk_4cc3ss_2026}"
