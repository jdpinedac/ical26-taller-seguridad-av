# ICAL26 — Cuando IT frena tu proyecto AV

Materiales del taller de seguridad para integradores AV, presentado en
**InfoComm América Latina 2026** (Ciudad de México, 22 de octubre de 2026).

Parte 1: Juan Pineda · Pyxis — Parte 2: Eduardo Travi · AVI SPL

## Qué hay aquí

- `docs/` — página pública (GitHub Pages) con las diapositivas y el kit en PDF.
- `build/` ... los scripts de Python que generan el deck y el kit.

## Para reconstruir

El deck se arma sobre el template oficial de AVIXA, que **no se incluye** en este
repositorio. Para compilar localmente, copia el archivo del template como
`template.pptx` en la raíz y vuelve a colocar los logos de marca del evento en
`assets/logos/`. Luego:

```
python build.py            # genera el deck (.pptx + .pdf)
cd kit && python build_kit_wp.py   # genera el kit (.pdf)
```

Requiere un entorno con `python-pptx`, `weasyprint` y `pandoc`.

## Aviso

Material educativo. Las marcas de equipos se omiten a propósito. Esto no es
asesoría legal: consulta la normativa vigente de tu país.
