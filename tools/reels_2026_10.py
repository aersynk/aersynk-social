"""Reel specs for 19 Oct to 1 Nov 2026. Run: python3 tools/reels_2026_10.py r02 r03 ...  (no args = all)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from art import (a, GROW, drone, label, grid, panels, person, pin, card,  # noqa: E402
                 CY, BL, VI, AM, GO, SOS, INK, MU, LINE, PANEL)
from reel_engine import build  # noqa: E402

NOTE = "Animated illustration. Voice is computer-generated."
F = "posts/2026-10"

# ---------------- R02 What is GSD ----------------
def r02():
    big_grid = f'<g {a(inn="0.2,1.2")}>' + grid(190, 120, 700, 700, 70, LINE, 3) + '</g>' + \
        f'<rect x="470" y="400" width="70" height="70" fill="{CY}" fill-opacity=".5" stroke="{CY}" stroke-width="4" {a(inn="1.2,1.8")}/>'
    one_px = (f'<rect x="140" y="560" width="800" height="260" rx="10" fill="#1E3424" stroke="{LINE}" stroke-width="2" {a(inn="0,0.6")}/>'
              f'<g {a(inn="0.6,1.4")}>' + grid(140, 560, 800, 260, 130, "#4F7A5A", 2) + '</g>'
              f'<rect x="530" y="560" width="130" height="130" fill="{CY}" fill-opacity=".35" stroke="{CY}" stroke-width="5" {a(inn="1.4,2.0")}/>'
              + f'<g {a(inn="1.8,2.4")}>' + label(595, 520, "1 pixel", 40, CY) + '</g>'
              + f'<g {a(inn="0.4,1.0")}>' + drone(595, 160, 1.6) + '</g>'
              + f'<path d="M595,200 L540,560 M595,200 L650,560" stroke="{CY}" stroke-width="2" stroke-dasharray="6 8" {a(inn="1.0,1.6")}/>')
    low = (f'<g {a(move="0,1.2,0,-220")}>' + drone(540, 330, 1.6) + '</g>'
           + f'<path d="M540,370 L360,700 L720,700 Z" fill="{CY}" fill-opacity=".08" stroke="{CY}" stroke-width="2" stroke-dasharray="6 8" {a(inn="1.0,1.6")}/>'
           + f'<g {a(inn="1.4,2.6")}>' + grid(360, 700, 360, 200, 24, CY, 2) + '</g>'
           + f'<g {a(inn="2.2,2.8")}>' + label(540, 970, "Smaller pixels, more detail", 36, INK) + '</g>')
    high = (f'<g {a(move="0,1.2,0,200")}>' + drone(540, 90, 1.6) + '</g>'
            + f'<path d="M540,130 L180,700 L900,700 Z" fill="{BL}" fill-opacity=".08" stroke="{BL}" stroke-width="2" stroke-dasharray="6 8" {a(inn="1.0,1.6")}/>'
            + f'<g {a(inn="1.4,2.6")}>' + grid(180, 700, 720, 200, 90, BL, 2) + '</g>'
            + f'<g {a(inn="2.2,2.8")}>' + label(540, 970, "Bigger pixels, faster coverage", 36, INK) + '</g>')
    pick = (card(120, 200, 840, 230, "Checking cracks", "Fine GSD: fly low", CY, a(inn="0.2,0.8", move="0.2,0.8,0,40"))
            + card(120, 500, 840, 230, "Site overview", "Coarse GSD: fly high", BL, a(inn="1.0,1.6", move="1.0,1.6,0,40")))
    return {"id": "r02-gsd", "folder": f"{F}/r02-what-is-gsd", "note": NOTE, "scenes": [
        {"title": "What is GSD?", "voice": "What is G S D, and why does it matter for a drone survey?", "svg": big_grid},
        {"step": "Ground sampling distance", "title": "One pixel, on the ground.", "voice": "G S D is the size of one image pixel, measured on the ground.", "svg": one_px},
        {"step": "Fly lower", "title": "More detail, more flying.", "voice": "Fly lower, and each pixel covers less ground, so you see more detail.", "svg": low},
        {"step": "Fly higher", "title": "Faster, less detail.", "voice": "Fly higher, and you cover more ground faster, but with less detail.", "svg": high},
        {"step": "The rule", "title": "Pick it for the decision.", "voice": "So choose the G S D for the decision you need to make.", "svg": pick, "hold": 0.4}],
        "end": {"title": "Planning a survey?", "voice": "Planning a survey? Get in touch at aersynk dot io."}}


# ---------------- R03 Thermal solar ----------------
def r03():
    arr_x, arr_y = 130, 230
    normal = f'<g {a(inn="0,0.8")}>' + panels(arr_x, arr_y, 6, 5, 120, 80, 18, "#1B3550", BL) + '</g>' + \
        f'<g {a(inn="0.8,1.4")}>' + label(540, 760, "Visual camera: all panels look the same", 34, MU) + '</g>'
    thermal = (panels(arr_x, arr_y, 6, 5, 120, 80, 18, "#162A6B", "#3A4FA0")
               + f'<rect x="{arr_x + 3 * 138}" y="{arr_y + 2 * 98}" width="120" height="80" rx="4" fill="{AM}" {a(inn="0.8,1.6")}/>'
               + f'<circle cx="{arr_x + 3 * 138 + 60}" cy="{arr_y + 2 * 98 + 40}" r="70" fill="none" stroke="{SOS}" stroke-width="5" {GROW} {a(grow="1.4,2.0")}/>'
               + f'<g {a(inn="1.8,2.4")}>' + label(540, 760, "Thermal camera: one module runs hot", 34, INK) + '</g>')
    sun = (f'<g {a(inn="0,0.8")}><circle cx="540" cy="330" r="110" fill="{GO}" fill-opacity=".25" stroke="{GO}" stroke-width="5"/>'
           + "".join(f'<line x1="{540 + 150 * c}" y1="{330 + 150 * s}" x2="{540 + 200 * c}" y2="{330 + 200 * s}" stroke="{GO}" stroke-width="6" stroke-linecap="round"/>'
                     for c, s in [(1, 0), (-1, 0), (0, 1), (0, -1), (.707, .707), (-.707, .707), (.707, -.707), (-.707, -.707)]) + '</g>'
           + f'<g {a(inn="1.0,1.6")}>' + label(540, 680, "600 W/m² or more", 64, INK, weight=800) + '</g>'
           + f'<g {a(inn="1.8,2.4")}>' + label(540, 750, "Irradiance guidance in IEC TS 62446-3", 32, MU) + '</g>')
    confirm = (panels(arr_x, arr_y, 6, 5, 120, 80, 18, "#162A6B", "#3A4FA0")
               + f'<rect x="{arr_x + 3 * 138}" y="{arr_y + 2 * 98}" width="120" height="80" rx="4" fill="{AM}"/>'
               + f'<g {a(inn="0.3,0.9", move="0.3,0.9,0,-40")}>' + pin(arr_x + 3 * 138 + 60, arr_y + 2 * 98 + 30, GO) + '</g>'
               + f'<g {a(inn="1.4,2.0", move="1.4,2.0,-80,0")}>' + person(870, 820, 1.1) + '</g>'
               + f'<path d="M800,860 C700,860 640,700 600,560" fill="none" stroke="{GO}" stroke-width="4" stroke-dasharray="4 12" pathLength="1" {a(draw="2.0,3.0")}/>')
    return {"id": "r03-thermal-solar", "folder": f"{F}/r03-thermal-solar", "note": NOTE, "scenes": [
        {"step": "Solar inspections", "title": "Faults you cannot see.", "voice": "A thermal drone can find faulty solar panels that look perfectly normal to the eye.", "svg": normal},
        {"step": "Thermal view", "title": "Hot spots stand out.", "voice": "In thermal, a damaged cell or a failed bypass diode shows up as a hot spot.", "svg": thermal},
        {"step": "Conditions matter", "title": "Strong, steady sunlight.", "voice": "Conditions matter. Inspect in strong, steady sun, at six hundred watts per square metre or more, as I E C guidance recommends.", "svg": sun},
        {"step": "Then", "title": "Map it, then check it.", "voice": "The drone maps each hot spot, and a technician confirms the cause on the ground.", "svg": confirm, "hold": 0.3}],
        "end": {"title": "Solar site to inspect?", "voice": "Got a solar site to inspect? Get in touch at aersynk dot io."}}


# ---------------- R04 Stockpile volumes ----------------
PILE = "M120,760 C240,700 300,420 470,330 C560,285 640,300 720,380 C820,480 880,690 960,760"


def r04():
    import random
    rnd = random.Random(4)
    pile = f'<path d="{PILE}" fill="{PANEL}" stroke="{INK}" stroke-width="5" pathLength="1" {a(draw="0.1,1.6")}/>'
    pts = []
    for i in range(140):
        x = rnd.uniform(140, 940)
        # rough height of curve: sample by simple shape
        import math
        y = 760 - 430 * math.exp(-((x - 560) / 230) ** 2) + rnd.uniform(-8, 8)
        t0 = 0.3 + i * 0.012
        pts.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="5" fill="{CY}" {a(inn=f"{t0:.2f},{t0 + 0.25:.2f}")}/>')
    surface = f'<path d="{PILE}" fill="{PANEL}" stroke="{LINE}" stroke-width="3"/>' + "".join(pts)
    base = (f'<path d="{PILE}" fill="{PANEL}" stroke="{CY}" stroke-width="4"/>'
            f'<line x1="120" y1="760" x2="960" y2="760" stroke="{GO}" stroke-width="7" stroke-linecap="round" pathLength="1" {a(draw="0.3,1.5")}/>'
            + f'<g {a(inn="1.4,2.0")}>' + label(540, 830, "Base surface", 38, GO) + '</g>')
    volume = (f'<path d="{PILE} Z" fill="{CY}" fill-opacity=".35" stroke="{CY}" stroke-width="4" {a(inn="0.2,1.4")}/>'
              f'<line x1="120" y1="760" x2="960" y2="760" stroke="{GO}" stroke-width="7"/>'
              + f'<g {a(inn="1.2,1.8")}>' + label(540, 600, "Volume", 64, INK, weight=800) + '</g>')
    bars = []
    for i, (lab, h) in enumerate([("Month 1", 300), ("Month 2", 360), ("Month 3", 250)]):
        x = 200 + i * 250
        t0 = 0.3 + i * 0.6
        bars.append(f'<path d="M{x},760 C{x + 40},{760 - h} {x + 140},{760 - h} {x + 180},760 Z" fill="{CY}" fill-opacity=".3" stroke="{CY}" stroke-width="4" {a(inn=f"{t0},{t0 + 0.5}", move=f"{t0},{t0 + 0.5},0,40")}/>'
                    + f'<g {a(inn=f"{t0 + 0.2},{t0 + 0.7}")}>' + label(x + 90, 820, lab, 32, MU) + '</g>')
    trend = "".join(bars) + f'<line x1="140" y1="760" x2="940" y2="760" stroke="{GO}" stroke-width="5"/>' + \
        f'<g {a(inn="2.0,2.6")}>' + label(540, 380, "Same base. Same method.", 44, INK, weight=700) + '</g>'
    return {"id": "r04-stockpile", "folder": f"{F}/r04-stockpile-volumes", "note": NOTE, "scenes": [
        {"step": "Stockpiles", "title": "How drones measure a pile.", "voice": "How does a drone measure a stockpile?", "svg": pile},
        {"step": "Step 1: Survey", "title": "The whole surface, measured.", "voice": "Overlapping photos become millions of 3D points across the whole surface, not just a few spot heights.", "svg": surface},
        {"step": "Step 2: Base", "title": "Define what it sits on.", "voice": "Next, define the base surface the pile sits on, and state it in the report.", "svg": base},
        {"step": "Step 3: Volume", "title": "Surface minus base.", "voice": "The volume is the space between the measured surface and that base.", "svg": volume},
        {"step": "Every month", "title": "Same method, every month.", "voice": "Use the same method every month, and the trend actually means something.", "svg": trend, "hold": 0.3}],
        "end": {"title": "Monthly volume surveys?", "voice": "Need monthly volume surveys? Get in touch at aersynk dot io."}}


# ---------------- R05 RTK myth ----------------
def target(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-40" y="-40" width="80" height="80" fill="{INK}"/>'
            f'<rect x="-40" y="-40" width="40" height="40" fill="#08131C"/><rect x="0" y="0" width="40" height="40" fill="#08131C"/></g>')


def r05():
    myth = (f'<g {a(inn="0,0.8")}>' + drone(540, 380, 2.2) + f'<line x1="540" y1="330" x2="540" y2="270" stroke="{INK}" stroke-width="5"/><circle cx="540" cy="262" r="10" fill="{GO}"/></g>'
            + f'<g {a(inn="0.6,1.2")}>' + label(540, 560, "RTK on board", 40, GO) + '</g>'
            + f'<g {a(inn="1.4,2.0")}><rect x="250" y="640" width="580" height="120" rx="20" fill="none" stroke="{SOS}" stroke-width="5"/>' + label(540, 718, "No ground control?", 48, SOS, weight=800) + '</g>')
    photos = []
    for i in range(12):
        x, y = 200 + (i % 4) * 190, 220 + (i // 4) * 190
        t0 = 0.2 + i * 0.12
        photos.append(f'<g {a(inn=f"{t0:.2f},{t0 + 0.3:.2f}")}><rect x="{x}" y="{y}" width="200" height="140" fill="{CY}" fill-opacity=".06" stroke="{CY}" stroke-width="2"/>'
                      f'<path d="M{x + 100},{y + 50} v40 M{x + 80},{y + 70} h40" stroke="{GO}" stroke-width="4"/></g>')
    rtk = "".join(photos) + f'<g {a(inn="1.8,2.4")}>' + label(540, 860, "Each photo position is more precise", 36, INK) + '</g>'
    check = (f'<rect x="120" y="160" width="840" height="620" rx="10" fill="#1E3424" stroke="{LINE}" stroke-width="2"/>'
             + f'<g {a(inn="0.3,0.8")}>' + target(300, 330) + '</g>' + f'<g {a(inn="0.6,1.1")}>' + target(780, 300) + '</g>'
             + f'<g {a(inn="0.9,1.4")}>' + target(560, 620) + '</g>'
             + f'<g {a(inn="1.4,2.0", move="1.4,2.0,0,-60")}><line x1="560" y1="620" x2="560" y2="420" stroke="{INK}" stroke-width="6"/><circle cx="560" cy="410" r="22" fill="{GO}"/></g>'
             + f'<g {a(inn="2.0,2.6")}>' + label(540, 860, "Independent check points, measured on site", 36, INK) + '</g>')
    lines = "".join(f'<line x1="380" y1="{320 + i * 70}" x2="{700 - (i % 2) * 120}" y2="{320 + i * 70}" stroke="{MU}" stroke-width="10" stroke-linecap="round"/>' for i in range(5))
    report = (f'<g {a(inn="0.2,0.8", move="0.2,0.8,0,40")}><rect x="320" y="180" width="440" height="600" rx="20" fill="{PANEL}" stroke="{CY}" stroke-width="4"/>'
              + label(540, 260, "Check point report", 36, INK, weight=700) + lines + '</g>'
              + f'<path d="M470,700 l40,44 l90,-110" fill="none" stroke="{CY}" stroke-width="14" stroke-linecap="round" stroke-linejoin="round" pathLength="1" {a(draw="1.2,1.9")}/>')
    return {"id": "r05-rtk-myth", "folder": f"{F}/r05-rtk-check-points", "note": NOTE, "scenes": [
        {"step": "Myth", "title": "“RTK means no ground control.”", "voice": "Myth: an R T K drone means you no longer need ground control.", "svg": myth},
        {"step": "What RTK does", "title": "Better photo positions.", "voice": "R T K improves the position of every photo the drone takes. That is a real step forward.", "svg": rtk},
        {"step": "What proves it", "title": "Check points prove accuracy.", "voice": "But independent check points, measured on the ground, are how you prove the final map is accurate.", "svg": check},
        {"step": "Tip", "title": "Ask for the report.", "voice": "So ask any survey supplier for their check point report.", "svg": report, "hold": 0.3}],
        "end": {"title": "Need a survey you can trust?", "voice": "Planning a survey? Get in touch at aersynk dot io."}}


# ---------------- R06 Orthomosaic, DSM, DTM ----------------
def profile(path, col, extra=""):
    return f'<path d="{path}" fill="none" stroke="{col}" stroke-width="6" stroke-linejoin="round" pathLength="1" {extra}/>'


DSM = "M80,700 L200,690 L230,560 L260,690 L330,680 L360,520 L400,500 L440,520 L470,680 L560,660 L600,600 L640,600 L660,650 L700,640 L740,560 L780,640 L1000,620"
DTM = "M80,700 C300,690 500,660 700,640 C820,630 900,625 1000,620"


def r06():
    three = (card(120, 140, 840, 180, "Orthomosaic", "A map you can measure on", CY, a(inn="0.2,0.7", move="0.2,0.7,0,30"))
             + card(120, 380, 840, 180, "DSM", "Height of everything on top", BL, a(inn="0.8,1.3", move="0.8,1.3,0,30"))
             + card(120, 620, 840, 180, "DTM", "Height of the bare ground", VI, a(inn="1.4,1.9", move="1.4,1.9,0,30")))
    tiles = "".join(f'<rect x="{140 + (i % 5) * 160}" y="{160 + (i // 5) * 150}" width="160" height="150" fill="{c}"/>'
                    for i, c in enumerate(["#2E4A35", "#3B5A3A", "#4D5B3A", "#5B5640", "#3E4E3D"] * 4))
    ortho = (f'<g {a(inn="0,0.8")}>{tiles}<path d="M140,640 C400,520 600,560 940,300" stroke="#9C8E74" stroke-width="28" fill="none"/></g>'
             f'<line x1="260" y1="300" x2="760" y2="560" stroke="{GO}" stroke-width="6" stroke-linecap="round" pathLength="1" {a(draw="1.0,1.8")}/>'
             + f'<g {a(inn="1.8,2.3")}>' + label(560, 410, "Distance", 40, GO, extra='transform="rotate(27 560 410)"') + '</g>')
    trees = ""
    for x in (230, 740):
        trees += f'<circle cx="{x}" cy="560" r="38" fill="#2E5A3A" stroke="#4F8A5A" stroke-width="3" {a(inn="0.3,0.9")}/>'
    dsm = (trees + f'<rect x="360" y="500" width="80" height="185" fill="{PANEL}" stroke="{MU}" stroke-width="3" {a(inn="0.3,0.9")}/>'
           + f'<rect x="590" y="600" width="70" height="55" rx="10" fill="{PANEL}" stroke="{MU}" stroke-width="3" {a(inn="0.3,0.9")}/>'
           + profile(DSM, BL, a(draw="0.8,2.2")) + f'<g {a(inn="2.0,2.6")}>' + label(540, 840, "Trees, buildings, vehicles included", 36, INK) + '</g>')
    loops = "".join(f'<ellipse cx="840" cy="300" rx="{30 + i * 28}" ry="{20 + i * 20}" fill="none" stroke="{VI}" stroke-width="3" {a(inn=f"{1.4 + i * 0.15:.2f},{1.8 + i * 0.15:.2f}")}/>' for i in range(5))
    contours = (f'<rect x="680" y="170" width="320" height="260" rx="14" fill="{PANEL}" stroke="{LINE}" stroke-width="2" {a(inn="1.2,1.6")}/>' + loops
                + f'<g {a(inn="1.6,2.0")}>' + label(840, 470, "Contours, top view", 28, MU) + '</g>')
    dtm = (profile(DSM, BL, 'stroke-opacity=".25"') + profile(DTM, VI, a(draw="0.2,1.4")) + contours
           + f'<g {a(inn="2.0,2.6")}>' + label(540, 840, "Contours are drawn from here", 36, INK) + '</g>')
    return {"id": "r06-ortho-dsm-dtm", "folder": f"{F}/r06-ortho-dsm-dtm", "note": NOTE, "scenes": [
        {"step": "Mapping outputs", "title": "Three outputs, three questions.", "voice": "Orthomosaic, D S M, D T M. Three drone mapping outputs that answer different questions.", "svg": three},
        {"step": "Orthomosaic", "title": "A map you can measure on.", "voice": "An orthomosaic is a map image to scale. You can measure distances and areas on it.", "svg": ortho},
        {"step": "DSM", "title": "Everything on top.", "voice": "A digital surface model records the height of everything on top: trees, buildings and vehicles.", "svg": dsm},
        {"step": "DTM", "title": "The bare ground.", "voice": "A digital terrain model is the bare ground, with those removed. Contours come from here.", "svg": dtm, "hold": 0.3}],
        "end": {"title": "Not sure which you need?", "voice": "Not sure which output you need? Ask us at aersynk dot io."}}


# ---------------- R07 NDVI ----------------
def field_rows(col="#3E6B47", extra=""):
    return f'<g {extra}>' + "".join(f'<line x1="140" y1="{200 + i * 40}" x2="940" y2="{200 + i * 40}" stroke="{col}" stroke-width="10" stroke-linecap="round"/>' for i in range(15)) + '</g>'


def r07():
    field = f'<rect x="120" y="180" width="840" height="600" rx="12" fill="#2A3B2C" {a(inn="0,0.6")}/>' + field_rows("#3E6B47", a(inn="0.3,1.2"))
    plant = (f'<g {a(inn="0,0.6")}><path d="M540,780 C540,640 540,560 540,480" stroke="#4F8A5A" stroke-width="10" fill="none"/>'
             f'<path d="M540,600 C460,560 420,500 430,450 C500,470 540,520 540,600" fill="#4F8A5A"/><path d="M540,560 C620,520 660,460 650,410 C580,430 540,480 540,560" fill="#4F8A5A"/></g>'
             f'<path d="M180,240 L470,500" stroke="{VI}" stroke-width="8" pathLength="1" {a(draw="0.6,1.2")}/><path d="M470,500 L200,780" stroke="{VI}" stroke-width="14" pathLength="1" {a(draw="1.2,1.8")}/>'
             + f'<g {a(inn="1.4,1.9")}>' + label(250, 840, "Near-infrared: strong", 32, VI, anchor="start") + '</g>'
             f'<path d="M900,240 L610,500" stroke="{SOS}" stroke-width="8" pathLength="1" {a(draw="1.8,2.4")}/><path d="M610,500 L880,780" stroke="{SOS}" stroke-width="3" pathLength="1" {a(draw="2.4,2.9")}/>'
             + f'<g {a(inn="2.6,3.1")}>' + label(830, 840, "Red: weak", 32, SOS, anchor="end") + '</g>')
    ndvi = (f'<defs><radialGradient id="stress" cx=".68" cy=".4" r=".3"><stop offset="0" stop-color="{AM}"/><stop offset=".6" stop-color="{GO}" stop-opacity=".6"/><stop offset="1" stop-color="#3FA060" stop-opacity="0"/></radialGradient></defs>'
            f'<rect x="120" y="180" width="840" height="600" rx="12" fill="#2F8A52"/>'
            f'<rect x="120" y="180" width="840" height="600" rx="12" fill="url(#stress)" {a(inn="0.4,1.6")}/>'
            + field_rows("#1F6A3A")
            + f'<g {a(inn="1.6,2.2")}>' + label(540, 860, "Low NDVI: stressed plants", 36, INK) + '</g>')
    check = (f'<rect x="120" y="180" width="840" height="600" rx="12" fill="#2F8A52"/><rect x="120" y="180" width="840" height="600" rx="12" fill="url(#stress2)"/>'
             f'<defs><radialGradient id="stress2" cx=".68" cy=".4" r=".3"><stop offset="0" stop-color="{AM}"/><stop offset=".6" stop-color="{GO}" stop-opacity=".6"/><stop offset="1" stop-color="#3FA060" stop-opacity="0"/></radialGradient></defs>'
             + field_rows("#1F6A3A")
             + f'<g {a(inn="0.2,0.8", move="0.2,0.8,0,-40")}>' + pin(690, 440, GO) + '</g>'
             + f'<path d="M180,760 C320,700 520,620 680,450" fill="none" stroke="{INK}" stroke-width="5" stroke-dasharray="4 12" pathLength="1" {a(draw="1.0,2.4")}/>'
             + f'<g {a(inn="2.4,3.0")}>' + label(540, 860, "Water? Nutrients? Pests? Disease?", 36, INK) + '</g>')
    return {"id": "r07-ndvi", "folder": f"{F}/r07-ndvi", "note": NOTE, "scenes": [
        {"step": "Crop maps", "title": "An NDVI map shows where to look.", "voice": "An N D V I map shows you where to look in a field.", "svg": field},
        {"step": "How it works", "title": "Near-infrared versus red.", "voice": "Healthy plants reflect lots of near-infrared light. N D V I compares it with red light.", "svg": plant},
        {"step": "What it shows", "title": "Low values flag stress.", "voice": "Low values highlight stressed areas across the whole block.", "svg": ndvi},
        {"step": "What it does not", "title": "Then check on the ground.", "voice": "But the cause could be water, nutrients, pests or disease, so the diagnosis still happens on the ground.", "svg": check, "hold": 0.3}],
        "end": {"title": "Want a crop map of your block?", "voice": "Want a crop map of your block? Get in touch at aersynk dot io."}}


# ---------------- R08 Thermal myth ----------------
def warm_person(x, y, s=1.0, extra=""):
    return (f'<g transform="translate({x},{y}) scale({s})" {extra}><ellipse cx="0" cy="-70" rx="26" ry="28" fill="{AM}"/>'
            f'<path d="M-40,-36 Q0,-50 40,-36 L46,40 L26,40 L22,110 L-22,110 L-26,40 L-46,40 Z" fill="{SOS}" fill-opacity=".85"/></g>')


def r08():
    myth = (f'<rect x="300" y="230" width="480" height="480" rx="20" fill="#3A3F4A" stroke="{MU}" stroke-width="4" {a(inn="0,0.6")}/>'
            + f'<g {a(inn="0.8,1.4")}><rect x="250" y="760" width="580" height="110" rx="20" fill="none" stroke="{SOS}" stroke-width="5"/>' + label(540, 832, "See through walls?", 46, SOS, weight=800) + '</g>')
    surface = (f'<rect x="120" y="160" width="840" height="640" rx="12" fill="#101A3A" {a(inn="0,0.5")}/>'
               + f'<g {a(inn="0.5,1.3")}>' + warm_person(540, 560, 1.8) + '</g>'
               + f'<g {a(inn="1.4,2.0")}>' + label(540, 860, "Warm surfaces glow", 36, INK) + '</g>')
    wall = (f'<rect x="120" y="160" width="840" height="640" rx="12" fill="#101A3A"/>'
            + warm_person(300, 560, 1.4) + f'<g {a(inn="0.3,0.9")}>' + label(300, 760, "Outside: visible", 32, INK) + '</g>'
            + f'<g {a(inn="0.9,1.5")}>' + person(760, 560, 1.4, MU, 'stroke-dasharray="6 10" opacity=".5"') + '</g>'
            + f'<rect x="600" y="300" width="320" height="400" fill="#2A2F3A" stroke="{MU}" stroke-width="4" {a(inn="1.3,1.9", move="1.3,1.9,0,-60")}/>'
            + f'<g {a(inn="1.9,2.5")}>' + label(760, 760, "Behind a wall: hidden", 32, INK) + '</g>')
    rain = "".join(f'<line x1="{140 + (i * 53) % 820}" y1="{180 + (i * 97) % 560}" x2="{120 + (i * 53) % 820}" y2="{230 + (i * 97) % 560}" stroke="{BL}" stroke-width="3" stroke-opacity=".7"/>' for i in range(60))
    weather = (f'<rect x="120" y="160" width="840" height="640" rx="12" fill="#101A3A"/>'
               + warm_person(540, 560, 1.6, a(out="0.6,2.2")) + f'<g {a(inn="0.2,1.0")}>{rain}</g>'
               + f'<rect x="120" y="160" width="840" height="640" rx="12" fill="#8FA3B5" {a(inn="0.8,2.4")} style="mix-blend-mode:normal" fill-opacity=".35"/>'
               + f'<g {a(inn="1.8,2.4")}>' + label(540, 860, "Rain, fog and humidity cut the range", 36, INK) + '</g>')
    return {"id": "r08-thermal-myth", "folder": f"{F}/r08-thermal-myth", "note": NOTE, "scenes": [
        {"step": "Myth", "title": "“Thermal sees through walls.”", "voice": "Myth: thermal cameras can see through walls.", "svg": myth},
        {"step": "What thermal sees", "title": "Surface heat.", "voice": "Thermal cameras show differences in surface temperature. People and vehicles stand out at night.", "svg": surface},
        {"step": "What it cannot", "title": "Walls, roofs and glass block it.", "voice": "But walls, roofs and glass block the view completely.", "svg": wall},
        {"step": "And weather", "title": "Weather cuts the range.", "voice": "Rain, fog and high humidity also reduce how far it can see clearly.", "svg": weather, "hold": 0.3}],
        "end": {"title": "Securing a site?", "voice": "Securing a large site? Talk to us at aersynk dot io."}}



# ---------------- R09 How a job runs ----------------
def r09():
    intro = (f'<g {a(inn="0,0.6")}>' + drone(540, 300, 2.4) + '</g>'
             + "".join(f'<g {a(inn=f"{0.6 + i * 0.25:.2f},{0.9 + i * 0.25:.2f}")}><circle cx="{240 + i * 200}" cy="620" r="52" fill="{PANEL}" stroke="{CY}" stroke-width="5"/>'
                       + label(240 + i * 200, 640, str(i + 1), 52, CY, weight=800) + '</g>' for i in range(4)))
    brief = (f'<g {a(inn="0,0.6", move="0,0.6,0,40")}><rect x="220" y="160" width="640" height="560" rx="22" fill="{PANEL}" stroke="{CY}" stroke-width="4"/>'
             + label(540, 250, "Job brief", 44, INK, weight=700) + '</g>'
             + "".join(f'<g {a(inn=f"{0.6 + i * 0.4:.1f},{0.9 + i * 0.4:.1f}")}>' + label(280, 350 + i * 110, t, 40, MU, anchor="start", weight=500) + '</g>'
                       for i, t in enumerate(["Site and location", "Preferred dates", "What you need delivered"])))
    checks = ["Aircraft", "Payload or sensor", "Operator certificate", "Approvals"]
    plan = "".join(f'<g {a(inn=f"{0.2 + i * 0.5:.1f},{0.5 + i * 0.5:.1f}")}><rect x="200" y="{160 + i * 150}" width="680" height="110" rx="18" fill="{PANEL}" stroke="{LINE}" stroke-width="2"/>'
                   + label(260, 228 + i * 150, t, 40, INK, anchor="start", weight=600)
                   + f'<path d="M790,{205 + i * 150} l18,20 l36,-44" fill="none" stroke="{CY}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/></g>'
                   for i, t in enumerate(checks))
    lines = "".join(f'<line x1="200" y1="{360 + i * 70}" x2="880" y2="{360 + i * 70}" stroke="{CY}" stroke-width="3" stroke-dasharray="6 10" pathLength="1" {a(draw=f"{0.3 + i * 0.3:.1f},{0.8 + i * 0.3:.1f}")}/>' for i in range(5))
    fly = (f'<rect x="160" y="320" width="760" height="400" rx="12" fill="#1E3424" stroke="{LINE}" stroke-width="2"/>' + lines
           + f'<g {a(move="0,2.4,-500,0")}>' + drone(700, 250, 1.6) + '</g>'
           + f'<g {a(inn="1.8,2.4")}>' + label(540, 800, "Checks before and after the flight", 36, INK) + '</g>')
    files = ""
    for i, (t, c) in enumerate([("Map", CY), ("Model", BL), ("Report", GO)]):
        x = 170 + i * 260
        files += (f'<g {a(inn=f"{0.3 + i * 0.5:.1f},{0.8 + i * 0.5:.1f}", move=f"{0.3 + i * 0.5:.1f},{0.8 + i * 0.5:.1f},0,50")}>'
                  f'<path d="M{x},220 h160 l60,60 v300 h-220 z" fill="{PANEL}" stroke="{c}" stroke-width="4"/>' + label(x + 110, 450, t, 40, INK, weight=700) + '</g>')
    deliver = files + f'<g {a(inn="1.9,2.5")}>' + label(540, 720, "In the format you asked for", 38, INK) + '</g>'
    return {"id": "r09-how-a-job-runs", "folder": f"{F}/r09-how-a-job-runs", "note": NOTE, "scenes": [
        {"step": "Pilot for hire", "title": "How a drone job runs.", "voice": "Need drone work done? Here is how a job runs with AerSynk, in four steps.", "svg": intro},
        {"step": "Step 1: Brief", "title": "You tell us the job.", "voice": "First, the brief. You share the site, the dates and what you need delivered.", "svg": brief},
        {"step": "Step 2: Plan", "title": "We plan it properly.", "voice": "Then we confirm the aircraft, the payload, the operator certificate and any approvals.", "svg": plan},
        {"step": "Step 3: Fly", "title": "We fly it.", "voice": "The flight is carried out on site, with checks before and after.", "svg": fly},
        {"step": "Step 4: Deliver", "title": "You get the results.", "voice": "And you receive the data, or the processed results, in the format you asked for.", "svg": deliver, "hold": 0.3}],
        "end": {"title": "Need a drone pilot?", "voice": "Need a drone pilot? Request one at aersynk dot io."}}


# ---------------- R10 Drone docks ----------------
def dock(x, y, s=1.0, open_=False):
    lid = f'<path d="M{-150},{-10} L{-150},{-120} L0,{-160}" fill="none" stroke="{INK}" stroke-width="6"/>' if open_ else f'<rect x="-150" y="-40" width="300" height="34" rx="8" fill="{PANEL}" stroke="{INK}" stroke-width="5"/>'
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-150" y="-10" width="300" height="160" rx="16" fill="{PANEL}" stroke="{INK}" stroke-width="5"/>'
            f'{lid}<rect x="-120" y="40" width="240" height="20" rx="6" fill="{CY}" fill-opacity=".4"/></g>')


def r10():
    box = f'<g {a(inn="0,0.6", move="0,0.6,0,40")}>' + dock(540, 520, 1.6) + '</g>' + f'<g {a(inn="0.8,1.4")}>' + label(540, 860, "A weatherproof box for a drone", 36, INK) + '</g>'
    what = (dock(540, 600, 1.3, True) + f'<g {a(move="0.3,1.8,0,300")}>' + drone(540, 300, 1.6) + '</g>'
            + "".join(f'<g {a(inn=f"{1.0 + i * 0.4:.1f},{1.4 + i * 0.4:.1f}")}>' + label(x, 900, t, 38, CY, weight=700) + '</g>'
                      for i, (x, t) in enumerate([(260, "Houses"), (540, "Charges"), (820, "Launches")])))
    clock = (f'<g {a(inn="0,0.6")}><circle cx="300" cy="400" r="150" fill="{PANEL}" stroke="{CY}" stroke-width="6"/>'
             f'<line x1="300" y1="400" x2="300" y2="300" stroke="{INK}" stroke-width="8" stroke-linecap="round"/><line x1="300" y1="400" x2="370" y2="440" stroke="{INK}" stroke-width="8" stroke-linecap="round"/></g>'
             + f'<g {a(inn="0.8,1.4")}>' + label(300, 640, "On a schedule", 38, INK) + '</g>'
             + f'<g {a(inn="1.2,1.8")}><circle cx="780" cy="400" r="150" fill="{PANEL}" stroke="{GO}" stroke-width="6"/>' + label(780, 425, "Now", 64, GO, weight=800) + '</g>'
             + f'<g {a(inn="1.6,2.2")}>' + label(780, 640, "Or on demand", 38, INK) + '</g>')
    cloud = (dock(260, 640, 0.9) + f'<path d="M640,380 a90,90 0 0 1 170,-30 a70,70 0 0 1 90,90 h-260 a60,60 0 0 1 0,-60 z" fill="{PANEL}" stroke="{CY}" stroke-width="5" {a(inn="0.2,0.8")}/>'
             + f'<path d="M330,560 C420,420 560,420 660,440" fill="none" stroke="{CY}" stroke-width="5" stroke-dasharray="6 12" pathLength="1" {a(draw="0.8,1.8")}/>'
             + f'<g {a(inn="1.8,2.4")}>' + label(540, 860, "Data uploads to a cloud platform", 36, INK) + '</g>')
    rules = (dock(300, 600, 0.9) + f'<g {a(inn="0.4,1.0")}>' + person(780, 560, 1.4, CY) + '</g>'
             + f'<g {a(inn="1.0,1.6")}><rect x="560" y="740" width="440" height="100" rx="18" fill="{PANEL}" stroke="{GO}" stroke-width="4"/>'
             + label(780, 803, "Approved operator", 38, GO, weight=700) + '</g>'
             + f'<g {a(inn="1.8,2.4")}>' + label(540, 920, "The dock does not remove the rules", 36, INK) + '</g>')
    return {"id": "r10-drone-docks", "folder": f"{F}/r10-drone-docks", "note": NOTE, "scenes": [
        {"step": "Enterprise drones", "title": "What does a drone dock do?", "voice": "What does a drone dock actually do?", "svg": box},
        {"step": "The dock", "title": "Houses, charges, launches.", "voice": "It is a weatherproof box that houses the drone, charges it, and launches it.", "svg": what},
        {"step": "Missions", "title": "Scheduled or on demand.", "voice": "Missions can run on a schedule, like a daily site check, or on demand.", "svg": clock},
        {"step": "Data", "title": "Data goes straight up.", "voice": "The data uploads automatically to a cloud platform.", "svg": cloud},
        {"step": "The rules", "title": "People still run it.", "voice": "But remote operations still need an approved operator and a responsible remote pilot.", "svg": rules, "hold": 0.3}],
        "end": {"title": "Thinking about docks?", "voice": "Thinking about drone docks? Ask us at aersynk dot io."}}

# ---------------- R11 AerSynk Survey (plan item 17) ----------------
def layer(y, col, name, extra=""):
    return (f'<g {extra}><polygon points="540,{y} 900,{y + 90} 540,{y + 180} 180,{y + 90}" fill="{PANEL}" fill-opacity=".92" stroke="{col}" stroke-width="4"/>'
            + label(540, y + 102, name, 34, col, weight=700) + '</g>')


SENSORS = [("Photos", CY), ("LiDAR", BL), ("Magnetics", VI), ("Spectral", GO)]


def r11():
    sensors = (f'<g {a(inn="0,0.6")}>' + drone(540, 170, 2.0) + '</g>'
               + "".join(f'<g {a(inn=f"{0.6 + i * 0.35:.2f},{1.0 + i * 0.35:.2f}", move=f"{0.6 + i * 0.35:.2f},{1.0 + i * 0.35:.2f},0,40")}>'
                         f'<rect x="{100 + (i % 2) * 460}" y="{380 + (i // 2) * 200}" width="420" height="150" rx="20" fill="{PANEL}" stroke="{c}" stroke-width="4"/>'
                         + label(310 + (i % 2) * 460, 470 + (i // 2) * 200, t, 46, c, weight=700) + '</g>' for i, (t, c) in enumerate(SENSORS)))
    boxes = ""
    for i, (t, c) in enumerate(SENSORS):
        x, y = 110 + (i % 2) * 560, 140 + (i // 2) * 300
        boxes += (f'<g {a(inn=f"{0.2 + i * 0.3:.1f},{0.6 + i * 0.3:.1f}")}><rect x="{x}" y="{y}" width="300" height="200" rx="16" fill="{PANEL}" stroke="{c}" stroke-width="4"/>'
                  + label(x + 150, y + 90, t, 40, c, weight=700) + label(x + 150, y + 145, "Separate tool", 28, MU, weight=500) + '</g>')
    manual = boxes + f'<g {a(inn="1.6,2.2")}>' + person(540, 470, 1.2, AM) + '</g>' + "".join(
        f'<line x1="540" y1="420" x2="{x}" y2="{y}" stroke="{AM}" stroke-width="3" stroke-dasharray="6 10" pathLength="1" {a(draw="1.8,2.6")}/>'
        for x, y in [(410, 290), (670, 290), (410, 590), (670, 590)]) + f'<g {a(inn="2.4,3.0")}>' + label(540, 820, "Lined up by hand", 40, INK) + '</g>'
    stack = "".join(layer(560 - i * 130, c, t, a(inn=f"{0.2 + i * 0.35:.2f},{0.6 + i * 0.35:.2f}", move=f"{0.2 + i * 0.35:.2f},{0.6 + i * 0.35:.2f},0,-60"))
                    for i, (t, c) in enumerate(reversed(SENSORS))) + f'<g {a(inn="1.8,2.4")}>' + label(540, 880, "Every sensor on the same map", 40, INK) + '</g>'
    steps = [("Plan", CY), ("Fly", BL), ("Process", VI), ("Deliver", GO)]
    flow = "".join(f'<g {a(inn=f"{0.2 + i * 0.45:.2f},{0.6 + i * 0.45:.2f}")}><rect x="240" y="{120 + i * 170}" width="600" height="120" rx="20" fill="{PANEL}" stroke="{c}" stroke-width="4"/>'
                   + label(540, 197 + i * 170, t, 48, c, weight=700) + '</g>' for i, (t, c) in enumerate(steps))
    flow += "".join(f'<path d="M540,{240 + i * 170} v40" stroke="{MU}" stroke-width="4" {a(inn=f"{0.5 + i * 0.45:.2f},{0.8 + i * 0.45:.2f}")}/>' for i in range(3))
    proto = (layer(300, BL, "Demo data") + f'<g {a(inn="0.6,1.2")}><rect x="250" y="620" width="580" height="110" rx="55" fill="{PANEL}" stroke="{GO}" stroke-width="4"/>'
             + label(540, 690, "Working prototype", 44, GO, weight=700) + '</g>'
             + f'<g {a(inn="1.4,2.0")}>' + label(540, 830, "Real-data processing: one sensor at a time", 34, INK) + '</g>')
    return {"id": "r11-aersynk-survey", "folder": f"{F}/r11-aersynk-survey-uk", "note": NOTE + " Prototype shown on demo data.", "scenes": [
        {"step": "What we are building", "title": "One survey, many sensors.", "voice": "One drone survey can mean photos, LiDAR, magnetic data and spectral data.", "svg": sensors},
        {"step": "The problem", "title": "Four tools. One analyst.", "voice": "Usually each one lives in separate software, and someone lines them all up by hand.", "svg": manual},
        {"step": "AerSynk Survey", "title": "Every sensor, one map.", "voice": "AerSynk Survey puts every flight and every sensor on the same map.", "svg": stack},
        {"step": "One workspace", "title": "From plan to deliverable.", "voice": "From planning the flights to the finished deliverable, in one workspace.", "svg": flow},
        {"step": "Where it stands", "title": "A working prototype.", "voice": "Today it is a working prototype on demo data, and we are adding real-data processing one sensor at a time.", "svg": proto, "hold": 0.3}],
        "end": {"title": "Survey or exploration team?", "line": "aersynk.io", "sub": "Request early access",
                "voice": "Survey or exploration team? Request early access at aersynk dot io."}}


# ---------------- R12 AerSynk Rescue (plan item 24) ----------------
MOUNTAIN = "M60,900 L60,520 L180,470 L330,430 L760,420 L880,450 L1020,520 L1020,900 Z"


def phone(x, y, s=1.0, extra=""):
    return (f'<g transform="translate({x},{y}) scale({s})" {extra}><rect x="-90" y="-170" width="180" height="340" rx="26" fill="{PANEL}" stroke="{INK}" stroke-width="5"/>'
            f'<circle cx="0" cy="0" r="58" fill="{SOS}" fill-opacity=".85" stroke="{SOS}" stroke-width="4"/>' + label(0, 14, "SOS", 40, INK, weight=800) + '</g>')


def r12():
    mtn = f'<path d="{MOUNTAIN}" fill="#14283A" stroke="{BL}" stroke-width="4"/>'
    hiker = (f'<g {a(inn="0,0.8")}>' + mtn + '</g>' + f'<g {a(inn="0.8,1.4")}>' + person(700, 400, 0.9, AM) + '</g>'
             + f'<g {a(inn="1.4,2.0")}>' + label(540, 970, "Somewhere on the mountain", 36, INK) + '</g>')
    sos = (f'<g {a(grow="0.2,0.9")} {GROW}>' + phone(540, 470, 1.6) + '</g>'
           + "".join(f'<circle cx="540" cy="470" r="{140 + i * 70}" fill="none" stroke="{SOS}" stroke-width="4" {a(inn=f"{1.0 + i * 0.3:.1f},{1.3 + i * 0.3:.1f}")}/>' for i in range(3))
           + f'<g {a(inn="1.8,2.4")}>' + label(540, 920, "One press starts the rescue", 38, INK) + '</g>')
    fly = (mtn + dock(220, 760, 0.6) + person(800, 400, 0.7, AM)
           + f'<circle cx="800" cy="300" r="40" fill="none" stroke="{SOS}" stroke-width="4" {a(inn="0.2,0.6")}/>'
           + f'<path d="M220,700 C360,400 540,250 660,240" fill="none" stroke="{CY}" stroke-width="4" stroke-dasharray="6 12" pathLength="1" {a(draw="0.4,2.2")}/>'
           + f'<g {a(move="0.4,2.4,-460,440")}>' + drone(680, 230, 1.3) + '</g>')
    team = (mtn + person(800, 400, 0.7, AM) + drone(660, 200, 1.3)
            + f'<g {a(inn="0.4,1.0")}>' + pin(800, 300, GO) + '</g>'
            + f'<g {a(inn="1.0,1.6")}><rect x="140" y="80" width="420" height="110" rx="18" fill="{PANEL}" stroke="{GO}" stroke-width="4"/>'
            + label(350, 148, "Rescue team", 42, GO, weight=700) + '</g>'
            + f'<g {a(inn="1.6,2.2")}>' + person(250, 740, 0.8, INK) + person(360, 740, 0.8, INK) + '</g>')
    status = (f'<g {a(inn="0,0.6")}><rect x="170" y="240" width="740" height="150" rx="75" fill="{PANEL}" stroke="{GO}" stroke-width="5"/>'
              + label(540, 335, "In development", 60, GO, weight=800) + '</g>'
              + f'<g {a(inn="0.8,1.4")}>' + label(540, 520, "Not live yet.", 52, INK, weight=700) + '</g>'
              + f'<g {a(inn="1.4,2.0")}>' + label(540, 640, "In an emergency, call the", 36, MU, weight=500)
              + label(540, 690, "official rescue services.", 36, MU, weight=500) + '</g>')
    return {"id": "r12-aersynk-rescue", "folder": f"{F}/r12-aersynk-rescue-uk", "note": "Concept animation. AerSynk Rescue is in development, not live. Voice is computer-generated.", "scenes": [
        {"step": "What we are building", "title": "A hiker needs help.", "voice": "Picture a hiker who needs help, somewhere on Table Mountain.", "svg": hiker},
        {"step": "AerSynk Rescue", "title": "One SOS press.", "voice": "The idea behind AerSynk Rescue: one press of an SOS button starts the whole rescue.", "svg": sos},
        {"step": "The concept", "title": "A drone launches from its dock.", "voice": "A drone launches from its dock and flies toward the signal.", "svg": fly},
        {"step": "The aim", "title": "Help the team find them.", "voice": "The aim is to help the rescue team locate the hiker.", "svg": team},
        {"step": "Where it stands", "title": "Not live yet.", "voice": "AerSynk Rescue is in development and not live yet. In an emergency, always call the official rescue services.", "svg": status, "hold": 0.3}],
        "end": {"title": "Rescue organisation, guide or park?", "line": "aersynk.io", "sub": "Register as a partner",
                "voice": "Rescue organisation, guide or park? Register as a partner at aersynk dot io."}}


REELS = {"r02": r02, "r03": r03, "r04": r04, "r05": r05, "r06": r06, "r07": r07, "r08": r08, "r09": r09, "r10": r10,
         "r11": r11, "r12": r12}

if __name__ == "__main__":
    keys = sys.argv[1:] or list(REELS)
    for k in keys:
        res = build(REELS[k]())
        print(k, res)
