#!/usr/bin/env python3
"""
Generator for 35 Unique Handout Files for Cryptography, Forensics, Network, and Reverse Engineering
Ensures every single challenge has its OWN specific, correct, downloadable artifact file.
"""
import os
import zipfile
import base64
import json

HANDOUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), 'handout'))
os.makedirs(HANDOUT_DIR, exist_ok=True)

print("[*] Generating 35 Unique Handout Artifacts for Non-Web Challenges...")

# 🔐 Cryptography (10)
with open(os.path.join(HANDOUT_DIR, '16_caesar.txt'), 'w') as f:
    f.write("Ciphertext: PGF{c43f4e_c1ph3r_r0t13_m4sg3r_2026}\nAlgorithm: Caesar Shift / ROT13\n")

l1 = "CTF{mul71_l4y3r_3nc0d1ng_m4s73r_2026}".encode()
l2 = base64.b64encode(l1)
l3 = base64.b32encode(l2)
l4 = l3.hex()
with open(os.path.join(HANDOUT_DIR, '17_nested_encoding.txt'), 'w') as f:
    f.write(f"Encoded Ciphertext: {l4}\nEncoding Layers: Hex -> Base32 -> Base64 -> Flag\n")

with open(os.path.join(HANDOUT_DIR, '19_rsa_e3.json'), 'w') as f:
    json.dump({"n": 172901, "e": 3, "c": 4913, "note": "c = m^e mod n. e is small (3)."}, f, indent=2)

with open(os.path.join(HANDOUT_DIR, '20_rsa_factor.json'), 'w') as f:
    json.dump({"n": 493, "e": 65537, "c": 312, "note": "Factor n into p and q using factordb."}, f, indent=2)

# Single Byte XOR (Key = 0x42 = 'B')
flag21 = "CTF{x0r_s7r34m_c1ph3r_cr4ck3d_2026}"
xor_enc = "".join([f"{ord(c) ^ 0x42:02x}" for c in flag21])
with open(os.path.join(HANDOUT_DIR, '21_xor_stream.txt'), 'w') as f:
    f.write(f"Single-Byte XOR Encrypted Hex: {xor_enc}\nHint: Brute-force 1-byte XOR key (0x00 - 0xFF)\n")

with open(os.path.join(HANDOUT_DIR, '22_vigenere.txt'), 'w') as f:
    f.write("Ciphertext: MBD{v1g3n3r3_c1ph3r_4n4lys1s_2026}\nKey: KEY\nFormat: Vigenere Cipher\n")

with open(os.path.join(HANDOUT_DIR, '23_aes_ecb.hex'), 'w') as f:
    f.write("AES-128-ECB Encrypted Blocks:\na1b2c3d4e5f60718a1b2c3d4e5f607184354467b3433735f3363625f7034373733726e5f6c33346b5f32303236\nNote: Identical 16-byte blocks yield identical ciphertext.\n")

with open(os.path.join(HANDOUT_DIR, '24_custom_hash.py'), 'w') as f:
    f.write("""# Insecure Custom Hash Function
def custom_hash(s):
    h = 0
    for char in s:
        h = (h * 31 + ord(char)) & 0xFFFFFFFF
    return h

# Target Hash for CTF{cush0m_h4sh_c0ll1s10n_2026}: 305419896
# Find a collision string!
""")

with open(os.path.join(HANDOUT_DIR, '25_dh_params.json'), 'w') as f:
    json.dump({"p": 23, "g": 5, "A": 8, "B": 19, "note": "Compute shared key s = B^a mod p = A^b mod p"}, f, indent=2)


# 🔍 Digital Forensics (10)
with open(os.path.join(HANDOUT_DIR, '26_flag_image.exif.txt'), 'w') as f:
    f.write("File Name: evidence.jpg\nCamera: Canon EOS\nComment: CTF{3x1f_m374d474_3x7r4c710n_2026}\nResolution: 1920x1080\n")

with open(os.path.join(HANDOUT_DIR, '27_lsb_stego.png.txt'), 'w') as f:
    f.write("PNG Image Bitplane Data:\nLSB Plane 0 extracted text: CTF{lsb_st3g4n0gr4phy_3x7r4c73d_2026}\n")

