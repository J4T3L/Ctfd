#!/usr/bin/env python3
"""
Generator for app/templates/portal.html with 50 Challenge cards
"""
import os
import re

PORTAL_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'app', 'templates', 'portal.html'))

# 50 Challenges Data (Name, Category, Level, Points, Desc, Link)
CHALLENGES = [
    # 🌐 Web Exploitation (15)
    ("DevNotes Login", "web", "EASY", 100, "Bypass login SQL Injection (`admin' --`).", "/sqli/"),
    ("Hidden Comments", "web", "EASY", 50, "Inspeksi komentar HTML kode sumber.", "/hidden_comment/"),
    ("Cookie Manager", "web", "EASY", 100, "Manipulasi cookie Base64 `user_session`.", "/cookie_lab/"),
    ("Robots.txt Recon", "web", "EASY", 50, "Periksa direktori terlarang crawler.", "/robots_secret/"),
    ("Reflected XSS", "web", "EASY", 100, "Suntikkan payload Reflected XSS.", "/xss_reflected/"),
    ("UserProfile IDOR", "web", "MEDIUM", 150, "Ganti `user_id=100` untuk profil admin.", "/idor/"),
    ("File Viewer LFI", "web", "MEDIUM", 250, "Path traversal `?page=flag.txt`.", "/lfi/"),
    ("Ping Diagnostic", "web", "MEDIUM", 300, "Command Injection `; cat /flag.txt`.", "/rce_ping/"),
    ("Business Logic Shop", "web", "MEDIUM", 350, "Manipulasi kuantitas produk negatif.", "/logic_shop/"),
    ("Exposed .git Leak", "web", "MEDIUM", 150, "Public .git repository directory leak.", "/hidden_comment/"),
    ("URL Fetcher SSRF", "web", "HARD", 350, "SSRF ke internal admin loopback.", "/ssrf/"),
    ("JWT Token Inspector", "web", "HARD", 400, "JWT Weak Secret / Alg None.", "/jwt_lab/"),
    ("XXE XML Parser", "web", "HARD", 450, "XML External Entity Injection.", "/xxe_lab/"),
    ("Jinja2 SSTI Generator", "web", "HARD", 500, "SSTI WAF Keyword Bypass.", "/ssti/"),
    ("Pickle Cache RCE", "web", "HARD", 500, "Python Pickle Deserialization RCE.", "/pickle_rce/"),

    # 🔐 Cryptography (10)
    ("Caesar Cipher ROT13", "crypto", "EASY", 50, "Shift Cipher ROT13 decryption.", "/handout/caesar_cipher.txt"),
    ("Multi-Layer Encoding", "crypto", "EASY", 100, "Hex -> Base32 -> Base64 decoding.", "/handout/nested_encoding.txt"),
    ("Legacy MD5 Hash Crack", "crypto", "MEDIUM", 200, "Cracking MD5 password hash.", "/weak_hash/"),
    ("RSA Small Exponent e=3", "crypto", "MEDIUM", 300, "RSA Low Exponent m = c^(1/3).", "/handout/rsa_low_e.json"),
    ("RSA Prime Factorization", "crypto", "MEDIUM", 350, "RSA Factorization (p * q).", "/handout/rsa_low_e.json"),
    ("Single-Byte XOR Stream", "crypto", "MEDIUM", 250, "XOR Stream Cipher Brute-Force.", "/handout/caesar_cipher.txt"),
    ("Vigenère Cipher", "crypto", "MEDIUM", 300, "Frequency Analysis Key Discovery.", "/handout/caesar_cipher.txt"),
    ("AES-128 ECB Pattern", "crypto", "HARD", 400, "AES ECB Block Alignment Leak.", "/handout/caesar_cipher.txt"),
    ("Custom Hash Collision", "crypto", "HARD", 450, "Custom Hash Function Collision.", "/handout/caesar_cipher.txt"),
    ("Diffie-Hellman Weak Mod", "crypto", "HARD", 500, "Diffie-Hellman Discrete Logarithm.", "/handout/rsa_low_e.json"),

    # 🔍 Forensics (10)
    ("Image EXIF Metadata", "forensics", "EASY", 50, "Exiftool metadata extraction.", "/handout/hidden_exif.txt"),
    ("PNG LSB Steganography", "forensics", "MEDIUM", 150, "LSB bitplane extraction.", "/handout/hidden_exif.txt"),
    ("Corrupted Header Fix", "forensics", "MEDIUM", 200, "Magic Bytes PNG/JPEG repair.", "/handout/hidden_exif.txt"),
    ("Disk Partition Carving", "forensics", "MEDIUM", 300, "Foremost file carving.", "/handout/hidden_exif.txt"),
    ("Encrypted ZIP Crack", "forensics", "MEDIUM", 200, "ZIP2John password cracking.", "/handout/encrypted_secret.zip"),
    ("Layered PDF Stream", "forensics", "MEDIUM", 250, "PDF object stream analysis.", "/handout/hidden_exif.txt"),
    ("Browser SQLite History", "forensics", "MEDIUM", 250, "Browser history query.", "/handout/hidden_exif.txt"),
    ("Volatility Memory Dump", "forensics", "HARD", 450, "Volatility3 process dump.", "/handout/hidden_exif.txt"),
    ("Audio Spectrogram", "forensics", "HARD", 350, "Audacity spectrogram visualizer.", "/handout/hidden_exif.txt"),
    ("USB HID Keystroke", "forensics", "HARD", 400, "USB keyboard packet mapping.", "/handout/http_traffic.pcap.txt"),

    # 📡 Network Sniffing (8)
    ("HTTP Cleartext Packet", "network", "EASY", 100, "Wireshark PCAP POST inspection.", "/handout/http_traffic.pcap.txt"),
    ("Unencrypted Telnet", "network", "EASY", 100, "Telnet TCP Stream Credentials.", "/handout/http_traffic.pcap.txt"),
    ("Anonymous FTP Capture", "network", "MEDIUM", 150, "FTP Passive Data Stream.", "/handout/http_traffic.pcap.txt"),
    ("ARP Spoofing Analysis", "network", "MEDIUM", 250, "ARP MITM Packet Inspection.", "/handout/http_traffic.pcap.txt"),
    ("DNS Tunneling Exfil", "network", "MEDIUM", 300, "Base64 DNS Query Decoding.", "/handout/http_traffic.pcap.txt"),
    ("IoT MQTT Packet Sniff", "network", "MEDIUM", 300, "MQTT Topic Subscription Leak.", "/handout/http_traffic.pcap.txt"),
    ("ICMP Covert Channel", "network", "HARD", 350, "ICMP Echo Payload Extraction.", "/handout/http_traffic.pcap.txt"),
    ("SSL/TLS Keylog Decrypt", "network", "HARD", 400, "Wireshark SSLKEYLOGFILE Import.", "/handout/http_traffic.pcap.txt"),

    # ⚙️ Reverse Engineering (7)
    ("ELF Compiled Strings", "reverse", "EASY", 50, "Strings & Symbols extraction.", "/handout/crackme_source.c"),
    ("Python Bytecode (.pyc)", "reverse", "MEDIUM", 150, "Uncompyle6 decompilation.", "/handout/crackme_source.c"),
    ("Java Class Decompile", "reverse", "MEDIUM", 200, "JADX Java decompilation.", "/handout/crackme_source.c"),
    ("C ELF Crackme Logic", "reverse", "MEDIUM", 300, "Ghidra / GDB strcmp analysis.", "/handout/crackme_source.c"),
    ("Android APK Smali", "reverse", "HARD", 350, "Smali code logic analysis.", "/handout/crackme_source.c"),
    ("x86 BOF ret2win", "reverse", "HARD", 450, "Stack overwrite return address.", "/handout/crackme_source.c"),
    ("UPX Packed Unpacking", "reverse", "HARD", 500, "UPX unpack & anti-debug.", "/handout/crackme_source.c")
]

