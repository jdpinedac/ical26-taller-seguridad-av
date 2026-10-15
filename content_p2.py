# -*- coding: utf-8 -*-
# Contenido del deck - Parte 2 (Eduardo Travi, AVI SPL) - ICAL26
# La prueba de concepto con SIP. Los conceptos son los mismos que estudia la
# ciberseguridad y que vimos en la parte 1 (Kill Chain, CIA, NIST, defensa en
# profundidad); aquí se demuestran en vivo. Direcciones y nombres son de un
# laboratorio ficticio, sólo para la demostración didáctica.

SLIDES_P2 = [
  {
    "kind": "poc",
    "title": "La evolución de la sala: de la caja anónima al nodo de identidad",
    "layout": "twocol",
    "panels": [
      {"col": "grey", "head": "Ayer (2011): la caja anónima", "head_h": 0.95, "items": [
        "Marcación directa por IP (H.323 / SIP plano).",
        "Cuentas genéricas, sin autenticación de usuario.",
        "Audio y video aislados del resto del negocio.",
        "Riesgo percibido por IT: bajo. Un electrodoméstico más."]},
      {"col": "blue", "head": "Hoy (2026): el nodo de identidad corporativa", "head_h": 0.95, "items": [
        "Autenticación por identidad del usuario y por tokens.",
        "Integración nativa con agentes de IA y asistentes corporativos.",
        "Accede a datos sensibles según el perfil de quien inicia sesión.",
        "Riesgo real: acceso lateral a modelos y repositorios de datos."]},
    ],
    "banner": "Si no validamos la identidad de los extremos, no sólo arriesgamos la llamada:",
    "banner_sub": "abrimos la puerta a los agentes de IA y a los datos a los que ellos acceden.",
    "notes": "La sala de juntas dejó de ser un equipo aislado: hoy es una terminal "
             "corporativa autenticada, con asistentes de IA que cruzan datos según los "
             "permisos del usuario. Por eso validar la identidad de los extremos deja de "
             "ser un lujo y pasa a ser parte del diseño.",
  },
  {
    "kind": "poc",
    "title": "La trampa del integrador: ni negligencia ni bloqueo ciego",
    "layout": "twocol",
    "panels": [
      {"col": "red", "head": "Extremo 1: negligencia por comodidad", "head_h": 0.95, "size": 11, "head_shape": "chevron", "items": [
        "Desactivar cifrados (SRTP / TLS) para evitar demoras.",
        "APIs de automatización abiertas y con credenciales por defecto.",
        "Redes de sala sin validación ni inspección."]},
      {"col": "teal", "head": "El rol del integrador moderno", "head_h": 0.95, "size": 11, "head_shape": "chevron", "items": [
        "La IA y la nube llegaron a la sala sin pedir permiso.",
        "Nuestro valor no es bloquear ni ser laxos:",
        "es diseñar con los marcos de IT (CIA, NIST) desde el plano inicial."]},
      {"col": "red", "head": "Extremo 2: seguridad por oscuridad", "head_h": 0.95, "size": 11, "head_shape": "chevron", "items": [
        "Desconectar el equipo o prohibir la integración con IA.",
        "Bloqueos ciegos que frustran la adopción del usuario.",
        "Soluciones que degradan la productividad del negocio."]},
    ],
    "banner": "Ni candados que impidan trabajar ni puertas abiertas: seguridad desde el diseño.",
    "notes": "Ante las exigencias de IT caemos en dos extremos: la negligencia por "
             "comodidad y el bloqueo ciego. Ambos nos dejan fuera del negocio. El rol es "
             "entender el lenguaje de IT para que la productividad fluya sin perforar el perímetro.",
  },
  {
    "kind": "poc",
    "title": "El concepto del «goteo»: cómo se arma un ataque dirigido",
    "layout": "twocol",
    "panels": [
      {"col": "blue", "head": "Información pública (OSINT)", "head_h": 0.95, "size": 11, "items": [
        "Redes profesionales: organigramas, directivos, jerarquías.",
        "Proveedores habituales de TI, soporte y marcas usadas."]},
      {"col": "orange", "head": "Información de la red interna", "head_h": 0.95, "size": 11, "items": [
        "Puertos y servicios expuestos en el segmento.",
        "Dispositivos de sala que responden sin autenticación previa."]},
      {"col": "teal", "head": "Información de los dispositivos AV", "head_h": 0.95, "size": 11, "items": [
        "Agendas corporativas guardadas en la memoria del equipo.",
        "Historial reciente de llamadas y hábitos de reunión."]},
    ],
    "banner": "Nada es grave por separado. Combinado, es el guion de un ataque dirigido.",
    "banner_sub": "Es el mismo «goteo» que vimos en la parte 1, ahora demostrado en vivo.",
    "notes": "En el mundo real los ataques ocurren por goteo: piezas aisladas que, por sí "
             "solas, parecen inofensivas. Sumadas, dan la jerarquía completa de la empresa "
             "para un engaño de precisión. Vamos a demostrarlo sobre el laboratorio.",
  },
  {
    "kind": "poc",
    "title": "Topología del laboratorio: la VLAN de sala expuesta",
    "layout": "hosts",
    "hosts": [
      {"col": "blue",    "name": "Servidor SIP",           "ip": "192.168.0.191", "role": "Proxy de señalización interno."},
      {"col": "orange",  "name": "Teléfono de escritorio", "ip": "192.168.0.21",  "role": "Interno administrativo / Finanzas (ext. 1320)."},
      {"col": "teal",    "name": "Terminal de VC de sala", "ip": "192.168.0.79",  "role": "Códec de la sala de directorio (ext. 1340)."},
      {"col": "magenta", "name": "Laptop (técnico)",       "ip": "192.168.0.45",  "role": "Conectada a una boca de red de la sala."},
    ],
    "right": {"col": "indigo", "head": "Premisa de diseño equivocada",
              "quote": "«La VLAN AV es privada; por eso no necesita certificados ni cifrado estricto.»"},
    "banner": "Veamos qué pasa cuando asumimos que una red privada es, por eso mismo, una red segura.",
    "notes": "Una VLAN de sala donde conviven un proxy SIP, un teléfono ejecutivo y un códec "
             "de directorio. La justificación típica es «es una red de video privada, nadie "
             "entra aquí». Partamos de esa premisa y veámosla fallar.",
  },
  {
    "kind": "poc",
    "title": "Demo 1: reconocimiento y topología",
    "tag": "Fase Kill Chain · Reconocimiento (sin credenciales de red)",
    "layout": "hosts",
    "hosts": [
      {"col": "blue",    "name": "Servidor SIP",           "ip": "192.168.0.191", "role": "Proxy SIP escuchando en el puerto 5060."},
      {"col": "orange",  "name": "Teléfono de escritorio", "ip": "192.168.0.21",  "role": "Interno administrativo / Finanzas (ext. 1320)."},
      {"col": "teal",    "name": "Terminal de VC de sala", "ip": "192.168.0.79",  "role": "Códec de directorio: SIP + puertos 22 y 24 abiertos."},
      {"col": "magenta", "name": "Laptop (técnico)",       "ip": "192.168.0.45",  "role": "Punto de observación en el segmento."},
    ],
    "command": "nmap -sS -sU -p 22,24,80,443,5060 192.168.0.0/24",
    "command_label": "Comando de auditoría de red",
    "banner": "Un escaneo revela la topología completa: el proxy SIP y el códec de sala, sin una sola credencial.",
    "notes": "Paso uno de la Kill Chain: reconocimiento. Sin credenciales, el escaneo del "
             "segmento muestra el proxy SIP en 5060 y el códec de sala, con puertos de "
             "control abiertos por defecto. Es la misma herramienta que vimos en la parte 1.",
  },
  {
    "kind": "poc",
    "title": "Demo 2: señalización en claro (análisis de tráfico)",
    "tag": "Fase Kill Chain · Explotación de la confianza implícita",
    "layout": "twocol",
    "panels": [
      {"col": "magenta", "head": "La vulnerabilidad", "items": [
        "SIP plano sobre UDP (puerto 5060): encabezados, identidades y extensiones viajan legibles.",
        "Negociación de medios (SDP) sin claves criptográficas (RTP/AVP)."]},
      {"col": "teal", "head": "Lo que falta", "items": [
        "Sin SIP sobre TLS: nada cifra la señalización.",
        "Sin mTLS: el proxy acepta el registro de cualquier softphone en el 5060.",
        "Ausencia de validación criptográfica de la identidad del equipo."]},
    ],
    "banner": "Diseñar sin exigir TLS deja la identidad y la señalización al descubierto.",
    "notes": "Como la red se diseñó sin exigir SIP sobre TLS, la señalización viaja en "
             "texto legible y el proxy confía en cualquier equipo que le hable por el 5060. "
             "Es el eslabón que la defensa en profundidad cierra con cifrado y mTLS.",
  },
  {
    "kind": "poc",
    "title": "Demo 3: el «goteo» de inteligencia local",
    "tag": "Fase Kill Chain · Recolección de datos",
    "layout": "twocol",
    "panels": [
      {"col": "blue", "head": "Lo que el equipo entrega", "items": [
        "La libreta de contactos completa del códec (p. ej. 20 directivos).",
        "El historial reciente de llamadas: con quién, a qué hora y cuánto duró."]},
      {"col": "orange", "head": "Por qué importa", "items": [
        "Identifica con precisión a la dirección y a la mesa de ayuda de TI.",
        "Confirma actividad reciente: con quién acaba de sesionar la sala."]},
    ],
    "banner": "Un códec que entrega su agenda por una API sin proteger completa el «goteo».",
    "banner_sub": "Lo evitan credenciales robustas y la API restringida por IP.",
    "notes": "Una API de automatización sin proteger entrega la agenda y el historial de "
             "llamadas. Con eso el goteo se completa: organigrama, quién manda y con quién "
             "se habló. El control es simple: credenciales fuertes y acceso a la API por IP.",
  },
  {
    "kind": "poc",
    "title": "Demo 4: armado del vector (suplantación de identidad)",
    "tag": "Fase Kill Chain · Armado del vector",
    "layout": "twocol",
    "panels": [
      {"col": "magenta", "head": "La suplantación", "items": [
        "Un softphone estándar con el nombre visible «Soporte AV».",
        "Una dirección SIP tomada de la propia agenda de la empresa."]},
      {"col": "teal", "head": "La falla que lo permite", "items": [
        "El proxy reenvía la señalización confiando en el origen.",
        "La red no desafía a un equipo que dice representar a «Soporte»."]},
    ],
    "banner": "No hace falta malware ni un día cero: basta la confianza implícita en «la red interna».",
    "notes": "Con un softphone común, el nombre «Soporte AV» y una dirección legítima de la "
             "agenda, la infraestructura no desafía la identidad. El control que lo frena es "
             "el certificado mutuo de máquina (mTLS).",
  },
  {
    "kind": "poc",
    "title": "Demo 5: acción sobre el objetivo (pretexto telefónico)",
    "tag": "Fase Kill Chain · Acción sobre el objetivo · Ingeniería social",
    "layout": "twocol",
    "panels": [
      {"col": "orange", "head": "Lo que ve la sala", "items": [
        "La pantalla muestra una llamada entrante de «Soporte AV».",
        "Audio nítido y bidireccional, como cualquier llamada legítima."]},
      {"col": "magenta", "head": "Por qué el engaño funciona", "items": [
        "Un pretexto creíble: una supuesta falla de audio en la sesión anterior.",
        "Confianza ciega: el usuario asume que el aviso en pantalla es legítimo."]},
    ],
    "banner": "Con datos reales y un identificador falso, el pretexto telefónico resulta convincente.",
    "banner_sub": "La cadena técnica terminó quebrando la seguridad de la sala.",
    "notes": "El ataque se cierra con una llamada que aparece en pantalla como «Soporte AV», "
             "justo después de una sesión real. El usuario no desconfía. Lo que parecía un "
             "detalle técnico del AV terminó siendo el vector de ingeniería social.",
  },
  {
    "kind": "poc",
    "title": "Remediación: defensa en profundidad, etapa por etapa",
    "tag": "De la Kill Chain al control técnico que la evita",
    "layout": "mapping",
    "rows": [
      ["Escaneo de red", "Control de acceso 802.1X + microsegmentación."],
      ["Fuga de agenda por API", "Credenciales robustas + API restringida por IP."],
      ["Señalización SIP en claro", "SIP sobre TLS (puerto 5061) obligatorio."],
      ["Suplantación de softphone", "Certificados mutuos de máquina (mTLS)."],
      ["Audio sin cifrar", "SRTP / AES configurado como «requerido»."],
    ],
    "banner": "Cada etapa se neutraliza desde el diseño. No es presupuesto: es criterio.",
    "notes": "Ninguna de estas defensas es cara. Con 802.1X la laptop ni recibe IP; con la "
             "API restringida no hay fuga de agenda; con mTLS el proxy rechaza el softphone; "
             "con SRTP obligatorio la llamada falsa ni timbra. Se cierra desde el plano, no después.",
  },
  {
    "kind": "poc",
    "title": "La nueva postura del integrador AV",
    "layout": "cards",
    "subtitle": "De técnicos de equipamiento a garantes de la seguridad y la identidad corporativa",
    "cards": [
      {"col": "blue",    "head": "1. Hablar el idioma de IT",
       "desc": "Diseñar con marcos formales (CIA, NIST, Zero Trust) desde la primera reunión con el cliente."},
      {"col": "orange",  "head": "2. Habilitar sin exponer",
       "desc": "Proteger la infraestructura para que los agentes de IA y las salas operen con gobernanza."},
      {"col": "magenta", "head": "3. Responsabilidad compartida",
       "desc": "La frontera entre AV y ciberseguridad desapareció: la sala es un nodo de cómputo crítico."},
    ],
    "banner": "Seguridad diseñada desde el día cero. Ése es el socio estratégico que IT quiere.",
    "notes": "IT no es el enemigo: es el custodio de los activos más valiosos. Cuando "
             "llegamos con segmentación, cifrado, validación de identidad y gobernanza para "
             "los agentes de IA, dejamos de traer dolores de cabeza y pasamos a habilitar "
             "la colaboración moderna. Gracias.",
  },
]
