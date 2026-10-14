"""Render HTML graphics to PNG (or JPEG) with headless Chromium.

Usage: python3 tools/render.py path/to/slide-01.html [more.html ...]
Each output image is written next to its HTML file with the same name.
"""
import asyncio
import sys
from pathlib import Path

from playwright.async_api import async_playwright


async def main(files):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        for f in files:
            path = Path(f).resolve()
            html = path.read_text()
            height = 1920 if "--h:1920px" in html else 1350
            page = await browser.new_page(viewport={"width": 1080, "height": height})
            await page.goto(path.as_uri())
            await page.evaluate("document.fonts.ready")
            await page.wait_for_timeout(150)
            out = path.with_suffix(".jpg")
            await page.screenshot(path=str(out), type="jpeg", quality=92)
            await page.close()
            print(out)
        await browser.close()


if __name__ == "__main__":
    asyncio.run(main(sys.argv[1:]))
