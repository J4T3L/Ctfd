from flask import Blueprint, request

xxe_bp = Blueprint('xxe_lab', __name__)

@xxe_bp.route('/xxe_lab/', methods=['GET', 'POST'])
def xxe():
    if request.method == 'POST':
        data_str = request.data.decode('utf-8', errors='ignore')
        if 'SYSTEM' in data_str or 'ENTITY' in data_str or 'flag' in data_str:
            return "<response><status>success</status><data>CTF{xxe_xml_3x73rn4l_3n717y_2026}</data></response>"
        return "<response><status>success</status><data>XML Parsed OK</data></response>"
    return "XXE XML Parser Endpoint Ready"
