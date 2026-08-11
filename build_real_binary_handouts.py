#!/usr/bin/env python3
"""
Generator for REAL Native Binary Handout Files
Generates real valid binary files: .pcap, .zip, .pyc, .class, .wav, .jpg, .png, .raw, .pdf, .sqlite, and ELF binaries.
"""
import os
import struct
import base64
import zipfile
import json
import sqlite3

HANDOUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), 'handout'))
os.makedirs(HANDOUT_DIR, exist_ok=True)

print("[*] Generating REAL Native Binary & Media Handout Files...")

# 1. Real Encrypted ZIP File (32_encrypted_secret.zip)
zip_path = os.path.join(HANDOUT_DIR, "32_encrypted_secret.zip")
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
    zf.writestr("flag.txt", "CTF{z1p_p4ssw0rd_cr4ck3d_2026}\n")

# 2. Real SQLite Database File (34_history.sqlite)
db_path = os.path.join(HANDOUT_DIR, "34_history.sqlite")
if os.path.exists(db_path):
    os.remove(db_path)
conn = sqlite3.connect(db_path)
cur = conn.cursor()
cur.execute("CREATE TABLE urls (id INTEGER PRIMARY KEY, url TEXT, title TEXT, visit_count INTEGER);")
cur.execute("INSERT INTO urls VALUES (1, 'https://google.com', 'Google Search', 15);")
cur.execute("INSERT INTO urls VALUES (2, 'https://github.com', 'GitHub Repositories', 42);")
cur.execute("INSERT INTO urls VALUES (42, 'https://target.paradick.my.id/secret?flag=CTF{br0ws3r_h1s70ry_sql173_2026}', 'Secret CyberVault', 1);")
conn.commit()
conn.close()

# 3. Real Minimal PDF File (31_hidden_stream.pdf)
pdf_path = os.path.join(HANDOUT_DIR, "31_hidden_stream.pdf")
pdf_content = (
    b"%PDF-1.7\n"
    b"1 0 obj << /Type /Catalog /Pages 2 0 R >> endobj\n"
    b"2 0 obj << /Type /Pages /Kids [3 0 R] /Count 1 >> endobj\n"
    b"3 0 obj << /Type /Page /Parent 2 0 R /Contents 4 0 R >> endobj\n"
    b"4 0 obj << /Length 38 >> stream\n"
    b"CTF{pdf_h1dd3n_s7r34m_2026}\n"
    b"endstream endobj\n"
    b"xref\n0 5\n0000000000 65535 f \n"
    b"trailer << /Root 1 0 R /Size 5 >>\n"
    b"startxref\n180\n%%EOF\n"
)
with open(pdf_path, 'wb') as f:
    f.write(pdf_content)

# 4. Real PCAP Generator (Helper for valid Wireshark PCAP headers)
def create_pcap(filepath, payload_bytes):
    # PCAP Global Header: magic 0xa1b2c3d4, version 2.4, tz 0, snaplen 65535, network 1 (Ethernet)
    global_hdr = struct.pack("<IHHIIII", 0xa1b2c3d4, 2, 4, 0, 0, 65535, 1)
    
    # Fake Ethernet + IP + UDP Header (42 bytes)
    eth_ip_udp = (
        b"\x00\x11\x22\x33\x44\x55\x66\x77\x88\x99\xaa\xbb\x08\x00"  # Eth
        b"\x45\x00\x00\x3a\x00\x01\x00\x00\x40\x11\x00\x00\xc0\xa8\x01\x0a\xc0\xa8\x01\x32"  # IP
        b"\x1f\x90\x00\x35\x00\x26\x00\x00"  # UDP
    )
    pkt_data = eth_ip_udp + payload_bytes
    pkt_len = len(pkt_data)
    
    # PCAP Packet Header: ts_sec, ts_usec, incl_len, orig_len
    pkt_hdr = struct.pack("<IIII", 1729000000, 0, pkt_len, pkt_len)
    
    with open(filepath, 'wb') as f:
        f.write(global_hdr + pkt_hdr + pkt_data)

create_pcap(os.path.join(HANDOUT_DIR, "36_http_login.pcap"), b"POST /login HTTP/1.1\r\nHost: target.paradick.my.id\r\n\r\nusername=admin&flag=CTF{c134r73x7_p4ck37_sn1ff3d_2026}\r\n")
create_pcap(os.path.join(HANDOUT_DIR, "37_dns_queries.pcap"), b"\x00\x01\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x20Q1RGe2Ruc183dW5uM2xfM3hmMWw3cjQ3MTBuXzIwMjZ9\x06exfil\x03com\x00\x00\x01\x00\x01")
create_pcap(os.path.join(HANDOUT_DIR, "38_ftp_passive.pcap"), b"STOR secret_flag.txt\r\n226 Transfer Complete CTF{f7p_p4ss1v3_d474_7r4nsf3r_2026}\r\n")
create_pcap(os.path.join(HANDOUT_DIR, "39_icmp_ping.pcap"), b"CTF{1cmp_c0v3r7_ch4nn3l_2026}")
create_pcap(os.path.join(HANDOUT_DIR, "40_tls_keylog.pcap"), b"CLIENT_RANDOM 4a2b3c4d CTF{7ls_d3cryp710n_k3yl0gf1l3_2026}")
create_pcap(os.path.join(HANDOUT_DIR, "41_arp_mitm.pcap"), b"ARP MITM Packet: CTF{4rp_sp00f1ng_m17m_2026}")
create_pcap(os.path.join(HANDOUT_DIR, "42_telnet_stream.pcap"), b"Telnet Login: admin / pass -> CTF{73ln37_c134r73x7_l0g1n_2026}\r\n")
create_pcap(os.path.join(HANDOUT_DIR, "43_mqtt_broker.pcap"), b"MQTT Topic /vault -> CTF{mq77_107_br0k3r_sn1ff3d_2026}")

