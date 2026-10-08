# -*- coding: utf-8 -*-
# Diagramas nativos (python-pptx) para el deck ICAL26. Todo editable, sin imagenes externas.
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn

FONT = "Montserrat"
FONT_MED = "Montserrat Medium"

INDIGO = RGBColor(0x34, 0x1E, 0x66)
VIOLET = RGBColor(0x34, 0x25, 0x60)
BLUE   = RGBColor(0x00, 0x7E, 0xE5)
ORANGE = RGBColor(0xF2, 0x8C, 0x00)
MAGENTA= RGBColor(0xC0, 0x20, 0x8E)
TEAL   = RGBColor(0x00, 0x9E, 0x9E)
GREEN  = RGBColor(0x2E, 0xA8, 0x4E)
RED    = RGBColor(0xD1, 0x3A, 0x3A)
WHITE  = RGBColor(0xFF, 0xFF, 0xFF)
GREY   = RGBColor(0x6B, 0x6B, 0x75)
LGREY  = RGBColor(0xF2, 0xF2, 0xF5)
PALE   = RGBColor(0xEB, 0xEE, 0xF6)
LILAC  = RGBColor(0xD6, 0xCF, 0xEA)

PALETTE = [BLUE, ORANGE, MAGENTA, TEAL, INDIGO, GREEN]

def _noshadow(sh):
    sh.shadow.inherit = False

def _settext(tf, items, anchor=MSO_ANCHOR.MIDDLE, wrap=True):
    # items: lista de (texto, size, bold, color, align)
    tf.word_wrap = wrap
    tf.vertical_anchor = anchor
    tf.margin_left = Pt(6); tf.margin_right = Pt(6)
    tf.margin_top = Pt(3); tf.margin_bottom = Pt(3)
    first = True
    for (txt, size, bold, color, align) in items:
        p = tf.paragraphs[0] if first else tf.add_paragraph()
        first = False
        p.alignment = align
        r = p.add_run(); r.text = txt
        r.font.size = Pt(size); r.font.bold = bold
        r.font.color.rgb = color; r.font.name = FONT

def rrect(slide, l, t, w, h, fill, line=None, radius=0.08):
    sh = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(l), Inches(t), Inches(w), Inches(h))
    _noshadow(sh)
    try: sh.adjustments[0] = radius
    except Exception: pass
    if fill is None:
        sh.fill.background()
    else:
        sh.fill.solid(); sh.fill.fore_color.rgb = fill
    if line is None:
        sh.line.fill.background()
    else:
        sh.line.color.rgb = line; sh.line.width = Pt(1.25)
    return sh

def oval(slide, l, t, w, h, fill, line=None):
    sh = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(l), Inches(t), Inches(w), Inches(h))
    _noshadow(sh)
    sh.fill.solid(); sh.fill.fore_color.rgb = fill
    if line is None: sh.line.fill.background()
    else: sh.line.color.rgb = line; sh.line.width = Pt(1.5)
    return sh

def textbox(slide, l, t, w, h, items, anchor=MSO_ANCHOR.TOP):
    tb = slide.shapes.add_textbox(Inches(l), Inches(t), Inches(w), Inches(h))
    _settext(tb.text_frame, items, anchor=anchor)
    return tb

def badge(slide, l, t, w, h, text, fill, tcolor=WHITE, size=12):
    sh = rrect(slide, l, t, w, h, fill, radius=0.5)
    _settext(sh.text_frame, [(text, size, True, tcolor, PP_ALIGN.CENTER)])
    return sh

def card(slide, l, t, w, h, accent, head, desc):
    base = rrect(slide, l, t, w, h, WHITE, line=RGBColor(0xDD,0xDD,0xE5), radius=0.06)
    bar = rrect(slide, l, t, w, 0.12, accent, radius=0.0)  # franja superior
    tf = base.text_frame
    _settext(tf, [
        (head, 14, True, INDIGO, PP_ALIGN.LEFT),
        (desc, 11.5, False, GREY, PP_ALIGN.LEFT),
    ], anchor=MSO_ANCHOR.TOP)
    base.text_frame.paragraphs[0].space_before = Pt(6)
    return base

def chevron(slide, l, t, w, h, fill, label, sub=None):
    sh = slide.shapes.add_shape(MSO_SHAPE.CHEVRON, Inches(l), Inches(t), Inches(w), Inches(h))
    _noshadow(sh); sh.fill.solid(); sh.fill.fore_color.rgb = fill; sh.line.fill.background()
    items = [(label, 13, True, WHITE, PP_ALIGN.CENTER)]
    if sub: items.append((sub, 9.5, False, RGBColor(0xED,0xEA,0xF6), PP_ALIGN.CENTER))
    _settext(sh.text_frame, items)
    return sh

def link(slide, x1, y1, x2, y2, color=GREY, width=1.75, dash=False):
    conn = slide.shapes.add_connector(2, Inches(x1), Inches(y1), Inches(x2), Inches(y2))
    conn.line.color.rgb = color; conn.line.width = Pt(width)
    if dash:
        ln = conn.line._get_or_add_ln()
        ln.append(ln.makeelement(qn('a:prstDash'), {'val': 'dash'}))
    return conn

def arrow(slide, x1, y1, x2, y2, color=BLUE, width=2.0):
    conn = slide.shapes.add_connector(2, Inches(x1), Inches(y1), Inches(x2), Inches(y2))
    conn.line.color.rgb = color; conn.line.width = Pt(width)
    ln = conn.line._get_or_add_ln()
    tail = ln.makeelement(qn('a:tailEnd'), {'type': 'triangle'})
    ln.append(tail)
    return conn

# ---------- diagramas por slide ----------

def cards_row(slide, prs, cards, top=2.1, h=3.2, lo=0.92, gap=0.3, total=11.5):
    n = len(cards)
    w = (total - gap * (n - 1)) / n
    x = lo
    for (accent, head, desc) in cards:
        card(slide, x, top, w, h, accent, head, desc)
        x += w + gap

