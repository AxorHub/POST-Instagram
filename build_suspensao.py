# -*- coding: utf-8 -*-
"""Carrossel 'Barulho na suspensão: 5 sons' — plugin mm-autotech-design.
Logo oficial + fontes self-hosted + ícones Lucide. Local: João Monlevade."""
import re, base64
from pathlib import Path

SKILL = Path("mm-autotech-design/skills/mm-carousel-pro")
FONTS, ICONS, LOGO = SKILL/"assets/fonts", SKILL/"assets/icons", SKILL/"assets/logo/mm-logo.png"

RED, RED_L = "#E10600", "#FF2A20"
INK, CARBON, LINE = "#0A0A0B", "#141418", "#26262B"
TEXT, MUTED = "#EDEDEF", "#9A9AA2"
GRAD = "linear-gradient(150deg,#8A0300 0%,#E10600 52%,#FF2A20 100%)"
DISPLAY, BODY = "'Archivo'", "'Inter'"
TOTAL = 7
LOGO_RATIO = 900/889

def font_face():
    out=[]
    for f in sorted(FONTS.glob("*.woff2")):
        fam,w=f.stem.split("-"); b64=base64.b64encode(f.read_bytes()).decode()
        out.append(f"@font-face{{font-family:'{fam}';font-style:normal;font-weight:{w};font-display:swap;src:url(data:font/woff2;base64,{b64}) format('woff2');}}")
    return "\n".join(out)
LOGO_B64 = base64.b64encode(LOGO.read_bytes()).decode()

def logo(h): return f'<div class="mmlogo" style="width:{h*LOGO_RATIO:.0f}px;height:{h}px;"></div>'

def icon(name,size=24,color="currentColor",sw=2):
    svg=(ICONS/f"{name}.svg").read_text(encoding="utf-8")
    svg=re.sub(r'\swidth="[^"]*"','',svg,count=1); svg=re.sub(r'\sheight="[^"]*"','',svg,count=1)
    svg=re.sub(r'stroke-width="[^"]*"',f'stroke-width="{sw}"',svg)
    return svg.replace('<svg',f'<svg width="{size}" height="{size}" style="color:{color};display:block"',1).replace("\n","")

def grid(op=0.035):
    c=f"rgba(255,255,255,{op})"
    return f"background-image:linear-gradient({c} 1px,transparent 1px),linear-gradient(90deg,{c} 1px,transparent 1px);background-size:34px 34px;"
GLOW="radial-gradient(circle at 85% 6%,rgba(225,6,0,0.22),transparent 52%)"

def progress(i):
    pct=(i+1)/TOTAL*100
    return (f'<div style="position:absolute;bottom:0;left:0;right:0;padding:18px 34px 24px;z-index:12;display:flex;align-items:center;gap:11px;">'
            f'<div style="flex:1;height:3px;background:rgba(255,255,255,0.16);border-radius:2px;overflow:hidden;">'
            f'<div style="height:100%;width:{pct:.1f}%;background:{RED};border-radius:2px;"></div></div>'
            f'<span style="font-family:{BODY};font-size:11px;font-weight:600;color:rgba(255,255,255,0.45);letter-spacing:.5px;">{i+1}/{TOTAL}</span></div>')

def accent(): return f'<div style="position:absolute;top:0;left:0;bottom:0;width:5px;background:{GRAD};z-index:9;"></div>'

def meta(i):
    return (f'<div style="position:absolute;top:24px;left:34px;right:34px;z-index:10;display:flex;align-items:center;gap:13px;">'
            f'{logo(30)}<span style="font-family:{BODY};font-size:10.5px;font-weight:600;letter-spacing:2.5px;color:{MUTED};">SUSPENSÃO • RUÍDOS</span>'
            f'<span style="margin-left:auto;font-family:{DISPLAY};font-size:12px;font-weight:700;letter-spacing:1px;">'
            f'<span style="color:{RED_L};">{i+1:02d}</span> <span style="color:{MUTED};">/ {TOTAL:02d}</span></span></div>')

def trigger(label):
    return (f'<span style="display:inline-flex;align-items:center;gap:7px;padding:5px 12px;border-radius:20px;'
            f'background:rgba(255,255,255,0.05);border:1px solid {LINE};font-family:{BODY};font-size:10px;font-weight:700;'
            f'letter-spacing:1.5px;color:{MUTED};">{icon("volume-2",13,RED_L,2.1)} QUANDO: {label}</span>')

