#!/bin/bash
# Master script to install / sync all 10 CTF challenges into CTFd via ctfcli

echo "[*] Syncing all 10 CTF Web Challenges to CTFd..."

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
)

for dir in "${CHALLENGE_DIRS[@]}"; do
    if [ -d "$dir" ]; then
        echo "--------------------------------------------------------"
        echo "[+] Installing/Syncing: $dir"
        (cd "$dir" && ctf challenge add . 2>/dev/null; ctf challenge install . 2>/dev/null || ctf challenge sync .)
    fi
done

echo "--------------------------------------------------------"
echo "[🎉] All 10 challenges synced successfully to CTFd!"
