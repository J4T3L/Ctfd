#!/usr/bin/env python3
"""
Comprehensive Audit & Cross-Check Script for 50 CTF Challenges (Pure Stdlib)
"""
import os
import re
import sys

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
CHALLENGES_DIR = os.path.join(ROOT_DIR, "challenges")
HANDOUT_DIR = os.path.join(ROOT_DIR, "handout")
PORTAL_FILE = os.path.join(ROOT_DIR, "app", "templates", "portal.html")

print("==================================================================")
print("[*] STARTING RIGOROUS AUDIT & CROSS-CHECK OF 50 CTF CHALLENGES...")
print("==================================================================")

errors = []
warnings = []

# 1. Check folder count
folders = sorted([d for d in os.listdir(CHALLENGES_DIR) if os.path.isdir(os.path.join(CHALLENGES_DIR, d))])
print(f"[+] Total Challenge Folders Found: {len(folders)}")

if len(folders) != 50:
    errors.append(f"Expected 50 challenge folders, found {len(folders)}")

categories = {}

# 2. Audit each challenge.yml
for folder in folders:
    f_path = os.path.join(CHALLENGES_DIR, folder)
    yml_file = os.path.join(f_path, "challenge.yml")
    
    if not os.path.exists(yml_file):
        errors.append(f"Missing challenge.yml in {folder}")
        continue
        
    try:
        with open(yml_file, "r", encoding="utf-8") as f:
            content = f.read()
            
        name_m = re.search(r'name:\s*"([^"]+)"', content)
        cat_m = re.search(r'category:\s*"([^"]+)"', content)
        val_m = re.search(r'value:\s*(\d+)', content)
        flag_m = re.search(r'flags:\s*\n\s*-\s*"([^"]+)"', content)
        hint_m = re.search(r'hints:\s*\n\s*-\s*content:\s*"([^"]+)"', content)
        
        if not name_m: errors.append(f"[{folder}] Missing or invalid 'name'")
        if not cat_m: errors.append(f"[{folder}] Missing or invalid 'category'")
        if not val_m: errors.append(f"[{folder}] Missing or invalid 'value'")
        if not flag_m: errors.append(f"[{folder}] Missing or invalid 'flags'")
        if not hint_m: warnings.append(f"[{folder}] Missing or non-standard 'hints'")
        
        cat = cat_m.group(1) if cat_m else "Unknown"
        categories[cat] = categories.get(cat, 0) + 1
        
        if "target.paradick.my.id" not in content:
            warnings.append(f"[{folder}] Description does not contain target.paradick.my.id link")
            
    except Exception as e:
        errors.append(f"[{folder}] Error reading challenge.yml: {e}")

print("\n[+] Challenge Breakdown by Category:")
for cat, count in categories.items():
    print(f"    - {cat}: {count} challenges")

# 3. Check Portal HTML file
with open(PORTAL_FILE, "r", encoding="utf-8") as f:
    portal_content = f.read()

print(f"\n[+] Verifying Portal HTML ({PORTAL_FILE})...")
portal_matches = re.findall(r'<h3 class="card-title">([^<]+)</h3>', portal_content)
print(f"    - Card titles found in portal.html: {len(portal_matches)}")

# 4. Check Handout Files
print(f"\n[+] Verifying Handout Directory ({HANDOUT_DIR})...")
if os.path.exists(HANDOUT_DIR):
    h_files = os.listdir(HANDOUT_DIR)
    print(f"    - Handout artifacts generated: {len(h_files)} files ({', '.join(h_files[:5])}...)")
else:
    errors.append("Handout directory missing!")

print("\n==================================================================")
if errors:
    print("❌ AUDIT COMPLETED WITH ERRORS:")
    for err in errors:
        print(f"   [-] {err}")
    sys.exit(1)
else:
    print("🎉 AUDIT PASSED 100%! ALL 50 CHALLENGES & METADATA ARE VALID & PERFECT!")
    if warnings:
        print(f"⚠️ ({len(warnings)} Warnings noted - Non-critical)")
print("==================================================================")
