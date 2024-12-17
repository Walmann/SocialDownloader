#!/bin/bash

# Variabler
VENV_DIR="$PWD/.venv"  # Navnet på det virtuelle miljøet
REQ_FILE="requirements.txt"  # Fil med pakkekrav

# Sjekk om Python er installert
# if ! command -v python3 &>/dev/null; then
if ! which python3 > /dev/null 2>&1; then
    echo "Python3 er ikke installert. Installer det først."
    exit 1
else
    echo "Python3 er installert: $(python3 --version)"
fi

# Sjekk om requirements.txt finnes
if [ ! -f "$REQ_FILE" ]; then
    echo "Filen $REQ_FILE finnes ikke. Opprett denne for å installere pakkene."
    exit 1
fi

# Sjekk om det virtuelle miljøet allerede eksisterer
if [ -d "$VENV_DIR" ]; then
    echo "Det virtuelle miljøet finnes allerede. Aktiverer det..."
else
    echo "Det virtuelle miljøet finnes ikke. Oppretter ett nytt..."
    python3 -m venv "$VENV_DIR"

    if [ $? -ne 0 ]; then
        echo "Kunne ikke opprette det virtuelle miljøet."
        exit 1
    fi

    echo "Det virtuelle miljøet er opprettet."
fi

# Aktiver det virtuelle miljøet
source "$VENV_DIR/bin/activate"

if [ $? -ne 0 ]; then
    echo "Kunne ikke aktivere det virtuelle miljøet."
    exit 1
fi

echo "Det virtuelle miljøet er aktivert."

# Installer pakkene fra requirements.txt
echo "Installerer pakkene fra $REQ_FILE..."
pip install --upgrade pip  # Oppdater pip
pip install -r "$REQ_FILE"

if [ $? -ne 0 ]; then
    echo "Kunne ikke installere pakkene."
    deactivate
    exit 1
fi

echo "Pakkene er installert."

# Ferdig
echo "Skriptet er fullført. Starter SocialDownloader via continousDownload.py"

python3 ./continousDownload.py
