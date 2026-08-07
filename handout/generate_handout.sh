#!/bin/bash
# Generate distribution zip for CTF competitors

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"

cd "$ROOT_DIR" || exit 1

echo "[*] Packaging player handout zip archive..."
rm -f cybervault_handout.zip

zip -r cybervault_handout.zip \
    app/ \
    Dockerfile \
    docker-compose.yml \
    handout/README.md \
    -x "*.pyc" -x "*__pycache__*" -x "*.DS_Store"

echo "[+] Successfully created cybervault_handout.zip"
