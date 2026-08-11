import os
from flask import Flask, send_from_directory, render_template, request

from routes.ssti import ssti_bp
from routes.sqli import sqli_bp, init_sqli_db
from routes.comment_leak import comment_bp
from routes.cookie_lab import cookie_bp
from routes.idor import idor_bp
from routes.lfi import lfi_bp
from routes.rce_ping import rce_bp
from routes.ssrf import ssrf_bp
from routes.jwt_lab import jwt_bp
from routes.pickle_rce import pickle_bp
from routes.xss_reflected import xss_bp
from routes.robots_secret import robots_bp
from routes.weak_hash import hash_bp
from routes.xxe_lab import xxe_bp
from routes.logic_shop import logic_bp

DIST_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../frontend/dist'))

app = Flask(__name__, static_folder=os.path.join(DIST_DIR, 'assets'), static_url_path='/assets')
app.secret_key = "ctf_web_15_challenge_master_key_2026"

# Register all 15 CTF Blueprints
app.register_blueprint(sqli_bp)
app.register_blueprint(comment_bp)
app.register_blueprint(cookie_bp)
app.register_blueprint(idor_bp)
app.register_blueprint(lfi_bp)
app.register_blueprint(rce_bp)
app.register_blueprint(ssrf_bp)
app.register_blueprint(jwt_bp)
app.register_blueprint(ssti_bp)
app.register_blueprint(pickle_bp)
app.register_blueprint(xss_bp)
app.register_blueprint(robots_bp)
app.register_blueprint(hash_bp)
app.register_blueprint(xxe_bp)
app.register_blueprint(logic_bp)

# Catch-all route to serve React Single Page Application
@app.route('/')
@app.route('/dashboard')
@app.route('/app/<path:path>')
def serve_react(path=''):
    if os.path.exists(DIST_DIR):
        return send_from_directory(DIST_DIR, 'index.html')
    else:
        return render_template('portal.html')

if __name__ == '__main__':
    init_sqli_db()
    app.run(host='0.0.0.0', port=8000, debug=False)
else:
    init_sqli_db()
