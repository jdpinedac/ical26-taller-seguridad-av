# -*- coding: utf-8 -*-
# Incrusta Montserrat (TTF) dentro de un .pptx para que sea portable.
import sys, os, zipfile, shutil
import lxml.etree as ET

FONTDIR = os.path.expanduser("~/.local/share/fonts/montserrat")
# (typeface, {regular, bold}) -> archivos TTF
FAMILIES = [
    ("Montserrat",        {"regular": "Montserrat-Regular.ttf", "bold": "Montserrat-Bold.ttf"}),
    ("Montserrat Medium", {"regular": "Montserrat-Medium.ttf",  "bold": "Montserrat-SemiBold.ttf"}),
]

P  = "http://schemas.openxmlformats.org/presentationml/2006/main"
R  = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
CT = "http://schemas.openxmlformats.org/package/2006/content-types"
RL = "http://schemas.openxmlformats.org/package/2006/relationships"
REL_FONT = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/font"

def q(ns, tag): return "{%s}%s" % (ns, tag)

def embed(path):
    parts = {}
    with zipfile.ZipFile(path) as z:
        for n in z.namelist():
            parts[n] = z.read(n)

    # 1) agregar las partes de fuente
    font_parts = []   # (partname, rId placeholder, styles->partname)
    fam_rels = []     # (typeface, {style: rId})
    # recolectar rIds existentes del presentation.rels
    rels_name = "ppt/_rels/presentation.xml.rels"
    rels = ET.fromstring(parts[rels_name])
    used = []
    for rel in rels:
        rid = rel.get("Id")
        if rid and rid.startswith("rId"):
            try: used.append(int(rid[3:]))
            except: pass
    nxt = (max(used) + 1) if used else 1

    fidx = 1
    for typeface, styles in FAMILIES:
        style_rids = {}
        for style, fname in styles.items():
            data = open(os.path.join(FONTDIR, fname), "rb").read()
            partname = "ppt/fonts/font%d.fntdata" % fidx
            parts[partname] = data
            rid = "rId%d" % nxt; nxt += 1
            fidx += 1
            # relationship
            rel = ET.SubElement(rels, q(RL, "Relationship"))
            rel.set("Id", rid)
            rel.set("Type", REL_FONT)
            rel.set("Target", "fonts/%s" % os.path.basename(partname))
            style_rids[style] = rid
        fam_rels.append((typeface, style_rids))
    parts[rels_name] = ET.tostring(rels, xml_declaration=True, encoding="UTF-8", standalone=True)

    # 2) content types: Default para fntdata
    ctypes = ET.fromstring(parts["[Content_Types].xml"])
    has = any(d.get("Extension") == "fntdata" for d in ctypes if d.tag == q(CT, "Default"))
    if not has:
        d = ET.SubElement(ctypes, q(CT, "Default"))
        d.set("Extension", "fntdata")
        d.set("ContentType", "application/x-fontdata")
    parts["[Content_Types].xml"] = ET.tostring(ctypes, xml_declaration=True, encoding="UTF-8", standalone=True)

    # 3) presentation.xml: embedTrueTypeFonts + embeddedFontLst
    pres = ET.fromstring(parts["ppt/presentation.xml"])
    pres.set("embedTrueTypeFonts", "1")
    # quitar embeddedFontLst previo si existe
    for e in pres.findall(q(P, "embeddedFontLst")):
        pres.remove(e)
    efl = ET.Element(q(P, "embeddedFontLst"))
    for typeface, style_rids in fam_rels:
        ef = ET.SubElement(efl, q(P, "embeddedFont"))
        fo = ET.SubElement(ef, q(P, "font")); fo.set("typeface", typeface)
        for style in ("regular", "bold", "italic", "boldItalic"):
            if style in style_rids:
                se = ET.SubElement(ef, q(P, style))
                se.set(q(R, "id"), style_rids[style])
    # insertar en orden de schema: tras notesSz/sldSz, antes de defaultTextStyle/custShowLst/extLst
    order_after = [q(P, "notesSz"), q(P, "sldSz"), q(P, "sldIdLst")]
    insert_at = len(pres)
    for i, ch in enumerate(pres):
        if ch.tag in (q(P, "custShowLst"), q(P, "photoAlbum"), q(P, "custDataLst"),
                      q(P, "kinsoku"), q(P, "defaultTextStyle"), q(P, "modifyVerifier"), q(P, "extLst")):
            insert_at = i; break
    pres.insert(insert_at, efl)
    parts["ppt/presentation.xml"] = ET.tostring(pres, xml_declaration=True, encoding="UTF-8", standalone=True)

    # 4) reescribir el zip
    tmp = path + ".tmp"
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as z:
        for name, data in parts.items():
            z.writestr(name, data)
    os.replace(tmp, path)
    print("Incrustadas %d fuentes en %s" % (fidx - 1, path))

if __name__ == "__main__":
    embed(sys.argv[1])
