# -*- coding: utf-8 -*-
import re
FILES = ["content.py", "diagrams.py"]

# 1) Reemplazos dirigidos (antes del blanket). Silenciosos si no estan.
TARGETED = [
    # interrogativas / signos
    ('"title": "Que vamos a hacer en estos 90 minutos",',
     '"title": "¿Qué vamos a hacer en estos 90 minutos?",'),
    ('"title": "Que proponer: seguridad por fase del proyecto",',
     '"title": "Qué proponer: seguridad por fase del proyecto",'),
    ('"title": "Las preguntas que IT te va a hacer (y como responder)",',
     '"title": "Las preguntas que IT te va a hacer (y cómo responder)",'),
    ("completo: que hay, que version corre, que esta expuesto.",
     "completo: qué hay, qué versión corre, qué está expuesto."),
    ("Solo mirar. Y ya sabe por donde.", "Solo mirar. Y ya sabe por dónde."),
    ("Eso es lo que esta en juego.", "Eso es lo que está en juego."),
    ('"big": "Tu proyecto AV esta listo.', '"big": "Tu proyecto AV está listo.'),
    ("Por que IT es tan restrictivo:", "Por qué IT es tan restrictivo:"),
    # preguntas slide 21 (quitar '->' y abrir con ¿)
    ("Que puertos abre este equipo? -> Lista documentada de puertos y servicios.",
     "¿Qué puertos abre este equipo?  Lista documentada de puertos y servicios."),
    ("En que red va a estar? -> En la VLAN AV, segmentada, con estas reglas.",
     "¿En qué red va a estar?  En la VLAN AV, segmentada, con estas reglas."),
    ("Como se autentican y gestionan las credenciales? -> Cuentas administradas, sin fabrica.",
     "¿Cómo se autentican y gestionan las credenciales?  Cuentas administradas, sin fábrica."),
    ("Como actualizamos y monitoreamos? -> Plan de firmware y logs hacia su SIEM.",
     "¿Cómo actualizamos y monitoreamos?  Plan de firmware y logs hacia su SIEM."),
    # diagramas: interrogativas indirectas / porque-como
    ("Que dispositivos hay y que exponen.", "Qué dispositivos hay y qué exponen."),
    ("Que se hace ante un incidente.", "Qué se hace ante un incidente."),
    ("Como se vuelve a operar.", "Cómo se vuelve a operar."),
    ("Quien responde por la seguridad del equipo.", "Quién responde por la seguridad del equipo."),
    ("Logs y monitoreo: saber cuando pasa algo.", "Logs y monitoreo: saber cuándo pasa algo."),
    ("Tacticas (el por que) y tecnicas (el como), observadas en incidentes reales.",
     "Tácticas (el porqué) y técnicas (el cómo), observadas en incidentes reales."),
    ("Que el sistema este cuando se lo necesita.", "Que el sistema esté cuando se lo necesita."),
    ("acordar quien lo mantiene en el tiempo.", "acordar quién lo mantiene en el tiempo."),
    ("acordar quien actualiza firmware.", "acordar quién actualiza firmware."),
    # voseo -> tuteo
    ("Para vos es un codec, un DSP, un controlador.", "Para ti es un codec, un DSP, un controlador."),
    ("Por eso no desconfian de vos. Desconfian de un host desconocido en su red.",
     "Por eso no desconfían de ti. Desconfían de un host desconocido en su red."),
    ("Vos tambien lo corres desde tu telefono, sobre la red del laboratorio.",
     "Si quieres, lo corres tú también desde tu teléfono, sobre la red del laboratorio."),
    ("Lleva vos el minimo: segmentacion, credenciales, cifrado, logs. Como estandar, no como extra.",
     "Lleva tú el mínimo: segmentación, credenciales, cifrado, logs. Como estándar, no como extra."),
    ("Documentalo y hacelo parte de la entrega. Protege al cliente y te protege a vos.",
     "Documentálo y hazlo parte de la entrega. Protege al cliente y te protege a ti."),
    ("Es un diferencial comercial: sos el integrador que entrega seguro por defecto.",
     "Es un diferencial comercial: eres el integrador que entrega seguro por defecto."),
    # agenda: punto 2 (escaner opcional, se puede sin instalar nada)
    ('("Para seguir la demo, un escaner de red opcional en el telefono. El kit se descarga despues.", 1, False),',
     '("Puedes seguir todo sin instalar nada.", 1, False),\n      ("Para quien quiera ir mas a fondo: un escaner de red opcional en el telefono.", 1, False),\n      ("El kit se descarga despues.", 1, False),'),
    # laboratorio: SSID/clave y matiz opcional
    ("Conectate a la WiFi del laboratorio (SSID y clave en pantalla).",
     "Conectate a la red ICAL26-LAB (clave: seguridadav26)."),
    ("Opcional: instala un escaner de red. En el telefono, Fing o Network Scanner; en laptop, nmap.",
     "Opcional, para ir mas a fondo: instala un escaner de red. En el telefono, Fing o Network Scanner; en laptop, nmap."),
    ('("SSID y clave en pantalla", 9, False, RGBColor(0xE3,0xEE,0xFA), PP_ALIGN.CENTER)',
     '("ICAL26-LAB  /  seguridadav26", 9, False, RGBColor(0xE3,0xEE,0xFA), PP_ALIGN.CENTER)'),
]