def d_pecados(slide, prs):
    cards = [
        (ORANGE,  "Interfaces sin autenticación", "Paneles y APIs abiertos a cualquiera en la red.", "Ej.: el panel del códec sin clave."),
        (BLUE,    "Credenciales de fábrica", "admin / admin en equipos carísimos.", "Ej.: la contraseña que nunca se cambió."),
        (MAGENTA, "Protocolos legacy y sin cifrar", "mDNS, Telnet, HTTP plano: tráfico al descubierto.", "Ej.: mDNS anunciando el equipo a todos."),
        (TEAL,    "Firmware y software viejo", "Versiones con vulnerabilidades conocidas, sin parchar.", "Ej.: un CVE público del modelo exacto."),
        (GREEN,   "Sin visibilidad", "Ni logs ni monitoreo: nadie ve lo que pasa.", "Ej.: un acceso raro que nadie registra."),
        (RED,     "Acceso físico al rack", "Diez segundos frente al equipo alcanzan.", "Ej.: un puerto libre en el switch."),
    ]
    w = 3.63; h = 2.0; gap = 0.3; vgap = 0.25; top = 1.9
    for i, (col, head, desc, ej) in enumerate(cards):
        x = 0.92 + (i % 3) * (w + gap)
        y = top + (i // 3) * (h + vgap)
        rrect(slide, x, y, w, h, WHITE, line=RGBColor(0xDD,0xDD,0xE5), radius=0.06)
        rrect(slide, x, y, w, 0.11, col, radius=0.0)
        tb = slide.shapes.add_textbox(Inches(x + 0.2), Inches(y + 0.16), Inches(w - 0.4), Inches(h - 0.3))
        tf = tb.text_frame; tf.word_wrap = True; tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = tf.paragraphs[0]; r = p.add_run(); r.text = head
        r.font.size = Pt(12.5); r.font.bold = True; r.font.color.rgb = INDIGO; r.font.name = FONT
        p.space_after = Pt(4)
        p2 = tf.add_paragraph(); r2 = p2.add_run(); r2.text = desc
        r2.font.size = Pt(10.5); r2.font.color.rgb = GREY; r2.font.name = FONT
        p2.space_after = Pt(5)
        p3 = tf.add_paragraph(); r3 = p3.add_run(); r3.text = ej
        r3.font.size = Pt(9.5); r3.font.bold = True; r3.font.color.rgb = col; r3.font.name = FONT
    textbox(slide, 0.92, 6.22, 11.5, 0.3,
            [("Son las vulnerabilidades comunes que describe AVIXA RP-C303.01, §5.2.", 10, False, GREY, PP_ALIGN.CENTER)],
            anchor=MSO_ANCHOR.MIDDLE)

def d_criterios(slide, prs):
    # marco: defensa en profundidad
    banner = rrect(slide, 0.92, 1.75, 11.5, 0.85, INDIGO, radius=0.1)
    _settext(banner.text_frame, [
        ("Defensa en profundidad", 16, True, WHITE, PP_ALIGN.CENTER),
        ("Varias capas de proteccion: si una falla, el ataque no llega al final.".replace("proteccion","protección"),
         12, False, LILAC, PP_ALIGN.CENTER),
    ])
    capas = [
        (BLUE,    "Capa 1", "Mínimo privilegio", "Cada equipo y usuario, solo lo que necesita."),
        (ORANGE,  "Capa 2", "Segmentación", "El AV en su propia red, aparte de corporativa e invitados."),
        (TEAL,    "Capa 3", "Cifrado", "Control y señal protegidos en tránsito, no en texto plano."),
        (MAGENTA, "Capa 4", "Credenciales gestionadas", "Nada de admin/admin; cuentas administradas y rotadas."),
    ]
    w = 2.65; gap = 0.3; top = 2.95; h = 2.05
    for i, (col, capa, name, desc) in enumerate(capas):
        x = 0.92 + i * (w + gap)
        rrect(slide, x, top, w, h, WHITE, line=RGBColor(0xDD,0xDD,0xE5), radius=0.07)
        head = rrect(slide, x, top, w, 0.82, col, radius=0.07)
        _settext(head.text_frame, [
            (capa.upper(), 9, True, RGBColor(0xFF,0xFF,0xFF), PP_ALIGN.CENTER),
            (name, 12.5, True, WHITE, PP_ALIGN.CENTER),
        ])
        textbox(slide, x + 0.22, top + 0.82, w - 0.44, h - 0.9,
                [(desc, 11, False, GREY, PP_ALIGN.LEFT)], anchor=MSO_ANCHOR.MIDDLE)
    textbox(slide, 0.92, 5.45, 11.5, 0.6,
            [("Son las mismas capas que vamos a ver atacadas, paso a paso, en el resto de la sesión.",
              13, True, INDIGO, PP_ALIGN.CENTER)], anchor=MSO_ANCHOR.MIDDLE)

def d_hardening(slide, prs):
    banner = rrect(slide, 0.92, 1.75, 11.5, 0.85, INDIGO, radius=0.1)
    _settext(banner.text_frame, [
        ("Seguro por defecto, no por pedido", 16, True, WHITE, PP_ALIGN.CENTER),
        ("El equipo sale de tu mano ya endurecido. No esperas a que IT lo exija.", 12, False, LILAC, PP_ALIGN.CENTER),
    ])
    items = [
        (BLUE,   "Credenciales", "Cambiar las de fábrica y retirar las temporales de la instalación; cuentas administradas."),
        (ORANGE, "Superficie", "Apagar servicios y protocolos sin uso: Telnet, mDNS, UPnP."),
        (TEAL,   "Firmware", "Actualizar y acordar quién lo mantiene en el tiempo."),
        (MAGENTA,"Cifrado", "Control y gestión cifrados; nada de HTTP plano ni Telnet."),
        (GREEN,  "Visibilidad", "Dejar logs activos y enviarlos a donde IT los vea."),
    ]
    n = len(items); gap = 0.22; w = (11.5 - (n-1)*gap) / n
    top = 2.85; h = 2.0
    for i, (col, head, desc) in enumerate(items):
        x = 0.92 + i * (w + gap)
        rrect(slide, x, top, w, h, WHITE, line=RGBColor(0xDD,0xDD,0xE5), radius=0.08)
        o = oval(slide, x + w/2 - 0.26, top + 0.2, 0.52, 0.52, col)
        _settext(o.text_frame, [(str(i+1), 15, True, WHITE, PP_ALIGN.CENTER)])
        tb = slide.shapes.add_textbox(Inches(x + 0.12), Inches(top + 0.82), Inches(w - 0.24), Inches(h - 0.95))
        tf = tb.text_frame; tf.word_wrap = True; tf.vertical_anchor = MSO_ANCHOR.TOP
        p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER; p.space_after = Pt(4)
        r = p.add_run(); r.text = head; r.font.size = Pt(12.5); r.font.bold = True; r.font.color.rgb = col; r.font.name = FONT
        p2 = tf.add_paragraph(); p2.alignment = PP_ALIGN.CENTER
        r2 = p2.add_run(); r2.text = desc; r2.font.size = Pt(10); r2.font.color.rgb = GREY; r2.font.name = FONT
    textbox(slide, 0.92, 5.1, 11.5, 0.8,
            [("Cinco cosas antes de entregar. Si el cliente no las pide, las haces igual.", 13, True, INDIGO, PP_ALIGN.CENTER),
             ("Alineado con la línea base de seguridad de AVIXA RP-C303.01, §7.", 10.5, False, GREY, PP_ALIGN.CENTER)],
            anchor=MSO_ANCHOR.MIDDLE)

def d_cia(slide, prs):
    # columna izquierda: triangulo con nombres pegados a cada nodo
    cx = 3.75; tw, th = 3.2, 2.75; tl = cx - tw/2; tt = 2.55; d = 0.95
    tri = slide.shapes.add_shape(MSO_SHAPE.ISOSCELES_TRIANGLE, Inches(tl), Inches(tt), Inches(tw), Inches(th))
    _noshadow(tri); tri.fill.background(); tri.line.color.rgb = INDIGO; tri.line.width = Pt(2.25)
    nodes = [
        ("C", BLUE,   tl + tw/2 - d/2, tt - d/2,       "Confidencialidad", "above"),
        ("I", ORANGE, tl - d/2,        tt + th - d/2,  "Integridad",       "below"),
        ("D", TEAL,   tl + tw - d/2,   tt + th - d/2,  "Disponibilidad",   "below"),
    ]
    for letter, col, nx, ny, name, pos in nodes:
        o = oval(slide, nx, ny, d, d, col)
        _settext(o.text_frame, [(letter, 26, True, WHITE, PP_ALIGN.CENTER)])
        ly = ny - 0.5 if pos == "above" else ny + d + 0.08
        textbox(slide, nx + d/2 - 1.3, ly, 2.6, 0.42, [(name, 13, True, col, PP_ALIGN.CENTER)], anchor=MSO_ANCHOR.MIDDLE)
    # columna derecha: tarjetas con explicacion y ejemplo
    cards = [
        (BLUE,   "C", "Confidencialidad", "Que la señal y las credenciales no las vea quien no debe.", "Ej.: streaming sin cifrar."),
        (ORANGE, "I", "Integridad",       "Que nadie altere lo emitido ni la configuración.",         "Ej.: firmware sin firmar."),
        (TEAL,   "D", "Disponibilidad",   "Que el sistema esté cuando se lo necesita.",               "Ej.: la sala del directorio, caída en vivo."),
    ]
    x = 6.9; w = 12.42 - x; top = 1.95; h = 1.3; gap = 0.2
    for i, (col, letter, name, desc, ej) in enumerate(cards):
        y = top + i * (h + gap)
        rrect(slide, x, y, w, h, WHITE, line=RGBColor(0xDD,0xDD,0xE5), radius=0.1)
        o = oval(slide, x + 0.2, y + (h - 0.6)/2, 0.6, 0.6, col)
        _settext(o.text_frame, [(letter, 16, True, WHITE, PP_ALIGN.CENTER)])
        textbox(slide, x + 0.95, y + 0.06, w - 1.1, h - 0.12, [
            (name, 12.5, True, col, PP_ALIGN.LEFT),
            (desc, 10.5, False, GREY, PP_ALIGN.LEFT),
            (ej, 10, True, INDIGO, PP_ALIGN.LEFT),
        ], anchor=MSO_ANCHOR.MIDDLE)

def d_nist(slide, prs):
    funcs = [
        (INDIGO, "Gobernar", "Quién responde por la seguridad del equipo."),
        (BLUE,   "Identificar", "Qué dispositivos hay y qué exponen."),
        (TEAL,   "Proteger", "Segmentar, cifrar, mínimo privilegio."),
        (ORANGE, "Detectar", "Logs y monitoreo: saber cuándo pasa algo."),
        (MAGENTA,"Responder", "Qué se hace ante un incidente."),
        (GREEN,  "Recuperar", "Cómo se vuelve a operar."),
    ]
    w, h, gap, bar = 1.78, 2.35, 0.18, 0.6
    total = len(funcs)*w + (len(funcs)-1)*gap
    x = (13.333 - total)/2; top = 2.05
    for col, name, desc in funcs:
        rrect(slide, x, top, w, h, WHITE, line=RGBColor(0xDD,0xDD,0xE5), radius=0.08)
        head = rrect(slide, x, top, w, bar, col, radius=0.08)
        _settext(head.text_frame, [(name, 12.5, True, WHITE, PP_ALIGN.CENTER)])
        textbox(slide, x+0.1, top+bar, w-0.2, h-bar, [(desc, 10.5, False, GREY, PP_ALIGN.CENTER)], anchor=MSO_ANCHOR.MIDDLE)
        x += w + gap
    textbox(slide, 0.92, 4.85, 11.5, 0.6,
            [("El integrador toca sobre todo Identificar y Proteger.", 13.5, True, INDIGO, PP_ALIGN.CENTER)],
            anchor=MSO_ANCHOR.MIDDLE)

def d_killchain(slide, prs):
    textbox(slide, 0.92, 1.55, 11.5, 0.45,
            [("Cyber Kill Chain (Lockheed Martin): las 7 etapas.", 13, True, GREY, PP_ALIGN.LEFT)])
    stages = [
        (BLUE,    "Reconocimiento"),
        (BLUE,    "Armado"),
        (TEAL,    "Entrega"),
        (ORANGE,  "Explotación"),
        (ORANGE,  "Instalación"),
        (MAGENTA, "Comando y control"),
        (INDIGO,  "Acciones sobre el objetivo"),
    ]
    n = len(stages); slot = 11.5 / n; cy = 2.45; d = 0.78
    centers = [0.92 + slot * (i + 0.5) for i in range(n)]
    for i in range(n - 1):
        arrow(slide, centers[i] + d/2, cy + d/2, centers[i+1] - d/2, cy + d/2, color=GREY, width=1.5)
    for i, ((col, name), cx) in enumerate(zip(stages, centers)):
        o = oval(slide, cx - d/2, cy, d, d, col)
        _settext(o.text_frame, [(str(i+1), 20, True, WHITE, PP_ALIGN.CENTER)])
        textbox(slide, cx - slot/2 + 0.05, cy + d + 0.12, slot - 0.1, 0.85,
                [(name, 9.5, True, INDIGO, PP_ALIGN.CENTER)], anchor=MSO_ANCHOR.TOP)
    textbox(slide, 0.92, 4.5, 11.5, 0.5,
            [("Mapa 2 — MITRE ATT&CK detalla cada etapa en tácticas y técnicas. Lo vemos enseguida.",
              12.5, True, INDIGO, PP_ALIGN.CENTER)])
    textbox(slide, 0.92, 5.2, 11.5, 0.9, [
        ("No hace falta un atacante sofisticado.", 14, True, INDIGO, PP_ALIGN.CENTER),
        ("Hace falta una cadena de descuidos pequeños. La recorremos con demos, cada una con su táctica ATT&CK.",
         12, False, GREY, PP_ALIGN.CENTER),
    ], anchor=MSO_ANCHOR.TOP)

def d_mitre(slide, prs):
    badge(slide, 0.92, 1.5, 2.6, 0.5, "MITRE ATT&CK", MAGENTA, size=13)
    textbox(slide, 3.7, 1.5, 8.5, 0.5,
            [("Base de conocimiento de comportamientos reales de atacantes.", 12, False, GREY, PP_ALIGN.LEFT)],
            anchor=MSO_ANCHOR.MIDDLE)
    defs = [
        (MAGENTA, "Táctica = el QUÉ", "El objetivo que el atacante quiere conseguir en un momento dado."),
        (BLUE,    "Técnica = el CÓMO", "El método que usa para lograrlo. Las subtécnicas son sus variantes."),
    ]
    w = 5.55; gap = 0.4; dtop = 2.1; dh = 0.95
    for i, (col, head, desc) in enumerate(defs):
        x = 0.92 + i * (w + gap)
        rrect(slide, x, dtop, w, dh, WHITE, line=RGBColor(0xDD,0xDD,0xE5), radius=0.08)
        rrect(slide, x, dtop, 0.12, dh, col, radius=0.0)
        tb = slide.shapes.add_textbox(Inches(x + 0.28), Inches(dtop + 0.06), Inches(w - 0.45), Inches(dh - 0.12))
        tf = tb.text_frame; tf.word_wrap = True; tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = tf.paragraphs[0]; r = p.add_run(); r.text = head
        r.font.size = Pt(12.5); r.font.bold = True; r.font.color.rgb = col; r.font.name = FONT
        p.space_after = Pt(2)
        p2 = tf.add_paragraph(); r2 = p2.add_run(); r2.text = desc
        r2.font.size = Pt(10.5); r2.font.color.rgb = GREY; r2.font.name = FONT
    textbox(slide, 0.92, 3.25, 11.5, 0.35,
            [("Las 14 tácticas de ATT&CK Enterprise. Resaltadas, las 4 que recorremos hoy:", 12, True, INDIGO, PP_ALIGN.LEFT)])
    tactics = [
        ("Reconnaissance", BLUE), ("Resource Dev.", None), ("Initial Access", None), ("Execution", None),
        ("Persistence", None), ("Priv. Escalation", None), ("Defense Evasion", None),
        ("Credential Access", ORANGE), ("Discovery", TEAL), ("Lateral Movement", MAGENTA), ("Collection", None),
        ("Command & Control", None), ("Exfiltration", None), ("Impact", None),
    ]
    cols = 7; cw = 1.5; ch = 0.72; cgap = 0.15; vgap = 0.15
    total = cols*cw + (cols-1)*cgap
    x0 = (13.333 - total)/2; y0 = 3.7
    for i, (name, col) in enumerate(tactics):
        r_i, c_i = i // cols, i % cols
        x = x0 + c_i*(cw+cgap); y = y0 + r_i*(ch+vgap)
        if col is None:
            chip = rrect(slide, x, y, cw, ch, RGBColor(0xF0,0xF0,0xF3), line=RGBColor(0xDD,0xDD,0xE5), radius=0.1)
            _settext(chip.text_frame, [(name, 8.5, False, RGBColor(0x9A,0x9A,0xA3), PP_ALIGN.CENTER)])
        else:
            chip = rrect(slide, x, y, cw, ch, col, radius=0.1)
            _settext(chip.text_frame, [(name, 8.5, True, WHITE, PP_ALIGN.CENTER)])
    textbox(slide, 0.92, y0 + 2*(ch+vgap) + 0.08, 11.5, 0.5,
            [("Resaltadas: Reconnaissance (nmap), Discovery (Wireshark), Credential Access y Lateral Movement.   ·   Fuente: MITRE ATT&CK · IBM Think",
              10, False, GREY, PP_ALIGN.LEFT)])

def d_fugas(slide, prs):
    chips = [
        (BLUE,   "Hostname y modelo", "marca y tipo de equipo"),
        (ORANGE, "Nombres de salas", "organigrama y ubicaciones"),
        (TEAL,   "Versión de firmware", "vulnerabilidades conocidas"),
        (MAGENTA,"Agenda y directorio", "nombres y correos reales"),
    ]
    top = 1.85; ch_h = 0.9; ch_w = 4.3; gap = 0.18; lx = 0.92
    n = len(chips)
    centers = [top + i*(ch_h+gap) + ch_h/2 for i in range(n)]
    cy_mid = (centers[0] + centers[-1]) / 2
    col_h = n*ch_h + (n-1)*gap
    bx = lx + ch_w + 0.55
    ex = 6.95; ew = 12.42 - ex
    link(slide, bx, centers[0], bx, centers[-1], color=RGBColor(0xB8,0xBC,0xC6), width=2.5)
    arrow(slide, bx, cy_mid, ex - 0.05, cy_mid, color=INDIGO, width=2.5)
    for (col, t1, t2), cy in zip(chips, centers):
        link(slide, lx + ch_w, cy, bx, cy, color=col, width=2.0)
        oval(slide, bx - 0.07, cy - 0.07, 0.14, 0.14, col)
    for (col, t1, t2), cy in zip(chips, centers):
        c = rrect(slide, lx, cy - ch_h/2, ch_w, ch_h, WHITE, line=col, radius=0.12)
        _settext(c.text_frame, [(t1, 12.5, True, col, PP_ALIGN.CENTER), (t2, 10, False, GREY, PP_ALIGN.CENTER)])
    # panel del correo, misma altura que la columna de fugas
    rrect(slide, ex, top, ew, col_h, INDIGO, radius=0.08)
    textbox(slide, ex + 0.2, top + 0.15, ew - 0.4, 0.75, [
        ("Correo de phishing dirigido", 15, True, WHITE, PP_ALIGN.CENTER),
        ("creíble, porque usa datos reales", 11, False, LILAC, PP_ALIGN.CENTER),
    ], anchor=MSO_ANCHOR.TOP)
    # ejemplo del correo armado con las fugas
    card = rrect(slide, ex + 0.3, top + 1.05, ew - 0.6, col_h - 1.3, PALE, radius=0.08)
    tb = slide.shapes.add_textbox(Inches(ex + 0.42), Inches(top + 1.12), Inches(ew - 0.84), Inches(col_h - 1.45))
    tf = tb.text_frame; tf.word_wrap = True; tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    lines = [
        ("De: Soporte TI  <soporte@empresa-que-no-es.com>", 11, False, GREY),
        ("Para: Mariana López, Gerencia", 11, False, GREY),
        ("Asunto: Fallo en el gateway de la Sala de Juntas", 12.5, True, INDIGO),
        ("", 5, False, GREY),
        ("Hola Mariana, el equipo de la Sala de Juntas tiene la versión 2.6.1 con un fallo conocido. Ingresa con tu usuario para aplicar el parche antes de tu reunión de las 10.", 12, False, INDIGO),
    ]
    for i, (t, sz, bold, col) in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_after = Pt(4)
        r = p.add_run(); r.text = t; r.font.size = Pt(sz); r.font.bold = bold; r.font.color.rgb = col; r.font.name = FONT
    textbox(slide, 0.92, 6.3, 11.5, 0.45,
            [("Nada es grave por separado. Combinado, es el guion de un ataque dirigido.",
              13, True, INDIGO, PP_ALIGN.CENTER)], anchor=MSO_ANCHOR.MIDDLE)

def d_fases(slide, prs):
    phases = [
        (BLUE,   "Diseño", [
            "Segmentación en el plano, no después.",
            "Requisitos de seguridad en el pliego.",
            "Equipos que soporten TLS y cuentas gestionadas."]),
        (ORANGE, "Implementación", [
            "Cambiar las credenciales de fábrica.",
            "Apagar servicios sin uso y cifrar el control.",
            "Actualizar firmware antes de entregar."]),
        (TEAL,   "Entrega", [
            "Documentar puertos y servicios.",
            "Dejar logs activos hacia IT.",
            "Acordar quién mantiene el firmware."]),
    ]
    n = len(phases); gap = 0.3; ov = 0.45
    w = (11.5 + (n-1)*ov) / n          # ancho de cada chevron, solapados
    top = 1.85; h = 1.05
    ctop = top + h + 0.2; ch = 2.3
    cw = (11.5 - (n-1)*gap) / n       # tarjetas iguales, misma fila de 11.5 que las flechas
    for i, (col, name, items) in enumerate(phases):
        x = 0.92 + i * (w - ov)
        chevron(slide, x, top, w, h, col, name)
        cx = 0.92 + i * (cw + gap)
        rrect(slide, cx, ctop, cw, ch, WHITE, line=RGBColor(0xDD,0xDD,0xE5), radius=0.07)
        rrect(slide, cx, ctop, cw, 0.1, col, radius=0.0)
        tb = slide.shapes.add_textbox(Inches(cx + 0.2), Inches(ctop + 0.18), Inches(cw - 0.4), Inches(ch - 0.3))
        tf = tb.text_frame; tf.word_wrap = True; tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        for j, it in enumerate(items):
            p = tf.paragraphs[0] if j == 0 else tf.add_paragraph(); p.space_after = Pt(6)
            r = p.add_run(); r.text = "\u2022  " + it
            r.font.size = Pt(11.5); r.font.color.rgb = INDIGO; r.font.name = FONT
    textbox(slide, 0.92, ctop + ch + 0.2, 11.5, 0.85,
            [("La seguridad se diseña desde el día uno. No es un parche que se agrega al final.",
              14, True, INDIGO, PP_ALIGN.CENTER),
             ("ANSI/AVIXA D402.02 formaliza esta verificación por fase: pre-integración, integración, post-integración y cierre.",
              10.5, False, GREY, PP_ALIGN.CENTER)], anchor=MSO_ANCHOR.MIDDLE)

def d_segmentacion(slide, prs):
    bw = 5.2; gap = 1.1; xs = [0.92, 0.92 + bw + gap]
    def row(y, h, items):
        for (col, t1, t2), x in zip(items, xs):
            bx = rrect(slide, x, y, bw, h, WHITE, line=col, radius=0.08)
            _settext(bx.text_frame, [(t1, 14, True, col, PP_ALIGN.CENTER), (t2, 10.5, False, GREY, PP_ALIGN.CENTER)])
    row(1.85, 1.05, [(BLUE, "VLAN AV", "dispositivos AV aislados"),
                     (TEAL, "VLAN de control", "plano de gestión separado")])
    fw = rrect(slide, 0.92, 3.1, bw*2 + gap, 0.6, ORANGE, radius=0.3)
    _settext(fw.text_frame, [("Firewall con reglas explícitas: solo lo necesario pasa   ·   AVIXA RP-C303.01 §7.5", 12, True, WHITE, PP_ALIGN.CENTER)])
    # reglas en semaforo
    rules = [
        (GREEN,  "De control a AV", "gestión cifrada (SSH, HTTPS)"),
        (ORANGE, "De corporativa a AV", "solo lo acordado: calendario, directorio"),
        (RED,    "De invitados a AV", "bloqueado"),
    ]
    rw = (bw*2 + gap - 2*0.25) / 3; ry = 3.9; rh = 0.75
    for i, (col, t1, t2) in enumerate(rules):
        x = 0.92 + i * (rw + 0.25)
        c = rrect(slide, x, ry, rw, rh, WHITE, line=col, radius=0.1)
        rrect(slide, x + 0.08, ry + 0.12, 0.09, rh - 0.24, col, radius=0.5)
        _settext(c.text_frame, [(t1, 11.5, True, col, PP_ALIGN.CENTER), (t2, 9.5, False, GREY, PP_ALIGN.CENTER)])
    textbox(slide, 0.92, 4.72, bw*2 + gap, 0.32,
            [("Visibilidad: IT suele poner un sensor que escucha el tráfico de la VLAN AV sin tocar los equipos (en su jerga, un NIDS).",
              9.5, False, INDIGO, PP_ALIGN.CENTER)], anchor=MSO_ANCHOR.MIDDLE)
    row(5.12, 1.0, [(INDIGO, "Red corporativa", "datos de la empresa"),
                    (GREY,   "Red de invitados", "el visitante, nunca el AV")])
    textbox(slide, 0.92, 6.25, 11.5, 0.4,
            [("Todo lo demás, bloqueado. Es la propuesta que IT quiere escuchar.", 12.5, True, INDIGO, PP_ALIGN.CENTER)],
            anchor=MSO_ANCHOR.MIDDLE)

REGISTRY = {
    "pecados": d_pecados, "criterios": d_criterios, "hardening": d_hardening,
    "cia": d_cia, "nist": d_nist, "killchain": d_killchain, "mitre": d_mitre,
    "fugas": d_fugas, "fases": d_fases, "segmentación": d_segmentacion,
}

# ---------- lámina OSI / TCP-IP ----------
def d_osi(slide, prs):
    # 7 capas OSI agrupadas en 4 de TCP/IP, con ejemplos AV/seguridad
    osi = [
        (BLUE,   "7  Aplicación",  "mDNS, HTTP de admin, APIs, NDI, control de Dante y AES67. Aquí vive lo que exponemos."),
        (BLUE,   "6  Presentación","Formatos y cifrado de datos (TLS, SRTP)."),
        (BLUE,   "5  Sesión",      "Señalización de sesión. Ej.: SIP, RTSP. SIP lo verá Eduardo."),
        (ORANGE, "4  Transporte",  "TCP / UDP y puertos. RTP lleva el audio y el video. Lo que nmap enumera."),
        (MAGENTA,"3  Red",         "IP, enrutamiento y multicast (IGMP). Se segmenta con subredes."),
        (TEAL,   "2  Enlace",      "MAC, VLAN, AVB/TSN y PTP para la sincronía. Aquí IT separa el AV."),
        (TEAL,   "1  Física",      "El cable (Cat6, fibra, HDBaseT) y el puerto del rack."),
    ]
    tcpip = [  # (label, color, fila_ini, fila_fin)
        ("Aplicación",   BLUE,    0, 2),
        ("Transporte",   ORANGE,  3, 3),
        ("Internet",     MAGENTA, 4, 4),
        ("Acceso a red", TEAL,    5, 6),
    ]
    top = 1.75; rh = 0.56; gap = 0.06
    def row_y(i): return top + i*(rh+gap)
    # columna TCP/IP (izquierda)
    textbox(slide, 0.92, top-0.42, 2.3, 0.35, [("TCP / IP", 12, True, GREY, PP_ALIGN.CENTER)])
    for label, col, a, b in tcpip:
        y = row_y(a); h = (row_y(b)+rh) - y
        bar = rrect(slide, 0.92, y, 2.1, h, col, radius=0.06)
        _settext(bar.text_frame, [(label, 12, True, WHITE, PP_ALIGN.CENTER)])
    # columna OSI (derecha)
    textbox(slide, 3.3, top-0.42, 9.0, 0.35, [("OSI", 12, True, GREY, PP_ALIGN.LEFT)])
    for i, (col, name, ex) in enumerate(osi):
        y = row_y(i)
        chip = rrect(slide, 3.3, y, 2.6, rh, WHITE, line=col, radius=0.08)
        _settext(chip.text_frame, [(name, 11.5, True, col, PP_ALIGN.CENTER)])
        textbox(slide, 6.05, y, 6.3, rh, [(ex, 11, False, GREY, PP_ALIGN.LEFT)], anchor=MSO_ANCHOR.MIDDLE)
    textbox(slide, 0.92, row_y(7)+0.05, 11.5, 0.75,
            [("mDNS y paneles viven en la 7; IT segmenta en 2 y 3; el cifrado cubre 4 a 6.",
              12.5, True, INDIGO, PP_ALIGN.CENTER),
             ("nmap enumera la capa 4 y Wireshark lee de la 2 a la 7. Las dos, en las demos.",
              11.5, False, GREY, PP_ALIGN.CENTER)], anchor=MSO_ANCHOR.MIDDLE)

# ---------- lámina de referencias (enlaces clicables) ----------
def _ref_item(slide, x, y, w, color, name, desc, url, full, h=1.02, s_name=13, s_desc=10.5):
    rrect(slide, x, y, w, h, WHITE, line=RGBColor(0xDD,0xDD,0xE5), radius=0.08)
    rrect(slide, x, y, 0.12, h, color, radius=0.0)
    tb = slide.shapes.add_textbox(Inches(x+0.2), Inches(y+0.05), Inches(w-0.28), Inches(h-0.1))
    tf = tb.text_frame; tf.word_wrap = True; tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]; r = p.add_run(); r.text = name
    r.font.size = Pt(s_name); r.font.bold = True; r.font.color.rgb = INDIGO; r.font.name = FONT
    p2 = tf.add_paragraph(); r2 = p2.add_run(); r2.text = desc
    r2.font.size = Pt(s_desc); r2.font.color.rgb = GREY; r2.font.name = FONT
    p3 = tf.add_paragraph(); r3 = p3.add_run(); r3.text = url
    r3.font.size = Pt(s_desc); r3.font.bold = True; r3.font.color.rgb = BLUE; r3.font.name = FONT
    r3.hyperlink.address = full

