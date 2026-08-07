import os
from flask import Flask, render_template

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

app = Flask(__name__)
app.secret_key = "ctf_web_10_challenge_master_key_2026"

# Register all 10 CTF Blueprints
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

@app.route('/')
def portal():
    return render_template('portal.html')

if __name__ == '__main__':
    init_sqli_db()
    app.run(host='0.0.0.0', port=8000, debug=False)
else:
    init_sqli_db()
