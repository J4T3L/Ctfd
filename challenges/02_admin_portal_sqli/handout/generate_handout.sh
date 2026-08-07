#!/bin/bash
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
CHALLENGE_DIR="$(dirname "$SCRIPT_DIR")"

cd "$CHALLENGE_DIR" || exit 1

echo "[*] Packaging admin_portal_sqli_handout.zip..."
rm -f admin_portal_sqli_handout.zip

zip -r admin_portal_sqli_handout.zip \
    app/ \
    Dockerfile \
    docker-compose.yml \
    handout/README.md \
    -x "*.pyc" -x "*__pycache__*" -x "*.DS_Store" -x "app/database.db"

echo "[+] Successfully created admin_portal_sqli_handout.zip"
