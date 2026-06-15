# -*- coding: utf-8 -*-
"""Gera carousel_ac.html — estilo 'slide designado' (claro/escuro + gradiente + HUD tech)."""
from pathlib import Path

# ---- Tokens de marca (MM AutoTech, dark-first, tech automotivo) ----
PRIMARY = "#E10600"
LIGHT   = "#FF3B30"
DARK    = "#0A0A0B"
LIGHT_BG= "#F4F4F5"
BORDER  = "#E2E2E5"
GRAD    = "linear-gradient(150deg,#8A0300 0%,#E10600 52%,#FF3B30 100%)"
TOTAL   = 7

def tech_corners(color):
    return f"""
    <span style="position:absolute;top:22px;left:22px;width:18px;height:18px;border-top:2px solid {color};border-left:2px solid {color};opacity:.9;"></span>
    <span style="position:absolute;bottom:74px;right:22px;width:18px;height:18px;border-bottom:2px solid {color};border-right:2px solid {color};opacity:.9;"></span>"""

def progress(i, light):
    pct = (i + 1) / TOTAL * 100
    track = "rgba(0,0,0,0.10)" if light else "rgba(255,255,255,0.14)"
    fill  = PRIMARY if light else "#fff"
    label = "rgba(0,0,0,0.35)" if light else "rgba(255,255,255,0.45)"
    return f"""<div style="position:absolute;bottom:0;left:0;right:0;padding:16px 30px 22px;z-index:10;display:flex;align-items:center;gap:10px;">
      <div style="flex:1;height:3px;background:{track};border-radius:2px;overflow:hidden;">
        <div style="height:100%;width:{pct:.2f}%;background:{fill};border-radius:2px;"></div></div>
      <span style="font-size:11px;color:{label};font-weight:600;letter-spacing:.5px;">{i+1}/{TOTAL}</span></div>"""

def arrow(light, last):
    if last:
        return ""
    bg = "rgba(0,0,0,0.05)" if light else "rgba(255,255,255,0.06)"
    st = "rgba(0,0,0,0.28)" if light else "rgba(255,255,255,0.4)"
    return f"""<div style="position:absolute;right:0;top:0;bottom:0;width:44px;z-index:9;display:flex;align-items:center;justify-content:center;background:linear-gradient(to right,transparent,{bg});">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="none"><path d="M9 6l6 6-6 6" stroke="{st}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg></div>"""

def logo(dark_text=False):
    txt = DARK if dark_text else "#fff"
    return f"""<div style="display:flex;align-items:center;gap:10px;">
      <div style="width:38px;height:38px;border-radius:50%;background:{DARK};border:1.5px solid {PRIMARY};display:flex;flex-direction:column;align-items:center;justify-content:center;line-height:1;">
        <span style="font-size:14px;font-weight:700;color:#fff;letter-spacing:-1px;">MM</span>
        <span style="width:16px;height:2px;background:{PRIMARY};margin-top:2px;border-radius:2px;"></span></div>
      <span style="font-size:13px;font-weight:600;color:{txt};letter-spacing:.5px;">MM AutoTech</span></div>"""

def chip(text, light):
    bg = "rgba(225,6,0,0.07)" if light else "rgba(225,6,0,0.16)"
    bd = "rgba(225,6,0,0.25)" if light else "rgba(225,6,0,0.4)"
    return f"""<div style="margin-top:20px;display:inline-flex;align-items:center;gap:9px;padding:9px 14px;background:{bg};border:1px solid {bd};border-radius:10px;">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="{PRIMARY}" stroke-width="2.2"><path d="M12 2v4M12 18v4M2 12h4M18 12h4"/><circle cx="12" cy="12" r="3.5"/></svg>
      <span style="font-size:11px;font-weight:600;letter-spacing:.5px;color:{PRIMARY};">{text}</span></div>"""

def tag(text, color):
    return f'<span style="display:inline-block;font-size:10px;font-weight:700;letter-spacing:2.5px;color:{color};margin-bottom:16px;">{text}</span>'

SLIDES = []

