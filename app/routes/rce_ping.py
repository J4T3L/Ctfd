from flask import Blueprint, request

rce_bp = Blueprint('rce_ping', __name__)

@rce_bp.route('/rce_ping/', methods=['GET', 'POST'])
def rce():
    output = ""
    if request.method == 'POST':
        host = request.form.get('host', '')
        if ';' in host or '|' in host or '&' in host or 'cat' in host:
            output = "PING 127.0.0.1 (127.0.0.1) 56(84) bytes of data.\n64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.042 ms\nFlag Output: CTF{rce_c0mm4nd_1nj3ct10n_m4st3r_2026}"
        else:
            output = f"PING {host} (127.0.0.1) 56(84) bytes of data.\n64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.035 ms"
        return f"<h3>Ping Diagnostic Output:</h3><pre>{output}</pre>"
    return "Ping Diagnostic Utility Endpoint Ready"
