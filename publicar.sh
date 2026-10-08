#!/usr/bin/env bash
# Publica los materiales a GitHub Pages. El repo git vive en esta carpeta.
set -e
cd "$(dirname "$0")"
cp -f ICAL26-seguridad-AV-parte1.pdf docs/diapositivas.pdf 2>/dev/null || true
cp -f kit/ICAL26-kit.pdf              docs/kit.pdf          2>/dev/null || true
git add -A
git commit -q -m "${1:-Actualiza materiales del taller}" || { echo "Sin cambios que publicar."; exit 0; }
git push -q origin main
echo "Publicado: https://jdpinedac.github.io/ical26-taller-seguridad-av/"
