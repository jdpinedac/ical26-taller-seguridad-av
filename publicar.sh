#!/usr/bin/env bash
# Publica los materiales actuales a GitHub Pages.
# El codigo fuente vive en esta carpeta (Dropbox). El repo git es un espejo en ~/src.
set -e
GEN="$(cd "$(dirname "$0")" && pwd)"
MIRROR="$HOME/src/ical26-slides"
# refrescar los PDF publicos con lo ultimo generado
cp -f "$GEN/ICAL26-seguridad-AV-parte1.pdf" "$GEN/docs/diapositivas.pdf" 2>/dev/null || true
cp -f "$GEN/kit/ICAL26-kit.pdf"              "$GEN/docs/kit.pdf"          2>/dev/null || true
# espejar al repo git (preservando .git y .venv del espejo)
rsync -a --delete --exclude='.git/' --exclude='.venv/' --exclude='__pycache__/' --exclude='*.pyc' "$GEN"/ "$MIRROR"/
cd "$MIRROR"
git add -A
git commit -q -m "${1:-Actualiza materiales del taller}" 2>/dev/null || { echo "Sin cambios que publicar."; exit 0; }
git push -q origin main
echo "Publicado: https://jdpinedac.github.io/ical26-taller-seguridad-av/"
