"""Reusable line-art pieces for Reels and posts (1080 x 1000 scene box). Brand colours from templates/base.css."""

CY, BL, VI, AM, GO, SOS, INK, MU, LINE, PANEL = ("#34DEDC", "#6E9BD6", "#A07CC0", "#D9893A", "#F2C230",
                                                  "#E0563E", "#F3F7F6", "#A6BAC6", "#24394A", "#0E1F2C")


def a(**kw):
    """Animation attributes: a(inn='0,1', draw='0,1', move='0,1,0,40', out=..., grow=...)."""
    m = {"inn": "data-in", "out": "data-out", "draw": "data-draw", "move": "data-move", "grow": "data-grow"}
    return " ".join(f'{m[k]}="{v}"' for k, v in kw.items() if v)


GROW = 'style="transform-box:fill-box;transform-origin:center"'


def drone(x, y, s=1.0, col=INK):
    return (f'<g transform="translate({x},{y}) scale({s})" stroke="{col}" stroke-width="3.5" fill="{PANEL}">'
            '<line x1="-30" y1="-17" x2="30" y2="17"/><line x1="-30" y1="17" x2="30" y2="-17"/>'
            '<circle cx="-30" cy="-17" r="12"/><circle cx="30" cy="17" r="12"/><circle cx="-30" cy="17" r="12"/>'
            '<circle cx="30" cy="-17" r="12"/><rect x="-14" y="-10" width="28" height="20" rx="6"/></g>')


def label(x, y, text, size=34, col=INK, anchor="middle", weight=600, extra=""):
    return f'<text x="{x}" y="{y}" fill="{col}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" {extra}>{text}</text>'


def grid(x0, y0, w, h, step, col, sw=2, extra=""):
    lines = [f'<line x1="{x0 + x}" y1="{y0}" x2="{x0 + x}" y2="{y0 + h}"/>' for x in range(0, w + 1, step)]
    lines += [f'<line x1="{x0}" y1="{y0 + y}" x2="{x0 + w}" y2="{y0 + y}"/>' for y in range(0, h + 1, step)]
    return f'<g stroke="{col}" stroke-width="{sw}" {extra}>{"".join(lines)}</g>'


def panels(x0, y0, cols, rows, w=110, h=70, gap=14, fill="#1B3550", stroke=BL, hot=None, hot_extra=""):
    out = []
    for r in range(rows):
        for c in range(cols):
            x, y = x0 + c * (w + gap), y0 + r * (h + gap)
            out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')
    return "".join(out)


def person(x, y, s=1.0, col=INK, extra=""):
    return (f'<g transform="translate({x},{y}) scale({s})" fill="none" stroke="{col}" stroke-width="5" stroke-linecap="round" {extra}>'
            '<circle cx="0" cy="-70" r="22"/><path d="M0,-46 L0,30 M0,-20 L-36,10 M0,-20 L36,10 M0,30 L-26,90 M0,30 L26,90"/></g>')


def pin(x, y, col=GO):
    return f'<path d="M{x},{y} c-26,-34 -40,-52 -40,-74 a40,40 0 1 1 80,0 c0,22 -14,40 -40,74z" fill="{col}" fill-opacity=".25" stroke="{col}" stroke-width="4"/><circle cx="{x}" cy="{y - 76}" r="12" fill="{col}"/>'


def card(x, y, w, h, title, body, col=CY, extra=""):
    return (f'<g {extra}><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="{PANEL}" stroke="{col}" stroke-width="3"/>'
            + label(x + w / 2, y + h / 2 - 8, title, 40, INK, weight=700)
            + label(x + w / 2, y + h / 2 + 40, body, 30, MU, weight=500) + '</g>')
