import xml.etree.ElementTree as ET
from flask import Blueprint, render_template, request, flash

xxe_bp = Blueprint('xxe_lab', __name__, template_folder='../templates/xxe_lab', url_prefix='/xxe_lab')

@xxe_bp.route('/', methods=['GET', 'POST'])
def index():
    parsed_output = ""
    error = None
    xml_data = ""
    
    if request.method == 'POST':
        xml_data = request.form.get('xml_data', '')
        
        # XXE check simulation & parsing
        if '<!ENTITY' in xml_data or 'SYSTEM' in xml_data or 'file:' in xml_data:
            # Parse XXE entity injection to read /flag.txt
            if 'flag.txt' in xml_data or 'file:' in xml_data:
                try:
                    with open('flag.txt', 'r') as f:
                        flag_content = f.read().strip()
                    parsed_output = f"Parsed XML Element [entity]: {flag_content}"
                except Exception as e:
                    error = f"XXE Entity Execution Error: {str(e)}"
            else:
                parsed_output = "Parsed XML Element [entity]: Entity resolved successfully."
        else:
            try:
                root = ET.fromstring(xml_data)
                parsed_output = f"Root Element: <{root.tag}> | Text Content: {root.text}"
            except Exception as e:
                error = f"XML Parsing Error: {str(e)}"
                
    return render_template('xxe_lab/index.html', parsed_output=parsed_output, xml_data=xml_data, error=error)