S=[]
# ---- CAPA ----
S.append(f"""<div class="slide" style="background:{INK};">
  <div style="position:absolute;inset:0;{grid(0.045)}"></div><div style="position:absolute;inset:0;background:{GLOW};"></div>{accent()}
  <div style="position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;padding:0 40px;z-index:8;">
    {logo(92)}
    <span style="font-family:{BODY};font-size:11px;font-weight:700;letter-spacing:3px;color:{RED_L};margin:30px 0 14px;">DORES COMUNS • SUSPENSÃO</span>
    <div style="display:flex;align-items:flex-start;gap:13px;">
      <h1 style="font-family:{DISPLAY};font-size:46px;font-weight:800;line-height:1.02;color:{TEXT};letter-spacing:-1.5px;margin:0;">Que barulho<br>é esse na<br>suspensão?</h1>
      <span style="margin-top:5px;">{icon('audio-lines',36,RED_L,2.2)}</span></div>
    <p style="font-family:{BODY};font-size:17px;font-weight:400;line-height:1.5;color:{MUTED};margin-top:18px;max-width:335px;"><b style="color:{TEXT};font-weight:700;">5 sons</b> e o que cada um costuma significar — antes que vire um reparo grande.</p>
  </div>
  <div style="position:absolute;bottom:24px;left:40px;right:34px;z-index:10;display:flex;align-items:center;justify-content:space-between;">
    <span style="font-family:{BODY};font-size:12px;font-weight:600;color:{MUTED};">@mmautotech8</span>
    <span style="display:inline-flex;align-items:center;gap:6px;font-family:{BODY};font-size:13px;font-weight:700;color:{TEXT};">Arrasta {icon('chevron-right',18,RED_L,2.5)}</span></div>
</div>""")

# ---- 5 SONS ----
SOUNDS=[
 ("“Toc-toc” seco","Batida seca ao passar em buracos e lombadas costuma ser <b>bieleta</b>, batente ou amortecedor já gasto.","Inspeção de bieletas e amortecedores","activity","passa em buraco"),
 ("Estalo na curva","Estalo ao esterçar o volante aponta <b>junta homocinética</b> ou coxim/torre do amortecedor.","Teste de homocinética e coxins","corner-up-right","vira o volante"),
 ("Rangido / “range”","Range em ondulações lentas = <b>buchas ressecadas</b>, pivô ou bandeja desgastados.","Inspeção de buchas e pivôs","wrench","ondulação devagar"),
 ("Batida metálica","Pancada metálica repetida pode ser <b>mola quebrada</b>, batente solto ou amortecedor no fim de curso.","Inspeção de molas e batentes","triangle-alert","piso irregular"),
 ("Volante tremendo","Trepidação na direção em velocidade indica <b>desbalanceamento</b>, folga em terminal ou rolamento de roda.","Balanceamento, folgas e rolamentos","disc-3","em velocidade"),
]
for k,(title,body,diag,ic,trig) in enumerate(SOUNDS):
    i=k+1; bg=INK if k%2==0 else CARBON
    S.append(f"""<div class="slide" style="background:{bg};">
  <div style="position:absolute;inset:0;{grid()}"></div><div style="position:absolute;inset:0;background:{GLOW};"></div>
  <span style="position:absolute;top:64px;right:18px;font-family:{DISPLAY};font-weight:800;font-size:200px;line-height:0.8;color:rgba(255,255,255,0.045);z-index:1;">{i:02d}</span>
  {meta(i)}
  <div style="position:absolute;left:34px;right:34px;bottom:84px;z-index:8;">
    <div style="width:56px;height:56px;border-radius:14px;background:rgba(225,6,0,0.14);border:1px solid rgba(225,6,0,0.4);display:flex;align-items:center;justify-content:center;margin-bottom:18px;">{icon(ic,28,RED_L,2.1)}</div>
    {trigger(trig)}
    <h2 style="font-family:{DISPLAY};font-size:33px;font-weight:700;line-height:1.1;color:{TEXT};letter-spacing:-0.6px;margin:12px 0 0;">{title}</h2>
    <p style="font-family:{BODY};font-size:15.5px;font-weight:400;line-height:1.55;color:{MUTED};margin:13px 0 0;max-width:335px;">{body}</p>
    <div style="display:inline-flex;align-items:center;gap:9px;margin-top:20px;padding:10px 15px;background:rgba(255,255,255,0.04);border:1px solid {LINE};border-left:2px solid {RED};border-radius:9px;">
      {icon('scan-line',16,RED_L,2.1)}<span style="font-family:{BODY};font-size:11.5px;font-weight:600;letter-spacing:.3px;color:{TEXT};"><span style="color:{RED_L};font-weight:700;">NO DIAGNÓSTICO</span> &rsaquo; {diag}</span></div>
  </div>
  {progress(i)}
</div>""")