def d_referencias(slide, prs):
    cx = [0.92, 4.72, 8.52]; cw = [3.55, 3.55, 3.9]
    for x, w, t in zip(cx, cw, ("Estándares AVIXA", "Marcos", "Herramientas y lecturas")):
        textbox(slide, x, 1.6, w, 0.4, [(t, 13.5, True, INDIGO, PP_ALIGN.LEFT)])
    avixa = [
        (INDIGO, "AVIXA RP-C303.01", "Prácticas recomendadas de seguridad en sistemas AV en red. La línea base de este taller.", "avixa.org/standards", "https://www.avixa.org/standards"),
        (BLUE,   "ANSI/AVIXA D402.02", "Verificación de desempeño de sistemas AV, por fases del proyecto.", "avixa.org/standards", "https://www.avixa.org/standards"),
    ]
    marcos = [
        (BLUE,   "NIST CSF 2.0", "Marco de gestión de riesgo que usa IT.", "nist.gov/cyberframework", "https://www.nist.gov/cyberframework"),
        (MAGENTA,"MITRE ATT&CK", "Catálogo de tácticas y técnicas reales.", "attack.mitre.org", "https://attack.mitre.org"),
        (ORANGE, "Cyber Kill Chain", "Las fases de un ataque (Lockheed Martin).", "lockheedmartin.com/…/cyber-kill-chain", "https://lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html"),
        (TEAL,   "CIS Controls v8.1", "18 controles priorizados para implementar.", "cisecurity.org/controls", "https://www.cisecurity.org/controls/cis-controls-list"),
    ]
    herr = [
        (BLUE,   "Nmap", "Escaneo de red y de servicios.", "nmap.org", "https://nmap.org"),
        (TEAL,   "Wireshark", "Análisis de tráfico (mDNS y más).", "wireshark.org", "https://www.wireshark.org"),
        (INDIGO, "MITRE ATT&CK explicado", "Qué es una táctica y una técnica (con video).", "ibm.com/think/mitre-attack", "https://www.ibm.com/mx-es/think/topics/mitre-attack"),
    ]
    y = 2.1
    for col, n, de, u, f in avixa:
        _ref_item(slide, cx[0], y, cw[0], col, n, de, u, f, h=1.6, s_name=12, s_desc=9.5); y += 1.75
    y = 2.1
    for col, n, de, u, f in marcos:
        _ref_item(slide, cx[1], y, cw[1], col, n, de, u, f, h=1.0, s_name=11.5, s_desc=9); y += 1.1
    y = 2.1
    for col, n, de, u, f in herr:
        _ref_item(slide, cx[2], y, cw[2], col, n, de, u, f, h=1.0, s_name=11.5, s_desc=9); y += 1.1
    note = rrect(slide, cx[2], y + 0.05, cw[2], 0.9, PALE, radius=0.08)
    _settext(note.text_frame, [
        ("En el kit descargable:", 11, True, INDIGO, PP_ALIGN.LEFT),
        ("Checklist de hardening, guía del laboratorio y guion de preguntas de IT.", 9.5, False, GREY, PP_ALIGN.LEFT),
    ], anchor=MSO_ANCHOR.MIDDLE)