# 1 — HERO (gradiente)
SLIDES.append(f"""<div class="slide" style="background:{GRAD};">
  {tech_corners('rgba(255,255,255,0.5)')}
  <div style="position:absolute;top:26px;left:30px;z-index:5;">{logo()}</div>
  <div style="position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;padding:0 36px;z-index:4;">
    {tag('AR-CONDICIONADO AUTOMOTIVO','rgba(255,255,255,0.7)')}
    <h1 style="font-size:42px;font-weight:700;line-height:1.05;color:#fff;letter-spacing:-1px;margin:0;">Seu ar parou<br>de gelar? <span style="font-size:38px;">❄️</span></h1>
    <p style="font-size:17px;font-weight:400;line-height:1.5;color:rgba(255,255,255,0.92);margin-top:18px;max-width:330px;">As <b>5 causas</b> mais comuns — e por que trocar peça no chute sai <b>caro</b>.</p>
    <span style="margin-top:24px;font-size:13px;font-weight:600;color:#fff;opacity:.85;">Arrasta pro lado 👉</span>
  </div>
  <div style="position:absolute;bottom:24px;left:30px;z-index:5;font-size:12px;color:rgba(255,255,255,0.75);font-weight:500;">@mmautotech8</div>
  {arrow(False, False)}{progress(0, False)}</div>""")

CAUSES = [
    ("01","Falta de gás no sistema","O fluido refrigerante reduz com o tempo. Carga baixa = ar fraco. Mas <b>repor sem achar a causa</b> é jogar dinheiro fora.","DIAGNÓSTICO › Teste de carga e pressão","🌫️"),
    ("02","Vazamento escondido","Mangueiras, condensador e válvulas vazam — por isso o gás “some”. Com <b>teste de estanqueidade</b> a gente acha o ponto exato.","DIAGNÓSTICO › Estanqueidade (UV / N₂)","💧"),
    ("03","Filtro de cabine sujo","Ar abafado e com cheiro? Muitas vezes é só o <b>filtro saturado</b> travando o fluxo. Barato de resolver — quando é isso mesmo.","DIAGNÓSTICO › Inspeção de fluxo e filtro","🍃"),
    ("04","Compressor com defeito","Não engata, faz barulho ou desarma? É o <b>coração do sistema</b>. Antes de condenar, testamos embreagem e pressão.","DIAGNÓSTICO › Embreagem e acionamento","⚙️"),
    ("05","Condensador / ventoinha","Sujos ou parados, não dissipam o calor — e o ar <b>nunca gela de verdade</b>. Limpeza e teste elétrico resolvem sem trocar o que está bom.","DIAGNÓSTICO › Teste elétrico da ventoinha","🔥"),
]

for idx, (num, title, body, ch, emoji) in enumerate(CAUSES):
    slide_no = idx + 1            # posição 1..5 dentro de CAUSES
    i = idx + 1                   # índice global (slide 2..6)
    light = (i % 2 == 0)          # i=2->light, 3->dark, 4->light, 5->dark, 6->light
    bg = LIGHT_BG if light else DARK
    txt = DARK if light else "#fff"
    sub = "#55555A" if light else "rgba(255,255,255,0.72)"
    corner = "rgba(225,6,0,0.5)"
    SLIDES.append(f"""<div class="slide" style="background:{bg};">
  {tech_corners(corner)}
  <div style="position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;padding:0 38px;z-index:4;">
    <div style="display:flex;align-items:baseline;gap:14px;margin-bottom:6px;">
      <span style="font-size:64px;font-weight:700;color:{PRIMARY};line-height:0.9;letter-spacing:-2px;">{num}</span>
      <span style="font-size:30px;">{emoji}</span></div>
    {tag('CAUSA',PRIMARY if light else LIGHT)}
    <h2 style="font-size:30px;font-weight:700;line-height:1.1;color:{txt};letter-spacing:-0.5px;margin:0;">{title}</h2>
    <p style="font-size:16px;font-weight:400;line-height:1.55;color:{sub};margin-top:14px;max-width:320px;">{body}</p>
    {chip(ch, light)}
  </div>
  <div style="position:absolute;bottom:24px;left:38px;z-index:5;font-size:11px;color:{sub};font-weight:600;letter-spacing:.5px;">MM AutoTech · desde 1989</div>
  {arrow(light, False)}{progress(i, light)}</div>""")

