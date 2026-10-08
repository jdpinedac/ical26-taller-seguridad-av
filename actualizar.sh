#!/usr/bin/env bash
# Reconstruye deck + kit, refresca los PDF del evento y publica en GitHub Pages.
# Uso:  ./actualizar.sh "mensaje del cambio"
set -e
cd "$(dirname "$0")"
PY=".venv/bin/python"
[ -x "$PY" ] || { echo "Falta el entorno. Crealo: python3 -m venv .venv && .venv/bin/pip install -r requirements.txt"; exit 1; }

echo "1/3  Reconstruyendo el deck..."
ICAL26_PUBLISH_DIR="../slides" "$PY" build.py >/dev/null

echo "2/3  Reconstruyendo el kit..."
( cd kit && pandoc kit.md -o body_frag.html && ../"$PY" build_kit_wp.py >/dev/null )
cp -f kit/ICAL26-kit.pdf ../kit/ICAL26-kit.pdf
cp -f kit/kit.md         ../kit/kit.md

echo "3/3  Publicando en GitHub Pages..."
./publicar.sh "${1:-Actualiza deck y kit}"
