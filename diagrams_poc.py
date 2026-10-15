# -*- coding: utf-8 -*-
# Parte 2 del deck (Eduardo Travi, AVI SPL): la prueba de concepto con SIP.
# Objetivo: reproducir sus láminas lo más fiel posible (mismos títulos, textos y
# colores que él ya tomó de la parte 1), solo renderizadas con nuestros helpers y
# tipografía. Todo el contenido llega como datos desde content_p2.py.
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
import diagrams as D
from diagrams import (rrect, oval, textbox, _settext, card, chevron, arrow, link,
                      INDIGO, BLUE, ORANGE, MAGENTA, TEAL, GREEN, RED, WHITE, GREY, LILAC, PALE)

LINE = RGBColor(0xDD, 0xDD, 0xE5)
GREYBAN = RGBColor(0xEC, 0xEF, 0xF7)   # banda gris/lavanda del subtítulo (como Eduardo)
LEFT = 0.92
FULL = 11.5
RIGHT = LEFT + FULL
SW = 13.333
BODY_TOP = 2.5


def _color(name):
    return {"blue": BLUE, "orange": ORANGE, "magenta": MAGENTA, "teal": TEAL,
            "green": GREEN, "red": RED, "indigo": INDIGO, "grey": GREY}.get(name, BLUE)


def _bullets(slide, x, y, w, h, items, size=11.5, color=INDIGO, anchor=MSO_ANCHOR.TOP, space=6, bullet=True):
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame; tf.word_wrap = True; tf.vertical_anchor = anchor
    pre = "•  " if bullet else ""
    for j, it in enumerate(items):
        p = tf.paragraphs[0] if j == 0 else tf.add_paragraph(); p.space_after = Pt(space)
        r = p.add_run(); r.text = pre + it
        r.font.size = Pt(size); r.font.color.rgb = color; r.font.name = D.FONT
    return tb


def _topbanner(slide, text):
    if not text:
        return
    b = rrect(slide, LEFT, 1.78, FULL, 0.5, GREYBAN, radius=0.14)
    _settext(b.text_frame, [(text, 13, True, INDIGO, PP_ALIGN.CENTER)])


def _botbanner(slide, y, text, h=0.78, size=14, sub=None):
    b = rrect(slide, LEFT, y, FULL, h, INDIGO, radius=0.1)
    items = [(text, size, True, WHITE, PP_ALIGN.CENTER)]
    if sub:
        items.append((sub, 10.5, False, LILAC, PP_ALIGN.CENTER))
    _settext(b.text_frame, items)


# ---------- tarjeta con cabecera de color completa (+ subtítulo opcional) ----------
def _hcard(slide, x, y, w, h, col, head, items, sub=None, size=11.5):
    rrect(slide, x, y, w, h, WHITE, line=LINE, radius=0.06)
    hd = rrect(slide, x, y, w, 0.62, col, radius=0.06)
    _settext(hd.text_frame, [(head, 13, True, WHITE, PP_ALIGN.CENTER)])
    y0 = y + 0.62 + 0.14
    if sub:
        textbox(slide, x + 0.28, y0, w - 0.56, 0.36, [(sub, 12.5, True, col, PP_ALIGN.LEFT)])
        y0 += 0.4
    _bullets(slide, x + 0.28, y0, w - 0.56, y + h - y0 - 0.12, items, size=size)


# ---------- tarjeta con franja de color superior y título índigo dentro ----------
def _tcard(slide, x, y, w, h, col, head, items, size=11.5, bullet=True):
    rrect(slide, x, y, w, h, WHITE, line=LINE, radius=0.06)
    rrect(slide, x, y, w, 0.11, col, radius=0.0)
    textbox(slide, x + 0.28, y + 0.22, w - 0.56, 0.4, [(head, 13, True, INDIGO, PP_ALIGN.LEFT)])
    _bullets(slide, x + 0.28, y + 0.72, w - 0.56, h - 0.85, items, size=size, bullet=bullet)


# ---------- columna de hosts, devuelve los centros verticales ----------
def _host_col(slide, hosts, x, w, top, hh=0.82, gap=0.16):
    centers = []
    for i, hst in enumerate(hosts):
        yy = top + i * (hh + gap)
        col = _color(hst["col"])
        c = rrect(slide, x, yy, w, hh, WHITE, line=col, radius=0.1)
        _settext(c.text_frame, [
            (hst["name"], 12, True, col, PP_ALIGN.LEFT),
            (hst["role"], 9.5, False, GREY, PP_ALIGN.LEFT),
        ], anchor=MSO_ANCHOR.MIDDLE)
        centers.append(yy + hh / 2)
    col_h = len(hosts) * hh + (len(hosts) - 1) * gap
    return centers, col_h


# ====================== layouts ======================

def _cards_header(slide, s):
    panels = s["panels"]
    n = len(panels); gap = 0.35 if n == 2 else 0.3
    w = (FULL - gap * (n - 1)) / n
    top = BODY_TOP
    has_bot = bool(s.get("banner"))
    h = 2.95 if has_bot else 3.75
    for i, p in enumerate(panels):
        x = LEFT + i * (w + gap)
        _hcard(slide, x, top, w, h, _color(p["col"]), p["head"], p["items"],
               sub=p.get("sub"), size=p.get("size", 11.5))
    if has_bot:
        _botbanner(slide, top + h + 0.28, s["banner"])


