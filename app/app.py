import os
from flask import Flask, render_template
from routes.ssti import ssti_bp
from routes.sqli import sqli_bp, init_sqli_db

app = Flask(__name__)
app.secret_key = "cybervault_ctf_portal_unified_key_2026"

# Register Blueprints
app.register_blueprint(ssti_bp)
app.register_blueprint(sqli_bp)

@app.route('/')
def portal():
    return render_template('portal.html')

if __name__ == '__main__':
    init_sqli_db()
    app.run(host='0.0.0.0', port=8000, debug=False)
else:
    init_sqli_db()
