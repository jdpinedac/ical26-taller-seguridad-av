# Generador del taller ICAL26

Todo el código vive aquí, en Dropbox, así viaja entre máquinas y queda junto al
resto del proyecto. El entorno Python (`.venv`) y el control de versiones (`.git`)
se mantienen FUERA de Dropbox a propósito (Dropbox corrompe los `.git`).

## Preparar el entorno (una vez por máquina, fuera de Dropbox)

    python3 -m venv ~/ical26-venv
    ~/ical26-venv/bin/pip install -r requirements.txt
    # Requiere además: pandoc y libreoffice instalados en el sistema.

## Generar

    V=~/ical26-venv/bin/python     # o el venv que hayas creado
    $V build.py                    # deck -> ICAL26-seguridad-AV-parte1.pptx/.pdf
    cd kit && pandoc kit.md -o body_frag.html && $V build_kit_wp.py && cd ..

Para publicar a la vez los PDF en las carpetas del evento:

    ICAL26_PUBLISH_DIR="../slides" $V build.py

## Publicar la página (GitHub Pages)

    ./publicar.sh "mensaje del cambio"

Sincroniza esta carpeta con el repo espejo (~/src/ical26-slides) y hace push.
La página queda en https://jdpinedac.github.io/ical26-taller-seguridad-av/
