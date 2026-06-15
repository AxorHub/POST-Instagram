from pathlib import Path

# ---- Dark mode color system (X) + MM AutoTech red accent ----
SLIDE_BG       = "#000000"
TEXT_PRIMARY   = "#E7E9EA"
TEXT_MUTED     = "#71767B"
DIVIDER        = "#2F3336"
ICON_COLOR     = "#71767B"
ACCENT         = "#E10600"   # MM AutoTech brand red (replaces X blue)
SLIDE_NUM_BG   = "rgba(255,255,255,0.08)"
SLIDE_NUM_TEXT = "#71767B"

DISPLAY_NAME = "MM AutoTech"
HANDLE       = "mmautotech8"

# Brand "MM" avatar built inline (no photo provided) — black circle, white MM, red bar
AVATAR_HTML = f"""
<div style="width:48px;height:48px;border-radius:50%;flex-shrink:0;background:#0A0A0B;
            border:1.5px solid {ACCENT};display:flex;flex-direction:column;
            align-items:center;justify-content:center;line-height:1;">
  <span class="x-font" style="font-size:18px;font-weight:800;color:#fff;letter-spacing:-1px;">MM</span>
  <span style="width:20px;height:2px;background:{ACCENT};margin-top:2px;border-radius:2px;"></span>
</div>
"""

def hl(t):  # highlight helper — brand red emphasis
    return f'<span style="color:{ACCENT};font-weight:600;">{t}</span>'

# ---- Slide copy (PT-BR, tweet style) ----
slides = [
    {  # 1 Hook
        "body": f"Seu carro está te avisando. Você só não está ouvindo. 🚗💨<br><br>"
                f"{hl('5 sinais')} de que chegou a hora de passar o scanner 👇",
        "eng": ("1.2K", "3.4K", "21K", "486K"),
    },
    {  # 2
        "body": f"{hl('1.')} A luz da injeção acendeu no painel. 🔧<br><br>"
                f"Não é “frescura do carro”. É o sistema dizendo que algo saiu do padrão — "
                f"e ignorar só aumenta a conta lá na frente.",
        "eng": ("312", "1.1K", "9.8K", "204K"),
    },
    {  # 3
        "body": f"{hl('2.')} O consumo de combustível disparou. ⛽<br><br>"
                f"Gastando mais pra rodar o mesmo trajeto? Sensor de oxigênio, injeção ou "
                f"ignição podem estar falhando — só o scanner aponta onde.",
        "eng": ("268", "947", "8.2K", "176K"),
    },
    {  # 4
        "body": f"{hl('3.')} Trancos, falhas ou perda de força. 🌀<br><br>"
                f"Aquele “engasgo” na arrancada raramente é normal. O diagnóstico encontra "
                f"o código exato antes de virar dor de cabeça.",
        "eng": ("401", "1.3K", "11K", "239K"),
    },
    {  # 5
        "body": f"{hl('4.')} Bateria descarregando ou motor esquentando. 🔋🌡️<br><br>"
                f"Problemas elétricos e de temperatura deixam rastros nos módulos. "
                f"O scanner lê esses dados em tempo real.",
        "eng": ("229", "812", "7.4K", "158K"),
    },
    {  # 6
        "body": f"{hl('5.')} Vai comprar um usado? 📋<br><br>"
                f"Antes de fechar negócio, o scanner revela falhas ocultas que o vendedor "
                f"às vezes nem sabe que existem. {hl('Diagnosticar é prevenir.')}",
        "eng": ("517", "2.0K", "15K", "321K"),
    },
    {  # 7 CTA
        "body": f"Não deixe a pequena falha virar uma grande conta. 💸<br><br>"
                f"Agende seu diagnóstico com a {hl('MM AutoTech')} 👇<br><br>"
                f"📲 {hl('Chama a gente no WhatsApp!')}",
        "eng": ("689", "2.7K", "19K", "402K"),
    },
]
TOTAL = len(slides)

VERIFIED_SVG = f"""<svg width="18" height="18" viewBox="0 0 24 24" fill="{ACCENT}">
<path d="M22.25 12c0-1.43-.88-2.67-2.19-3.34.46-1.39.2-2.9-.81-3.91s-2.52-1.27-3.91-.81c-.66-1.31-1.91-2.19-3.34-2.19s-2.67.88-3.33 2.19c-1.4-.46-2.91-.2-3.92.81s-1.26 2.52-.8 3.91c-1.31.67-2.2 1.91-2.2 3.34s.89 2.67 2.2 3.34c-.46 1.39-.21 2.9.8 3.91s2.52 1.26 3.91.81c.67 1.31 1.91 2.19 3.34 2.19s2.68-.88 3.34-2.19c1.39.45 2.9.2 3.91-.81s1.27-2.52.81-3.91c1.31-.67 2.19-1.91 2.19-3.34zm-11.71 4.2L6.8 12.46l1.41-1.42 2.26 2.26 4.8-5.23 1.47 1.36-6.2 6.77z"/></svg>"""

