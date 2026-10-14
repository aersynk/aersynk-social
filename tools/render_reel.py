"""Render an animated reel page (with window.render(t)) to an MP4 with optional voice track.

Usage: python3 tools/render_reel.py reel.html out.mp4 --seconds 22 [--audio voice.wav]
Output: 1080x1920, 30 fps, H.264 + AAC, suitable for Instagram Reels and Facebook.
"""
import argparse
import asyncio
import subprocess
import tempfile
from pathlib import Path

from playwright.async_api import async_playwright

FPS = 30


async def frames(html, folder, seconds):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1080, "height": 1920})
        await page.goto(Path(html).resolve().as_uri())
        await page.evaluate("document.fonts.ready")
        n = int(seconds * FPS)
        for i in range(n):
            await page.evaluate(f"window.render({i / FPS})")
            await page.screenshot(path=f"{folder}/f{i:05d}.jpg", type="jpeg", quality=90)
        await browser.close()
        return n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("html")
    ap.add_argument("out")
    ap.add_argument("--seconds", type=float, required=True)
    ap.add_argument("--audio")
    a = ap.parse_args()
    with tempfile.TemporaryDirectory() as tmp:
        asyncio.run(frames(a.html, tmp, a.seconds))
        cmd = ["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(FPS), "-i", f"{tmp}/f%05d.jpg"]
        if a.audio:
            cmd += ["-i", a.audio]
        else:  # silent track: some apps reject videos without audio
            cmd += ["-f", "lavfi", "-t", str(a.seconds), "-i", "anullsrc=r=44100:cl=stereo"]
        cmd += ["-c:v", "libx264", "-profile:v", "high", "-pix_fmt", "yuv420p", "-crf", "20", "-preset", "medium",
                "-c:a", "aac", "-b:a", "128k", "-ar", "44100", "-ac", "2", "-shortest", "-movflags", "+faststart", a.out]
        subprocess.run(cmd, check=True)
    print(a.out)


if __name__ == "__main__":
    main()
