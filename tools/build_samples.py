"""Builds the sample graphics for the first approval round (posts 01, 02 and 06)."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent))
from kit import page, top, foot, layers_svg, drone_svg  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "posts" / "2026-10"


def write(folder, name, html):
    d = OUT / folder
    d.mkdir(parents=True, exist_ok=True)
    # html lives two levels below root, so fix relative paths
    html = html.replace('href="../templates', 'href="../../../templates').replace('src="../brand', 'src="../../../brand')
    (d / f"{name}.html").write_text(html)
    return d / f"{name}.html"


def tags(items):
    return '<div class="tags">' + "".join(f"<span>{t}</span>" for t in items) + "</div>"


def stage(text):
    return f'<div style="margin-top:34px;position:relative;z-index:2"><span class="stage">{text}</span></div>'


# ---------------- Post 01: Meet AerSynk carousel ----------------
def field_svg():
    rows = []
    for i in range(7):
        y = 230 + i * 34
        rows.append(f'<path d="M{60 + i * 18},{y} L{700 - i * 18},{y}" stroke="#0F7C7A" stroke-width="3" stroke-dasharray="2 14" stroke-linecap="round"/>')
    return ('<svg viewBox="0 0 760 520" xmlns="http://www.w3.org/2000/svg">'
            '<polygon points="40,470 720,470 640,200 120,200" fill="#0E1F2C" stroke="#24394A" stroke-width="2"/>'
            + "".join(rows)
            + '<path d="M120,200 L380,70 L640,200" fill="none" stroke="#34DEDC" stroke-width="2" stroke-dasharray="6 10" opacity=".7"/>'
            + drone_svg(380, 62, 1.5) + '</svg>')


def payload_svg():
    items = [("RGB camera", "#6E9BD6", False), ("Thermal", "#D9893A", True), ("LiDAR", "#A07CC0", False)]
    g = ['<svg viewBox="0 0 760 420" xmlns="http://www.w3.org/2000/svg">']
    for i, (lab, col, hi) in enumerate(items):
        x = 20 + i * 250
        g.append(f'<rect x="{x}" y="60" width="220" height="260" rx="18" fill="#0E1F2C" stroke="{col if hi else "#24394A"}" stroke-width="{4 if hi else 2}"/>')
        g.append(f'<circle cx="{x + 110}" cy="160" r="46" fill="none" stroke="{col}" stroke-width="4"/><circle cx="{x + 110}" cy="160" r="16" fill="{col}" fill-opacity=".5"/>')
        g.append(f'<text x="{x + 110}" y="270" fill="#F3F7F6" font-family="Instrument Sans" font-weight="600" font-size="28" text-anchor="middle">{lab}</text>')
    g.append('<path d="M405,350 l20,22 l40,-50" fill="none" stroke="#34DEDC" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>')
    g.append('</svg>')
    return "".join(g)


def rescue_svg():
    return ('<svg viewBox="0 0 760 420" xmlns="http://www.w3.org/2000/svg"><g fill="none" stroke="#24394A" stroke-width="2.5">'
            '<path d="M0 360 Q180 270 380 320 T760 260"/><path d="M50 300 Q210 170 400 230 T730 150"/><path d="M140 230 Q280 110 430 160 T690 60"/></g>'
            '<g transform="translate(500,170)"><circle r="78" fill="#E0563E" fill-opacity=".08" stroke="#E0563E" stroke-opacity=".4" stroke-width="2"/>'
            '<circle r="42" fill="#E0563E" fill-opacity=".16" stroke="#E0563E" stroke-opacity=".7" stroke-width="2"/><circle r="13" fill="#E0563E"/></g>'
            '<text x="500" y="290" fill="#E0563E" font-family="Instrument Sans" font-weight="700" font-size="28" text-anchor="middle">SOS</text>'
            '<rect x="70" y="330" width="70" height="38" rx="8" fill="#0E1F2C" stroke="#F3F7F6" stroke-width="3"/>'
            '<path d="M120 330 Q260 140 470 175" fill="none" stroke="#E0563E" stroke-width="4" stroke-dasharray="4 14" stroke-linecap="round"/>'
            + drone_svg(270, 210, 1.2) + '</svg>')


def post01():
    n = 6
    files = []
    files.append(write("01-meet-aersynk", "slide-1", page(
        top(f"1/{n}")
        + '<p class="kicker">Meet AerSynk</p>'
        + '<h1 class="l">Drone data for surveys. Drone response for emergencies.</h1>'
        + f'<div class="art">{layers_svg()}</div>'
        + foot("aersynk.io", "Drone software and services, South Africa"), seed=3)))
    files.append(write("01-meet-aersynk", "slide-2", page(
        top(f"2/{n}")
        + '<p class="kicker">We fly</p>'
        + '<h1>A BVLOS-certified remote pilot for hire.</h1>'
        + tags(["Agriculture", "Mapping and surveying", "Security", "Inspection", "Filming"])
        + f'<div class="art">{field_svg()}</div>'
        + '<p class="small" style="position:relative;z-index:2;margin-bottom:22px">Flights run under an approved partner operator\'s certificate, confirmed with you before the job is booked.</p>'
        + foot(), seed=5)))
    files.append(write("01-meet-aersynk", "slide-3", page(
        top(f"3/{n}")
        + '<p class="kicker">We advise</p>'
        + '<h1>The right drone, payload and workflow for the job.</h1>'
        + '<p class="body">So you do not pay for the wrong kit. Advice on aircraft, sensors, survey workflow and data processing.</p>'
        + f'<div class="art">{payload_svg()}</div>'
        + foot(), seed=7)))
    files.append(write("01-meet-aersynk", "slide-4", page(
        top(f"4/{n}")
        + '<p class="kicker">We build: AerSynk Survey</p>'
        + '<h1>Every sensor on one map, from flight to finished data.</h1>'
        + '<p class="body">417 sensors and payloads in one catalogue. Plan, fly, process and combine the results in one place.</p>'
        + stage("Working prototype on demo data")
        + f'<div class="art">{layers_svg()}</div>'
        + foot(), seed=9)))
    files.append(write("01-meet-aersynk", "slide-5", page(
        top(f"5/{n}")
        + '<p class="kicker" style="color:#E0563E">We build: AerSynk Rescue</p>'
        + '<h1>One SOS press starts the whole rescue.</h1>'
        + '<p class="body">Hikers rent a GPS and SOS tag. One press alerts dispatch and responders, and an authorised operator can send a drone. Starting on Table Mountain.</p>'
        + stage("In development, not live yet")
        + f'<div class="art">{rescue_svg()}</div>'
        + foot(), seed=11)))
    files.append(write("01-meet-aersynk", "slide-6", page(
        top(f"6/{n}")
        + '<p class="kicker">Work with us</p>'
        + '<h1 class="l">Have a site, a job or a question?</h1>'
        + '<p class="body">Send us the location and what you need. We will tell you what is realistic.</p>'
        + '<div style="flex:1"></div>'
        + '<div style="position:relative;z-index:2;display:grid;gap:26px;margin-bottom:60px">'
          '<div><p class="small">Website</p><p class="cta-line">aersynk.io</p></div>'
          '<div><p class="small">WhatsApp or call</p><p class="cta-line">073 290 4298</p></div>'
          '<div><p class="small">Email</p><p class="cta-line">aersynk@gmail.com</p></div></div>'
        + foot("Follow along as we build", ""), seed=13)))
    return files


# ---------------- Post 02: LinkedIn, why AerSynk exists ----------------
def tools_svg():
    boxes = [("Photos", "#6E9BD6"), ("LiDAR", "#A07CC0"), ("Magnetics", "#D9893A"), ("Spectral", "#34DEDC")]
    g = ['<svg viewBox="0 0 860 520" xmlns="http://www.w3.org/2000/svg">']
    for i, (lab, col) in enumerate(boxes):
        y = 20 + i * 122
        g.append(f'<rect x="10" y="{y}" width="290" height="92" rx="14" fill="#0E1F2C" stroke="{col}" stroke-width="3"/>')
        g.append(f'<text x="155" y="{y + 56}" fill="#F3F7F6" font-family="Instrument Sans" font-weight="600" font-size="30" text-anchor="middle">{lab}</text>')
        g.append(f'<path d="M300,{y + 46} C470,{y + 46} 470,256 580,256" fill="none" stroke="{col}" stroke-width="3" stroke-opacity=".8"/>')
    g.append('<rect x="580" y="176" width="270" height="160" rx="18" fill="#0F7C7A" fill-opacity=".25" stroke="#34DEDC" stroke-width="4"/>')
    g.append('<text x="715" y="248" fill="#F3F7F6" font-family="Bricolage Grotesque" font-weight="800" font-size="36" text-anchor="middle">One</text>')
    g.append('<text x="715" y="292" fill="#F3F7F6" font-family="Bricolage Grotesque" font-weight="800" font-size="36" text-anchor="middle">workspace</text>')
    g.append('</svg>')
    return "".join(g)


def post02():
    return [write("02-linkedin-why-aersynk", "image", page(
        top()
        + '<p class="kicker">Why AerSynk exists</p>'
        + '<h1>Built by people who fly drones for a living.</h1>'
        + '<p class="body">Advising clients on drone solutions showed us how much time teams lose moving survey data between separate tools.</p>'
        + f'<div class="art">{tools_svg()}</div>'
        + foot("aersynk.io", "Drone software and services, South Africa"), seed=17))]


# ---------------- Post 06: What is GSD ----------------
def gsd_svg():
    def grid(x0, y0, w, h, step, col):
        lines = []
        for x in range(0, w + 1, step):
            lines.append(f'<line x1="{x0 + x}" y1="{y0}" x2="{x0 + x}" y2="{y0 + h}"/>')
        for y in range(0, h + 1, step):
            lines.append(f'<line x1="{x0}" y1="{y0 + y}" x2="{x0 + w}" y2="{y0 + y}"/>')
        return f'<g stroke="{col}" stroke-width="2" opacity=".9">{"".join(lines)}</g>'
    g = ['<svg viewBox="0 0 880 600" xmlns="http://www.w3.org/2000/svg">']
    # low drone, small footprint, fine grid
    g.append('<path d="M220,170 L90,430 L350,430 Z" fill="#34DEDC" fill-opacity=".07" stroke="#34DEDC" stroke-width="2" stroke-dasharray="6 8"/>')
    g.append(grid(90, 430, 260, 120, 20, "#34DEDC"))
    g.append(drone_svg(220, 160, 1.3))
    g.append('<text x="220" y="595" fill="#F3F7F6" font-family="Instrument Sans" font-weight="600" font-size="30" text-anchor="middle">Fly lower</text>')
    # high drone, big footprint, coarse grid
    g.append('<path d="M650,40 L470,430 L830,430 Z" fill="#6E9BD6" fill-opacity=".07" stroke="#6E9BD6" stroke-width="2" stroke-dasharray="6 8"/>')
    g.append(grid(470, 430, 360, 120, 60, "#6E9BD6"))
    g.append(drone_svg(650, 30, 1.3))
    g.append('<text x="650" y="595" fill="#F3F7F6" font-family="Instrument Sans" font-weight="600" font-size="30" text-anchor="middle">Fly higher</text>')
    g.append('</svg>')
    return "".join(g)


def post06():
    return [write("06-what-is-gsd", "image", page(
        top()
        + '<p class="kicker">Survey basics</p>'
        + '<h1 class="l">What is GSD?</h1>'
        + '<p class="body"><b>Ground sampling distance</b> is the size of one image pixel on the ground. Lower flights give smaller pixels and more detail, but take more flight lines and processing time.</p>'
        + f'<div class="art">{gsd_svg()}</div>'
        + foot("aersynk.io", "Illustration, not to scale"), seed=21))]


if __name__ == "__main__":
    for f in post01() + post02() + post06():
        print(f)
