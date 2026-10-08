# -*- coding: utf-8 -*-
import base64
def b64(p): return "data:image/png;base64," + base64.b64encode(open(p,"rb").read()).decode()
pyxis=b64("assets/pyxis_w.png"); avispl=b64("assets/avispl_w.png")
html = f"""<!DOCTYPE html><html lang="es"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Cuando IT frena tu proyecto AV — ICAL26</title>
<style>
:root{{--indigo:#341E66;--blue:#007EE5;--ink:#2b2b2b;}}
*{{box-sizing:border-box;margin:0;padding:0;}}
body{{font-family:'Segoe UI',system-ui,-apple-system,sans-serif;color:var(--ink);line-height:1.55;}}
.hero{{background:linear-gradient(135deg,#2A1A52 0%,#341E66 42%,#0B4FA0 100%);color:#fff;text-align:center;padding:70px 20px 60px;}}
.hero .ev{{letter-spacing:2px;text-transform:uppercase;font-size:13px;color:#B9C7E8;margin-bottom:18px;}}
.hero h1{{font-size:40px;font-weight:800;letter-spacing:-.5px;max-width:880px;margin:0 auto;}}
.hero .rule{{width:70px;height:4px;background:#00A3FF;border-radius:3px;margin:22px auto;}}
.hero .sub{{font-size:19px;color:#D9E8FF;font-weight:600;}}
.hero .when{{font-size:15px;color:#9FB0D8;margin-top:22px;}}
.wrap{{max-width:900px;margin:0 auto;padding:0 20px;}}
.dl{{display:grid;grid-template-columns:1fr 1fr;gap:22px;margin:-40px auto 50px;max-width:900px;padding:0 20px;}}
.card{{background:#fff;border:1px solid #e6e6ec;border-radius:14px;padding:26px;box-shadow:0 10px 30px rgba(40,25,90,.08);}}
.card .tag{{display:inline-block;font-size:12px;font-weight:700;color:#fff;background:var(--blue);padding:3px 10px;border-radius:20px;margin-bottom:12px;}}
.card h3{{color:var(--indigo);font-size:20px;margin-bottom:6px;}}
.card p{{color:#666;font-size:14px;margin-bottom:18px;}}
.card a.btn{{display:inline-block;background:var(--indigo);color:#fff;text-decoration:none;font-weight:700;padding:11px 20px;border-radius:9px;font-size:14px;}}
.card a.btn:hover{{background:#45267f;}}
h2.sec{{color:var(--indigo);font-size:24px;margin:10px 0 24px;text-align:center;}}
.people{{display:grid;grid-template-columns:1fr 1fr;gap:26px;margin-bottom:56px;}}
.person{{border-left:4px solid var(--blue);padding-left:16px;}}
.person b{{color:var(--indigo);font-size:17px;}}
.person .role{{color:#777;font-size:13px;}}
.person .org{{color:#999;font-size:13px;margin-bottom:8px;}}
.person a{{color:var(--blue);text-decoration:none;font-size:14px;display:block;margin-top:3px;}}
footer{{background:#1d1340;color:#fff;text-align:center;padding:40px 20px;}}
footer .lbl{{letter-spacing:2px;text-transform:uppercase;font-size:11px;color:#9FB0D8;margin-bottom:16px;}}
footer img{{height:30px;margin:0 18px;vertical-align:middle;filter:brightness(1.1);}}
footer .disc{{color:#8794B8;font-size:12px;max-width:640px;margin:26px auto 0;}}
@media(max-width:680px){{.dl,.people{{grid-template-columns:1fr;}}.hero h1{{font-size:30px;}}}}
</style></head><body>
<div class="hero">
  <div class="ev">InfoComm América Latina 2026 · Ciudad de México · 22 de octubre de 2026</div>
  <h1>Cuando IT frena tu proyecto AV</h1>
  <div class="rule"></div>
  <div class="sub">Seguridad que se diseña, no se parcha</div>
  <div class="when">Taller de seguridad para integradores AV</div>
</div>
<div class="dl">
  <div class="card">
    <span class="tag">Diapositivas</span>
    <h3>Presentación del taller</h3>
    <p>Los conceptos, el marco de seguridad y el ciclo de vida de un ataque, con las demos.</p>
    <a class="btn" href="diapositivas.pdf">Descargar PDF</a>
  </div>
  <div class="card">
    <span class="tag">Kit</span>
    <h3>Kit para llevar</h3>
    <p>Checklist de hardening, guion de preguntas de IT y guía para montar tu laboratorio.</p>
    <a class="btn" href="kit.pdf">Descargar PDF</a>
  </div>
</div>
<div class="wrap">
  <h2 class="sec">Contacto</h2>
  <div class="people">
    <div class="person">
      <b>Juan Pineda</b>
      <div class="role">Service Delivery Manager / Tech Academy Lead</div>
      <div class="org">Pyxis</div>
      <a href="mailto:juan.pineda@pyxis.tech">juan.pineda@pyxis.tech</a>
      <a href="https://www.linkedin.com/in/jdpinedac/">linkedin.com/in/jdpinedac</a>
    </div>
    <div class="person">
      <b>Eduardo Travi</b>
      <div class="role">Business Development Manager, CTS</div>
      <div class="org">AVI SPL</div>
      <a href="mailto:Eduardo.Travi@avispl.com">Eduardo.Travi@avispl.com</a>
      <a href="https://www.linkedin.com/in/eduardotravi/">linkedin.com/in/eduardotravi</a>
    </div>
  </div>
</div>
<footer>
  <div class="lbl">Presentan</div>
  <img src="{pyxis}"><img src="{avispl}">
  <div class="disc">Material educativo. Las marcas de equipos se omiten a propósito. Esto no es asesoría legal: consulta la normativa vigente de tu país.</div>
</footer>
</body></html>"""
open("index.html","w",encoding="utf-8").write(html)
print("index.html generado:", len(html), "bytes")