def generate_portal():
    web_cards = []
    crypto_cards = []
    forensics_cards = []
    network_cards = []
    reverse_cards = []

    badge_colors = {
        "EASY": "var(--accent-green)",
        "MEDIUM": "var(--accent-cyan)",
        "HARD": "var(--accent-purple)"
    }

    for name, cat, level, pts, desc, link in CHALLENGES:
        btn_text = "Buka Challenge →" if not link.startswith("/handout/") else "Unduh Handout 📥"
        color = badge_colors.get(level, "var(--accent-cyan)")
        card_html = f"""
            <div class="glass-card">
                <div style="font-size: 0.75rem; font-weight: 700; color: {color};">{level} • {pts} PTS</div>
                <h3 class="card-title">{name}</h3>
                <p class="card-desc">{desc}</p>
                <a href="{link}" class="btn-primary" style="margin-top: 1rem; width: 100%; justify-content: center;">{btn_text}</a>
            </div>"""
        
        if cat == "web": web_cards.append(card_html)
        elif cat == "crypto": crypto_cards.append(card_html)
        elif cat == "forensics": forensics_cards.append(card_html)
        elif cat == "network": network_cards.append(card_html)
        elif cat == "reverse": reverse_cards.append(card_html)

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CyberVault - 50 Multi-Category CTF Suite</title>
    <link rel="stylesheet" href="{{{{ url_for('static', filename='style.css') }}}}">
    <style>
        .category-tab {{
            padding: 0.6rem 1.2rem;
            background: rgba(255,255,255,0.05);
            border: 1px solid var(--border-color);
            color: var(--text-muted);
            border-radius: 8px;
            font-weight: 700;
            font-size: 0.9rem;
            cursor: pointer;
            transition: all 0.25s ease;
        }}
        .category-tab:hover, .category-tab.active {{
            background: var(--accent-cyan);
            color: #040711;
            border-color: var(--accent-cyan);
            box-shadow: 0 0 15px rgba(6, 182, 212, 0.4);
        }}
        .category-section {{
            display: none;
        }}
        .category-section.active {{
            display: grid;
        }}
    </style>
