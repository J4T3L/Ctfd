# Modul Ajar: SQL Injection Auth Bypass (Easy)

## 📌 Deskripsi Challenge
- **Nama Challenge**: DevNotes - Admin Portal
- **Kategori**: Web Exploitation
- **Tingkat Kesulitan**: Easy (100 Poin)
- **Tujuan Pembelajaran**: Memahami konsep dasar kerentanan **SQL Injection (SQLi)** pada formulir autentikasi login dan cara melakukan remediasi (parameterized query).

---

## 🔍 1. Analisis Kode Sumber (Vulnerability Analysis)

Perhatikan potongan kode pada `app/app.py`:

```python
query = f"SELECT id, username, role, flag FROM users WHERE username = '{username}' AND password = '{password}'"
```

Aplikasi menggabungkan input pengguna secara langsung (*string concatenation*) ke dalam string query SQL tanpa melakukan sanitasi atau menggunakan *parameterized statement*.

---

## 🛠️ 2. Eksploitasi (Authentication Bypass)

Ketika penguji memasukkan username: `admin' --`

Query SQL yang tereksekusi di database SQLite menjadi:
```sql
SELECT id, username, role, flag FROM users WHERE username = 'admin' --' AND password = '...'
```

Di dalam sintaks SQL, dua tanda minus `--` dianggap sebagai **komentar**. Sehingga bagian pengujian password `' AND password = '...'` diabaikan sepenuhnya oleh mesin database.

Database secara otomatis mengembalikan baris data untuk pengguna `admin` tanpa perlu mengetahui kata sandinya!

---

## 🚀 3. Langkah Penyelesaian (Step-by-Step)

1. Buka formulir login di aplikasi target (`http://localhost:8002` atau URL publik).
2. Di kolom **Username**, ketik: `admin' --` (atau `' OR '1'='1`).
3. Di kolom **Password**, ketik karakter sembarang (misal: `12345`).
4. Klik **Authenticate →**.
5. Login berhasil sebagai `admin` dan flag ditampilkan di halaman dashboard:
   `CTF{34sy_sql_1nj3ct10n_byp4ss_2026}`

---

## 🛡️ 4. Remediasi (Cara Memperbaiki Kode)

Gunakan **Parameterized Query** / **Prepared Statements** agar input pengguna diperlakukan murni sebagai data, bukan perintah sintaks SQL:

```python
# KODE YANG AMAN:
query = "SELECT id, username, role, flag FROM users WHERE username = ? AND password = ?"
user = cursor.execute(query, (username, password)).fetchone()
```
