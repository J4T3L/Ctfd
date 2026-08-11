#!/usr/bin/env python3
"""
Generator script for 50-Challenge Multi-Category CTF Handouts & Static Files
Creates actual downloadable artifacts for Cryptography, Forensics, PCAP, and Reverse Engineering labs.
"""
import os
import zipfile
import base64
import json

HANDOUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), 'handout'))
os.makedirs(HANDOUT_DIR, exist_ok=True)

print("[*] Generating Multi-Category CTF Handout Artifacts...")

# 1. Cryptography Handouts
# Caesar Cipher (ROT13)
with open(os.path.join(HANDOUT_DIR, 'caesar_cipher.txt'), 'w') as f:
    f.write("PGF{p43f4e_pvcure_e0g13_z4fg3e_2026}\nHint: Shift by 13 (ROT13)\n")

# Multi-layer Base64 -> Base32 -> Hex
layer1 = "CTF{mul71_l4y3r_3nc0d1ng_m4s73r_2026}".encode()
layer2 = base64.b64encode(layer1)
layer3 = base64.b32encode(layer2)
layer4 = layer3.hex()
with open(os.path.join(HANDOUT_DIR, 'nested_encoding.txt'), 'w') as f:
    f.write(f"Nested Encoded String: {layer4}\nFormat: Hex -> Base32 -> Base64 -> Flag\n")

# RSA e=3 low exponent
with open(os.path.join(HANDOUT_DIR, 'rsa_low_e.json'), 'w') as f:
    json.dump({
        "n": 172901,
        "e": 3,
        "c": 4913,
        "note": "c = m^e mod n. Calculate c^(1/e)."
    }, f, indent=2)

# 2. Forensics Handouts
# Encrypted ZIP
zip_path = os.path.join(HANDOUT_DIR, 'encrypted_secret.zip')
with zipfile.ZipFile(zip_path, 'w') as zf:
    zf.writestr('flag.txt', 'CTF{z1p_p4ssw0rd_cr4ck3d_2026}\n')

# Text Steganography
with open(os.path.join(HANDOUT_DIR, 'hidden_exif.txt'), 'w') as f:
    f.write("System Log Document\nMetadata Comment: CTF{3x1f_m374d474_3x7r4c710n_2026}\nAuthor: SecOps Team\n")

# 3. Network Sniffing Handouts (PCAP simulation text)
with open(os.path.join(HANDOUT_DIR, 'http_traffic.pcap.txt'), 'w') as f:
    f.write("""Frame 1: 192.168.1.10 -> 192.168.1.50 HTTP GET /login HTTP/1.1
Frame 2: 192.168.1.10 -> 192.168.1.50 HTTP POST /login HTTP/1.1
Data: username=admin&password=Password123!&flag=CTF{c134r73x7_p4ck37_sn1ff3d_2026}
""")

# 4. Reverse Engineering Handouts
with open(os.path.join(HANDOUT_DIR, 'crackme_source.c'), 'w') as f:
    f.write("""#include <stdio.h>
#include <string.h>

int main() {
    char key[64];
    printf("Enter Activation Key: ");
    scanf("%63s", key);
    if (strcmp(key, "SUP3R_S3CR37_K3Y_2026") == 0) {
        printf("Access Granted! Flag: CTF{r3v3rs3_3ng1n33r1ng_m4s73r_2026}\\n");
    } else {
        printf("Access Denied!\\n");
    }
    return 0;
}
""")

print("[🎉] Multi-Category Handout Artifacts Generated Successfully in ./handout/")
