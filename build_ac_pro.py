# -*- coding: utf-8 -*-
"""Carrossel premium 'AC fraco' — plugin mm-autotech-design.
Logo oficial (transparente) + fontes self-hosted + ícones Lucide. Local: João Monlevade.
Obs.: o post de AC já agendado no Metricool NÃO é afetado por reexecutar isto."""
import re, base64
from pathlib import Path

SKILL = Path("mm-autotech-design/skills/mm-carousel-pro")
FONTS = SKILL / "assets/fonts"
ICONS = SKILL / "assets/icons"
LOGO  = SKILL / "assets/logo/mm-logo.png"

RED, RED_L, RED_D = "#E10600", "#FF2A20", "#8A0300"
INK, CARBON, LINE = "#0A0A0B", "#141418", "#26262B"
TEXT, MUTED = "#EDEDEF", "#9A9AA2"
GRAD = "linear-gradient(150deg,#8A0300 0%,#E10600 52%,#FF2A20 100%)"
DISPLAY, BODY = "'Archivo'", "'Inter'"
TOTAL = 7
LOGO_RATIO = 900 / 889  # w/h

def font_face():
    out = []
    for f in sorted(FONTS.glob("*.woff2")):
        fam, wght = f.stem.split("-")
        b64 = base64.b64encode(f.read_bytes()).decode()
        out.append(f"@font-face{{font-family:'{fam}';font-style:normal;font-weight:{wght};"
                   f"font-display:swap;src:url(data:font/woff2;base64,{b64}) format('woff2');}}")
    return "\n".join(out)

LOGO_B64 = base64.b64encode(LOGO.read_bytes()).decode()  # embutido uma vez no CSS

def logo(h):
    w = h * LOGO_RATIO
    return f'<div class="mmlogo" style="width:{w:.0f}px;height:{h}px;"></div>'

def icon(name, size=24, color="currentColor", sw=2):
    svg = (ICONS / f"{name}.svg").read_text(encoding="utf-8")
    svg = re.sub(r'\swidth="[^"]*"', '', svg, count=1)
    svg = re.sub(r'\sheight="[^"]*"', '', svg, count=1)
    svg = re.sub(r'stroke-width="[^"]*"', f'stroke-width="{sw}"', svg)
    svg = svg.replace('<svg', f'<svg width="{size}" height="{size}" style="color:{color};display:block"', 1)
    return svg.replace("\n", "")

def grid(op=0.035):
    c = f"rgba(255,255,255,{op})"
    return (f"background-image:linear-gradient({c} 1px,transparent 1px),"
            f"linear-gradient(90deg,{c} 1px,transparent 1px);background-size:34px 34px;")

GLOW = "radial-gradient(circle at 85% 6%,rgba(225,6,0,0.22),transparent 52%)"

def progress(i):
    pct = (i + 1) / TOTAL * 100
    return (f'<div style="position:absolute;bottom:0;left:0;right:0;padding:18px 34px 24px;z-index:12;'
            f'display:flex;align-items:center;gap:11px;">'
            f'<div style="flex:1;height:3px;background:rgba(255,255,255,0.16);border-radius:2px;overflow:hidden;">'
            f'<div style="height:100%;width:{pct:.1f}%;background:{RED};border-radius:2px;"></div></div>'
            f'<span style="font-family:{BODY};font-size:11px;font-weight:600;color:rgba(255,255,255,0.45);letter-spacing:.5px;">{i+1}/{TOTAL}</span></div>')

def accent_bar():
    return f'<div style="position:absolute;top:0;left:0;bottom:0;width:5px;background:{GRAD};z-index:9;"></div>'

def meta_bar(i):
    return (f'<div style="position:absolute;top:24px;left:34px;right:34px;z-index:10;display:flex;align-items:center;gap:13px;">'
            f'{logo(30)}'
            f'<span style="font-family:{BODY};font-size:10.5px;font-weight:600;letter-spacing:2.5px;color:{MUTED};">AR-CONDICIONADO</span>'
            f'<span style="margin-left:auto;font-family:{DISPLAY};font-size:12px;font-weight:700;letter-spacing:1px;">'
            f'<span style="color:{RED_L};">{i+1:02d}</span> <span style="color:{MUTED};">/ {TOTAL:02d}</span></span></div>')

SLIDES = []