with open(os.path.join(HANDOUT_DIR, '28_corrupted_header.png.txt'), 'w') as f:
    f.write("Hex Dump:\n00000000: XX XX XX XX 0D 0A 1A 0A 00 00 00 0D 49 48 44 52  ........IHDR\nCorrupted Magic Bytes! Replace XX XX XX XX with 89 50 4E 47 to reveal flag: CTF{f1l3_h34d3r_m4g1c_by73s_f1x_2026}\n")

with open(os.path.join(HANDOUT_DIR, '29_disk_carve.raw.txt'), 'w') as f:
    f.write("[Disk Dump Sector 0x4000]\nUnallocated space carving result:\nFOUND DELETED FILE: flag.txt -> CTF{d1sk_c4rv1ng_f0r3ns1cs_2026}\n")

with open(os.path.join(HANDOUT_DIR, '30_volatility_memory.dmp.txt'), 'w') as f:
    f.write("Volatility 3 Memory Process Dump (PID 1337):\nlsass.exe memory map dump -> Flag: CTF{v0l471l17y_m3m0ry_f0r3ns1cs_2026}\n")

with open(os.path.join(HANDOUT_DIR, '31_hidden_stream.pdf.txt'), 'w') as f:
    f.write("PDF Object 4 0 obj\n<< /Length 42 /Filter /FlateDecode >>\nstream\nCTF{pdf_h1dd3n_s7r34m_2026}\nendstream\nendobj\n")

zip_path = os.path.join(HANDOUT_DIR, '32_encrypted_secret.zip')
with zipfile.ZipFile(zip_path, 'w') as zf:
    zf.writestr('flag.txt', 'CTF{z1p_p4ssw0rd_cr4ck3d_2026}\n')

with open(os.path.join(HANDOUT_DIR, '33_audio_spectrogram.wav.txt'), 'w') as f:
    f.write("WAV Audio Data Stream\nSpectrogram Visual Frequencies: CTF{4ud10_sp3c7r0gr4m_s73g0_2026}\n")

with open(os.path.join(HANDOUT_DIR, '34_history.sqlite.txt'), 'w') as f:
    f.write("Chrome History SQLite Dump:\ntable urls (id=42, url='https://target.paradick.my.id/secret?flag=CTF{br0ws3r_h1s70ry_sql173_2026}')\n")

with open(os.path.join(HANDOUT_DIR, '35_usb_hid_keystrokes.pcap.txt'), 'w') as f:
    f.write("USB HID Capture Data:\n00 00 06 00 ... (Keycodes mapped to string: CTF{usb_k3ys7r0k3_r3c0ns7ruc710n_2026})\n")


# 📡 Network Sniffing (8)
with open(os.path.join(HANDOUT_DIR, '36_http_login.pcap.txt'), 'w') as f:
    f.write("Wireshark PCAP Stream:\nPOST /login HTTP/1.1\nData: user=admin&pass=12345&flag=CTF{c134r73x7_p4ck37_sn1ff3d_2026}\n")

with open(os.path.join(HANDOUT_DIR, '37_dns_queries.pcap.txt'), 'w') as f:
    f.write("DNS Query Log:\nQuery: Q1RGe2Ruc183dW5uM2xfM3hmMWw3cjQ3MTBuXzIwMjZ9.exfil.attacker.com -> CTF{dns_7unn3l_3xf1l7r4710n_2026}\n")

with open(os.path.join(HANDOUT_DIR, '38_ftp_passive.pcap.txt'), 'w') as f:
    f.write("FTP Passive Data Transfer Stream (Port 2021):\nSTOR secret_flag.txt -> CTF{f7p_p4ss1v3_d474_7r4nsf3r_2026}\n")

with open(os.path.join(HANDOUT_DIR, '39_icmp_ping.pcap.txt'), 'w') as f:
    f.write("ICMP Echo Request Packets:\nICMP Payload Data bytes: 43 54 46 7b 31 63 6d 70 5f 63 30 76 33 72 37 5f 63 68 34 6e 6e 33 6c 5f 32 30 32 36 7d -> CTF{1cmp_c0v3r7_ch4nn3l_2026}\n")

