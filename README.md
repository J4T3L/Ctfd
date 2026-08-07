# CTF Web Challenge: CyberVault Report Generator

Paket CTF Web Challenge ini dirancang untuk platform CTFd (`ctfcli` compatible).

---

## 📁 Struktur Direktori

- `app/`: Source code aplikasi web Flask & Jinja2
- `Dockerfile` & `docker-compose.yml`: Konfigurasi Docker container
- `challenge.yml`: Metadata CTFd (kategori, poin, deskripsi, hint, file lampiran)
- `flag.txt`: Teks flag sasaran (`CTF{s3rv3r_s1d3_t3mpl4t3_1nj3ct10n_m4st3r_2026}`)
- `cybervault_handout.zip`: Paket berkas lampiran untuk diberikan kepada peserta CTF
- `solution/`: Script exploit (`solve.py`) dan dokumentasi penyelesaian (`WRITEUP.md`)

---

## 🚀 Panduan Deployment LXC & Cloudflare Tunnel

Berikut langkah-langkah lengkap memasang challenge di dalam **LXC Container** dan mempublikasikannya menggunakan **Cloudflare Tunnel**:

### Langkah 1: Persiapan LXC Container
Masuk (SSH / Console) ke LXC container Anda (Ubuntu / Debian):

```bash
# Update package manager & install dependency
apt update && apt install -y python3 python3-pip python3-venv curl git docker.io docker-compose-plugin

# Copy atau upload folder project ke /opt/cybervault
mkdir -p /opt/cybervault
```

#### Cara A: Menggunakan Docker di dalam LXC (Direkomendasikan)
```bash
cd /opt/cybervault
docker compose up --build -d
```

#### Cara B: Menggunakan Systemd Service (Tanpa Docker)
```bash
cd /opt/cybervault

# Copy flag.txt ke root filesystem
cp flag.txt /flag.txt
chmod 444 /flag.txt

# Setup Virtual Environment
python3 -m venv venv
./venv/bin/pip install -r app/requirements.txt

# Buat Systemd Service
cat << 'EOF' > /etc/systemd/system/cybervault.service
[Unit]
Description=CyberVault CTF Web Challenge Service
After=network.target

[Service]
User=www-data
WorkingDirectory=/opt/cybervault
ExecStart=/opt/cybervault/venv/bin/gunicorn --bind 127.0.0.1:8000 --workers 2 app:app
Restart=always

[Install]
WantedBy=multi-user.target
EOF

# Jalankan service
systemctl daemon-reload
systemctl enable --now cybervault
```

---

### Langkah 2: Setup Tunneling (Cloudflare Tunnel / `cloudflared`)

Cloudflare Tunnel memungkinkan aplikasi web di LXC diakses dari internet secara aman dengan HTTPS gratis tanpa butuh IP Publik dedicated.

#### 1. Install `cloudflared` di LXC
```bash
curl -L --output cloudflared.deb https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
dpkg -i cloudflared.deb
```

#### 2A. Opsi Quick Tunnel (Instant & Gratis, Tanpa Account/Domain)
Jalankan perintah ini untuk mendapatkan URL publik sementara:
```bash
cloudflared tunnel --url http://127.0.0.1:8000
```
Output akan menampilkan URL seperti:
`https://random-name.trycloudflare.com`

#### 2B. Opsi Named Tunnel (Domain Sendiri / CTF Domain)
```bash
# Login ke akun Cloudflare Anda
cloudflared tunnel login

# Buat tunnel baru
cloudflared tunnel create cybervault-challenge

# Sambungkan domain ke tunnel (Contoh: cybervault.ctfku.com)
cloudflared tunnel route dns cybervault-challenge cybervault.ctfku.com

# Buat berkas konfigurasi /etc/cloudflared/config.yml
cat << 'EOF' > /etc/cloudflared/config.yml
tunnel: cybervault-challenge
credentials-file: /root/.cloudflared/<TUNNEL_ID>.json

ingress:
  - hostname: cybervault.ctfku.com
    service: http://127.0.0.1:8001
  - service: http_status:404
EOF

# Install & jalankan sebagai service di LXC
cloudflared service install
systemctl enable --now cloudflared
```

---

### Langkah 3: Update `challenge.yml` untuk CTFd

Setelah mendapatkan URL Tunnel (misal: `https://cybervault.ctfku.com` atau `https://xxx.trycloudflare.com`), perbarui bagian **`description`** pada `challenge.yml`:

```yaml
description: |
  CyberVault adalah platform generator laporan audit keamanan modern berbasis template Jinja2.
  Tim pengembang telah memasang WAF untuk mencegah eksekusi kode berbahaya.
  
  Apakah Anda dapat meloloskan diri dari pembatasan WAF dan membaca berkas rahasia di `/flag.txt`?

  **Target**: `https://cybervault.ctfku.com`
```

Impor `challenge.yml` ke CTFd menggunakan `ctfcli`:
```bash
ctf challenge add .
ctf challenge install .
```

---

## 🧪 Menguji Deployment dari Luar
Uji eksploitasi otomatis terhadap URL Tunnel dari luar LXC:
```bash
python3 solution/solve.py https://cybervault.ctfku.com
```