# ---------- 1 · CAPA (dark) ----------
SLIDES.append(f"""<div class="slide" style="background:{INK};">
  <div style="position:absolute;inset:0;{grid(0.045)}"></div>
  <div style="position:absolute;inset:0;background:{GLOW};"></div>
  {accent_bar()}
  <div style="position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;padding:0 40px;z-index:8;">
    {logo(92)}
    <span style="font-family:{BODY};font-size:11px;font-weight:700;letter-spacing:3px;color:{RED_L};margin:30px 0 14px;">DIAGNÓSTICO • AR-CONDICIONADO</span>
    <div style="display:flex;align-items:flex-start;gap:13px;">
      <h1 style="font-family:{DISPLAY};font-size:47px;font-weight:800;line-height:1.0;color:{TEXT};letter-spacing:-1.5px;margin:0;">Seu ar parou<br>de gelar?</h1>
      <span style="margin-top:5px;">{icon('snowflake',36,RED_L,2.2)}</span></div>
    <p style="font-family:{BODY};font-size:17px;font-weight:400;line-height:1.5;color:{MUTED};margin-top:18px;max-width:330px;">As <b style="color:{TEXT};font-weight:700;">5 causas</b> mais comuns — e por que trocar peça no chute sai <b style="color:{TEXT};font-weight:700;">caro</b>.</p>
  </div>
  <div style="position:absolute;bottom:24px;left:40px;right:34px;z-index:10;display:flex;align-items:center;justify-content:space-between;">
    <span style="font-family:{BODY};font-size:12px;font-weight:600;color:{MUTED};">@mmautotech8</span>
    <span style="display:inline-flex;align-items:center;gap:6px;font-family:{BODY};font-size:13px;font-weight:700;color:{TEXT};">Arrasta {icon('chevron-right',18,RED_L,2.5)}</span></div>
</div>""")

# ---------- 2..6 · CAUSAS ----------
CAUSES = [
    ("Falta de gás no sistema", "O fluido refrigerante reduz com o tempo. Carga baixa = ar fraco. Mas <b>repor sem achar a causa</b> é jogar dinheiro fora.", "Teste de carga e pressão", "gauge"),
    ("Vazamento escondido", "Mangueiras, condensador e válvulas vazam — por isso o gás “some”. Com <b>teste de estanqueidade</b> achamos o ponto exato.", "Estanqueidade (UV / N₂)", "droplets"),
    ("Filtro de cabine sujo", "Ar abafado e com cheiro? Muitas vezes é só o <b>filtro saturado</b> travando o fluxo. Barato — quando é isso mesmo.", "Inspeção de fluxo e filtro", "wind"),
    ("Compressor com defeito", "Não engata, faz barulho ou desarma? É o <b>coração do sistema</b>. Antes de condenar, testamos embreagem e pressão.", "Embreagem e acionamento", "cog"),
    ("Condensador / ventoinha", "Sujos ou parados, não dissipam o calor — e o ar <b>nunca gela de verdade</b>. Limpeza e teste elétrico resolvem.", "Teste elétrico da ventoinha", "fan"),
]
for k, (title, body, diag, ic) in enumerate(CAUSES):
    i = k + 1
    bg = INK if k % 2 == 0 else CARBON
    SLIDES.append(f"""<div class="slide" style="background:{bg};">
  <div style="position:absolute;inset:0;{grid()}"></div>
  <div style="position:absolute;inset:0;background:{GLOW};"></div>
  <span style="position:absolute;top:64px;right:18px;font-family:{DISPLAY};font-weight:800;font-size:200px;line-height:0.8;color:rgba(255,255,255,0.045);z-index:1;">{i:02d}</span>
  {meta_bar(i)}
  <div style="position:absolute;left:34px;right:34px;bottom:84px;z-index:8;">
    <div style="width:56px;height:56px;border-radius:14px;background:rgba(225,6,0,0.14);border:1px solid rgba(225,6,0,0.4);display:flex;align-items:center;justify-content:center;margin-bottom:20px;">
      {icon(ic,28,RED_L,2.1)}</div>
    <span style="font-family:{BODY};font-size:11px;font-weight:700;letter-spacing:2.5px;color:{RED_L};">CAUSA {i:02d}</span>
    <h2 style="font-family:{DISPLAY};font-size:33px;font-weight:700;line-height:1.1;color:{TEXT};letter-spacing:-0.6px;margin:10px 0 0;">{title}</h2>
    <p style="font-family:{BODY};font-size:16px;font-weight:400;line-height:1.55;color:{MUTED};margin:14px 0 0;max-width:330px;">{body}</p>
    <div style="display:inline-flex;align-items:center;gap:9px;margin-top:22px;padding:10px 15px;background:rgba(255,255,255,0.04);border:1px solid {LINE};border-left:2px solid {RED};border-radius:9px;">
      {icon('scan-line',16,RED_L,2.1)}
      <span style="font-family:{BODY};font-size:11.5px;font-weight:600;letter-spacing:.3px;color:{TEXT};"><span style="color:{RED_L};font-weight:700;">DIAGNÓSTICO</span> &rsaquo; {diag}</span></div>
  </div>
  {progress(i)}
</div>""")