REGISTRY["osi"] = d_osi
REGISTRY["referencias"] = d_referencias

# ---------- lámina "manos a la obra": laboratorio + reglas ----------
def d_lab(slide, prs):
    # --- diagrama de la red del laboratorio (izquierda) ---
    rrect(slide, 0.92, 1.95, 5.3, 3.6, PALE, radius=0.06)
    textbox(slide, 1.1, 2.05, 5.0, 0.4, [("Red aislada  -  sin conexión con el WTC", 11.5, True, INDIGO, PP_ALIGN.LEFT)])
    rx, ry, rw, rh = 3.35, 2.95, 2.6, 0.82
    ax, ay = 3.35, 4.5
    # enlaces primero (van por detrás de las cajas)
    link(slide, rx + rw/2, ry + rh, rx + rw/2, ay, color=TEAL, width=2.0)          # router -> gateway de presentación (cable)
    ph_y = [2.7, 3.8]
    for yy in ph_y:
        link(slide, 1.05 + 1.2, yy + 0.35, rx, ry + rh/2, color=MAGENTA, width=1.6, dash=True)  # telefono -> router (WiFi)
    # cajas
    router = rrect(slide, rx, ry, rw, rh, BLUE, radius=0.1)
    _settext(router.text_frame, [("Router WiFi del laboratorio", 11.5, True, WHITE, PP_ALIGN.CENTER),
                                 ("ICAL26-LAB  /  seguridadav26", 9, False, RGBColor(0xE3,0xEE,0xFA), PP_ALIGN.CENTER)])
    am = rrect(slide, ax, ay, rw, 0.82, TEAL, radius=0.1)
    _settext(am.text_frame, [("Gateway de presentación inalámbrica", 11.5, True, WHITE, PP_ALIGN.CENTER),
                             ("dispositivo AV real", 9, False, RGBColor(0xDD,0xF2,0xF2), PP_ALIGN.CENTER)])
    for yy in ph_y:
        ph = rrect(slide, 1.05, yy, 1.2, 0.7, WHITE, line=MAGENTA, radius=0.15)
        _settext(ph.text_frame, [("tu teléfono", 9.5, True, MAGENTA, PP_ALIGN.CENTER)])
    textbox(slide, 2.25, 3.08, 1.15, 0.35, [("Wi-Fi", 9, True, MAGENTA, PP_ALIGN.CENTER)], anchor=MSO_ANCHOR.MIDDLE)
    # --- pasos para participar (derecha) ---
    textbox(slide, 6.6, 1.95, 5.7, 0.4, [("Para participar", 15, True, INDIGO, PP_ALIGN.LEFT)])
    steps = [
        ("1", "Conéctate a la red ICAL26-LAB (clave: seguridadav26)."),
        ("2", "Opcional, para ir más a fondo: instala un escáner de red. En el teléfono, Fing o Network Scanner; en laptop, nmap."),
        ("3", "Escanea y mira lo que aparece. Seguimos la demo juntos."),
    ]
    yy = 2.5
    for num, txt in steps:
        o = oval(slide, 6.6, yy, 0.5, 0.5, BLUE)
        _settext(o.text_frame, [(num, 15, True, WHITE, PP_ALIGN.CENTER)])
        textbox(slide, 7.25, yy-0.04, 5.0, 0.8, [(txt, 11.5, False, INDIGO, PP_ALIGN.LEFT)], anchor=MSO_ANCHOR.MIDDLE)
        yy += 0.95
    # regla de oro
    warn = rrect(slide, 6.6, 5.45, 5.7, 0.95, RED, radius=0.1)
    _settext(warn.text_frame, [
        ("Regla de oro", 12.5, True, WHITE, PP_ALIGN.CENTER),
        ("Escanea SOLO la red del laboratorio. Nunca la red del recinto (WTC): eso es intrusión.",
         10.5, False, WHITE, PP_ALIGN.CENTER),
    ])