def engagement(eng, idx):
    reply, repost, like, views = eng
    return f"""
  <div style="height:1px;background:{DIVIDER};margin:0 22px;"></div>
  <div class="x-engagement" style="display:flex;align-items:center;padding:12px 22px 20px;gap:0;">
    <div style="display:flex;align-items:center;gap:6px;flex:1;">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="{ICON_COLOR}" stroke-width="1.8"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
      <span class="x-font" style="font-size:13px;color:{TEXT_MUTED};">{reply}</span>
    </div>
    <div style="display:flex;align-items:center;gap:6px;flex:1;">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="{ICON_COLOR}" stroke-width="1.8"><path d="M17 1l4 4-4 4"/><path d="M3 11V9a4 4 0 0 1 4-4h14"/><path d="M7 23l-4-4 4-4"/><path d="M21 13v2a4 4 0 0 1-4 4H3"/></svg>
      <span class="x-font" style="font-size:13px;color:{TEXT_MUTED};">{repost}</span>
    </div>
    <div style="display:flex;align-items:center;gap:6px;flex:1;">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="{ICON_COLOR}" stroke-width="1.8"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>
      <span class="x-font" style="font-size:13px;color:{TEXT_MUTED};">{like}</span>
    </div>
    <div style="display:flex;align-items:center;gap:6px;flex:1;">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="{ICON_COLOR}" stroke-width="1.8"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>
      <span class="x-font" style="font-size:13px;color:{TEXT_MUTED};">{views}</span>
    </div>
    <div style="margin-left:auto;padding:4px 10px;background:{SLIDE_NUM_BG};border-radius:20px;">
      <span class="x-font" style="font-size:13px;font-weight:500;color:{SLIDE_NUM_TEXT};">{idx+1}/{TOTAL}</span>
    </div>
  </div>"""

def slide(s, idx):
    return f"""
  <div class="x-slide" style="width:420px;height:525px;flex-shrink:0;background:{SLIDE_BG};display:flex;flex-direction:column;">
    <div class="x-header" style="display:flex;align-items:center;gap:12px;padding:20px 22px 14px;">
      {AVATAR_HTML}
      <div style="display:flex;flex-direction:column;gap:1px;">
        <div style="display:flex;align-items:center;gap:4px;">
          <span class="x-font" style="font-size:16px;font-weight:700;color:{TEXT_PRIMARY};">{DISPLAY_NAME}</span>
          {VERIFIED_SVG}
        </div>
        <span class="x-font" style="font-size:15px;font-weight:400;color:{TEXT_MUTED};">@{HANDLE}</span>
      </div>
    </div>
    <div style="height:1px;background:{DIVIDER};margin:0 22px;"></div>
    <div class="x-content" style="flex:1;padding:20px 22px 16px;display:flex;align-items:center;">
      <p class="x-font" style="font-size:20px;font-weight:400;line-height:1.55;color:{TEXT_PRIMARY};margin:0;">{s['body']}</p>
    </div>
    {engagement(s['eng'], idx)}
  </div>"""

slides_html = "".join(slide(s, i) for i, s in enumerate(slides))
dots = "".join(
    f'<span class="x-dot" data-i="{i}" style="width:7px;height:7px;border-radius:50%;background:{ACCENT if i==0 else "rgba(255,255,255,0.25)"};transition:background .2s;"></span>'
    for i in range(TOTAL)
)

html = f"""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{ background:#16181C; display:flex; align-items:center; justify-content:center; min-height:100vh; padding:24px; font-family:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif; }}
  .x-font {{ font-family:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif; }}
  .x-frame {{ width:420px; background:{SLIDE_BG}; border-radius:18px; overflow:hidden; box-shadow:0 12px 40px rgba(0,0,0,.6); border:1px solid {DIVIDER}; }}
  .x-topbar {{ display:flex; align-items:center; gap:14px; padding:12px 18px; border-bottom:1px solid {DIVIDER}; }}
  .carousel-viewport {{ width:420px; height:525px; overflow:hidden; cursor:grab; }}
  .carousel-track {{ display:flex; transition:transform .35s cubic-bezier(.22,.61,.36,1); }}
  .x-dots {{ display:flex; align-items:center; justify-content:center; gap:7px; padding:14px 0 16px; }}
</style></head>
<body>
  <div class="x-frame">
    <div class="x-topbar">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="#E7E9EA"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231 5.45-6.231Zm-1.161 17.52h1.833L7.084 4.126H5.117L17.083 19.77Z"/></svg>
      <div style="flex:1;display:flex;align-items:center;gap:8px;background:rgba(255,255,255,0.06);border-radius:20px;padding:7px 14px;">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="{TEXT_MUTED}" stroke-width="2"><circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/></svg>
        <span class="x-font" style="font-size:13px;color:{TEXT_MUTED};">Pesquisar</span>
      </div>
    </div>
    <div class="carousel-viewport">
      <div class="carousel-track">{slides_html}</div>
    </div>
    <div class="x-dots">{dots}</div>
  </div>
<script>
  const track=document.querySelector('.carousel-track');
  const dots=[...document.querySelectorAll('.x-dot')];
  const total={TOTAL}; let cur=0;
  function go(i){{ cur=Math.max(0,Math.min(total-1,i)); track.style.transform='translateX('+(-cur*420)+'px)';
    dots.forEach((d,k)=>d.style.background=k===cur?'{ACCENT}':'rgba(255,255,255,0.25)'); }}
  dots.forEach(d=>d.addEventListener('click',()=>go(+d.dataset.i)));
  let sx=0,drag=false;
  const vp=document.querySelector('.carousel-viewport');
  vp.addEventListener('pointerdown',e=>{{drag=true;sx=e.clientX;vp.style.cursor='grabbing';}});
  window.addEventListener('pointerup',e=>{{ if(!drag)return; drag=false; vp.style.cursor='grab';
    const dx=e.clientX-sx; if(dx<-40)go(cur+1); else if(dx>40)go(cur-1); }});
</script>
</body></html>"""

Path("carousel.html").write_text(html, encoding="utf-8")
print("OK -> carousel.html  (", TOTAL, "slides )")
