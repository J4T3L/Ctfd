# 🛡️ CyberVault - 50 Multi-Category CTF Master Suite
> **Modul Ajar Praktikum Keamanan Siber & Jaringan Komputer**
> Repositori laboratorium CTF (Capture The Flag) multi-kategori lengkap dengan 50 tantangan praktikum (Web Exploitation, Cryptography, Digital Forensics, Network Sniffing, dan Reverse Engineering).

---

## 🚀 Keunggulan Arsitektur Baru

- **⚡ Waktu Build Docker Instan (< 5 Detik)**: Berbasis *Pure HTML5 + Vanilla CSS + Python 3.11-slim Flask Gateway*. Bebas kompilasi berat Node.js/npm sehingga ringan dan cepat di LXC container.
- **🎨 Glassmorphism UI & Hint Modal Pop-Up**: Antarmuka modern dengan **5 Filter Tab Kategori** serta tombol **`💡 Hint & Recommended Tools`** pada ke-50 kartu challenge.
- **🧩 100% Unique Handout Puzzles**: Berkas latihan non-web murni berwujud puzzle (*ciphertext, hex, base64/32, pcap log, opcode bytecode, c code, corrupt header*) tanpa bocoran flag plaintext.
- **🔌 1-Click Direct REST API Importer (`import_to_ctfd.py`)**: Script otomatis untuk mengimpor seluruh 50 challenge, flag, poin, dan petunjuk ke CTFd dalam 1 klik.

---

## 🏆 Pembagian 50 Challenge (5 Kategori Utama)

| Kategori CTF | Jumlah Lab | Topik & Celah Keamanan | Recommended Tools |
|---|---|---|---|
| **🌐 Web Exploitation** | 15 Labs | SQLi, HTML Comment, Base64 Cookie, Robots.txt, Reflected XSS, IDOR, LFI, RCE Ping, Logic Shop, SSRF, JWT, XXE, Jinja2 SSTI, Pickle RCE, Git Leak | `Burp Suite`, `nuclei`, `ffuf`, `sqlmap`, `tplmap`, `jwt_tool` |
| **🔐 Cryptography** | 10 Labs | Caesar/ROT13, Multi-Layer Encoding, MD5 Crack, RSA Small e, RSA Factorization, XOR Stream, Vigenère, AES ECB, Custom Hash, Diffie-Hellman | `CyberChef`, `hashcat`, `john`, `Z3 Solver`, `SageMath` |
| **🔍 Digital Forensics** | 10 Labs | EXIF Metadata, PNG LSB Stego, Magic Bytes Repair, Disk Carving, Volatility Dump, PDF Stream, Encrypted ZIP, Audio Spectrogram, SQLite History, USB HID | `exiftool`, `zsteg`, `autopsy`, `volatility3`, `Audacity`, `zip2john` |
| **📡 Network Sniffing** | 8 Labs | HTTP Cleartext, DNS Tunneling, FTP Passive Capture, ICMP Covert, TLS Decryption, ARP Spoofing MITM, Telnet Stream, IoT MQTT Broker | `Wireshark`, `tshark`, `mosquitto_sub` |
| **⚙️ Reverse Engineering** | 7 Labs | ELF Strings, Python `.pyc` Decompile, Java Class, C Crackme, Android APK Smali, x86 BOF ret2win, UPX Unpacking | `Ghidra`, `GDB`, `uncompyle6`, `JADX-GUI`, `pwntools`, `upx` |

---

## 💻 Quickstart Deployment di Server LXC

Jalankan perintah 1-klik ini di terminal server LXC Anda (`/opt/cybervault`):

```bash
cd /opt/cybervault
git fetch origin && git reset --hard origin/main
docker compose up --build -d
python3 import_to_ctfd.py
```

- **Web Target Portal**: `https://target.paradick.my.id/` (Port 8001 / Container Port 8000)
- **Scoreboard CTFd**: `https://ctfd.paradick.my.id/` (Port 80)

---

## 📑 Dokumentasi & Kunci Jawaban

Seluruh kunci jawaban, petunjuk eksplorasi, dan panduan penggunaan tools untuk ke-50 challenge tersimpan di berkas:
👉 **[`solution/PANDUAN_SOLUSI_DAN_TOOLS_50_CHALLENGES.txt`](file:///Users/superbia/Website/ctfd/solution/PANDUAN_SOLUSI_DAN_TOOLS_50_CHALLENGES.txt)**

---

## 📁 Struktur Repositori

```text
ctfd/
├── app/                  # Flask Server Gateway & 15 Blueprint Celah Web
│   ├── app.py            # Main App Gateway
│   ├── routes/           # 15 Flask Blueprint Web Vulnerabilities
│   ├── static/           # Vanilla CSS Glassmorphism Stylesheet
│   └── templates/        # Portal HTML & Hint Modals 50 Challenge
├── challenges/           # 50 Folder Metadata CTFd (01_sqli - 50_rev_upx_packed)
├── handout/              # 35 Berkas Handout Soal Puzzles (.txt, .json, .hex, .pcap, .zip, .c, .bin)
├── solution/             # Panduan Kunci Jawaban (PANDUAN_SOLUSI_DAN_TOOLS_50_CHALLENGES.txt) & Test Suite
├── Dockerfile            # Pure Python 3.11-slim (<5 Detik Build Time)
├── docker-compose.yml    # Port Mapping 8001:8000
├── import_to_ctfd.py     # Script 1-Klik Auto-Import 50 Challenge ke CTFd
├── flag.txt              # System Flag Base untuk LFI/RCE/SSTI
└── README.md             # Dokumentasi Modul Ajar
```

---
*Created for Modul Ajar Jarkom & Cyber Security 2026*