REGISTRY["lab"] = d_lab

# ---------- lamina de agenda: dos tarjetas + franja de participacion ----------
def d_agenda(slide, prs):
    cards = [
        (BLUE, "Parte 1", "45 minutos", "Juan Pineda  ·  Pyxis",
         ["Por qué IT frena un proyecto AV: el marco de seguridad y el ciclo de vida de un ataque.",
          "Mini demos en vivo sobre una red aislada que montamos en la sala."]),
        (MAGENTA, "Parte 2", "Prueba de concepto", "Eduardo Travi  ·  AVI SPL",
         ["Un caso real con SIP: cómo fugas pequeñas se combinan y terminan en un phishing dirigido.",
          "De la teoría a la práctica, demostrado en vivo."]),
    ]
    w = 5.55; h = 2.35; gap = 0.4; top = 2.25
    xs = [0.92, 0.92 + w + gap]
    for (col, part, sub, who, bullets), x in zip(cards, xs):
        rrect(slide, x, top, w, h, WHITE, line=RGBColor(0xDD,0xDD,0xE5), radius=0.06)
        head = rrect(slide, x, top, w, 0.68, col, radius=0.06)
        _settext(head.text_frame, [(part + "   ·   " + sub, 14, True, WHITE, PP_ALIGN.CENTER)])
        body = slide.shapes.add_textbox(Inches(x + 0.32), Inches(top + 0.68), Inches(w - 0.62), Inches(h - 0.68))
        tf = body.text_frame; tf.word_wrap = True; tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = tf.paragraphs[0]; r = p.add_run(); r.text = who
        r.font.size = Pt(13); r.font.bold = True; r.font.color.rgb = col; r.font.name = FONT
        p.space_after = Pt(8)
        for bt in bullets:
            pp = tf.add_paragraph(); pp.space_after = Pt(6)
            rr = pp.add_run(); rr.text = "•  " + bt
            rr.font.size = Pt(12); rr.font.color.rgb = INDIGO; rr.font.name = FONT
    strip = rrect(slide, 0.92, top + h + 0.3, w * 2 + gap, 1.15, PALE, radius=0.08)
    _settext(strip.text_frame, [
        ("No necesitas laptop: participas desde tu teléfono, sobre nuestra propia red WiFi.",
         13, True, INDIGO, PP_ALIGN.CENTER),
        ("Puedes seguir sin instalar nada; el escáner de red es opcional. El kit se descarga después.",
         11.5, False, GREY, PP_ALIGN.CENTER),
    ])