# 2) Blanket por palabra completa (ASCII -> acentuado/n~). Pares (old, new).
PAIRS = [
    ("diseno","diseño"),("disena","diseña"),("disenados","diseñados"),("disenar","diseñar"),
    ("senal","señal"),("telefono","teléfono"),("companía","compañía"),
    ("tactica","táctica"),("tacticas","tácticas"),("Tacticas","Tácticas"),
    ("tecnica","técnica"),("tecnicas","técnicas"),
    ("version","versión"),("Version","Versión"),
    ("segmentacion","segmentación"),("Segmentacion","Segmentación"),
    ("autenticacion","autenticación"),("organizacion","organización"),
    ("aplicacion","aplicación"),("Aplicacion","Aplicación"),
    ("presentacion","presentación"),("Presentacion","Presentación"),
    ("sesion","sesión"),("Sesion","Sesión"),
    ("fisica","física"),("Fisica","Física"),("fisico","físico"),
    ("publico","público"),("publica","pública"),
    ("catalogo","catálogo"),("Catalogo","Catálogo"),
    ("analisis","análisis"),("Analisis","Análisis"),
    ("trafico","tráfico"),("configuracion","configuración"),
    ("practica","práctica"),("tramite","trámite"),("revision","revisión"),
    ("gestion","gestión"),("Gestion","Gestión"),
    ("minimo","mínimo"),("Minimo","Mínimo"),
    ("despues","después"),("penso","pensó"),("instalo","instaló"),
    ("pequenos","pequeños"),("pequenas","pequeñas"),
    ("conexion","conexión"),("intrusion","intrusión"),
    ("fabrica","fábrica"),("estandar","estándar"),("maquina","máquina"),
    ("politicas","políticas"),("lamina","lámina"),("laminas","láminas"),
    ("mas","más"),("aqui","aquí"),("Aqui","Aquí"),("todavia","todavía"),
    ("caida","caída"),("vera","verá"),("angulo","ángulo"),("dia","día"),
    ("creible","creíble"),("demas","demás"),("explicitas","explícitas"),
    ("explicita","explícita"),("transito","tránsito"),("contrasena","contraseña"),
    ("ahi","ahí"),("Ahi","Ahí"),("area","área"),
    ("desconfian","desconfían"),("tambien","también"),("Tambien","También"),
    ("escaner","escáner"),("Conectate","Conéctate"),("Llevate","Llévate"),
    ("(el por que)","(el porqué)"),("(el como)","(el cómo)"),
    ("y como responder","y cómo responder"),
]

for fn in FILES:
    s = open(fn, encoding="utf-8").read()
    for a, b in TARGETED:
        s = s.replace(a, b)
    for a, b in PAIRS:
        if "(" in a or ")" in a or " " in a:
            s = s.replace(a, b)  # frases con parentesis/espacios: replace directo
        else:
            s = re.sub(r'\b' + re.escape(a) + r'\b', b, s)
    open(fn, "w", encoding="utf-8").write(s)
print("ortografia aplicada")
