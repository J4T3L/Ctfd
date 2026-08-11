#!/usr/bin/env python3
"""
Master Generator for 50 Multi-Category CTF Challenge Folders & Metadata (challenge.yml)
With direct lightweight endpoint routes and downloadable handout URLs.
"""
import os

CHALLENGES_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), 'challenges'))
os.makedirs(CHALLENGES_DIR, exist_ok=True)

CHALLENGES_DATA = [
    # 🌐 1. Web Exploitation (15)
    ("01_sqli", "DevNotes - Admin Portal", "Web Exploitation", 100, "CTF{34sy_sql_1nj3ct10n_byp4ss_2026}", "easy", "https://target.paradick.my.id/sqli/", "💡 Tool Recommended: `Burp Suite` / `sqlmap` / `ffuf`. Gunakan payload SQLi `admin' --` pada kolom username."),
    ("02_comment_leak", "DevCompany - Hidden Comments", "Web Exploitation", 50, "CTF{h7ml_c0mm3n7_l34k_d1sc0v3r3d_2026}", "easy", "https://target.paradick.my.id/hidden_comment/", "💡 Tool Recommended: `curl` / `ffuf`. Inspeksi komentar HTML kode sumber halaman."),
    ("03_cookie_lab", "Cookie Session Manager", "Web Exploitation", 100, "CTF{c00k13_m4n1pul4710n_m4s73r_2026}", "easy", "https://target.paradick.my.id/cookie_lab/", "💡 Tool Recommended: `Burp Suite` / `DevTools`. Dekode cookie Base64 `user_session` lalu ubah menjadi `role=admin`."),
    ("04_robots_secret", "Robots.txt Recon", "Web Exploitation", 50, "CTF{r0b07s_7x7_d1sc0v3ry_m4s73r_2026}", "easy", "https://target.paradick.my.id/robots_secret/", "💡 Tool Recommended: `curl` / `nikto`. Periksa berkas `/robots.txt`."),
    ("05_xss_reflected", "Reflected XSS Engine", "Web Exploitation", 100, "CTF{xss_r3fl3c73d_s3cr37_l34k_2026}", "easy", "https://target.paradick.my.id/xss_reflected/", "💡 Tool Recommended: `Burp Suite` / `nuclei`. Suntikkan payload `<script>alert(1)</script>` pada parameter pencarian."),
    ("06_idor", "UserProfile Portal", "Web Exploitation", 150, "CTF{1d0r_pr1v1l3g3_3sc4l4710n_2026}", "medium", "https://target.paradick.my.id/idor/", "💡 Tool Recommended: `ffuf` / `Burp Intruder`. Ubah parameter `user_id=100` untuk membuka profil admin."),
    ("07_lfi", "File Viewer Pro", "Web Exploitation", 250, "CTF{s3rv3r_s1d3_t3mpl4t3_1nj3ct10n_m4st3r_2026}", "medium", "https://target.paradick.my.id/lfi/", "💡 Tool Recommended: `ffuf` / `nuclei`. Lakukan Path Traversal `?page=flag.txt`."),
    ("08_rce_ping", "Ping Diagnostic Utility", "Web Exploitation", 300, "CTF{s3rv3r_s1d3_t3mpl4t3_1nj3ct10n_m4st3r_2026}", "medium", "https://target.paradick.my.id/rce_ping/", "💡 Tool Recommended: `Burp Suite` / `nuclei`. Suntikkan pemisah perintah `; cat /flag.txt`."),
    ("09_logic_shop", "Business Logic Shop", "Web Exploitation", 350, "CTF{l0g1c_fl4w_pr1c3_m4n1pul4710n_2026}", "medium", "https://target.paradick.my.id/logic_shop/", "💡 Tool Recommended: `Burp Suite Repeater`. Masukkan nilai kuantitas negatif (misal `-10`)."),
    ("10_ssrf", "URL Content Fetcher", "Web Exploitation", 350, "CTF{ssrf_1n73rn4l_n37w0rk_4cc3ss_2026}", "hard", "https://target.paradick.my.id/ssrf/", "💡 Tool Recommended: `Burp Suite` / `nuclei`. Tembak URL internal loopback `http://127.0.0.1:8000/ssrf/internal/admin/secret`."),
    ("11_jwt_lab", "JWT Inspector", "Web Exploitation", 400, "CTF{jw7_w34k_s3cr37_3sc4l4710n_2026}", "hard", "https://target.paradick.my.id/jwt_lab/", "💡 Tool Recommended: `jwt_tool` / `hashcat`. Crack token JWT dengan secret `secret123` atau uji `alg: none`."),
    ("12_xxe_lab", "XXE XML Parser", "Web Exploitation", 450, "CTF{34sy_sql_1nj3ct10n_byp4ss_2026}", "hard", "https://target.paradick.my.id/xxe_lab/", "💡 Tool Recommended: `Burp Suite` / `nuclei`. Suntikkan DOCTYPE ENTITY `file:///flag.txt`."),
    ("13_ssti", "CyberVault Report Generator", "Web Exploitation", 500, "CTF{s3rv3r_s1d3_t3mpl4t3_1nj3ct10n_m4st3r_2026}", "hard", "https://target.paradick.my.id/ssti/", "💡 Tool Recommended: `tplmap` / `nuclei`. Bypass WAF Jinja2 untuk membaca `/flag.txt`."),
    ("14_pickle_rce", "Pickle Deserialization Vault", "Web Exploitation", 500, "CTF{s3rv3r_s1d3_t3mpl4t3_1nj3ct10n_m4st3r_2026}", "hard", "https://target.paradick.my.id/pickle_rce/", "💡 Tool Recommended: `Python 3`. Buat objek `__reduce__` RCE pada cookie `pickle_session`."),
    ("15_git_leak", "Exposed .git Directory Leak", "Web Exploitation", 150, "CTF{g17_d1r3c70ry_3xp0s3d_2026}", "medium", "https://target.paradick.my.id/hidden_comment/", "💡 Tool Recommended: `GitTools` / `git-dumper`. Unduh folder `.git` yang terekspos publik."),

    # 🔐 2. Cryptography & Hash Cracking (10)
    ("16_crypto_caesar", "Caesar Cipher ROT13", "Cryptography", 50, "CTF{c43s4r_c1ph3r_r0t13_m4sg3r_2026}", "easy", "https://target.paradick.my.id/handout/caesar_cipher.txt", "💡 Tool Recommended: `CyberChef` / `tr`. Dekripsi cipher ROT13 pada ciphertext."),
    ("17_crypto_base64_multi", "Multi-Layer Nested Encoding", "Cryptography", 100, "CTF{mul71_l4y3r_3nc0d1ng_m4s73r_2026}", "easy", "https://target.paradick.my.id/handout/nested_encoding.txt", "💡 Tool Recommended: `CyberChef` / `base32`. Dekode urutan Hex -> Base32 -> Base64."),
    ("18_crypto_md5", "Legacy MD5 Password Hash", "Cryptography", 200, "CTF{md5_w34k_h4sh_cr4ck3d_2026}", "medium", "https://target.paradick.my.id/weak_hash/", "💡 Tool Recommended: `hashcat` / `john`. Pecahkan hash MD5 `e10adc3949ba59abbe56e057f20f883e`."),
    ("19_crypto_rsa_e3", "RSA Small Exponent Attack", "Cryptography", 300, "CTF{rs4_sm4ll_3xp0n3n7_2026}", "medium", "https://target.paradick.my.id/handout/rsa_low_e.json", "💡 Tool Recommended: `python3`. Hitung akar pangkat 3 dari ciphertext $m = c^{1/3}$ saat $e=3$."),
    ("20_crypto_rsa_factor", "RSA Prime Factorization Attack", "Cryptography", 350, "CTF{rs4_f4c70r1z4710n_f4ct0rdb_2026}", "medium", "https://target.paradick.my.id/handout/rsa_low_e.json", "💡 Tool Recommended: `factordb.py` / `sage`. Faktorkan nilai $n$ kecil untuk mendapatkan nilai $p$ dan $q$."),
    ("21_crypto_xor", "Single-Byte XOR Stream Cipher", "Cryptography", 250, "CTF{x0r_s7r34m_c1ph3r_cr4ck3d_2026}", "medium", "https://target.paradick.my.id/handout/caesar_cipher.txt", "💡 Tool Recommended: `CyberChef` / `xortool`. Brute-force 256 kemungkinan single-byte XOR key."),
    ("22_crypto_vigenere", "Vigenère Cipher Frequency Analysis", "Cryptography", 300, "CTF{v1g3n3r3_c1ph3r_4n4lys1s_2026}", "medium", "https://target.paradick.my.id/handout/caesar_cipher.txt", "💡 Tool Recommended: `dcode.fr` / `vigenere-solver`. Analisis frekuensi huruf untuk mencari panjang kunci."),
    ("23_crypto_aes_ecb", "AES-128 ECB Mode Pattern Leak", "Cryptography", 400, "CTF{43s_3cb_p4773rn_l34k_2026}", "hard", "https://target.paradick.my.id/handout/caesar_cipher.txt", "💡 Tool Recommended: `python3`. Manfaatkan sifat independen blok AES ECB mode untuk ekstrasi flag."),
    ("24_crypto_custom_hash", "Insecure Custom Hash Collision", "Cryptography", 450, "CTF{cush0m_h4sh_c0ll1s10n_2026}", "hard", "https://target.paradick.my.id/handout/caesar_cipher.txt", "💡 Tool Recommended: `z3-solver` / `python3`. Temukan string lain yang menghasilkan hash collision."),
    ("25_crypto_dh_weak", "Diffie-Hellman Weak Modulus Attack", "Cryptography", 500, "CTF{d1ff13_h3llm4n_w34k_p_2026}", "hard", "https://target.paradick.my.id/handout/rsa_low_e.json", "💡 Tool Recommended: `pari/gp` / `sage`. Hitung logaritma diskrit (Discrete Log Problem) pada p kecil."),

    # 🔍 3. Digital Forensics & Steganography (10)
    ("26_forensics_exif", "Image EXIF Metadata Extraction", "Digital Forensics", 50, "CTF{3x1f_m374d474_3x7r4c710n_2026}", "easy", "https://target.paradick.my.id/handout/hidden_exif.txt", "💡 Tool Recommended: `exiftool` / `strings`. Ekstrak tag Exif/Comment pada gambar."),
    ("27_forensics_stego_lsb", "PNG Image LSB Steganography", "Digital Forensics", 150, "CTF{lsb_st3g4n0gr4phy_3x7r4c73d_2026}", "medium", "https://target.paradick.my.id/handout/hidden_exif.txt", "💡 Tool Recommended: `zsteg` / `stegsolve`. Ekstrak bit terendah (LSB) pada bitplane gambar PNG."),
    ("28_forensics_file_fix", "Corrupted Image Header Repair", "Digital Forensics", 200, "CTF{f1l3_h34d3r_m4g1c_by73s_f1x_2026}", "medium", "https://target.paradick.my.id/handout/hidden_exif.txt", "💡 Tool Recommended: `hexeditor` / `xxd`. Perbaiki 8 byte pertama magic bytes header PNG (`89 50 4E 47`)."),
    ("29_forensics_disk", "Deleted File Partition Carving", "Digital Forensics", 300, "CTF{d1sk_c4rv1ng_f0r3ns1cs_2026}", "medium", "https://target.paradick.my.id/handout/hidden_exif.txt", "💡 Tool Recommended: `autopsy` / `foremost` / `scalpel`. Carving berkas terhapus dari disk image."),
    ("30_forensics_volatility", "Memory Dump Volatility Analysis", "Digital Forensics", 450, "CTF{v0l471l17y_m3m0ry_f0r3ns1cs_2026}", "hard", "https://target.paradick.my.id/handout/hidden_exif.txt", "💡 Tool Recommended: `volatility3`. Analisis daftar proses (`pslist`) dan dumped memory process."),
    ("31_forensics_pdf", "Layered PDF Hidden Stream", "Digital Forensics", 250, "CTF{pdf_h1dd3n_s7r34m_2026}", "medium", "https://target.paradick.my.id/handout/hidden_exif.txt", "💡 Tool Recommended: `pdf-parser` / `pdfid`. Analisis stream objek PDF tersembunyi."),
    ("32_forensics_zip", "Encrypted ZIP Hash Cracking", "Digital Forensics", 200, "CTF{z1p_p4ssw0rd_cr4ck3d_2026}", "medium", "https://target.paradick.my.id/handout/encrypted_secret.zip", "💡 Tool Recommended: `zip2john` & `john`. Ekstrak hash dari ZIP terenkripsi lalu crack dengan wordlist."),
    ("33_forensics_audio", "Audio Spectrogram Hidden Signal", "Digital Forensics", 350, "CTF{4ud10_sp3c7r0gr4m_s73g0_2026}", "hard", "https://target.paradick.my.id/handout/hidden_exif.txt", "💡 Tool Recommended: `Audacity` / `sonic-visualiser`. Buka tampilan Spectrogram pada berkas audio WAV."),
    ("34_forensics_browser", "Browser History SQLite Analysis", "Digital Forensics", 250, "CTF{br0ws3r_h1s70ry_sql173_2026}", "medium", "https://target.paradick.my.id/handout/hidden_exif.txt", "💡 Tool Recommended: `sqlite3` / `DB Browser`. Query tabel `urls` pada SQLite History browser."),
    ("35_forensics_usb", "USB HID Keystroke Packet Reconstruction", "Digital Forensics", 400, "CTF{usb_k3ys7r0k3_r3c0ns7ruc710n_2026}", "hard", "https://target.paradick.my.id/handout/http_traffic.pcap.txt", "💡 Tool Recommended: `tshark` / `python3`. Petakan USB HID Keycodes dari pcap ke tombol keyboard."),

    # 📡 4. Network Sniffing & PCAP Analysis (8)
    ("36_net_http_cleartext", "HTTP Cleartext Packet Inspection", "Network Sniffing", 100, "CTF{c134r73x7_p4ck37_sn1ff3d_2026}", "easy", "https://target.paradick.my.id/handout/http_traffic.pcap.txt", "💡 Tool Recommended: `Wireshark` / `tshark`. Filter paket `http.request.method == \"POST\"`."),
    ("37_net_dns_tunnel", "DNS Tunneling Exfiltration", "Network Sniffing", 300, "CTF{dns_7unn3l_3xf1l7r4710n_2026}", "medium", "https://target.paradick.my.id/handout/http_traffic.pcap.txt", "💡 Tool Recommended: `tshark` / `python3`. Dekode subdomain query DNS A/TXT berformat Base64."),
    ("38_net_ftp_pcap", "Anonymous FTP Data Extraction", "Network Sniffing", 150, "CTF{f7p_p4ss1v3_d474_7r4nsf3r_2026}", "medium", "https://target.paradick.my.id/handout/http_traffic.pcap.txt", "💡 Tool Recommended: `Wireshark`. Follow TCP Stream pada port FTP-DATA (port 20/passive)."),
    ("39_net_icmp_covert", "ICMP Echo Covert Channel", "Network Sniffing", 350, "CTF{1cmp_c0v3r7_ch4nn3l_2026}", "hard", "https://target.paradick.my.id/handout/http_traffic.pcap.txt", "💡 Tool Recommended: `tshark`. Ekstrak byte data payload pada paket ICMP ping request."),
    ("40_net_tls_decrypt", "SSL/TLS Decryption Keylog", "Network Sniffing", 400, "CTF{7ls_d3cryp710n_k3yl0gf1l3_2026}", "hard", "https://target.paradick.my.id/handout/http_traffic.pcap.txt", "💡 Tool Recommended: `Wireshark`. Impor berkas `SSLKEYLOGFILE` pada Wireshark TLS Preferences."),
    ("41_net_arp_spoof", "ARP Cache Poisoning Analysis", "Network Sniffing", 250, "CTF{4rp_sp00f1ng_m17m_2026}", "medium", "https://target.paradick.my.id/handout/http_traffic.pcap.txt", "💡 Tool Recommended: `Wireshark`. Cari peringatan Duplicate IP / MAC address re-binding."),
    ("42_net_telnet_auth", "Unencrypted Telnet Credentials", "Network Sniffing", 100, "CTF{73ln37_c134r73x7_l0g1n_2026}", "easy", "https://target.paradick.my.id/handout/http_traffic.pcap.txt", "💡 Tool Recommended: `Wireshark`. Follow TCP Stream pada port 23 Telnet."),
    ("43_net_mqtt_iot", "IoT MQTT Broker Packet Sniffing", "Network Sniffing", 300, "CTF{mq77_107_br0k3r_sn1ff3d_2026}", "medium", "https://target.paradick.my.id/handout/http_traffic.pcap.txt", "💡 Tool Recommended: `Wireshark` / `mosquitto_sub`. Inspect MQTT Publish Message packets."),

    # ⚙️ 5. Reverse Engineering & Binary Analysis (7)
    ("44_rev_strings", "ELF Compiled Strings Inspection", "Reverse Engineering", 50, "CTF{r3v3rs3_3ng1n33r1ng_m4s73r_2026}", "easy", "https://target.paradick.my.id/handout/crackme_source.c", "💡 Tool Recommended: `strings` / `ghidra`. Ekstrak string tercetak pada biner ELF."),
    ("45_rev_pyc", "Python Bytecode Decompilation", "Reverse Engineering", 150, "CTF{py7h0n_by73c0d3_d3c0mp1l3d_2026}", "medium", "https://target.paradick.my.id/handout/crackme_source.c", "💡 Tool Recommended: `uncompyle6` / `decompyle++`. Dekompilasi berkas `.pyc` kembali ke kode sumber Python."),
    ("46_rev_java_class", "Java Class Decompilation", "Reverse Engineering", 200, "CTF{j4v4_d3c0mp1l3r_j4dx_2026}", "medium", "https://target.paradick.my.id/handout/crackme_source.c", "💡 Tool Recommended: `jadx-gui` / `cfr`. Dekompilasi bytecode `.class` Java."),
    ("47_rev_crackme", "C ELF Binary Key Verification", "Reverse Engineering", 300, "CTF{c_3lf_cr4ckm3_gdb_2026}", "medium", "https://target.paradick.my.id/handout/crackme_source.c", "💡 Tool Recommended: `Ghidra` / `gdb`. Disassemble fungsi `main` & `strcmp` pada biner."),
    ("48_rev_apk", "Android APK Smali Logic", "Reverse Engineering", 350, "CTF{4ndr01d_4pk_sm4l1_r3v3rs3_2026}", "hard", "https://target.paradick.my.id/handout/crackme_source.c", "💡 Tool Recommended: `jadx-gui` / `apktool`. Decompile APK dan periksa kelas MainActivity."),
    ("49_rev_bof_ret2win", "x86 Buffer Overflow ret2win", "Reverse Engineering", 450, "CTF{b0f_r372w1n_st4ck_0v3rwr173_2026}", "hard", "https://target.paradick.my.id/handout/crackme_source.c", "💡 Tool Recommended: `pwntools` & `gdb-pwndbg`. Overwrite EIP/RIP untuk melompat ke fungsi `win()`."),
    ("50_rev_upx_packed", "UPX Binary Unpacking", "Reverse Engineering", 500, "CTF{upx_unp4ck3d_b1n4ry_2026}", "hard", "https://target.paradick.my.id/handout/crackme_source.c", "💡 Tool Recommended: `upx -d` / `x64dbg`. Unpack kompresi UPX pada biner sebelum analisis.")
]

print(f"[*] Generating {len(CHALLENGES_DATA)} Multi-Category CTF Challenge Folders with direct URLs...")

for folder, name, cat, val, flag, level, link, hint in CHALLENGES_DATA:
    c_dir = os.path.join(CHALLENGES_DIR, folder)
    os.makedirs(c_dir, exist_ok=True)
    
    yml_content = f"""name: "{name}"
author: "Modul Ajar Jarkom & Cyber Security"
category: "{cat}"
description: |
  Tantangan {cat} ({level.upper()}).
  Analisis dan selesaikan tantangan ini untuk menemukan flag rahasia!

  **Target Link / Handout**: [{link}]({link})

value: {val}
type: standard
state: visible

flags:
  - "{flag}"

tags:
  - {cat.lower().replace(' ', '-')}
  - {level}

hints:
  - content: "{hint}"
    cost: {max(5, val // 10)}
"""
    with open(os.path.join(c_dir, 'challenge.yml'), 'w', encoding='utf-8') as f:
        f.write(yml_content)

print(f"[🎉] All {len(CHALLENGES_DATA)} CTF Challenge metadata folders updated with direct URLs!")