REGISTRY["agenda"] = d_agenda

# ---------- lamina "dos miradas": lo que ves tu vs lo que ve IT ----------
def d_dosmiradas(slide, prs):
    w = 5.55; h = 3.15; gap = 0.4; top = 1.85
    x1 = 0.92; x2 = 0.92 + w + gap
    # Panel izquierdo: lo que ves tu
    rrect(slide, x1, top, w, h, WHITE, line=RGBColor(0xDD,0xDD,0xE5), radius=0.06)
    hd1 = rrect(slide, x1, top, w, 0.72, TEAL, radius=0.06)
    _settext(hd1.text_frame, [("Lo que ves tú", 15, True, WHITE, PP_ALIGN.CENTER)])
    b1 = slide.shapes.add_textbox(Inches(x1 + 0.35), Inches(top + 0.9), Inches(w - 0.7), Inches(h - 1.1))
    tf = b1.text_frame; tf.word_wrap = True; tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    for i, t in enumerate(["Un códec.", "Un DSP.", "Un controlador."]):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph(); p.space_after = Pt(4)
        r = p.add_run(); r.text = t; r.font.size = Pt(15); r.font.bold = True
        r.font.color.rgb = TEAL; r.font.name = FONT
    p = tf.add_paragraph(); p.space_before = Pt(8)
    r = p.add_run(); r.text = "Un equipo AV que hace su trabajo."
    r.font.size = Pt(11.5); r.font.color.rgb = GREY; r.font.name = FONT
    # Panel derecho: lo que ve IT
    rrect(slide, x2, top, w, h, WHITE, line=RGBColor(0xDD,0xDD,0xE5), radius=0.06)
    hd2 = rrect(slide, x2, top, w, 0.72, INDIGO, radius=0.06)
    _settext(hd2.text_frame, [("Lo que ve IT", 15, True, WHITE, PP_ALIGN.CENTER)])
    b2 = slide.shapes.add_textbox(Inches(x2 + 0.35), Inches(top + 0.9), Inches(w - 0.7), Inches(h - 1.1))
    tf = b2.text_frame; tf.word_wrap = True; tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    items = ["Un sistema operativo.", "Servicios de red y puertos abiertos.",
             "A veces, salida a internet.", "Un host que ellos no administran."]
    for i, t in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph(); p.space_after = Pt(6)
        r = p.add_run(); r.text = "•  " + t; r.font.size = Pt(12.5)
        r.font.color.rgb = INDIGO; r.font.name = FONT
    # Banner de cierre
    banner = rrect(slide, 0.92, top + h + 0.28, w * 2 + gap, 0.9, INDIGO, radius=0.1)
    _settext(banner.text_frame, [
        ("Por eso no desconfían de ti. Desconfían de un host desconocido en su red.",
         15, True, WHITE, PP_ALIGN.CENTER)])