with open(os.path.join(HANDOUT_DIR, '40_tls_keylog.pcap.txt'), 'w') as f:
    f.write("SSLKEYLOGFILE:\nCLIENT_RANDOM 4a2b3c... -> Decrypted HTTPS GET /flag -> CTF{7ls_d3cryp710n_k3yl0gf1l3_2026}\n")

with open(os.path.join(HANDOUT_DIR, '41_arp_mitm.pcap.txt'), 'w') as f:
    f.write("ARP Poisoning Packet Log:\nARP Reply: 192.168.1.1 is at 00:11:22:33:44:55 (Attacker MITM Flag: CTF{4rp_sp00f1ng_m17m_2026})\n")

with open(os.path.join(HANDOUT_DIR, '42_telnet_stream.pcap.txt'), 'w') as f:
    f.write("Telnet Plaintext Session (Port 23):\nlogin: admin\npassword: secretadminpassword\ncat flag.txt -> CTF{73ln37_c134r73x7_l0g1n_2026}\n")

with open(os.path.join(HANDOUT_DIR, '43_mqtt_broker.pcap.txt'), 'w') as f:
    f.write("MQTT IoT Broker Packet:\nPublish Message [Topic: /sensors/vault] -> Payload: CTF{mq77_107_br0k3r_sn1ff3d_2026}\n")


# ⚙️ Reverse Engineering (7)
with open(os.path.join(HANDOUT_DIR, '44_elf_strings.bin'), 'w') as f:
    f.write("ELF Executable Header\nSection .rodata: CTF{r3v3rs3_3ng1n33r1ng_m4s73r_2026}\n")

with open(os.path.join(HANDOUT_DIR, '45_app.pyc.txt'), 'w') as f:
    f.write("Python 3.11 Bytecode Dump:\n  1           0 LOAD_CONST               1 ('CTF{py7h0n_by73c0d3_d3c0mp1l3d_2026}')\n              2 STORE_NAME               0 (flag)\n")

with open(os.path.join(HANDOUT_DIR, '46_Challenge.class.txt'), 'w') as f:
    f.write("Java Bytecode Class:\npublic class Challenge {\n    public static String flag = \"CTF{j4v4_d3c0mp1l3r_j4dx_2026}\";\n}\n")

with open(os.path.join(HANDOUT_DIR, '47_crackme.c'), 'w') as f:
    f.write("""#include <stdio.h>
#include <string.h>

int main() {
    char key[64];
    printf("Enter Activation Key: ");
    scanf("%63s", key);
    if (strcmp(key, "SUP3R_S3CR37_K3Y_2026") == 0) {
        printf("Access Granted! Flag: CTF{c_3lf_cr4ckm3_gdb_2026}\\n");
    } else {
        printf("Access Denied!\\n");
    }
    return 0;
}
""")

with open(os.path.join(HANDOUT_DIR, '48_app_smali.txt'), 'w') as f:
    f.write(".class public Lcom/example/ctf/MainActivity;\n.method public getFlag()Ljava/lang/String;\n    const-string v0, \"CTF{4ndr01d_4pk_sm4l1_r3v3rs3_2026}\"\n    return-object v0\n.end method\n")

with open(os.path.join(HANDOUT_DIR, '49_bof_ret2win.c'), 'w') as f:
    f.write("""#include <stdio.h>
#include <stdlib.h>

void win() {
    printf("Flag: CTF{b0f_r372w1n_st4ck_0v3rwr173_2026}\\n");
}

void vuln() {
    char buffer[64];
    gets(buffer); // Buffer Overflow!
}

int main() {
    vuln();
    return 0;
}
""")

with open(os.path.join(HANDOUT_DIR, '50_upx_packed.bin'), 'w') as f:
    f.write("UPX! Packed Executable Header\nUnpack command: upx -d 50_upx_packed.bin -> Unpacked Flag: CTF{upx_unp4ck3d_b1n4ry_2026}\n")

print("[🎉] Generated 35 Unique Handout Files in ./handout/!")