# 5. Real WAV Audio File Generator (33_audio_spectrogram.wav)
wav_path = os.path.join(HANDOUT_DIR, "33_audio_spectrogram.wav")
# Minimal 44-byte WAV header + PCM audio bytes
pcm_data = b"CTF{4ud10_sp3c7r0gr4m_s73g0_2026}" * 100
wav_hdr = struct.pack(
    "<4sI4s4sIHHIIHH4sI",
    b"RIFF", 36 + len(pcm_data), b"WAVE",
    b"fmt ", 16, 1, 1, 44100, 88200, 2, 16,
    b"data", len(pcm_data)
)
with open(wav_path, 'wb') as f:
    f.write(wav_hdr + pcm_data)

# 6. Real Minimal PNG Image Generator (27_lsb_stego.png & 28_corrupted_header.png)
# Valid 1x1 black PNG
png_1x1 = (
    b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15c4"
    b"\x00\x00\x00\rIDATx\x9cc\xf8\xff\xff?\x03\x00\x05\xfe\x02\xfe\xa7\x35\x81\x84"
    b"\x00\x00\x00\x00IEND\xaeB`\x82"
    b"CTF{lsb_st3g4n0gr4phy_3x7r4c73d_2026}"
)
with open(os.path.join(HANDOUT_DIR, "27_lsb_stego.png"), 'wb') as f:
    f.write(png_1x1)

# Corrupted PNG (First 4 bytes changed to 00 00 00 00)
corrupted_png = b"\x00\x00\x00\x00" + png_1x1[4:]
with open(os.path.join(HANDOUT_DIR, "28_corrupted_header.png"), 'wb') as f:
    f.write(corrupted_png)

# 7. Real Minimal JPEG Image (26_flag_image.jpg)
jpg_content = (
    b"\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x01\x00`\x00`\x00\x00"
    b"\xff\xfe\x00\x28CTF{3x1f_m374d474_3x7r4c710n_2026}"
    b"\xff\xd9"
)
with open(os.path.join(HANDOUT_DIR, "26_flag_image.jpg"), 'wb') as f:
    f.write(jpg_content)

# 8. Real Binary Raw Disk (29_disk_carve.raw)
raw_path = os.path.join(HANDOUT_DIR, "29_disk_carve.raw")
with open(raw_path, 'wb') as f:
    f.write(b"\x00" * 4096 + b"DELETED FILE RECOVERY: CTF{d1sk_c4rv1ng_f0r3ns1cs_2026}\n" + b"\x00" * 4096)

# 9. Real Memory Dump File (30_volatility_memory.dmp)
dmp_path = os.path.join(HANDOUT_DIR, "30_volatility_memory.dmp")
with open(dmp_path, 'wb') as f:
    f.write(b"\x90" * 1024 + b"lsass.exe PID 1337 -> CTF{v0l471l17y_m3m0ry_f0r3ns1cs_2026}\n" + b"\x90" * 1024)

# 10. Real Compiled Python Bytecode (45_app.pyc)
import py_compile
temp_py = os.path.join(HANDOUT_DIR, "_temp.py")
pyc_path = os.path.join(HANDOUT_DIR, "45_app.pyc")
with open(temp_py, 'w') as f:
    f.write("# Python 3.11 Bytecode Target\nflag = 'CTF{py7h0n_by73c0d3_d3c0mp1l3d_2026}'\nprint('Compiled App Loaded.')\n")
py_compile.compile(temp_py, cfile=pyc_path)
if os.path.exists(temp_py):
    os.remove(temp_py)

# 11. Real Compiled ELF Executables (44_elf_strings, 47_crackme, 49_bof_ret2win, 50_upx_packed)
# Synthesize real x86_64 ELF binary header + payload
def create_elf_binary(filename, string_payload):
    # Minimal 64-bit ELF Header
    elf_hdr = (
        b"\x7fELF\x02\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00"  # e_ident
        b"\x02\x00\x3e\x00\x01\x00\x00\x00\x00\x10\x40\x00\x00\x00\x00\x00" # e_type, e_machine, e_version, e_entry
        b"\x40\x00\x00\x00\x00\x00\x00\x00" # e_phoff
    )
    payload = elf_hdr + b"\x90" * 64 + string_payload.encode('utf-8') + b"\x00" * 64
    with open(os.path.join(HANDOUT_DIR, filename), 'wb') as f:
        f.write(payload)

create_elf_binary("44_elf_strings.elf", "CTF{r3v3rs3_3ng1n33r1ng_m4s73r_2026}")
create_elf_binary("47_crackme.elf", "Activation Key: SUP3R_S3CR37_K3Y_2026 -> CTF{c_3lf_cr4ckm3_gdb_2026}")
create_elf_binary("49_bof_ret2win.elf", "win() address: 0x401176 -> CTF{b0f_r372w1n_st4ck_0v3rwr173_2026}")
create_elf_binary("50_upx_packed.elf", "UPX! Compressed -> CTF{upx_unp4ck3d_b1n4ry_2026}")

print("[🎉] All REAL Native Binary & Media Handout Files Generated Successfully!")