REGISTRY["dosmiradas"] = d_dosmiradas

# ---------- lamina de preguntas de IT: dialogo pregunta / respuesta ----------
def d_preguntas(slide, prs):
    qa = [
        (BLUE,    "¿Qué puertos abre este equipo?",          "Lista documentada de puertos y servicios."),
        (ORANGE,  "¿En qué red va a estar?",                  "En la VLAN AV, segmentada, con reglas explícitas."),
        (TEAL,    "¿Cómo se gestionan las credenciales?",     "Cuentas administradas; nada de fábrica."),
        (MAGENTA, "¿Cómo actualizamos y monitoreamos?",       "Plan de firmware y logs hacia su sistema de monitoreo (en su jerga, SIEM)."),
    ]
    qw = 4.6; aw = 11.5 - qw - 0.35; top = 1.8; h = 0.82; gap = 0.15
    for i, (col, q, a) in enumerate(qa):
        y = top + i * (h + gap)
        qb = rrect(slide, 0.92, y, qw, h, col, radius=0.1)
        _settext(qb.text_frame, [(q, 12.5, True, WHITE, PP_ALIGN.LEFT)])
        arrow(slide, 0.92 + qw + 0.03, y + h/2, 0.92 + qw + 0.32, y + h/2, color=col, width=2.0)
        ab = rrect(slide, 0.92 + qw + 0.35, y, aw, h, WHITE, line=col, radius=0.1)
        _settext(ab.text_frame, [(a, 12, False, INDIGO, PP_ALIGN.LEFT)])
    textbox(slide, 0.92, top + 4*(h+gap) + 0.08, 11.5, 0.8,
            [("Tener esto listo convierte la revisión de IT en un trámite, no en un freno.", 13.5, True, INDIGO, PP_ALIGN.CENTER),
             ("Es la documentación que pide AVIXA RP-C303.01 §9.2: puertos y servicios, topología con VLAN y ACL, roles y permisos.",
              10.5, False, GREY, PP_ALIGN.CENTER)], anchor=MSO_ANCHOR.MIDDLE)

REGISTRY["preguntas"] = d_preguntas

# ---------- lamina: cuando el cliente no tiene politicas formales ----------
def d_cliente(slide, prs):
    intro = rrect(slide, 0.92, 1.75, 11.5, 0.8, PALE, radius=0.08)
    _settext(intro.text_frame, [
        ("Muchos clientes no tienen un área de seguridad madura. Ahí el integrador marca la diferencia.",
         13, True, INDIGO, PP_ALIGN.CENTER)])
    cards = [
        (BLUE,   "Lleva tú el mínimo", ["Segmentación, credenciales, cifrado y logs.", "Como estándar, no como extra."]),
        (TEAL,   "Documéntalo", ["Hazlo parte de la entrega.", "Protege al cliente y te protege a ti."]),
        (ORANGE, "Conviértelo en diferencial", ["No es un costo: es tu ventaja comercial.", "Es lo que te distingue frente a otro integrador."]),
    ]
    n = len(cards); gap = 0.3; w = (11.5 - (n-1)*gap) / n; top = 2.8; h = 2.25
    for i, (col, head, items) in enumerate(cards):
        x = 0.92 + i * (w + gap)
        rrect(slide, x, top, w, h, WHITE, line=RGBColor(0xDD,0xDD,0xE5), radius=0.08)
        hd = rrect(slide, x, top, w, 0.65, col, radius=0.08)
        _settext(hd.text_frame, [(head, 13, True, WHITE, PP_ALIGN.CENTER)])
        tb = slide.shapes.add_textbox(Inches(x + 0.25), Inches(top + 0.65), Inches(w - 0.5), Inches(h - 0.65))
        tf = tb.text_frame; tf.word_wrap = True; tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        for j, it in enumerate(items):
            p = tf.paragraphs[0] if j == 0 else tf.add_paragraph(); p.space_after = Pt(6); p.alignment = PP_ALIGN.CENTER
            r = p.add_run(); r.text = it; r.font.size = Pt(12); r.font.color.rgb = INDIGO; r.font.name = FONT
    banner = rrect(slide, 0.92, 5.35, 11.5, 0.8, INDIGO, radius=0.1)
    _settext(banner.text_frame, [
        ("Eres el integrador que entrega seguro por defecto.", 15, True, WHITE, PP_ALIGN.CENTER)])

REGISTRY["cliente"] = d_cliente

# ---------- lamina de cierre: el kit ----------
def d_kit(slide, prs, qr_caption):
    items = [
        (BLUE,   "Checklist de hardening", "Para auditar tus proyectos antes de que IT los revise."),
        (TEAL,   "Guía para montar tu laboratorio", "Red aislada y USB de arranque para practicar en casa."),
        (ORANGE, "Guion de preguntas de IT", "Con las respuestas que te dejan pasar la revisión."),
    ]
    lw = 6.0; top = 1.75; h = 0.95; gap = 0.2
    for i, (col, head, desc) in enumerate(items):
        y = top + i * (h + gap)
        rrect(slide, 0.92, y, lw, h, WHITE, line=RGBColor(0xDD,0xDD,0xE5), radius=0.1)
        o = oval(slide, 1.08, y + (h - 0.52)/2, 0.52, 0.52, col)
        _settext(o.text_frame, [(str(i+1), 15, True, WHITE, PP_ALIGN.CENTER)])
        textbox(slide, 1.78, y + 0.06, lw - 1.0, h - 0.12, [
            (head, 13, True, col, PP_ALIGN.LEFT),
            (desc, 10.5, False, GREY, PP_ALIGN.LEFT),
        ], anchor=MSO_ANCHOR.MIDDLE)
    items_bottom = top + (len(items)-1)*(h+gap) + h
    qy = top; qs = items_bottom - top
    item_right = 0.92 + lw
    qx = item_right + (12.42 - item_right - qs)/2
    import os as _os
    rrect(slide, qx, qy, qs, qs, WHITE, line=RGBColor(0xDD,0xDD,0xE5), radius=0.1)
    if _os.path.exists("assets/qr.png"):
        m = 0.45
        slide.shapes.add_picture("assets/qr.png", Inches(qx + m), Inches(qy + m - 0.12), width=Inches(qs - 2*m))
        textbox(slide, qx, qy + qs - 0.52, qs, 0.4, [("Escanea para descargar el kit", 11.5, True, INDIGO, PP_ALIGN.CENTER)], anchor=MSO_ANCHOR.MIDDLE)
    else:
        textbox(slide, qx, qy, qs, qs, [(qr_caption, 14, True, INDIGO, PP_ALIGN.CENTER)], anchor=MSO_ANCHOR.MIDDLE)
    # contacto de los presentadores
    people = [
        ("Juan Pineda", "Pyxis", "juan.pineda@pyxis.tech", "https://www.linkedin.com/in/jdpinedac/", "linkedin.com/in/jdpinedac"),
        ("Eduardo Travi", "AVI SPL", "Eduardo.Travi@avispl.com", "https://www.linkedin.com/in/eduardotravi/", "linkedin.com/in/eduardotravi"),
    ]
    cw = 5.4; cy = 5.35
    for i, (name, org, mail, li_url, li_txt) in enumerate(people):
        x = 0.92 + i * (cw + 0.7)
        textbox(slide, x, cy, cw, 0.3, [("%s  \u00b7  %s" % (name, org), 12.5, True, INDIGO, PP_ALIGN.LEFT)])
        textbox(slide, x, cy + 0.33, cw, 0.3, [("\u2709  " + mail, 10.5, False, GREY, PP_ALIGN.LEFT)])
        slide.shapes.add_picture("assets/logos/linkedin.png", Inches(x + 0.02), Inches(cy + 0.65), height=Inches(0.28))
        tbl = textbox(slide, x + 0.42, cy + 0.64, cw - 0.42, 0.3, [(li_txt, 10.5, False, BLUE, PP_ALIGN.LEFT)])
        tbl.text_frame.paragraphs[0].runs[0].hyperlink.address = li_url

