import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

INPUT_HTML = Path("carousel.html")
OUTPUT_DIR = Path("slides")
OUTPUT_DIR.mkdir(exist_ok=True)

TOTAL_SLIDES = 7
VIEW_W, VIEW_H = 420, 525
SCALE = 1080 / 420

async def export_slides():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            executable_path="/opt/pw-browsers/chromium-1194/chrome-linux/chrome")
        page = await browser.new_page(viewport={"width": VIEW_W, "height": VIEW_H},
                                       device_scale_factor=SCALE)
        await page.set_content(INPUT_HTML.read_text(encoding="utf-8"), wait_until="networkidle")
        await page.wait_for_timeout(3000)
        await page.evaluate("""() => {
            document.querySelectorAll('.x-topbar,.x-dots').forEach(el => el.style.display='none');
            const frame=document.querySelector('.x-frame');
            frame.style.cssText='width:420px;height:525px;max-width:none;border-radius:0;box-shadow:none;border:none;overflow:hidden;margin:0;';
            const vp=document.querySelector('.carousel-viewport');
            vp.style.cssText='width:420px;height:525px;overflow:hidden;cursor:default;';
            document.body.style.cssText='padding:0;margin:0;display:block;overflow:hidden;background:#000;';
        }""")
        await page.wait_for_timeout(500)
        for i in range(TOTAL_SLIDES):
            await page.evaluate("""(idx)=>{const t=document.querySelector('.carousel-track');
                t.style.transition='none';t.style.transform='translateX('+(-idx*420)+'px)';}""", i)
            await page.wait_for_timeout(350)
            await page.screenshot(path=str(OUTPUT_DIR / f"slide_{i+1}.png"),
                                  clip={"x": 0, "y": 0, "width": VIEW_W, "height": VIEW_H})
            print(f"Exported slide {i+1}/{TOTAL_SLIDES}")
        await browser.close()

asyncio.run(export_slides())
