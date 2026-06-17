import asyncio
from pathlib import Path
from playwright.async_api import async_playwright
INPUT_HTML=Path("carousel_suspensao.html"); OUTPUT_DIR=Path("slides_suspensao"); OUTPUT_DIR.mkdir(exist_ok=True)
TOTAL_SLIDES=7; VIEW_W,VIEW_H=420,525; SCALE=1080/420
async def run():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path="/opt/pw-browsers/chromium-1194/chrome-linux/chrome")
        pg=await b.new_page(viewport={"width":VIEW_W,"height":VIEW_H},device_scale_factor=SCALE)
        await pg.set_content(INPUT_HTML.read_text(encoding="utf-8"),wait_until="networkidle"); await pg.wait_for_timeout(1500)
        await pg.evaluate("""()=>{document.querySelectorAll('.ig-header,.ig-dots').forEach(e=>e.style.display='none');
          const f=document.querySelector('.ig-frame');f.style.cssText='width:420px;height:525px;border-radius:0;box-shadow:none;border:none;overflow:hidden;margin:0;';
          document.querySelector('.carousel-viewport').style.cssText='width:420px;height:525px;overflow:hidden;cursor:default;';
          document.body.style.cssText='padding:0;margin:0;display:block;overflow:hidden;background:#000;';}""")
        await pg.wait_for_timeout(400)
        for i in range(TOTAL_SLIDES):
            await pg.evaluate("""(idx)=>{const t=document.querySelector('.carousel-track');t.style.transition='none';t.style.transform='translateX('+(-idx*420)+'px)';}""",i)
            await pg.wait_for_timeout(320)
            await pg.screenshot(path=str(OUTPUT_DIR/f"slide_{i+1}.png"),clip={"x":0,"y":0,"width":VIEW_W,"height":VIEW_H})
            print("slide",i+1)
        await b.close()
asyncio.run(run())
