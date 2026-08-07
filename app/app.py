import re
from flask import Flask, request, render_template, render_template_string, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = "cybervault_super_secret_session_key_2026"

# Basic WAF / Blacklist for CTF challenge filtering
# Blocks direct calls to 'os', 'system', 'subprocess', 'import', 'mro'
FORBIDDEN_KEYWORDS = ['import', 'os', 'system', 'subprocess', 'mro', 'eval', 'exec']

def is_safe_template(template_str):
    """
    Check if the user-supplied template contains dangerous keywords.
    Note: Filter performs case-insensitive check on obvious dangerous keywords.
    """
    lowered = template_str.lower()
    for kw in FORBIDDEN_KEYWORDS:
        if kw in lowered:
            return False, f"Keyword '{kw}' is blocked by CyberVault WAF Security Filter!"
    return True, None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generator', methods=['GET'])
def generator():
    default_template = """<div class="report-card">
    <h2>Audit Report: {{ report_name }}</h2>
    <p>Auditor: <strong>{{ auditor }}</strong></p>
    <div class="status-badge status-passed">Status: {{ status }}</div>
    <hr class="divider"/>
    <p class="summary-text">{{ summary }}</p>
</div>"""
    return render_template('generator.html', default_template=default_template)

@app.route('/preview', methods=['POST'])
def preview():
    report_name = request.form.get('report_name', 'Security Audit 2026')
    auditor = request.form.get('auditor', 'SecOps Team')
    status = request.form.get('status', 'PASSED')
    summary = request.form.get('summary', 'No critical vulnerabilities detected.')
    user_template = request.form.get('template', '')

    if not user_template:
        flash("Template content cannot be empty!", "error")
        return redirect(url_for('generator'))

    # WAF Check
    is_safe, error_msg = is_safe_template(user_template)
    if not is_safe:
        return render_template('generator.html', 
                               default_template=user_template, 
                               waf_error=error_msg,
                               report_name=report_name,
                               auditor=auditor,
                               status=status,
                               summary=summary)

    try:
        # Vulnerable render string allowing Jinja2 SSTI
        rendered_output = render_template_string(
            user_template,
            report_name=report_name,
            auditor=auditor,
            status=status,
            summary=summary,
            request=request
        )
        return render_template('render.html', 
                               rendered_output=rendered_output, 
                               raw_template=user_template)
    except Exception as e:
        return render_template('generator.html', 
                               default_template=user_template, 
                               waf_error=f"Template Rendering Error: {str(e)}",
                               report_name=report_name,
                               auditor=auditor,
                               status=status,
                               summary=summary)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)
