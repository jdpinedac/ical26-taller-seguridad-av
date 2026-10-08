# Generador del taller ICAL26

Todo vive aquí, en Dropbox: el código, el repositorio git y los materiales.
Así viaja entre máquinas y queda junto al proyecto.

- El `.git` **sí** se sincroniza por Dropbox (viaja contigo). GitHub es el respaldo.
- El `.venv` **no** se sincroniza (un entorno de Linux no sirve en otra plataforma).
  Se recrea en cada máquina.

## Preparar el entorno (una vez por máquina)

    python3 -m venv .venv
    .venv/bin/pip install -r requirements.txt
    # Requiere además pandoc y libreoffice instalados en el sistema.

## Generar

    .venv/bin/python build.py                 # deck (.pptx + .pdf)
    cd kit && pandoc kit.md -o body_frag.html && ../.venv/bin/python build_kit_wp.py && cd ..

Para publicar los PDF en las carpetas del evento al generar:

    ICAL26_PUBLISH_DIR="../slides" .venv/bin/python build.py

## Publicar la página (GitHub Pages)

    ./publicar.sh "mensaje del cambio"

Página: https://jdpinedac.github.io/ical26-taller-seguridad-av/
