# -*- coding: utf-8 -*-
import base64, re
def b64(p): return "data:image/png;base64," + base64.b64encode(open(p,"rb").read()).decode()
infocomm=b64("assets/infocomm_s.png"); pyxis=b64("assets/pyxis_s.png"); avispl=b64("assets/avispl_s.png")
body=open("body_frag.html",encoding="utf-8").read()
# convertir divs de alerta/nota en tablas (soffice las rellena bien)
def _alert(m):
    inner = m.group(1).replace("<strong>", '<strong style="color:#ffffff;">')
    return ('<table style="width:100%;margin:12px 0;border-collapse:collapse;"><tr>'
            '<td style="background-color:#B31B1B;color:#ffffff;padding:12px 16px;border:none;">'
            + inner + '</td></tr></table>')
def _nota(m):
    return ('<table style="width:100%;margin:12px 0;border-collapse:collapse;"><tr>'
            '<td style="background-color:#EEF1F8;color:#2b2b2b;padding:10px 14px;border:none;border-left:5px solid #007EE5;font-size:10pt;">'
            + m.group(1) + '</td></tr></table>')
body=re.sub(r'<div class="alerta">\s*(.*?)\s*</div>', _alert, body, flags=re.S)
body=re.sub(r'<div class="nota">\s*(.*?)\s*</div>', _nota, body, flags=re.S)
css = """
@page { margin: 1.7cm; }
body { font-family:"Montserrat",sans-serif; font-size:10.5pt; color:#2b2b2b; line-height:1.5; }
.cover { text-align:center; page-break-after:always; }
.logostrip { margin:1.6cm auto 2.2cm auto; }
.logostrip td { padding:0 22px; vertical-align:middle; }
.cover h1 { color:#341E66; font-size:30pt; margin:0 0 8px 0; border:none; }
.cover .sub { color:#007EE5; font-size:14pt; font-weight:600; margin:0 auto 1.8cm auto; max-width:16cm; }
.cover .event { color:#555; font-size:11pt; margin-bottom:1.5cm; }
.cover .who { color:#341E66; font-size:11.5pt; line-height:1.55; }
.cover .who .role { color:#777; font-weight:400; font-size:10pt; }
.cover .foot { margin-top:2.6cm; color:#999; font-size:9pt; }
h1 { color:#341E66; font-size:17pt; border-bottom:3px solid #007EE5; padding-bottom:5px; margin-top:26px; }
h2 { color:#341E66; font-size:14pt; margin-top:22px; border-bottom:1px solid #E2E2E8; padding-bottom:3px; }
h3 { color:#007EE5; font-size:11.5pt; margin-bottom:3px; margin-top:16px; }
strong { color:#341E66; }
a { color:#007EE5; text-decoration:none; }
table { border-collapse:collapse; }
table.content, table:not(.logostrip):not(.alertbox):not(.notebox) { width:100%; font-size:9.3pt; margin:10px 0; }
th { background:#341E66; color:#fff; text-align:left; padding:6px 9px; }
td { border:1px solid #DCDCE2; padding:5px 9px; vertical-align:top; }
tr:nth-child(even) td { background:#F5F6F9; }
ul { margin:4px 0; } li { margin:3px 0; }
hr { border:none; border-top:1px solid #E6E6EC; margin:16px 0; }
.alertbox { width:100%; margin:12px 0; }
.alertbox td { background:#B31B1B; color:#fff; padding:12px 16px; border:none; }
.alertbox td strong { color:#fff; }
.notebox { width:100%; margin:12px 0; }
.notebox td { background:#EEF1F8; color:#2b2b2b; padding:10px 14px; border:none; border-left:5px solid #007EE5; font-size:10pt; }
.notebox td strong { color:#341E66; }
.logostrip td { border:none; background:none; }
"""
cover = f"""
<div class="cover">
  <table align="center" style="margin:1.3cm auto 1.8cm auto;border-collapse:collapse;"><tr><td align="center" style="border:none;padding:9px 0;"><img src="{infocomm}"></td></tr><tr><td align="center" style="border:none;padding:9px 0;"><img src="{pyxis}"></td></tr><tr><td align="center" style="border:none;padding:9px 0;"><img src="{avispl}"></td></tr></table>
  <h1>Kit del taller</h1>
  <div class="sub">Cuando IT frena tu proyecto AV: seguridad que se diseña, no se parcha</div>
  <div class="event">InfoComm América Latina 2026 · Ciudad de México · 22 de octubre de 2026</div>
  <div class="who">
    <b>Juan Pineda</b> · Pyxis<br><span class="role">Service Delivery Manager / Tech Academy Lead</span><br><br>
    <b>Eduardo Travi</b> · AVI SPL<br><span class="role">Business Development Manager, CTS</span>
  </div>
  <div class="foot">Material educativo. Las marcas de equipos se omiten a propósito. Esto no es asesoría legal.</div>
</div>
"""
html=f"<!DOCTYPE html><html><head><meta charset='utf-8'><style>{css}</style></head><body>{cover}{body}</body></html>"
open("kit_full.html","w",encoding="utf-8").write(html); print("armado")
