"""Shared building blocks for AerSynk social graphics.

Each graphic is an HTML page (1080 wide) rendered to PNG with headless Chromium.
Run: python3 tools/render.py <html files...>
"""
import math
import random

ROOT_REL = ".."  # templates/ and brand/ are one level up from the generated html folder


def contours(seed=1, w=1080, h=1350, hills=2, rings=9, color="#24394A"):
    """Soft topographic contour lines for the background (decorative, generated)."""
    rnd = random.Random(seed)
    paths = []
    for _ in range(hills):
        cx, cy = rnd.uniform(0.15, 0.85) * w, rnd.uniform(0.2, 0.9) * h
        base = rnd.uniform(60, 110)
        phase = [rnd.uniform(0, 6.28) for _ in range(3)]
        for r in range(1, rings + 1):
            pts = []
            for i in range(73):
                a = i / 72 * 2 * math.pi
                wob = 1 + 0.16 * math.sin(3 * a + phase[0]) + 0.09 * math.sin(5 * a + phase[1] + r * 0.2) + 0.05 * math.sin(7 * a + phase[2])
                rad = base * r * 0.62 * wob
                pts.append((cx + rad * math.cos(a), cy + rad * 0.82 * math.sin(a)))
            d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts) + "Z"
            paths.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="1.6"/>')
    return f'<svg class="contours" viewBox="0 0 {w} {h}" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">{"".join(paths)}</svg>'


def page(inner, h=1350, seed=1, title="AerSynk"):
    return f"""<!doctype html><html><head><meta charset="utf-8"><title>{title}</title>
<link rel="stylesheet" href="{ROOT_REL}/templates/base.css"><style>:root{{--h:{h}px}}</style></head>
<body>{contours(seed=seed, h=h)}<div class="frame"></div><div class="sheet">{inner}</div></body></html>"""


def top(count=None):
    c = f'<span class="count">{count}</span>' if count else ""
    return f'<div class="top"><img src="{ROOT_REL}/brand/logo-on-dark.png" alt="">{c}</div>'


def foot(left="aersynk.io", right=""):
    return f'<div class="foot"><span class="url">{left}</span><span>{right}</span></div>'


# ---------- illustrations (simple line drawings in the website's style) ----------

def layers_svg(labels=("Camera", "LiDAR", "Magnetometer"), colors=("#34DEDC", "#6E9BD6", "#A07CC0")):
    """Stacked survey layers, like the website's Survey illustration."""
    out = ['<svg viewBox="0 0 760 520" xmlns="http://www.w3.org/2000/svg">']
    for i, (lab, col) in enumerate(reversed(list(zip(labels, colors)))):
        y = 300 - i * 120
        out.append(f'<g transform="translate(0,{y})"><polygon points="380,0 740,90 380,180 20,90" fill="#0E1F2C" fill-opacity=".92" stroke="{col}" stroke-width="3"/>')
        out.append(f'<text x="760" y="96" fill="{col}" font-family="Instrument Sans" font-weight="600" font-size="28" text-anchor="end" dx="-6"></text></g>')
    # detail on top layer
    out.append('<g stroke="#34DEDC" stroke-width="2" fill="#34DEDC" fill-opacity=".18"><polygon points="300,105 380,85 460,105 380,125"/><polygon points="380,125 460,105 540,125 460,145"/></g>')
    out.append('</svg>')
    return "".join(out)


def drone_svg(x, y, s=1.0, color="#F3F7F6"):
    return (f'<g transform="translate({x},{y}) scale({s})" stroke="{color}" stroke-width="3" fill="#0E1F2C">'
            '<line x1="-26" y1="-15" x2="26" y2="15"/><line x1="-26" y1="15" x2="26" y2="-15"/>'
            '<circle cx="-26" cy="-15" r="10"/><circle cx="26" cy="15" r="10"/><circle cx="-26" cy="15" r="10"/><circle cx="26" cy="-15" r="10"/>'
            '<rect x="-12" y="-9" width="24" height="18" rx="5"/></g>')
