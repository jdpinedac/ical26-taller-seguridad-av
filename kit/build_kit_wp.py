# -*- coding: utf-8 -*-
import base64, re
from weasyprint import HTML
def b64(p): return "data:image/png;base64," + base64.b64encode(open(p,"rb").read()).decode()
infocomm=b64("assets/infocomm_w.png"); pyxis=b64("assets/pyxis_w.png"); avispl=b64("assets/avispl_w.png")
body=open("body_frag.html",encoding="utf-8").read()

CSS = """
@page { size: Letter; margin: 2cm 2.1cm 1.7cm 2.1cm;
  @bottom-left { content:"ICAL26 · Kit del taller de seguridad AV"; font-size:7.5pt; color:#A7ABB5; }
  @bottom-center { content:"Pyxis · AVI SPL"; font-size:7.5pt; color:#A7ABB5; }
  @bottom-right { content:counter(page); font-size:7.5pt; color:#A7ABB5; }
}
@page cover { margin:0; background: linear-gradient(135deg,#2A1A52 0%,#341E66 42%,#0B4FA0 100%);
  @bottom-left{content:""} @bottom-center{content:""} @bottom-right{content:""} }
* { box-sizing:border-box; }
html { font-family:"Montserrat",sans-serif; color:#2b2b2b; font-size:10.5pt; line-height:1.5; }

.cover { page: cover; break-after: page; color:#fff; min-height:25.3cm;
         display:flex; flex-direction:column; align-items:center; text-align:center; padding:2.3cm 2.2cm; }
.cover .event-logo { height:1.5cm; margin-bottom:1.1cm; }
.cover .title { font-size:33pt; font-weight:700; letter-spacing:-.5px; margin:.2cm 0 .2cm 0; }
.cover .rule { width:3.2cm; height:4px; background:#00A3FF; border-radius:3px; margin:.5cm 0 .9cm 0; }
.cover .sub { font-size:14.5pt; font-weight:600; color:#D9E8FF; max-width:15cm; }
.cover .event { font-size:11pt; color:#B9C7E8; margin-top:.7cm; }
.cover .people { display:flex; gap:2.4cm; margin-top:1.5cm; }
.cover .person b { font-size:12.5pt; }
.cover .person .role { font-size:9.5pt; color:#C4CFEA; }
.cover .person .org { font-size:10pt; color:#8FA8D8; margin-top:2px; }
.cover .partners { margin-top:auto; padding-top:1.2cm; }
.cover .partners .lbl { font-size:8.5pt; letter-spacing:2px; color:#9FB0D8; text-transform:uppercase; margin-bottom:.45cm; }
.cover .partners img { height:.95cm; margin:0 .9cm; vertical-align:middle; }
.cover .disc { font-size:8pt; color:#8794B8; margin-top:1cm; max-width:16cm; }

h1,h2 { color:#341E66; }
h2 { font-size:15.5pt; margin:26px 0 8px 0; padding-bottom:6px; border-bottom:2px solid #E4E4EC; position:relative; }
h2::before { content:""; position:absolute; left:0; bottom:-2px; width:2.6cm; height:2px; background:#007EE5; }
h3 { color:#007EE5; font-size:11.5pt; margin:16px 0 4px 0; }
p { margin:7px 0; }
strong { color:#341E66; }
a { color:#007EE5; text-decoration:none; border-bottom:1px solid #BFE0FF; }
ul { margin:5px 0 5px 4px; padding-left:16px; } li { margin:4px 0; }
hr { border:none; border-top:1px solid #ECECF1; margin:18px 0; }
table { border-collapse:collapse; width:100%; font-size:9.3pt; margin:12px 0; }
th { background:#341E66; color:#fff; text-align:left; padding:7px 9px; }
td { border:1px solid #E0E0E6; padding:6px 9px; vertical-align:top; }
tr:nth-child(even) td { background:#F6F7FA; }
.alerta { background:#B3201B; color:#fff; padding:13px 17px; border-radius:9px; margin:14px 0; }
.alerta strong { color:#fff; }
.nota { background:#EEF3FB; border-left:5px solid #007EE5; padding:11px 15px; border-radius:5px; margin:14px 0; font-size:10pt; }
"""

cover = f"""
<section class="cover">
  <img class="event-logo" src="{infocomm}">
  <div class="title">Kit del taller</div>
  <div class="rule"></div>
  <div class="sub">Cuando IT frena tu proyecto AV: seguridad que se diseña, no se parcha</div>
  <div class="event">InfoComm América Latina 2026 · Ciudad de México · 22 de octubre de 2026</div>
  <div class="people">
    <div class="person"><b>Juan Pineda</b><div class="role">Service Delivery Manager / Tech Academy Lead</div><div class="org">Pyxis</div></div>
    <div class="person"><b>Eduardo Travi</b><div class="role">Business Development Manager, CTS</div><div class="org">AVI SPL</div></div>
  </div>
  <div class="partners">
    <div class="lbl">Presentan</div>
    <img src="{pyxis}"><img src="{avispl}">
  </div>
  <div class="disc">Material educativo. Las marcas de equipos se omiten a propósito. Esto no es asesoría legal.</div>
</section>
"""
html = f"<!DOCTYPE html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{cover}{body}</body></html>"
HTML(string=html).write_pdf("ICAL26-kit.pdf")
print("PDF generado con WeasyPrint")