def _chevrons(slide, s):
    cols = s["cols"]
    n = len(cols); gap = 0.3; ov = 0.45
    w = (FULL + (n - 1) * ov) / n
    top = BODY_TOP; ch = 0.9
    ctop = top + ch + 0.18; cardh = 2.55
    cw = (FULL - (n - 1) * gap) / n
    for i, c in enumerate(cols):
        col = _color(c["col"])
        x = LEFT + i * (w - ov)
        chevron(slide, x, top, w, ch, col, c["head"])
        cx = LEFT + i * (cw + gap)
        rrect(slide, cx, ctop, cw, cardh, WHITE, line=LINE, radius=0.07)
        rrect(slide, cx, ctop, cw, 0.1, col, radius=0.0)
        _bullets(slide, cx + 0.22, ctop + 0.22, cw - 0.44, cardh - 0.4, c["items"], size=11.5)


def _topbar(slide, s):
    cards = s["cards"]
    n = len(cards); gap = 0.3
    w = (FULL - gap * (n - 1)) / n
    top = BODY_TOP
    h = s.get("card_h", 3.75)
    bullet = s.get("bullet", True)
    for i, c in enumerate(cards):
        x = LEFT + i * (w + gap)
        _tcard(slide, x, top, w, h, _color(c["col"]), c["head"], c["items"],
               size=c.get("size", 11.5), bullet=bullet)


def _hosts_premise(slide, s):
    top = BODY_TOP
    lw = 5.0
    centers, col_h = _host_col(slide, s["hosts"], LEFT, lw, top)
    # conector vertical + puntos + flecha hacia el panel de la premisa
    bx = LEFT + lw + 0.4
    link(slide, bx, centers[0], bx, centers[-1], color=RGBColor(0xB8, 0xBC, 0xC6), width=2.2)
    cy = (centers[0] + centers[-1]) / 2
    for cyi in centers:
        oval(slide, bx - 0.06, cyi - 0.06, 0.12, 0.12, RGBColor(0xB8, 0xBC, 0xC6))
        link(slide, LEFT + lw, cyi, bx, cyi, color=RGBColor(0xB8, 0xBC, 0xC6), width=1.6)
    px = bx + 0.5; pw = RIGHT - px
    arrow(slide, bx, cy, px - 0.03, cy, color=INDIGO, width=2.5)
    pr = s["premise"]
    rrect(slide, px, top, pw, col_h, INDIGO, radius=0.08)
    textbox(slide, px, top + 0.18, pw, 0.5, [(pr["head"], 14, True, WHITE, PP_ALIGN.CENTER)],
            anchor=MSO_ANCHOR.MIDDLE)
    q = rrect(slide, px + 0.3, top + 0.9, pw - 0.6, col_h - 1.2, PALE, radius=0.08)
    _settext(q.text_frame, [(pr["quote"], 12.5, False, INDIGO, PP_ALIGN.CENTER)])


def _hosts_command(slide, s):
    top = BODY_TOP
    rw = 5.4
    rx = RIGHT - rw
    centers, col_h = _host_col(slide, s["hosts"], rx, rw, top)
    # caja de comando a la izquierda
    cw = rx - 0.5 - LEFT
    box = rrect(slide, LEFT, top, cw, col_h, INDIGO, radius=0.08)
    textbox(slide, LEFT, top + 0.18, cw, 0.4, [(s.get("command_label", "Comando de Auditoría"),
            13, True, WHITE, PP_ALIGN.CENTER)], anchor=MSO_ANCHOR.MIDDLE)
    inner = rrect(slide, LEFT + 0.35, top + 0.85, cw - 0.7, col_h - 1.2, PALE, radius=0.08)
    tf = inner.text_frame; tf.word_wrap = True; tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
    r = p.add_run(); r.text = s["command"]; r.font.size = Pt(13); r.font.bold = True
    r.font.color.rgb = INDIGO; r.font.name = "Consolas"
    # conector vertical + flecha desde el comando hacia los hosts
    bx = rx - 0.4
    link(slide, bx, centers[0], bx, centers[-1], color=RGBColor(0xB8, 0xBC, 0xC6), width=2.2)
    cy = (centers[0] + centers[-1]) / 2
    for cyi in centers:
        oval(slide, bx - 0.06, cyi - 0.06, 0.12, 0.12, RGBColor(0xB8, 0xBC, 0xC6))
        link(slide, bx, cyi, rx, cyi, color=RGBColor(0xB8, 0xBC, 0xC6), width=1.6)
    arrow(slide, LEFT + cw + 0.03, cy, bx, cy, color=INDIGO, width=2.5)


_LAYOUTS = {
    "cards_header": _cards_header,
    "chevrons": _chevrons,
    "topbar": _topbar,
    "hosts_premise": _hosts_premise,
    "hosts_command": _hosts_command,
}


def d_poc(slide, prs, s):
    _topbanner(slide, s.get("topbanner"))
    _LAYOUTS[s["layout"]](slide, s)
