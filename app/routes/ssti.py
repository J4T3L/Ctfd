import os
from flask import Blueprint, request, render_template, render_template_string, flash, redirect, url_for

ssti_bp = Blueprint('ssti', __name__, template_folder='../templates/ssti', url_prefix='/ssti')

FORBIDDEN_KEYWORDS = ['import', 'os', 'system', 'subprocess', 'mro', 'eval', 'exec']

def is_safe_template(template_str):
    lowered = template_str.lower()
    for kw in FORBIDDEN_KEYWORDS:
        if kw in lowered:
            return False, f"Keyword '{kw}' is blocked by CyberVault WAF Security Filter!"
    return True, None

@ssti_bp.route('/')
def index():
    return render_template('ssti/index.html')

@ssti_bp.route('/generator', methods=['GET'])
def generator():
    default_template = """<div class="report-card">
    <h2>Audit Report: {{ report_name }}</h2>
    <p>Auditor: <strong>{{ auditor }}</strong></p>
    <div class="status-badge status-passed">Status: {{ status }}</div>
    <hr class="divider"/>
    <p class="summary-text">{{ summary }}</p>
</div>"""
    return render_template('ssti/generator.html', default_template=default_template)

@ssti_bp.route('/preview', methods=['POST'])
def preview():
    report_name = request.form.get('report_name', 'Security Audit 2026')
    auditor = request.form.get('auditor', 'SecOps Team')
    status = request.form.get('status', 'PASSED')
    summary = request.form.get('summary', 'No critical vulnerabilities detected.')
    user_template = request.form.get('template', '')

    if not user_template:
        flash("Template content cannot be empty!", "error")
        return redirect(url_for('ssti.generator'))

    is_safe, error_msg = is_safe_template(user_template)
    if not is_safe:
        return render_template('ssti/generator.html', 
                               default_template=user_template, 
                               waf_error=error_msg,
                               report_name=report_name,
                               auditor=auditor,
                               status=status,
                               summary=summary)

    try:
        rendered_output = render_template_string(
            user_template,
            report_name=report_name,
            auditor=auditor,
            status=status,
            summary=summary,
            request=request
        )
        return render_template('ssti/render.html', 
                               rendered_output=rendered_output, 
                               raw_template=user_template)
    except Exception as e:
        return render_template('ssti/generator.html', 
                               default_template=user_template, 
                               waf_error=f"Template Rendering Error: {str(e)}",
                               report_name=report_name,
                               auditor=auditor,
                               status=status,
                               summary=summary)