# ---------- 7 · CTA (dark) ----------
SLIDES.append(f"""<div class="slide" style="background:{INK};">
  <div style="position:absolute;inset:0;{grid(0.045)}"></div>
  <div style="position:absolute;inset:0;background:radial-gradient(circle at 50% 110%,rgba(225,6,0,0.28),transparent 60%);"></div>
  {accent_bar()}
  <div style="position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;padding:0 40px;z-index:8;">
    {logo(64)}
    <span style="font-family:{BODY};font-size:11px;font-weight:700;letter-spacing:3px;color:{RED_L};margin:26px 0 14px;">DIAGNÓSTICO JUSTO</span>
    <h2 style="font-family:{DISPLAY};font-size:36px;font-weight:800;line-height:1.08;color:{TEXT};letter-spacing:-1px;margin:0;">Antes de condenar peça, faça o teste certo.</h2>
    <p style="font-family:{BODY};font-size:16px;font-weight:400;line-height:1.5;color:{MUTED};margin-top:15px;max-width:320px;">A gente mostra o problema antes de cobrar a solução. Avaliação de ar-condicionado na MM AutoTech.</p>
    <div style="margin-top:26px;display:inline-flex;align-items:center;gap:10px;padding:14px 26px;background:#fff;border-radius:32px;width:fit-content;">
      {icon('message-circle',20,'#1FA855',2.2)}
      <span style="font-family:{DISPLAY};font-weight:700;font-size:15px;color:{INK};">Agende no WhatsApp</span></div>
  </div>
  <div style="position:absolute;bottom:24px;left:40px;z-index:10;font-family:{BODY};font-size:12px;font-weight:500;color:{MUTED};">@mmautotech8 · João Monlevade</div>
  {progress(6)}
</div>""")

dots = "".join(
    f'<span class="dot" data-i="{k}" style="width:7px;height:7px;border-radius:50%;background:{RED if k==0 else "rgba(0,0,0,0.18)"};transition:background .2s;"></span>'
    for k in range(TOTAL))

HTML = f"""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="UTF-8">
<style>
{font_face()}
.mmlogo{{background:url(data:image/png;base64,{LOGO_B64}) center/contain no-repeat;}}
*{{margin:0;padding:0;box-sizing:border-box;}}
body{{background:#202024;display:flex;align-items:center;justify-content:center;min-height:100vh;padding:24px;font-family:{BODY},sans-serif;}}
.ig-frame{{width:420px;background:#fff;border-radius:18px;overflow:hidden;box-shadow:0 14px 44px rgba(0,0,0,.55);}}
.ig-header{{display:flex;align-items:center;gap:11px;padding:12px 16px;border-bottom:1px solid #eee;}}
.carousel-viewport{{width:420px;height:525px;overflow:hidden;cursor:grab;}}
.carousel-track{{display:flex;transition:transform .35s cubic-bezier(.22,.61,.36,1);}}
.slide{{width:420px;height:525px;flex-shrink:0;position:relative;overflow:hidden;}}
.ig-dots{{display:flex;align-items:center;justify-content:center;gap:7px;padding:14px 0 16px;}}
</style></head><body>
  <div class="ig-frame">
    <div class="ig-header"><div class="mmlogo" style="width:{30*LOGO_RATIO:.0f}px;height:30px;"></div>
      <div style="display:flex;flex-direction:column;"><span style="font-size:13px;font-weight:700;color:#111;font-family:{BODY};">mmautotech8</span>
      <span style="font-size:11px;color:#888;font-family:{BODY};">Diagnóstico automotivo</span></div></div>
    <div class="carousel-viewport"><div class="carousel-track">{''.join(SLIDES)}</div></div>
    <div class="ig-dots">{dots}</div>
  </div>
<script>
  const track=document.querySelector('.carousel-track'),dots=[...document.querySelectorAll('.dot')],total={TOTAL};let cur=0;
  function go(i){{cur=Math.max(0,Math.min(total-1,i));track.style.transform='translateX('+(-cur*420)+'px)';
    dots.forEach((d,k)=>d.style.background=k===cur?'{RED}':'rgba(0,0,0,0.18)');}}
  dots.forEach(d=>d.addEventListener('click',()=>go(+d.dataset.i)));
  let sx=0,drag=false;const vp=document.querySelector('.carousel-viewport');
  vp.addEventListener('pointerdown',e=>{{drag=true;sx=e.clientX;vp.style.cursor='grabbing';}});
  window.addEventListener('pointerup',e=>{{if(!drag)return;drag=false;vp.style.cursor='grab';
    const dx=e.clientX-sx;if(dx<-40)go(cur+1);else if(dx>40)go(cur-1);}});
</script></body></html>"""

Path("carousel_ac_pro.html").write_text(HTML, encoding="utf-8")
print("carousel_ac_pro.html:", len(HTML), "bytes")
