# -*- coding: utf-8 -*-
# Contenido del deck - Parte 2 (Eduardo Travi, AVI SPL) - ICAL26
# Reproducción fiel de las láminas de Eduardo (sus títulos, textos y colores,
# que él ya tomó de la parte 1). Solo se renderizan con el estilo del deck.
# Direcciones y nombres son de un laboratorio de demostración.

SLIDES_P2 = [
  # ---------- 1: evolución de la sala ----------
  {
    "kind": "poc", "layout": "cards_header",
    "title": "La evolución de la sala: De la caja anónima al portal de Identidad e IA",
    "topbanner": "El cambio de paradigma en colaboración corporativa",
    "panels": [
      {"col": "blue", "head": "Ayer: La caja anónima (2011)", "sub": "La caja anónima (2011)", "items": [
        "Marcación directa por IP (H.323/SIP plano).",
        "Cuentas genéricas sin autenticación de usuario.",
        "Túnel de audio/video aislado del resto del negocio.",
        "Riesgo percibido por IT: Bajo (electrodoméstico)."]},
      {"col": "orange", "head": "Hoy: El nodo de identidad corporativa (2026)", "sub": "El nodo de identidad corporativa (2026)", "items": [
        "Autenticación basada en identidad de usuario y tokens.",
        "Integración nativa con agentes de IA y asistentes corporativos.",
        "La sala aprovisiona datos sensibles según los privilegios del perfil.",
        "Riesgo real: Acceso lateral a modelos y repositorios de datos."]},
    ],
    "notes": "Hace quince años la videoconferencia era una caja anónima: una IP fija, "
             "unos puertos abiertos y a transmitir. Hoy la sala es una terminal corporativa "
             "autenticada, con agentes de IA que cruzan datos según los permisos del usuario. "
             "Si no validamos la identidad de los extremos, abrimos la puerta a esos datos.",
  },
  # ---------- 2: la trampa del integrador ----------
  {
    "kind": "poc", "layout": "cards_header",
    "title": "La trampa del integrador: Ni negligencia ni barreras ciegas",
    "topbanner": "Gobernanza y diseño vs. extremos operativos",
    "panels": [
      {"col": "blue", "head": "Extremo 1: Negligencia por comodidad", "size": 11, "items": [
        "Desactivar cifrados (SRTP/TLS) para evitar demoras.",
        "APIs de automatización abiertas y con credenciales por defecto.",
        "Redes de sala sin validación ni inspección."]},
      {"col": "teal", "head": "El rol del integrador moderno", "size": 11, "items": [
        "La IA y la nube llegaron a la sala sin pedir permiso.",
        "Nuestro valor no es bloquear ni ser laxos: es diseñar con los marcos de IT (CIA, NIST) desde el plano inicial."]},
      {"col": "orange", "head": "Extremo 2: Seguridad por oscuridad", "size": 11, "items": [
        "Desconectar el equipamiento o prohibir la integración con IA.",
        "Bloqueos ciegos que frustran la adopción del usuario.",
        "Soluciones que degradan la productividad del negocio."]},
    ],
    "banner": "Eres el integrador que entrega seguro por defecto.",
    "notes": "Ante las exigencias de IT caemos en dos extremos: la negligencia por comodidad "
             "y el bloqueo ciego. Ambos nos dejan fuera del negocio. El rol es entender el "
             "lenguaje de IT para que la productividad fluya sin perforar el perímetro.",
  },
  # ---------- 3: el 'goteo' ----------
  {
    "kind": "poc", "layout": "chevrons",
    "title": "El concepto del 'Goteo': Cómo opera un atacante real",
    "topbanner": "De la recolección fragmentada al vector de ingeniería social de precisión",
    "cols": [
      {"col": "blue", "head": "Información Pública (OSINT)", "items": [
        "Redes profesionales: Organigramas, directivos, jerarquías.",
        "Proveedores habituales de TI, soporte y marcas utilizadas."]},
      {"col": "orange", "head": "Información de Red Interna", "items": [
        "Escaneo de puertos y servicios expuestos.",
        "Dispositivos de sala que responden sin autenticación previa."]},
      {"col": "teal", "head": "Información de dispositivos AV", "items": [
        "Agendas corporativas extraídas de la memoria del equipo.",
        "Historial reciente de llamadas y hábitos de reunión."]},
    ],
    "notes": "En el mundo real los ataques ocurren por goteo: piezas aisladas que, por sí "
             "solas, parecen inofensivas. Sumadas, dan la jerarquía completa de la empresa "
             "para un engaño de precisión. Vamos a demostrarlo sobre el laboratorio.",
  },
  # ---------- 4: topología del laboratorio ----------
  {
    "kind": "poc", "layout": "hosts_premise",
    "title": "Topología del Laboratorio: La VLAN de sala expuesta",
    "topbanner": "Entorno físico de demostración montado en escenario",
    "hosts": [
      {"col": "blue",    "name": "Servidor SIP (192.168.0.191)",           "role": "Proxy de señalización interno."},
      {"col": "orange",  "name": "Teléfono de escritorio (192.168.0.21)",  "role": "Interno administrativo / Finanzas (Ext. 1320)."},
      {"col": "teal",    "name": "Terminal de VC de sala (192.168.0.79)",  "role": "Códec de Sala Directorio (Ext. 1340)."},
      {"col": "magenta", "name": "Laptop Atacante (192.168.0.45)",         "role": "Conexión directa a boca de red de sala."},
    ],
    "premise": {"head": "Premisa de Diseño Equivocada",
                "quote": "'La VLAN AV es privada, por lo tanto no necesitamos certificados ni cifrado estricto'."},
    "notes": "Una VLAN de sala donde conviven un proxy SIP, un teléfono ejecutivo y un códec "
             "de directorio. La justificación típica es «es una red privada, nadie entra». "
             "Partamos de esa premisa y veámosla fallar.",
  },
  # ---------- 5: Demo 1 nmap ----------
  {
    "kind": "poc", "layout": "hosts_command",
    "title": "Demo 1: Reconocimiento y Topología (nmap)",
    "topbanner": "Fase Kill Chain: Reconocimiento activo sin credenciales de red",
    "command_label": "Comando de Auditoría",
    "command": "nmap -sS -sU -p 22,24,80,443,5060 192.168.0.0/24",
    "hosts": [
      {"col": "blue",    "name": "Servidor SIP (192.168.0.191)",           "role": "Proxy de señalización interno."},
      {"col": "orange",  "name": "Teléfono de escritorio (192.168.0.21)",  "role": "Interno administrativo / Finanzas (Ext. 1320)."},
      {"col": "teal",    "name": "Terminal de VC de sala (192.168.0.79)",  "role": "Códec de Sala Directorio (Ext. 1340)."},
      {"col": "magenta", "name": "Laptop Atacante (192.168.0.45)",         "role": "Conexión directa a boca de red de sala."},
    ],
    "notes": "Paso uno de la Kill Chain: reconocimiento. Sin credenciales, el escaneo muestra "
             "el proxy SIP en 5060 y el códec de sala, con puertos de control abiertos por "
             "defecto. Es la misma herramienta que vimos en la parte 1.",
  },
  # ---------- 6: Demo 2 señalización en claro ----------
  {
    "kind": "poc", "layout": "cards_header",
    "title": "Demo 2: Señalización en claro (Wireshark / sngrep)",
    "topbanner": "Fase Kill Chain: Explotación de la confianza implícita",
    "panels": [
      {"col": "blue", "head": "VULNERABILIDAD", "sub": "SIP Plano sobre UDP (Puerto 5060)", "items": [
        "Encabezados, identidades y extensiones viajan legibles en la red.",
        "Negociación SDP de medios sin llaves criptográficas (RTP/AVP)."]},
      {"col": "orange", "head": "ENCRIPTACIÓN / AUTENTICACIÓN", "sub": "Falta de mTLS / Autenticación Mutua", "items": [
        "El proxy SIP acepta cualquier registro de softphone en el puerto 5060.",
        "Ausencia total de validación criptográfica de identidad de máquina."]},
    ],
    "notes": "Como la red se diseñó sin exigir SIP sobre TLS, la señalización viaja en texto "
             "legible y el proxy confía en cualquier equipo que le hable por el 5060. Es el "
             "eslabón que la defensa en profundidad cierra con cifrado y mTLS.",
  },
  # ---------- 7: Demo 3 goteo local ----------
  {
    "kind": "poc", "layout": "topbar", "card_h": 3.5,
    "title": "Demo 3: El 'Goteo' de Inteligencia local (API/SSH)",
    "topbanner": "Fase Kill Chain: Recolección y Exfiltración de datos corporativos",
    "cards": [
      {"col": "orange", "head": "Comandos ejecutados en el Códec (IP .79)", "items": [
        "addrbook all → Exfiltración completa de la libreta de contactos (20 directivos).",
        "recentcalls → Historial de llamadas: con quién se habló, hora y duración."]},
      {"col": "blue", "head": "Impacto del Hallazgo", "items": [
        "Identificación exacta del CEO, Directores y Mesa de Ayuda TI.",
        "Confirmación de llamada reciente: La sala acaba de sesionar con Presidencia."]},
    ],
    "notes": "Una API de automatización sin proteger entrega la agenda y el historial de "
             "llamadas. Con eso el goteo se completa: organigrama, quién manda y con quién se "
             "habló. El control es simple: credenciales fuertes y acceso a la API por IP.",
  },
  # ---------- 8: Demo 4 armado del vector ----------
  {
    "kind": "poc", "layout": "topbar", "card_h": 3.5,
    "title": "Demo 4: Armado del Vector: Suplantación de Identidad (Spoofing)",
    "topbanner": "Fase Kill Chain: Armamento (Weaponization)",
    "cards": [
      {"col": "orange", "head": "Configuración del Atacante (MicroSIP)", "items": [
        "Display Name: 'Soporte AV'.",
        "Dirección SIP: soporte@contoso.net (obtenida de la agenda legítima)."]},
      {"col": "blue", "head": "Falla en el Enrutamiento", "items": [
        "El servidor Kamailio reenvía la señalización confiando en el origen.",
        "La red no desafía si la laptop de mantenimiento tiene permiso para representar a Soporte."]},
    ],
    "notes": "Con un softphone común, el nombre «Soporte AV» y una dirección legítima de la "
             "agenda, la infraestructura no desafía la identidad. El control que lo frena es "
             "el certificado mutuo de máquina (mTLS).",
  },
  # ---------- 9: Demo 5 acción sobre el objetivo ----------
  {
    "kind": "poc", "layout": "topbar", "card_h": 3.5,
    "title": "Demo 5: Acción sobre el Objetivo: Vishing de precisión en vivo",
    "topbanner": "Fase Kill Chain: Acción sobre el Objetivo / Ingeniería Social",
    "cards": [
      {"col": "orange", "head": "El Escenario en la Pantalla de la Sala", "items": [
        "La pantalla principal muestra la llamada entrante: 'Soporte AV'.",
        "Audio bidireccional instantáneo y corte fluido sin retardos."]},
      {"col": "blue", "head": "El Engaño (Vishing)", "items": [
        "'Estimada mesa de directorio: detectamos una intermitencia de audio en su reciente sesión con Presidencia. Por favor confirmen el código de verificación...'",
        "Confianza ciega: Los usuarios asumen que el aviso de su pantalla es legítimo."]},
    ],
    "notes": "El ataque se cierra con una llamada que aparece en pantalla como «Soporte AV», "
             "justo después de una sesión real. El usuario no desconfía. Lo que parecía un "
             "detalle técnico del AV terminó siendo el vector de ingeniería social.",
  },
  # ---------- 10: Remediación ----------
  {
    "kind": "poc", "layout": "topbar", "card_h": 3.9,
    "title": "Remediación: Aplicando Defensa en Profundidad",
    "topbanner": "Cómo neutralizar cada etapa de la Kill Chain desde el diseño",
    "cards": [
      {"col": "orange", "head": "Falla en la Demo → Control Técnico que la Evita", "size": 12, "items": [
        "Escaneo de red (nmap) → Control de acceso 802.1X + Microsegmentación.",
        "Fuga de agenda por API → Contraseñas robustas + Restricción de IP para APIs.",
        "Captura SIP en claro → SIP sobre TLS (puerto 5061) obligatorio.",
        "Suplantación de softphone → Certificados mutuos de máquina (mTLS).",
        "Audio sin cifrar → Cifrado AES / SRTP configurado como 'Requerido'."]},
    ],
    "notes": "Ninguna de estas defensas es cara. Con 802.1X la laptop ni recibe IP; con la "
             "API restringida no hay fuga de agenda; con mTLS el proxy rechaza el softphone; "
             "con SRTP obligatorio la llamada falsa ni timbra. Se cierra desde el plano.",
  },
  # ---------- 11: nueva postura ----------
  {
    "kind": "poc", "layout": "topbar", "card_h": 3.2, "bullet": False,
    "title": "La nueva postura del integrador AV",
    "topbanner": "De técnicos de equipamiento a garantes de la seguridad e identidad corporativa",
    "cards": [
      {"col": "orange", "head": "1. Hablar el idioma de IT", "items": [
        "Diseñar con marcos formales (CIA, NIST, Zero Trust) desde la primera reunión con el cliente."]},
      {"col": "blue", "head": "2. Habilitar la innovación sin comprometer la red", "items": [
        "Proteger la infraestructura para que los agentes de IA y las salas operen con total gobernanza."]},
      {"col": "magenta", "head": "3. Responsabilidad compartida", "items": [
        "La frontera entre AV y ciberseguridad desapareció: la sala de juntas es un nodo de cómputo crítico."]},
    ],
    "notes": "IT no es el enemigo: es el custodio de los activos más valiosos. Cuando llegamos "
             "con segmentación, cifrado, validación de identidad y gobernanza para los agentes "
             "de IA, dejamos de traer dolores de cabeza y pasamos a habilitar la colaboración "
             "moderna. Gracias.",
  },
]