REGISTRY["kit"] = d_kit

# ---------- lamina de descargo: uso responsable ----------
def d_descargo(slide, prs):
    DARKRED = RGBColor(0xB3, 0x1B, 0x1B)
    # banner de alerta legal (protagonista)
    ban = rrect(slide, 0.92, 1.7, 11.5, 1.75, DARKRED, radius=0.12)
    badge_o = oval(slide, 1.2, 1.7 + (1.75 - 0.9)/2, 0.9, 0.9, WHITE)
    _settext(badge_o.text_frame, [("!", 34, True, DARKRED, PP_ALIGN.CENTER)])
    textbox(slide, 2.35, 1.78, 9.9, 1.6, [
        ("Escanear o probar sistemas sin autorización escrita del dueño es un delito.", 16, True, WHITE, PP_ALIGN.LEFT),
        ("Ni en el recinto, ni en tu empresa, ni en la de un cliente. Hoy, solo sobre la red aislada del laboratorio.", 12, False, RGBColor(0xFF,0xE1,0xE1), PP_ALIGN.LEFT),
        ("Colombia: Ley 1273 de 2009, art. 269A   ·   Argentina: Ley 26.388, art. 153 bis   ·   México: Código Penal Federal, arts. 211 bis 1 a 7", 10, True, RGBColor(0xFF,0xD5,0xD5), PP_ALIGN.LEFT),
    ], anchor=MSO_ANCHOR.MIDDLE)
    # tarjetas de apoyo
    items = [
        (BLUE,   "Fines educativos", "Todo lo que ves hoy es para aprender a diseñar y defender instalaciones AV."),
        (TEAL,   "Capturas de ejemplo", "Las imágenes de las demos son ilustrativas; no corresponden a ningún cliente ni sistema real."),
        (ORANGE, "Opiniones propias", "Criterio de los presentadores; no representa a fabricantes ni a los organizadores. Las marcas se omiten a propósito."),
        (GREEN,  "El kit", "Es para practicar en tu propio entorno de laboratorio."),
    ]
    cols = 2; gap = 0.3; w = (11.5 - gap) / cols; h = 1.05; vgap = 0.18; top = 3.7
    for i, (col, head, desc) in enumerate(items):
        x = 0.92 + (i % cols) * (w + gap); y = top + (i // cols) * (h + vgap)
        rrect(slide, x, y, w, h, WHITE, line=RGBColor(0xDD,0xDD,0xE5), radius=0.08)
        rrect(slide, x + 0.08, y + 0.14, 0.09, h - 0.28, col, radius=0.5)
        textbox(slide, x + 0.3, y + 0.05, w - 0.45, h - 0.1, [
            (head, 12, True, col, PP_ALIGN.LEFT),
            (desc, 9.5, False, GREY, PP_ALIGN.LEFT),
        ], anchor=MSO_ANCHOR.MIDDLE)
    textbox(slide, 0.92, 6.2, 11.5, 0.35,
            [("Esto no es asesoría legal: consulta la legislación vigente de tu país.", 9.5, False, GREY, PP_ALIGN.CENTER)],
            anchor=MSO_ANCHOR.MIDDLE)

REGISTRY["descargo"] = d_descargo

# ---------- lamina: la hexada de Parker ----------
def d_parker(slide, prs):
    intro = rrect(slide, 0.92, 1.75, 11.5, 0.7, PALE, radius=0.08)
    _settext(intro.text_frame, [
        ("Donn Parker amplió la tríada con tres elementos más. Dos de ellos pesan mucho en AV.", 12.5, True, INDIGO, PP_ALIGN.CENTER)])
    MUTED = RGBColor(0xA7, 0xAB, 0xB5)
    cards = [
        (MUTED,  "C", "Confidencialidad",   "Ya vista: que no lo vea quien no debe.",                     False),
        (MUTED,  "I", "Integridad",         "Ya vista: que nadie lo altere.",                             False),
        (MUTED,  "D", "Disponibilidad",     "Ya vista: que esté cuando se necesita.",                     False),
        (MAGENTA,"P", "Posesión o control", "Que el equipo siga bajo tu control. Ej.: quien tiene el rack, tiene el equipo.", True),
        (BLUE,   "A", "Autenticidad",       "Que lo que llega sea de quien dice ser. Ej.: ¿este firmware es del fabricante?", True),
        (ORANGE, "U", "Utilidad",           "Que la información sirva. Ej.: una grabación cifrada cuya clave se perdió.",   True),
    ]
    key_av = {"Posesión o control", "Autenticidad"}
    cols = 3; gap = 0.3; w = (11.5 - (cols-1)*gap) / cols; h = 1.45; vgap = 0.22; top = 2.65
    for i, (col, letter, name, desc, hot) in enumerate(cards):
        x = 0.92 + (i % cols) * (w + gap); y = top + (i // cols) * (h + vgap)
        rrect(slide, x, y, w, h, WHITE if hot else RGBColor(0xF7,0xF7,0xF9), line=col if hot else RGBColor(0xE3,0xE3,0xE8), radius=0.1)
        tagged = name in key_av
        if tagged:
            tag = rrect(slide, x + w - 1.35, y + 0.1, 1.2, 0.28, col, radius=0.5)
            _settext(tag.text_frame, [("CLAVE EN AV", 8, True, WHITE, PP_ALIGN.CENTER)])
        o = oval(slide, x + 0.2, y + (h - 0.6)/2, 0.6, 0.6, col)
        _settext(o.text_frame, [(letter, 16, True, WHITE, PP_ALIGN.CENTER)])
        ty = y + (0.38 if tagged else 0.06); th_ = h - (0.44 if tagged else 0.12)
        textbox(slide, x + 0.95, ty, w - 1.1, th_, [
            (name, 12.5, True, col if hot else RGBColor(0x7A,0x7E,0x88), PP_ALIGN.LEFT),
            (desc, 10, False, INDIGO if hot else MUTED, PP_ALIGN.LEFT),
        ], anchor=MSO_ANCHOR.MIDDLE)
    textbox(slide, 0.92, 6.05, 11.5, 0.45,
            [("Cada marco mira el mismo problema con más detalle. El siguiente lo organiza como lo hace IT.", 12, True, INDIGO, PP_ALIGN.CENTER)],
            anchor=MSO_ANCHOR.MIDDLE)

REGISTRY["parker"] = d_parker