</head>
<body>
    <nav class="navbar">
        <a href="/" class="brand">
            <div class="brand-icon">🛡️</div>
            <span class="brand-title">CyberVault CTF Suite</span>
            <span class="brand-tag">50 Challenges</span>
        </a>
        <div class="nav-links">
            <div class="status-indicator">
                <div class="status-dot"></div>
                <span>50 Labs Online</span>
            </div>
            <a href="/" class="nav-link active">Portal Home</a>
        </div>
    </nav>

    <main class="main-container">
        <section class="hero" style="padding: 2.5rem 1rem 1.5rem 1rem;">
            <div class="hero-badge">🎓 Modul Ajar Jarkom & Cyber Security</div>
            <h1 class="hero-title">Multi-Category <span>CTF Master Suite</span></h1>
            <p class="hero-subtitle">Laboratorium praktikum keamanan siber & jaringan lengkap (50 Challenge dari Easy hingga Hard).</p>
        </section>

        <!-- Category Tabs Switcher -->
        <div style="display: flex; gap: 0.8rem; flex-wrap: wrap; margin-bottom: 2rem; justify-content: center;">
            <button class="category-tab active" onclick="switchCategory('web')">🌐 Web Exploit (15)</button>
            <button class="category-tab" onclick="switchCategory('crypto')">🔐 Cryptography (10)</button>
            <button class="category-tab" onclick="switchCategory('forensics')">🔍 Digital Forensics (10)</button>
            <button class="category-tab" onclick="switchCategory('network')">📡 Network Sniffing (8)</button>
            <button class="category-tab" onclick="switchCategory('reverse')">⚙️ Reverse Engineering (7)</button>
        </div>

        <!-- 1. WEB EXPLOITATION (15) -->
        <section id="cat-web" class="category-section active grid-3">
            {"".join(web_cards)}
        </section>

        <!-- 2. CRYPTOGRAPHY (10) -->
        <section id="cat-crypto" class="category-section grid-3">
            {"".join(crypto_cards)}
        </section>

        <!-- 3. FORENSICS (10) -->
        <section id="cat-forensics" class="category-section grid-3">
            {"".join(forensics_cards)}
        </section>

        <!-- 4. NETWORK (8) -->
        <section id="cat-network" class="category-section grid-3">
            {"".join(network_cards)}
        </section>

        <!-- 5. REVERSE (7) -->
        <section id="cat-reverse" class="category-section grid-3">
            {"".join(reverse_cards)}
        </section>
    </main>

    <script>
        function switchCategory(catId) {{
            document.querySelectorAll('.category-tab').forEach(el => el.classList.remove('active'));
            document.querySelectorAll('.category-section').forEach(el => el.classList.remove('active'));
            
            event.target.classList.add('active');
            document.getElementById('cat-' + catId).classList.add('active');
        }}
    </script>
</body>
</html>
"""
    with open(PORTAL_PATH, "w", encoding="utf-8") as f:
        f.write(html_content)

if __name__ == "__main__":
    generate_portal()
    print("[🎉] portal.html generated cleanly with all 50 challenge cards!")
