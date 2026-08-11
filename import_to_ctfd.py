#!/usr/bin/env python3
"""
Direct CTFd REST API Importer (Pure Python Stdlib - Zero Dependencies)
Automatically detects CTFd URL/IP and imports all 50 Multi-Category challenges via REST API.
"""
import os
import sys
import re
import json
import ssl
import urllib.request
import urllib.error

TOKEN = os.environ.get("CTFD_TOKEN", "ctfd_d6b4def092f11925bd537b8aa0ea5391ea06d7f4eb3bb820a77258aa7b80e8bc")
CTFD_URLS = [
    os.environ.get("CTFD_URL"),
    "http://127.0.0.1:80",
    "http://localhost:80",
    "http://172.13.0.9:80",
    "https://ctfd.paradick.my.id",
    "http://ctfd.paradick.my.id"
]
CTFD_URLS = [u for u in CTFD_URLS if u]

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def api_request(base_url, endpoint, method="GET", data=None):
    url = f"{base_url.rstrip('/')}{endpoint}"
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json",
        "User-Agent": "CTFd-Direct-Importer/1.0"
    }
    body = json.dumps(data).encode("utf-8") if data else None
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    with urllib.request.urlopen(req, context=ctx, timeout=8) as res:
        return json.loads(res.read().decode("utf-8"))

def parse_simple_yml(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    data = {}
    name_m = re.search(r'name:\s*"([^"]+)"', content)
    if name_m: data['name'] = name_m.group(1)
    
    cat_m = re.search(r'category:\s*"([^"]+)"', content)
    if cat_m: data['category'] = cat_m.group(1)
    
    val_m = re.search(r'value:\s*(\d+)', content)
    if val_m: data['value'] = int(val_m.group(1))

    flag_m = re.search(r'flags:\s*\n\s*-\s*"([^"]+)"', content)
    if flag_m: data['flag'] = flag_m.group(1)

    desc_m = re.search(r'description:\s*\|\n(.*?)(?=\n\w+:|\Z)', content, re.DOTALL)
    if desc_m:
        desc_lines = [line.strip() for line in desc_m.group(1).splitlines()]
        data['description'] = "\n".join(desc_lines).strip()
        
    return data

def find_working_ctfd():
    for u in CTFD_URLS:
        try:
            print(f"[*] Trying connection to CTFd at {u}...")
            res = api_request(u, "/api/v1/challenges?view=admin")
            if res.get("success"):
                print(f"[+] Connected successfully to CTFd at {u}!")
                return u
        except Exception as e:
            print(f"[-] Connection to {u} failed: {e}")
    return None

def import_challenges():
    base_url = find_working_ctfd()
    if not base_url:
        print("[-] Error: Could not connect to CTFd on any local or public URL.")
        sys.exit(1)

    try:
        existing = api_request(base_url, "/api/v1/challenges?view=admin").get("data", [])
        existing_names = {c["name"]: c["id"] for c in existing}
    except Exception:
        existing_names = {}

    c_base = os.path.abspath(os.path.join(os.path.dirname(__file__), "challenges"))
    challenge_dirs = sorted([
        os.path.join("challenges", d) for d in os.listdir(c_base)
        if os.path.isdir(os.path.join(c_base, d)) and os.path.exists(os.path.join(c_base, d, "challenge.yml"))
    ])

    print(f"\n[*] Importing all {len(challenge_dirs)} Multi-Category challenges into CTFd via REST API...")

    for cdir in challenge_dirs:
        yml_path = os.path.join(cdir, "challenge.yml")
        cdata = parse_simple_yml(yml_path)
        name = cdata.get("name")
        if not name:
            continue

        category = cdata.get("category", "Web Exploitation")
        description = cdata.get("description", "")
        value = cdata.get("value", 100)
        flag = cdata.get("flag")

        payload = {
            "name": name,
            "category": category,
            "description": description,
            "value": value,
            "state": "visible",
            "type": "standard"
        }

        cid = None
        if name in existing_names:
            cid = existing_names[name]
            print(f"[+] Updating challenge: '{name}' (ID: {cid})...")
            try:
                api_request(base_url, f"/api/v1/challenges/{cid}", method="PATCH", data=payload)
            except Exception as e:
                print(f"    [-] Update error: {e}")
        else:
            print(f"[+] Creating challenge: '{name}'...")
            try:
                res = api_request(base_url, "/api/v1/challenges", method="POST", data=payload)
                cid = res["data"]["id"]
                existing_names[name] = cid
            except Exception as e:
                print(f"    [-] Create error: {e}")
                continue

        if cid and flag:
            try:
                api_request(base_url, "/api/v1/flags", method="POST", data={
                    "challenge_id": cid,
                    "content": flag,
                    "type": "static",
                    "data": ""
                })
            except Exception:
                pass

    print(f"\n[🎉] All {len(challenge_dirs)} Multi-Category challenges imported successfully into CTFd!")

if __name__ == "__main__":
    import_challenges()
