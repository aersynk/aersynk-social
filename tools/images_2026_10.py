"""Image posts for 19 Oct to 1 Nov 2026 (carousels and single images). Run: python3 tools/images_2026_10.py"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from kit import page, top, foot  # noqa: E402
from art import drone, label, grid, panels, person, pin, card, CY, BL, VI, AM, GO, SOS, INK, MU, LINE, PANEL  # noqa: E402
from reels_2026_10 import DSM, DTM, profile, target, field_rows  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "posts" / "2026-10"


def svg(inner, vb="0 0 1080 1000"):
    return f'<svg viewBox="{vb}" xmlns="http://www.w3.org/2000/svg" style="font-family:Instrument Sans">{inner}</svg>'


def write(folder, name, html):
    d = OUT / folder
    d.mkdir(parents=True, exist_ok=True)
    html = html.replace('href="../templates', 'href="../../../templates').replace('src="../brand', 'src="../../../brand')
    p = d / f"{name}.html"
    p.write_text(html)
    return p


def slide(folder, n, total, kicker, title, body, art, seed, size="", foot_right="", vb="0 0 1080 1000"):
    cnt = f"{n}/{total}" if total > 1 else None
    h1 = f'<h1 class="{size}">{title}</h1>'
    b = f'<p class="body">{body}</p>' if body else ""
    return write(folder, f"slide-{n}" if total > 1 else "image", page(
        top(cnt) + f'<p class="kicker">{kicker}</p>' + h1 + b + f'<div class="art">{svg(art, vb)}</div>' + foot("aersynk.io", foot_right), seed=seed))


def cta_slide(folder, n, total, title, body, seed):
    return write(folder, f"slide-{n}", page(
        top(f"{n}/{total}") + '<p class="kicker">Work with us</p>' + f'<h1 class="l">{title}</h1>' + f'<p class="body">{body}</p>'
        + '<div style="flex:1"></div><div style="position:relative;z-index:2;display:grid;gap:26px;margin-bottom:60px">'
          '<div><p class="small">Website</p><p class="cta-line">aersynk.io</p></div>'
          '<div><p class="small">WhatsApp or call</p><p class="cta-line">073 290 4298</p></div></div>'
        + foot("Follow for more", ""), seed=seed))


TILES = "".join(f'<rect x="{140 + (i % 5) * 160}" y="{160 + (i // 5) * 150}" width="160" height="150" fill="{c}"/>'
                for i, c in enumerate(["#2E4A35", "#3B5A3A", "#4D5B3A", "#5B5640", "#3E4E3D"] * 4))


def post07():
    f, T = "07-ortho-dsm-dtm", 5
    out = [slide(f, 1, T, "Mapping outputs", "Orthomosaic, DSM, DTM: which do you need?", "Four drone mapping outputs, four different questions.",
                 card(120, 140, 840, 180, "Orthomosaic", "A map you can measure on", CY) + card(120, 380, 840, 180, "DSM", "Height of everything on top", BL)
                 + card(120, 620, 840, 180, "DTM", "Height of the bare ground", VI), 31, vb="100 120 880 700")]
    out.append(slide(f, 2, T, "Orthomosaic", "A map image you can measure on.", "Scale-correct, so distances and areas measured on it are real.",
                     TILES + '<path d="M140,640 C400,520 600,560 940,300" stroke="#9C8E74" stroke-width="28" fill="none"/>'
                     f'<line x1="260" y1="300" x2="760" y2="560" stroke="{GO}" stroke-width="6" stroke-linecap="round"/>', 33, vb="120 140 840 640"))
    trees = "".join(f'<circle cx="{x}" cy="560" r="38" fill="#2E5A3A" stroke="#4F8A5A" stroke-width="3"/>' for x in (230, 740))
    out.append(slide(f, 3, T, "DSM: digital surface model", "The height of everything on top.", "Trees, buildings and vehicles are all included.",
                     trees + f'<rect x="360" y="500" width="80" height="185" fill="{PANEL}" stroke="{MU}" stroke-width="3"/>'
                     f'<rect x="590" y="600" width="70" height="55" rx="10" fill="{PANEL}" stroke="{MU}" stroke-width="3"/>' + profile(DSM, BL), 35, vb="60 440 960 300"))
    loops = "".join(f'<ellipse cx="840" cy="300" rx="{30 + i * 28}" ry="{20 + i * 20}" fill="none" stroke="{VI}" stroke-width="3"/>' for i in range(5))
    out.append(slide(f, 4, T, "DTM: digital terrain model", "The bare ground.", "Trees and buildings removed. Contours are usually drawn from the DTM.",
                     profile(DSM, BL, 'stroke-opacity=".25"') + profile(DTM, VI) + f'<rect x="680" y="170" width="320" height="260" rx="14" fill="{PANEL}" stroke="{LINE}" stroke-width="2"/>' + loops
                     + label(840, 470, "Contours, top view", 28, MU), 37, vb="60 150 960 600"))
    out.append(cta_slide(f, 5, T, "Start from the question.", "Then pick the output. Not sure which one fits your project? Send us a message.", 39))
    return out


ARR = (130, 230)


def hot_panels():
    x0, y0 = ARR
    return panels(x0, y0, 6, 5, 120, 80, 18, "#162A6B", "#3A4FA0") + f'<rect x="{x0 + 3 * 138}" y="{y0 + 2 * 98}" width="120" height="80" rx="4" fill="{AM}"/>'


def sun_art():
    rays = "".join(f'<line x1="{540 + 150 * c}" y1="{330 + 150 * s}" x2="{540 + 200 * c}" y2="{330 + 200 * s}" stroke="{GO}" stroke-width="6" stroke-linecap="round"/>'
                   for c, s in [(1, 0), (-1, 0), (0, 1), (0, -1), (.707, .707), (-.707, .707), (.707, -.707), (-.707, -.707)])
    return f'<circle cx="540" cy="330" r="110" fill="{GO}" fill-opacity=".25" stroke="{GO}" stroke-width="5"/>' + rays + label(540, 680, "600 W/m² or more", 64, INK, weight=800)


def post08():
    f, T = "08-thermal-solar", 5
    x0, y0 = ARR
    out = [slide(f, 1, T, "Solar inspections", "Faulty panels can look perfectly normal.", "A thermal drone flight shows what the eye misses.",
                 hot_panels() + f'<circle cx="{x0 + 3 * 138 + 60}" cy="{y0 + 2 * 98 + 40}" r="70" fill="none" stroke="{SOS}" stroke-width="5"/>', 41, vb="100 180 880 520")]
    out.append(slide(f, 2, T, "What a hot spot can mean", "Damaged cells, failed diodes, heavy soiling.", "A hot spot tells you where to look. It does not tell you which fault it is.",
                     hot_panels(), 43, vb="100 180 880 520"))
    out.append(slide(f, 3, T, "Conditions matter", "Strong, steady sunlight.", "Guidance for thermal inspection of PV plants (IEC TS 62446-3) calls for irradiance of at least 600 W/m².",
                     sun_art(), 45, vb="140 80 800 680"))
    out.append(slide(f, 4, T, "Then", "Map it, then check it on the ground.", "The drone finds and maps each anomaly. A technician confirms the cause.",
                     hot_panels() + pin(x0 + 3 * 138 + 60, y0 + 2 * 98 + 30, GO) + person(870, 820, 1.1)
                     + f'<path d="M800,860 C700,860 640,700 600,560" fill="none" stroke="{GO}" stroke-width="4" stroke-dasharray="4 12"/>', 47, vb="100 140 880 800"))
    out.append(cta_slide(f, 5, T, "Solar site to inspect?", "Request a pilot at aersynk.io. Flights run under an approved partner operator's certificate.", 49))
    return out


STRESS = (f'<defs><radialGradient id="st" cx=".68" cy=".4" r=".3"><stop offset="0" stop-color="{AM}"/><stop offset=".6" stop-color="{GO}" stop-opacity=".6"/>'
          f'<stop offset="1" stop-color="#3FA060" stop-opacity="0"/></radialGradient></defs><rect x="120" y="180" width="840" height="600" rx="12" fill="#2F8A52"/>'
          '<rect x="120" y="180" width="840" height="600" rx="12" fill="url(#st)"/>')


def post14():
    f, T = "14-ndvi", 5
    out = [slide(f, 1, T, "Crop maps", "What an NDVI map can, and cannot, tell you.", "", STRESS + field_rows("#1F6A3A"), 51, vb="100 160 880 640")]
    plant = (f'<path d="M540,780 C540,640 540,560 540,480" stroke="#4F8A5A" stroke-width="10" fill="none"/>'
             f'<path d="M540,600 C460,560 420,500 430,450 C500,470 540,520 540,600" fill="#4F8A5A"/><path d="M540,560 C620,520 660,460 650,410 C580,430 540,480 540,560" fill="#4F8A5A"/>'
             f'<path d="M180,240 L470,500 L200,780" stroke="{VI}" stroke-width="12" fill="none"/>' + label(250, 840, "Near-infrared: strong", 32, VI, anchor="start")
             + f'<path d="M900,240 L610,500" stroke="{SOS}" stroke-width="8"/><path d="M610,500 L880,780" stroke="{SOS}" stroke-width="3"/>' + label(830, 840, "Red: weak", 32, SOS, anchor="end"))
    out.append(slide(f, 2, T, "How it works", "Healthy plants reflect near-infrared.", "NDVI compares near-infrared with red light to show differences in plant vigour.", plant, 53, vb="120 200 840 680"))
    out.append(slide(f, 3, T, "What it shows", "Low values flag stressed areas.", "Across the whole block, not just the rows you walked.", STRESS + field_rows("#1F6A3A"), 55, vb="100 160 880 640"))
    out.append(slide(f, 4, T, "What it cannot show", "The cause.", "Water, nutrients, pests or disease. The map shows where to look; the diagnosis happens on the ground.",
                     STRESS + field_rows("#1F6A3A") + pin(690, 440, GO) + f'<path d="M180,760 C320,700 520,620 680,450" fill="none" stroke="{INK}" stroke-width="5" stroke-dasharray="4 12"/>', 57, vb="100 160 880 640"))
    out.append(cta_slide(f, 5, T, "Want a crop map of your block?", "Send us a message about the crop, the hectares and what you want to find out.", 59))
    return out


def post13():
    steps = [("Brief", "Site, dates, needs"), ("Plan", "Kit and approvals"), ("Fly", "With checks"), ("Deliver", "In your format")]
    art = ""
    for i, (t, s) in enumerate(steps):
        x, y = 100 + (i % 2) * 480, 100 + (i // 2) * 250
        art += (f'<circle cx="{x + 60}" cy="{y + 60}" r="58" fill="{PANEL}" stroke="{CY}" stroke-width="5"/>' + label(x + 60, y + 80, str(i + 1), 56, CY, weight=800)
                + label(x + 140, y + 52, t, 56, INK, anchor="start", weight=700) + label(x + 140, y + 104, s, 36, MU, anchor="start", weight=500))
    p = write("13-pilot-for-hire", "image", page(
        top() + '<p class="kicker">Pilot for hire</p><h1>Need a drone pilot for a job?</h1>'
        + '<div class="tags"><span>Agriculture</span><span>Mapping and surveying</span><span>Security</span><span>Inspection</span><span>Filming</span></div>'
        + f'<div class="art">{svg(art, "80 80 960 500")}</div>'
        + '<p class="small" style="position:relative;z-index:2;margin-bottom:22px">A BVLOS-certified remote pilot. Flights run under an approved partner operator\'s certificate, confirmed with you before booking.</p>'
        + foot("aersynk.io", "WhatsApp 073 290 4298"), seed=61))
    return [p]


def doc(x, y, w, h, big, small, col, extra=""):
    return (f'<g {extra}><path d="M{x},{y} h{w - 60} l60,60 v{h - 60} h-{w} z" fill="{PANEL}" stroke="{col}" stroke-width="4"/>'
            + label(x + w / 2, y + h / 2 + 10, big, 84, col, weight=800) + label(x + w / 2, y + h / 2 + 70, small, 30, MU, weight=500) + '</g>')


def post15():
    f, T = "15-roc-when-you-hire", 5
    out = [slide(f, 1, T, "Rules and safety", "Hiring a drone service in SA? Ask for these two things.",
                 "Two documents show a commercial drone job is set up properly.",
                 doc(120, 140, 380, 480, "ROC", "The operator", CY) + doc(580, 140, 380, 480, "RPL", "The pilot", GO), 71, size="m", vb="100 120 880 520")]
    building = (f'<rect x="200" y="300" width="300" height="420" rx="8" fill="{PANEL}" stroke="{INK}" stroke-width="4"/>'
                + "".join(f'<rect x="{240 + c * 80}" y="{350 + r * 90}" width="50" height="50" fill="none" stroke="{MU}" stroke-width="3"/>' for r in range(4) for c in range(3)))
    out.append(slide(f, 2, T, "1. The operator", "The ROC.",
                     "An RPAS Operator Certificate, issued by SACAA under Part 101. It covers the organisation that runs the flight.",
                     building + doc(580, 260, 320, 440, "ROC", "Operator", CY), 73, vb="160 240 780 500"))
    card_ = (f'<rect x="520" y="380" width="420" height="260" rx="22" fill="{PANEL}" stroke="{GO}" stroke-width="4"/>'
             + label(730, 490, "RPL", 84, GO, weight=800) + label(730, 560, "Remote Pilot Licence", 30, MU, weight=500))
    out.append(slide(f, 3, T, "2. The pilot", "The pilot's licence.",
                     "A Remote Pilot Licence (RPL) for the person at the controls, rated for the aircraft and the type of flight.",
                     person(320, 560, 2.0, INK) + card_, 75, vb="160 300 820 420"))
    link = (doc(120, 160, 340, 440, "ROC", "Partner operator", CY)
            + f'<path d="M480,380 h120" stroke="{MU}" stroke-width="6" stroke-dasharray="10 10"/>'
            + f'<rect x="620" y="250" width="340" height="260" rx="22" fill="{PANEL}" stroke="{GO}" stroke-width="4"/>'
            + label(790, 360, "Our pilot", 50, GO, weight=800) + label(790, 420, "BVLOS-certified", 30, MU, weight=500))
    out.append(slide(f, 4, T, "How AerSynk works", "Our flights run under a partner's ROC.",
                     "AerSynk does not hold its own ROC. Our BVLOS-certified remote pilot flies under an approved partner operator's certificate, and we confirm the details with you before booking.",
                     link, 77, size="m", vb="100 140 880 480"))
    out.append(cta_slide(f, 5, T, "Questions about the rules?", "Send us a message. General information, not legal advice: check current requirements with SACAA.", 79))
    return out


def li05():
    art = (f'<rect x="120" y="160" width="840" height="620" rx="10" fill="#1E3424" stroke="{LINE}" stroke-width="2"/>'
           + target(300, 330) + target(780, 300) + target(560, 620)
           + f'<line x1="560" y1="620" x2="560" y2="420" stroke="{INK}" stroke-width="6"/><circle cx="560" cy="410" r="22" fill="{GO}"/>'
           + label(540, 860, "Independent check points, measured on site", 36, INK))
    return [slide("05-linkedin-rtk", 1, 1, "Myth vs fact", "RTK drones still need independent check points.",
                  "RTK improves every photo position. Check points not used in processing are how you prove the map's accuracy.", art, 63, size="m", vb="100 140 880 760")]


def li09():
    art = sun_art() + f'<g transform="translate(0,40)">{panels(250, 720, 5, 2, 100, 60, 16, "#162A6B", "#3A4FA0")}</g>'
    return [slide("09-linkedin-solar-pv", 1, 1, "Solar PV thermography", "Thermal inspection only works in the right conditions.",
                  "IEC TS 62446-3 guidance calls for strong, stable sunlight of at least 600 W/m². Inspect in poor light and faults can hide.", art, 65, size="m", vb="140 80 800 820")]


def li12():
    def col(x, title, items, c):
        s = f'<rect x="{x}" y="60" width="440" height="700" rx="20" fill="{PANEL}" stroke="{c}" stroke-width="3"/>' + label(x + 220, 150, title, 52, c, weight=800)
        for i, it in enumerate(items):
            s += label(x + 34, 270 + i * 110, it, 38, INK, anchor="start", weight=500)
        return s
    art = (col(80, "In-house", ["Frequent flights", "Routine, repeat work", "Team to run it", "Budget for kit"], CY)
           + col(560, "Hire a pilot", ["Occasional flights", "Specialist sensors", "No admin burden", "Pay per job"], GO)
           + label(540, 850, "Count it all: training, licensing, insurance,", 36, MU) + label(540, 900, "software, maintenance and time.", 36, MU))
    return [slide("12-linkedin-inhouse-or-hire", 1, 1, "Business value", "In-house drone team, or hire a pilot?",
                  "The kit is the smallest part of the cost.", art, 67, size="m", vb="60 40 960 900")]


if __name__ == "__main__":
    sel = sys.argv[1:]
    fns = {"07": post07, "08": post08, "13": post13, "14": post14, "15": post15, "li05": li05, "li09": li09, "li12": li12}
    files = [f for k, fn in fns.items() if not sel or k in sel for f in fn()]
    print("\n".join(str(f) for f in files))
