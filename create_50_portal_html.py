#!/usr/bin/env python3
"""
Generator for app/templates/portal.html featuring:
- 50 Multi-Category CTF Challenge Cards with REAL native binary URLs (.pcap, .zip, .pyc, .class, .wav, .jpg, .png, .raw, .pdf, .sqlite, .elf)
- Interactive Glassmorphism Hint & Recommended Tools Modal Popup
"""
import os

PORTAL_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'app', 'templates', 'portal.html'))

# 50 Challenges Master Data
CHALLENGES = [
    # 🌐 1. Web Exploitation (15)
    ("web-1", "DevNotes Login", "web", "EASY", 100, "Bypass login SQL Injection (`admin' --`).", "/sqli/", "Burp Suite / sqlmap", "Gunakan Burp Suite Interceptor atau isi form login dengan payload SQL Injection: admin' -- pada kolom Username."),
    ("web-2", "Hidden Comments", "web", "EASY", 50, "Inspeksi komentar HTML kode sumber.", "/hidden_comment/", "Browser View Source / curl", "Buka halaman web lalu tekan Ctrl+U (Inspect Source Code). Cari komentar HTML &lt;!-- Secret Admin Endpoint: ... --&gt; untuk menemukan rute rahasia."),
    ("web-3", "Cookie Manager", "web", "EASY", 100, "Manipulasi cookie Base64 `user_session`.", "/cookie_lab/", "DevTools (F12) / CyberChef", "Buka DevTools F12 -&gt; Application -&gt; Cookies. Ambil cookie user_session (Base64), ubah role=guest menjadi role=admin (cm9sZT1hZG1pbg==)."),
    ("web-4", "Robots.txt Recon", "web", "EASY", 50, "Periksa direktori terlarang crawler.", "/robots_secret/", "curl / Browser", "Akses file https://target.paradick.my.id/robots_secret/robots.txt di browser. Cari path Disallow terlarang lalu buka rute tersebut."),
    ("web-5", "Reflected XSS", "web", "EASY", 100, "Suntikkan payload Reflected XSS.", "/xss_reflected/", "Burp Suite / nuclei", "Masukkan payload JavaScript &lt;script&gt;alert(1)&lt;/script&gt; pada kolom pencarian untuk mengeksekusi reflected XSS script."),
    ("web-6", "UserProfile IDOR", "web", "MEDIUM", 150, "Ganti `user_id=100` untuk profil admin.", "/idor/", "ffuf / Burp Intruder", "Buka URL https://target.paradick.my.id/idor/?user_id=102. Ganti nilai parameter URL user_id menjadi 100 untuk melihat akun Administrator."),
    ("web-7", "File Viewer LFI", "web", "MEDIUM", 250, "Path traversal `?page=flag.txt`.", "/lfi/", "ffuf / nuclei", "Lakukan Local File Inclusion / Path Traversal dengan mengganti parameter URL ?page=welcome.txt menjadi ?page=flag.txt."),
    ("web-8", "Ping Diagnostic", "web", "MEDIUM", 300, "Command Injection `; cat /flag.txt`.", "/rce_ping/", "Burp Suite / Terminal", "Form ping tidak melakukan sanitasi masukan. Inject perintah shell dengan pemisah titik koma: 127.0.0.1; cat /flag.txt."),
    ("web-9", "Business Logic Shop", "web", "MEDIUM", 350, "Manipulasi kuantitas produk negatif.", "/logic_shop/", "Burp Suite Repeater", "Saat membeli item flag ($1000), isi kolom kuantitas dengan bilangan negatif (misal -10). Total harga akan bernilai negatif dan mengkreditkan saldo akun Anda."),
    ("web-10", "Exposed .git Leak", "web", "MEDIUM", 150, "Public .git repository directory leak.", "/hidden_comment/", "GitTools / git-dumper", "Gunakan tool git-dumper untuk mengunduh folder .git terekspos, lalu periksa sejarah git log commit untuk menemukan file flag."),
    ("web-11", "URL Fetcher SSRF", "web", "HARD", 350, "SSRF ke internal admin loopback.", "/ssrf/", "Burp Suite / nuclei", "Lakukan Server-Side Request Forgery dengan memasukkan URL internal loopback server: http://127.0.0.1:8000/ssrf/internal/admin/secret."),
    ("web-12", "JWT Token Inspector", "web", "HARD", 400, "JWT Weak Secret / Alg None.", "/jwt_lab/", "jwt_tool / CyberChef", "Edit header JWT token menjadi {\"alg\":\"none\",\"typ\":\"JWT\"} dan payload {\"user\":\"admin\",\"role\":\"admin\"} lalu hapus bagian signature-nya."),
    ("web-13", "XXE XML Parser", "web", "HARD", 450, "XML External Entity Injection.", "/xxe_lab/", "Burp Suite / nuclei", "Kirim payload XML XXE pada request: &lt;!DOCTYPE test [ &lt;!ENTITY xxe SYSTEM \"file:///flag.txt\"&gt; ]&gt;&lt;data&gt;&amp;xxe;&lt;/data&gt;."),
    ("web-14", "Jinja2 SSTI Generator", "web", "HARD", 500, "SSTI WAF Keyword Bypass.", "/ssti/", "tplmap / nuclei", "Lakukan Server-Side Template Injection pada Jinja2 dengan payload bypass WAF: &#123;&#123; self.__init__.__globals__.__builtins__.open('/flag.txt').read() &#125;&#125;."),
    ("web-15", "Pickle Cache RCE", "web", "HARD", 500, "Python Pickle Deserialization RCE.", "/pickle_rce/", "Python 3 (pickle & base64)", "Buat skrip Python untuk menserialisasi kelas dengan method __reduce__ RCE cat /flag.txt, lalu encode hasil pickle ke Base64 dan pasang di cookie pickle_session."),

    # 🔐 2. Cryptography (10)
    ("crypto-16", "Caesar Cipher ROT13", "crypto", "EASY", 50, "Shift Cipher ROT13 decryption.", "/handout/16_caesar.txt", "CyberChef / tr", "Buka file 16_caesar.txt. Masukkan ciphertext ke CyberChef lalu gunakan operasi ROT13 (Shift 13) untuk membaca flag."),
    ("crypto-17", "Multi-Layer Encoding", "crypto", "EASY", 100, "Hex -> Base32 -> Base64 decoding.", "/handout/17_nested_encoding.txt", "CyberChef / Base32", "Buka file 17_nested_encoding.txt. Gunakan CyberChef dengan urutan resep: From Hex -&gt; From Base32 -&gt; From Base64."),
    ("crypto-18", "Legacy MD5 Hash Crack", "crypto", "MEDIUM", 200, "Cracking MD5 password hash.", "/weak_hash/", "hashcat / john / CrackStation", "Salin hash MD5 e10adc3949ba59abbe56e057f20f883e. Gunakan hashcat -m 0 e10adc3949ba59abbe56e057f20f883e rockyou.txt untuk mendapatkan password password123. Flag: CTF{password123}."),
    ("crypto-19", "RSA Small Exponent e=3", "crypto", "MEDIUM", 300, "RSA Low Exponent m = c^(1/3).", "/handout/19_rsa_e3.json", "Python 3 / SymPy", "Buka file 19_rsa_e3.json. Karena e=3 sangat kecil (c &lt; n), hitung nilai m dengan menghitung akar pangkat tiga dari ciphertext: m = c**(1/3) = 17. Flag: CTF{17}."),
    ("crypto-20", "RSA Prime Factorization", "crypto", "MEDIUM", 350, "RSA Factorization (p * q).", "/handout/20_rsa_factor.json", "factordb.com / SageMath", "Buka file 20_rsa_factor.json. Masukkan nilai n=493 ke factordb.com untuk menemukan p=17 dan q=29, phi=448, d=257, m=pow(312, 257, 493) = 448. Flag: CTF{448}."),
    ("crypto-21", "Single-Byte XOR Stream", "crypto", "MEDIUM", 250, "XOR Stream Cipher Brute-Force.", "/handout/21_xor_stream.txt", "CyberChef / xortool", "Buka file 21_xor_stream.txt. Masukkan hex ciphertext ke CyberChef -&gt; pilih operasi XOR Brute Force (kunci 1-byte 0x42)."),
    ("crypto-22", "Vigenère Cipher", "crypto", "MEDIUM", 300, "Frequency Analysis Key Discovery.", "/handout/22_vigenere.txt", "dcode.fr / Vigenere Solver", "Buka file 22_vigenere.txt. Masukkan ciphertext MBD{...} ke dcode.fr Vigenere Solver dengan kunci KEY untuk dekripsi."),
    ("crypto-23", "AES-128 ECB Mode Pattern Leak", "crypto", "HARD", 400, "AES ECB Block Alignment Leak.", "/handout/23_aes_ecb.hex", "Python 3 / CyberChef", "Buka file 23_aes_ecb.hex. Analisis blok hex 16-byte identik pada ECB mode yang mengindikasikan struktur data plaintext."),
    ("crypto-24", "Custom Hash Collision", "crypto", "HARD", 450, "Custom Hash Function Collision.", "/handout/24_custom_hash.py", "Z3 Solver / Python 3", "Buka file 24_custom_hash.py. Gunakan Z3 Theorem Prover untuk mencari string lain yang menghasilkan nilai hash 305419896."),
    ("crypto-25", "Diffie-Hellman Weak Mod", "crypto", "HARD", 500, "Diffie-Hellman Discrete Logarithm.", "/handout/25_dh_params.json", "SageMath / Pari-GP", "Buka file 25_dh_params.json. Hitung Discrete Logarithm Problem g^a = A (mod p) pada p=23 yang sangat kecil menggunakan SageMath (a=6, s=12). Flag: CTF{12}."),

    # 🔍 3. Digital Forensics (10)
    ("forensics-26", "Image EXIF Metadata", "forensics", "EASY", 50, "Exiftool metadata extraction.", "/handout/26_flag_image.jpg", "exiftool / strings", "Buka gambar 26_flag_image.jpg. Gunakan perintah terminal strings 26_flag_image.jpg atau exiftool untuk menemukan tag User Comment."),
    ("forensics-27", "PNG Image LSB Steganography", "forensics", "MEDIUM", 150, "LSB bitplane extraction.", "/handout/27_lsb_stego.png", "zsteg / Stegsolve", "Buka gambar 27_lsb_stego.png. Gunakan zsteg 27_lsb_stego.png untuk mengekstrak bitplane terendah (LSB) Plane 0."),
    ("forensics-28", "Corrupted Header Fix", "forensics", "MEDIUM", 200, "Magic Bytes PNG/JPEG repair.", "/handout/28_corrupted_header.png", "Hex Editor / xxd", "Buka file 28_corrupted_header.png di Hex Editor. Magic bytes 4 byte pertama rusak (00 00 00 00). Perbaiki menjadi 89 50 4E 47 untuk membuka gambar."),
    ("forensics-29", "Disk Partition Carving", "forensics", "MEDIUM", 300, "Foremost file carving.", "/handout/29_disk_carve.raw", "Autopsy / foremost", "Buka file 29_disk_carve.raw. Lakukan carving sektor memori mentah unallocated space dengan foremost -i 29_disk_carve.raw untuk mengekstrak berkas."),
    ("forensics-30", "Volatility Memory Dump", "forensics", "HARD", 450, "Volatility3 process dump.", "/handout/30_volatility_memory.dmp", "volatility3", "Buka file 30_volatility_memory.dmp. Periksa memori proses lsass.exe PID 1337 dengan volatility3 windows.pslist untuk mengekstrak string flag."),
    ("forensics-31", "Layered PDF Stream", "forensics", "MEDIUM", 250, "PDF object stream analysis.", "/handout/31_hidden_stream.pdf", "pdf-parser / pdfdetach", "Buka file 31_hidden_stream.pdf. Analisis struktur stream objek PDF dengan pdf-parser -c 31_hidden_stream.pdf untuk mengekstrak stream 4 0 obj."),
    ("forensics-32", "Encrypted ZIP Crack", "forensics", "MEDIUM", 200, "ZIP2John password cracking.", "/handout/32_encrypted_secret.zip", "zip2john & john", "Unduh file 32_encrypted_secret.zip. Ekstrak hash dengan zip2john 32_encrypted_secret.zip &gt; hash.txt lalu crack dengan john --wordlist=rockyou.txt hash.txt."),
    ("forensics-33", "Audio Spectrogram", "forensics", "HARD", 350, "Audacity spectrogram visualizer.", "/handout/33_audio_spectrogram.wav", "Audacity / Sonic Visualiser", "Buka file 33_audio_spectrogram.wav di Audacity. Ubah mode tampilan audio dari Waveform menjadi Spectrogram untuk melihat visual frekuensi pesan."),
    ("forensics-34", "Browser SQLite History", "forensics", "MEDIUM", 250, "Browser history query.", "/handout/34_history.sqlite", "sqlite3 / DB Browser", "Buka file 34_history.sqlite di DB Browser for SQLite. Jalankan query SQL: SELECT url FROM urls WHERE url LIKE '%secret%';."),
    ("35-usb", "USB HID Keystroke", "forensics", "HARD", 400, "USB keyboard packet mapping.", "/handout/35_usb_hid_keystrokes.pcap", "tshark / Python 3", "Buka file 35_usb_hid_keystrokes.pcap di Wireshark / tshark. Petakan hex byte USB HID keycode (0x06=C, 0x17=T, 0x09=F, ...) menjadi karakter keyboard."),

    # 📡 4. Network Sniffing (8)
    ("net-36", "HTTP Cleartext Packet", "network", "EASY", 100, "Wireshark PCAP POST inspection.", "/handout/36_http_login.pcap", "Wireshark / tshark", "Buka file 36_http_login.pcap di Wireshark. Filter dengan http.request.method == \"POST\", lalu klik kanan -&gt; Follow TCP Stream."),
    ("net-37", "DNS Tunneling Exfil", "network", "MEDIUM", 300, "Base64 DNS Query Decoding.", "/handout/37_dns_queries.pcap", "tshark / CyberChef", "Buka file 37_dns_queries.pcap di Wireshark. Ambil subdomain query DNS Q1RGe2Ruc183dW5u... lalu decode dari Base64."),
    ("net-38", "Anonymous FTP Capture", "network", "MEDIUM", 150, "FTP Passive Data Stream.", "/handout/38_ftp_passive.pcap", "Wireshark", "Buka file 38_ftp_passive.pcap di Wireshark. Filter dengan ftp-data untuk melihat stream transfer file pasif FTP."),
    ("net-39", "ICMP Covert Channel", "network", "HARD", 350, "ICMP Echo Payload Extraction.", "/handout/39_icmp_ping.pcap", "tshark / CyberChef", "Buka file 39_icmp_ping.pcap di Wireshark. Ekstrak data payload hex pada paket ICMP Echo Request (43 54 46 7b...), lalu decode Hex ke ASCII."),
    ("net-40", "SSL/TLS Keylog Decrypt", "network", "HARD", 400, "Wireshark SSLKEYLOGFILE Import.", "/handout/40_tls_keylog.pcap", "Wireshark TLS Preferences", "Buka file 40_tls_keylog.pcap di Wireshark. Impor baris SSLKEYLOGFILE ke Wireshark (Preferences -&gt; Protocols -&gt; TLS -&gt; (Pre)-Master-Secret log filename)."),
    ("net-41", "ARP Spoofing Analysis", "network", "MEDIUM", 250, "ARP MITM Packet Inspection.", "/handout/41_arp_mitm.pcap", "Wireshark", "Buka file 41_arp_mitm.pcap di Wireshark. Cari paket ARP Reply bermerek Man-in-the-Middle untuk mendeteksi data yang disadap."),
    ("net-42", "Unencrypted Telnet", "network", "EASY", 100, "Telnet TCP Stream Credentials.", "/handout/42_telnet_stream.pcap", "Wireshark", "Buka file 42_telnet_stream.pcap di Wireshark. Filter telnet lalu Follow TCP Stream pada port 23 untuk membaca password."),
    ("net-43", "IoT MQTT Packet Sniff", "network", "MEDIUM", 300, "MQTT Topic Subscription Leak.", "/handout/43_mqtt_broker.pcap", "Wireshark / mosquitto_sub", "Buka file 43_mqtt_broker.pcap di Wireshark. Filter mqtt lalu periksa payload pada topic /sensors/vault/security."),

    # ⚙️ 5. Reverse Engineering (7)
    ("rev-44", "ELF Compiled Strings", "reverse", "EASY", 50, "Strings & Symbols extraction.", "/handout/44_elf_strings.elf", "strings / ghidra", "Buka file 44_elf_strings.elf. Jalankan perintah terminal strings 44_elf_strings.elf | grep CTF untuk membaca string biner."),
    ("rev-45", "Python Bytecode (.pyc)", "reverse", "MEDIUM", 150, "Uncompyle6 decompilation.", "/handout/45_app.pyc", "uncompyle6 / decompyle++", "Buka file 45_app.pyc. Dekompilasi bytecode .pyc Python 3.11 dengan uncompyle6 45_app.pyc ke kode sumber Python murni."),
    ("rev-46", "Java Class Decompile", "reverse", "MEDIUM", 200, "JADX Java decompilation.", "/handout/46_Challenge.class", "jadx-gui / cfr", "Buka file 46_Challenge.class. Buka bytecode .class Java menggunakan decompiler jadx-gui 46_Challenge.class."),
    ("rev-47", "C ELF Crackme Logic", "reverse", "MEDIUM", 300, "Ghidra / GDB strcmp analysis.", "/handout/47_crackme.elf", "Ghidra / GDB", "Buka file 47_crackme.elf di Ghidra. Periksa logika pemanggilan fungsi strcmp(key, \"SUP3R_S3CR37_K3Y_2026\") pada fungsi main."),
    ("rev-48", "Android APK Smali", "reverse", "HARD", 350, "Smali code logic analysis.", "/handout/48_app_smali.txt", "jadx-gui / apktool", "Buka file 48_app_smali.txt. Periksa disassembly kode Smali const-string v0 pada kelas MainActivity."),
    ("rev-49", "x86 BOF ret2win", "reverse", "HARD", 450, "Stack overwrite return address.", "/handout/49_bof_ret2win.elf", "pwntools / gdb-pwndbg", "Buka biner 49_bof_ret2win.elf di Ghidra/GDB. Kerentanan gets(buffer) memungkinkan Buffer Overflow untuk meng-overwrite return address EIP ke alamat win()."),
    ("rev-50", "UPX Packed Unpacking", "reverse", "HARD", 500, "UPX unpack & anti-debug.", "/handout/50_upx_packed.elf", "upx -d / x64dbg", "Buka biner 50_upx_packed.elf. Dekompresi biner UPX dengan perintah upx -d 50_upx_packed.elf sebelum melakukan analisis biner.")
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

    for cid, name, cat, level, pts, desc, link, tool, hint in CHALLENGES:
        btn_text = "Buka Challenge →" if not link.startswith("/handout/") else "Unduh Handout 📥"
        color = badge_colors.get(level, "var(--accent-cyan)")
        
        safe_name = name.replace("'", "\\'")
        safe_tool = tool.replace("'", "\\'")
        safe_hint = hint.replace("'", "\\'").replace('"', '&quot;')

        card_html = f"""
            <div class="glass-card">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="font-size: 0.75rem; font-weight: 700; color: {color};">{level} • {pts} PTS</span>
                    <span style="font-size: 0.7rem; font-weight: 700; background: rgba(255,255,255,0.08); padding: 0.15rem 0.4rem; borderRadius: 4px; color: var(--text-muted);">{cat.upper()}</span>
                </div>
                <h3 class="card-title" style="margin-top: 0.4rem;">{name}</h3>
                <p class="card-desc">{desc}</p>

                <div style="margin-top: 1rem; display: flex; flex-direction: column; gap: 0.5rem;">
                    <button onclick="openHintModal('{safe_name}', '{cat.upper()}', '{safe_tool}', '{safe_hint}')" class="btn-hint" style="width: 100%; justify-content: center;">
                        💡 Hint & Recommended Tools
                    </button>
                    <a href="{link}" class="btn-primary" style="width: 100%; justify-content: center;">{btn_text}</a>
                </div>
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
        .btn-hint {{
            background: rgba(168, 85, 247, 0.12);
            border: 1px solid var(--accent-purple);
            color: var(--accent-purple);
            padding: 0.5rem 1rem;
            border-radius: 6px;
            font-size: 0.82rem;
            font-weight: 700;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            transition: all 0.2s ease;
        }}
        .btn-hint:hover {{
            background: var(--accent-purple);
            color: #fff;
            box-shadow: 0 0 12px rgba(168, 85, 247, 0.4);
        }}

        /* Hint Modal Styles */
        .modal-overlay {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            background: rgba(4, 7, 17, 0.85);
            backdrop-filter: blur(8px);
            display: none;
            justify-content: center;
            align-items: center;
            z-index: 9999;
        }}
        .modal-overlay.active {{
            display: flex;
        }}
        .modal-box {{
            background: #0a1128;
            border: 1px solid var(--accent-cyan);
            box-shadow: 0 0 30px rgba(6, 182, 212, 0.3);
            border-radius: 12px;
            width: 90%;
            max-width: 550px;
            padding: 1.8rem;
            color: #fff;
            position: relative;
        }}
        .modal-header {{
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 1.2rem;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 0.8rem;
        }}
        .modal-close {{
            background: none;
            border: none;
            color: var(--text-muted);
            font-size: 1.5rem;
            cursor: pointer;
            line-height: 1;
        }}
        .modal-close:hover {{
            color: var(--accent-pink);
        }}
        .tool-badge {{
            display: inline-block;
            background: rgba(6, 182, 212, 0.15);
            border: 1px solid var(--accent-cyan);
            color: var(--accent-cyan);
            padding: 0.3rem 0.8rem;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 700;
            margin-bottom: 1rem;
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

    <!-- HINT POPUP MODAL -->
    <div id="hintModal" class="modal-overlay" onclick="closeModalOnOverlay(event)">
        <div class="modal-box">
            <div class="modal-header">
                <div>
                    <span id="modalCategory" style="font-size: 0.72rem; font-weight: 700; color: var(--accent-purple); letter-spacing: 0.5px;">CATEGORY</span>
                    <h3 id="modalTitle" style="font-size: 1.4rem; font-weight: 800; color: #fff; margin-top: 0.2rem;">Challenge Title</h3>
                </div>
                <button class="modal-close" onclick="closeHintModal()">&times;</button>
            </div>
            
            <div>
                <div style="font-size: 0.8rem; color: var(--text-sub); margin-bottom: 0.3rem;">🛠️ Recommended Tools:</div>
                <div id="modalTool" class="tool-badge">Tool Name</div>

                <div style="font-size: 0.8rem; color: var(--text-sub); margin-bottom: 0.3rem;">💡 Hint & Petunjuk Pengerjaan:</div>
                <p id="modalHint" style="color: var(--text-muted); font-size: 0.92rem; line-height: 1.6; background: rgba(255,255,255,0.03); padding: 1rem; border-radius: 8px; border: 1px solid var(--border-color);">
                    Hint text details...
                </p>
            </div>

            <div style="margin-top: 1.5rem; display: flex; justify-content: flex-end;">
                <button class="btn-primary" onclick="closeHintModal()">Mengerti, Tutup Hint 👍</button>
            </div>
        </div>
    </div>

    <script>
        function switchCategory(catId) {{
            document.querySelectorAll('.category-tab').forEach(el => el.classList.remove('active'));
            document.querySelectorAll('.category-section').forEach(el => el.classList.remove('active'));
            
            event.target.classList.add('active');
            document.getElementById('cat-' + catId).classList.add('active');
        }}

        function openHintModal(title, category, tool, hint) {{
            document.getElementById('modalTitle').innerText = title;
            document.getElementById('modalCategory').innerText = category + ' • HINT GUIDE';
            document.getElementById('modalTool').innerText = tool;
            document.getElementById('modalHint').innerText = hint;
            document.getElementById('hintModal').classList.add('active');
        }}

        function closeHintModal() {{
            document.getElementById('hintModal').classList.remove('active');
        }}

        function closeModalOnOverlay(e) {{
            if (e.target.id === 'hintModal') {{
                closeHintModal();
            }}
        }}
    </script>
</body>
</html>
"""
    with open(PORTAL_PATH, "w", encoding="utf-8") as f:
        f.write(html_content)

if __name__ == "__main__":
    generate_portal()
    print("[🎉] portal.html generated cleanly with REAL native binary URLs!")
