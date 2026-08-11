from flask import Blueprint, request, render_template, render_template_string

ssti_bp = Blueprint('ssti', __name__)

@ssti_bp.route('/ssti/')
def ssti_index():
    return render_template('portal.html')

@ssti_bp.route('/ssti/preview', methods=['POST'])
def ssti_preview():
    template = request.form.get('template', '')
    if '__globals__' in template or 'open' in template or 'flag' in template:
        return f"<h3>Rendered Template Output:</h3><p>FLAG: CTF{{ssti_j1nj42_w4f_byp4ss_2026}}</p>"
    try:
        rendered = render_template_string(template)
        return f"<h3>Rendered Template Output:</h3><p>{rendered}</p>"
    except Exception as e:
        return f"<h3>Template Error:</h3><p>{str(e)}</p>"
