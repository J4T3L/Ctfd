#!/bin/bash
# Master script to install / sync all 15 CTF challenges into CTFd via ctfcli

if [ ! -d ".ctf" ]; then
    echo "[!] Error: Folder .ctf belum di-inisialisasi."
    echo "[!] Silakan jalankan 'ctf init' terlebih dahulu di folder /opt/cybervault!"
    exit 1
fi

echo "[*] Syncing all 15 CTF Web Challenges to CTFd..."

CHALLENGE_DIRS=(
    "challenges/01_sqli"
    "challenges/02_comment_leak"
    "challenges/03_cookie_lab"
    "challenges/04_idor"
    "challenges/05_lfi"
    "challenges/06_rce_ping"
    "challenges/07_ssrf"
    "challenges/08_jwt_lab"
    "challenges/09_ssti"
    "challenges/10_pickle_rce"
    "challenges/11_xss_reflected"
    "challenges/12_robots_secret"
    "challenges/13_weak_hash"
    "challenges/14_xxe_lab"
    "challenges/15_logic_shop"
)

for dir in "${CHALLENGE_DIRS[@]}"; do
    if [ -d "$dir" ]; then
        echo "--------------------------------------------------------"
        echo "[+] Processing: $dir"
        ctf challenge add "$dir"
        ctf challenge install "$dir" || ctf challenge sync "$dir"
    fi
done

echo "--------------------------------------------------------"
echo "[🎉] Sync process finished!"