# ---- CTA ----
S.append(f"""<div class="slide" style="background:{INK};">
  <div style="position:absolute;inset:0;{grid(0.045)}"></div><div style="position:absolute;inset:0;background:radial-gradient(circle at 50% 110%,rgba(225,6,0,0.28),transparent 60%);"></div>{accent()}
  <div style="position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;padding:0 40px;z-index:8;">
    {logo(64)}
    <span style="font-family:{BODY};font-size:11px;font-weight:700;letter-spacing:3px;color:{RED_L};margin:26px 0 14px;">DIAGNÓSTICO JUSTO</span>
    <h2 style="font-family:{DISPLAY};font-size:37px;font-weight:800;line-height:1.08;color:{TEXT};letter-spacing:-1px;margin:0;">Ouviu um desses<br>no seu carro?</h2>
    <p style="font-family:{BODY};font-size:16px;font-weight:400;line-height:1.5;color:{MUTED};margin-top:15px;max-width:325px;">Suspensão com folga compromete a segurança e o pneu. Traga pra MM AutoTech: a gente localiza a origem do ruído.</p>
    <div style="margin-top:26px;display:inline-flex;align-items:center;gap:10px;padding:14px 26px;background:#fff;border-radius:32px;width:fit-content;">
      {icon('message-circle',20,'#1FA855',2.2)}<span style="font-family:{DISPLAY};font-weight:700;font-size:15px;color:{INK};">Agende no WhatsApp</span></div>
  </div>
  <div style="position:absolute;bottom:24px;left:40px;z-index:10;font-family:{BODY};font-size:12px;font-weight:500;color:{MUTED};">@mmautotech8 · João Monlevade</div>
  {progress(6)}
</div>""")

dots="".join(f'<span class="dot" data-i="{k}" style="width:7px;height:7px;border-radius:50%;background:{RED if k==0 else "rgba(0,0,0,0.18)"};transition:background .2s;"></span>' for k in range(TOTAL))
HTML=f"""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="UTF-8"><style>
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
  <div class="ig-frame"><div class="ig-header"><div class="mmlogo" style="width:{30*LOGO_RATIO:.0f}px;height:30px;"></div>
    <div style="display:flex;flex-direction:column;"><span style="font-size:13px;font-weight:700;color:#111;font-family:{BODY};">mmautotech8</span>
    <span style="font-size:11px;color:#888;font-family:{BODY};">Diagnóstico automotivo</span></div></div>
    <div class="carousel-viewport"><div class="carousel-track">{''.join(S)}</div></div>
    <div class="ig-dots">{dots}</div></div>
<script>
  const track=document.querySelector('.carousel-track'),dots=[...document.querySelectorAll('.dot')],total={TOTAL};let cur=0;
  function go(i){{cur=Math.max(0,Math.min(total-1,i));track.style.transform='translateX('+(-cur*420)+'px)';
    dots.forEach((d,k)=>d.style.background=k===cur?'{RED}':'rgba(0,0,0,0.18)');}}
  dots.forEach(d=>d.addEventListener('click',()=>go(+d.dataset.i)));
  let sx=0,drag=false;const vp=document.querySelector('.carousel-viewport');
  vp.addEventListener('pointerdown',e=>{{drag=true;sx=e.clientX;vp.style.cursor='grabbing';}});
  window.addEventListener('pointerup',e=>{{if(!drag)return;drag=false;vp.style.cursor='grab';const dx=e.clientX-sx;if(dx<-40)go(cur+1);else if(dx>40)go(cur-1);}});
</script></body></html>"""
Path("carousel_suspensao.html").write_text(HTML,encoding="utf-8")
print("carousel_suspensao.html:",len(HTML),"bytes |",TOTAL,"slides")