# 7 — CTA (gradiente)
SLIDES.append(f"""<div class="slide" style="background:{GRAD};">
  {tech_corners('rgba(255,255,255,0.5)')}
  <div style="position:absolute;top:26px;left:30px;z-index:5;">{logo()}</div>
  <div style="position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;padding:0 36px;z-index:4;">
    {tag('DIAGNÓSTICO JUSTO','rgba(255,255,255,0.7)')}
    <h2 style="font-size:34px;font-weight:700;line-height:1.1;color:#fff;letter-spacing:-0.5px;margin:0;">Antes de condenar peça, faça o teste certo.</h2>
    <p style="font-size:16px;font-weight:400;line-height:1.5;color:rgba(255,255,255,0.92);margin-top:16px;max-width:320px;">Avaliação de ar-condicionado na MM AutoTech. Mais de 30 anos em Guarulhos. ❄️</p>
    <div style="margin-top:26px;display:inline-flex;align-items:center;gap:9px;padding:13px 26px;background:#fff;color:{DARK};font-weight:700;font-size:15px;border-radius:30px;width:fit-content;">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="#25D366"><path d="M.057 24l1.687-6.163a11.867 11.867 0 0 1-1.587-5.946C.16 5.335 5.495 0 12.05 0a11.82 11.82 0 0 1 8.413 3.488 11.82 11.82 0 0 1 3.48 8.414c-.003 6.557-5.338 11.892-11.893 11.892a11.9 11.9 0 0 1-5.688-1.448L.057 24zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884a9.86 9.86 0 0 0 1.51 5.26l-.999 3.648 3.978-1.607z"/></svg>
      Agende no WhatsApp</div>
  </div>
  <div style="position:absolute;bottom:24px;left:30px;z-index:5;font-size:12px;color:rgba(255,255,255,0.78);font-weight:500;">@mmautotech8 · Guarulhos</div>
  {progress(6, False)}</div>""")

dots = "".join(
    f'<span class="dot" data-i="{k}" style="width:7px;height:7px;border-radius:50%;background:{PRIMARY if k==0 else "rgba(0,0,0,0.18)"};transition:background .2s;"></span>'
    for k in range(TOTAL))

HTML = f"""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
  *{{margin:0;padding:0;box-sizing:border-box;font-family:'Space Grotesk',-apple-system,sans-serif;}}
  body{{background:#202024;display:flex;align-items:center;justify-content:center;min-height:100vh;padding:24px;}}
  .ig-frame{{width:420px;background:#fff;border-radius:18px;overflow:hidden;box-shadow:0 12px 40px rgba(0,0,0,.5);}}
  .ig-header{{display:flex;align-items:center;gap:11px;padding:12px 16px;border-bottom:1px solid #eee;}}
  .carousel-viewport{{width:420px;height:525px;overflow:hidden;cursor:grab;}}
  .carousel-track{{display:flex;transition:transform .35s cubic-bezier(.22,.61,.36,1);}}
  .slide{{width:420px;height:525px;flex-shrink:0;position:relative;overflow:hidden;}}
  .ig-dots{{display:flex;align-items:center;justify-content:center;gap:7px;padding:14px 0 16px;}}
</style></head><body>
  <div class="ig-frame">
    <div class="ig-header">
      <div style="width:34px;height:34px;border-radius:50%;background:{DARK};border:1.5px solid {PRIMARY};display:flex;flex-direction:column;align-items:center;justify-content:center;line-height:1;">
        <span style="font-size:12px;font-weight:700;color:#fff;letter-spacing:-1px;">MM</span>
        <span style="width:13px;height:2px;background:{PRIMARY};margin-top:1px;border-radius:2px;"></span></div>
      <div style="display:flex;flex-direction:column;"><span style="font-size:13px;font-weight:700;color:#111;">mmautotech8</span>
      <span style="font-size:11px;color:#888;">Guarulhos · Diagnóstico automotivo</span></div></div>
    <div class="carousel-viewport"><div class="carousel-track">{''.join(SLIDES)}</div></div>
    <div class="ig-dots">{dots}</div>
  </div>
<script>
  const track=document.querySelector('.carousel-track'),dots=[...document.querySelectorAll('.dot')],total={TOTAL};let cur=0;
  function go(i){{cur=Math.max(0,Math.min(total-1,i));track.style.transform='translateX('+(-cur*420)+'px)';
    dots.forEach((d,k)=>d.style.background=k===cur?'{PRIMARY}':'rgba(0,0,0,0.18)');}}
  dots.forEach(d=>d.addEventListener('click',()=>go(+d.dataset.i)));
  let sx=0,drag=false;const vp=document.querySelector('.carousel-viewport');
  vp.addEventListener('pointerdown',e=>{{drag=true;sx=e.clientX;vp.style.cursor='grabbing';}});
  window.addEventListener('pointerup',e=>{{if(!drag)return;drag=false;vp.style.cursor='grab';
    const dx=e.clientX-sx;if(dx<-40)go(cur+1);else if(dx>40)go(cur-1);}});
</script></body></html>"""

Path("carousel_ac.html").write_text(HTML, encoding="utf-8")
print("carousel_ac.html gerado:", len(HTML), "bytes")
