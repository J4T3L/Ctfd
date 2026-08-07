import hmac
import hashlib
import base64
import json
from flask import Blueprint, render_template, request, make_response, redirect, url_for

jwt_bp = Blueprint('jwt_lab', __name__, template_folder='../templates/jwt_lab', url_prefix='/jwt_lab')

# Vulnerable Weak JWT secret key
JWT_SECRET = "secret123"

def b64_encode(data):
    return base64.urlsafe_b64encode(data).decode('utf-8').rstrip('=')

def b64_decode(data):
    padding = '=' * (4 - (len(data) % 4))
    return base64.urlsafe_b64decode(data + padding)

def create_jwt(payload_dict):
    header = {"alg": "HS256", "typ": "JWT"}
    header_b64 = b64_encode(json.dumps(header).encode('utf-8'))
    payload_b64 = b64_encode(json.dumps(payload_dict).encode('utf-8'))
    
    signature_input = f"{header_b64}.{payload_b64}".encode('utf-8')
    sig = hmac.new(JWT_SECRET.encode('utf-8'), signature_input, hashlib.sha256).digest()
    sig_b64 = b64_encode(sig)
    
    return f"{header_b64}.{payload_b64}.{sig_b64}"

def verify_jwt(token):
    try:
        parts = token.split('.')
        if len(parts) != 3:
            return None
        
        header_b64, payload_b64, sig_b64 = parts
        header = json.loads(b64_decode(header_b64))
        
        # None algorithm confusion vulnerability check
        if header.get('alg') == 'none' or header.get('alg') == 'NONE':
            payload = json.loads(b64_decode(payload_b64))
            return payload

        signature_input = f"{header_b64}.{payload_b64}".encode('utf-8')
        expected_sig = b64_encode(hmac.new(JWT_SECRET.encode('utf-8'), signature_input, hashlib.sha256).digest())
        
        if hmac.compare_digest(sig_b64, expected_sig):
            payload = json.loads(b64_decode(payload_b64))
            return payload
    except Exception:
        pass
    return None

@jwt_bp.route('/')
def index():
    token = request.cookies.get('jwt_auth')
    if not token:
        token = create_jwt({"user": "guest", "role": "user"})
        resp = make_response(redirect(url_for('jwt_lab.index')))
        resp.set_cookie('jwt_auth', token)
        return resp

    payload = verify_jwt(token)
    is_admin = False
    flag = None
    
    if payload and payload.get('role') == 'admin':
        is_admin = True
        flag = "CTF{jw7_w34k_s3cr37_3sc4l4710n_2026}"

    return render_template('jwt_lab/index.html', token=token, payload=payload, is_admin=is_admin, flag=flag)
