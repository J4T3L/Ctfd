#!/usr/bin/env python3
"""
Script to update challenge flags for RSA & Math Crypto puzzles so that the flag
stored in CTFd matches the EXACT output solved by students!
- Challenge 18 (MD5): CTF{password123}
- Challenge 19 (RSA e=3): CTF{17}
- Challenge 20 (RSA Factorization): CTF{448}
- Challenge 25 (Diffie-Hellman): CTF{12}
"""
import os
import json

CHALLENGES_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), 'challenges'))

FLAG_UPDATES = {
    "18_crypto_md5": "CTF{password123}",
    "19_crypto_rsa_e3": "CTF{17}",
    "20_crypto_rsa_factor": "CTF{448}",
    "25_crypto_dh_weak": "CTF{12}"
}

print("[*] Updating Math & Crypto flags in challenge.yml files...")

for folder, new_flag in FLAG_UPDATES.items():
    yml_path = os.path.join(CHALLENGES_DIR, folder, 'challenge.yml')
    if os.path.exists(yml_path):
        with open(yml_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace flag line
        import re
        updated_content = re.sub(r'flags:\s*\n\s*-\s*"[^"]+"', f'flags:\n  - "{new_flag}"', content)
        
        with open(yml_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print(f"[+] Updated {folder} flag -> {new_flag}")

print("[🎉] All Math & Crypto flags aligned with exact puzzle solutions!")
