"""Reel engine: turns a short scene spec into a voiced, subtitled 1080x1920 MP4.

A spec is a dict:
  {
    "id": "r02-gsd",
    "scenes": [
      {"step": "Step 1", "title": "Headline on screen", "voice": "Spoken line.", "svg": "<g>...</g>", "hold": 0.6},
      ...
    ],
    "end": {"title": "Planning a mapping job?", "line": "aersynk.io", "sub": "WhatsApp or call 073 290 4298"},
    "note": "Animated illustration. Not real survey data."
  }

Inside a scene's svg (drawn in a 1080 x 1000 box), elements animate with attributes, in seconds from the
start of that scene:
  data-in="a,b"      fade in between a and b
  data-out="a,b"     fade out between a and b
  data-draw="a,b"    draw the stroke between a and b (give the element pathLength="1")
  data-move="a,b,dx,dy"  move from (dx,dy) offset to its place between a and b
  data-grow="a,b"    scale up from 0 to 1 (set transform-origin with style="transform-box:fill-box;transform-origin:center")
Voice lines are spoken with a free offline voice (Piper), placed on one track, and burned in as subtitles.
"""
import html
import json
import subprocess
import sys
import wave
import array
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VOICE = Path("/tmp/piper-voices/en-us-ryan-high.onnx")
SR = 22050
LEAD = 0.35    # seconds of silence before each line
TAIL = 0.55    # seconds after each line before the next scene
END_SECONDS = 4.2


SPOKEN = [("G S D", "GSD"), ("R T K", "RTK"), ("D S M", "DSM"), ("D T M", "DTM"), ("N D V I", "NDVI"),
          ("I E C", "IEC"), ("S A C A A", "SACAA"), ("R O C", "ROC"), ("aersynk dot io", "aersynk.io"),
          ("six hundred watts per square metre", "600 W/m\u00b2")]


def display(text):
    """Subtitle text: voice lines are written the way they should be spoken; show them the way they are written."""
    for spoken, written in SPOKEN:
        text = text.replace(spoken, written)
    return text


def tts(text, out):
    subprocess.run([sys.executable, "-m", "piper", "-m", str(VOICE), "--length-scale", "1.05", "-f", str(out)],
                   input=text.encode(), check=True, capture_output=True)
    w = wave.open(str(out))
    return w.getnframes() / w.getframerate()


def build(spec):
    out_dir = ROOT / spec["folder"]
    out_dir.mkdir(parents=True, exist_ok=True)
    tmp = out_dir / "_voice"
    tmp.mkdir(exist_ok=True)
    t = 0.0
    timings = []
    for i, sc in enumerate(spec["scenes"]):
        d = tts(sc["voice"], tmp / f"l{i}.wav")
        start = t
        voice_at = t + LEAD
        end = voice_at + d + TAIL + sc.get("hold", 0)
        timings.append({"a": round(start, 3), "b": round(end, 3), "v": round(voice_at, 3)})
        t = end
    end_voice = spec["end"].get("voice")
    end_start = t
    if end_voice:
        d = tts(end_voice, tmp / "end.wav")
        total = end_start + max(END_SECONDS, LEAD + d + 0.8)
    else:
        total = end_start + END_SECONDS
    # audio track
    buf = array.array("h", [0] * int(total * SR))
    def place(path, at):
        w = wave.open(str(path))
        data = array.array("h", w.readframes(w.getnframes()))
        o = int(at * SR)
        n = min(len(data), len(buf) - o)
        buf[o:o + n] = data[:n]
    for i, tm in enumerate(timings):
        place(tmp / f"l{i}.wav", tm["v"])
    if end_voice:
        place(tmp / "end.wav", end_start + LEAD)
    wav = out_dir / "voice.wav"
    w = wave.open(str(wav), "wb")
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(buf.tobytes()); w.close()
    for f in tmp.iterdir():
        f.unlink()
    tmp.rmdir()
    (out_dir / "reel.html").write_text(page(spec, timings, end_start, total))
    (out_dir / "timing.json").write_text(json.dumps({"scenes": timings, "end": end_start, "total": round(total, 2)}, indent=1))
    mp4 = out_dir / "reel.mp4"
    subprocess.run([sys.executable, str(ROOT / "tools" / "render_reel.py"), str(out_dir / "reel.html"), str(mp4),
                    "--seconds", f"{total:.2f}", "--audio", str(wav)], check=True)
    # cover frame: middle of the last content scene
    last = timings[-1]
    cover_t = (last["a"] + last["b"]) / 2
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{cover_t:.2f}", "-i", str(mp4), "-frames:v", "1", "-q:v", "3",
                    str(out_dir / "cover.jpg")], check=True)
    wav.unlink()
    return {"mp4": mp4, "seconds": round(total, 1), "cover_ms": int(cover_t * 1000)}


def page(spec, timings, end_start, total):
    rel = "../../.."
    scenes_svg = []
    for i, sc in enumerate(spec["scenes"]):
        scenes_svg.append(f'<g class="scene" data-i="{i}">{sc["svg"]}</g>')
    meta = [{"a": tm["a"], "b": tm["b"], "step": sc.get("step", ""), "title": sc["title"], "sub": display(sc["voice"])}
            for tm, sc in zip(timings, spec["scenes"])]
    end = spec["end"]
    note = spec.get("note", "Animated illustration.")
    return f"""<!doctype html><html><head><meta charset="utf-8"><title>{html.escape(spec['id'])}</title>
<link rel="stylesheet" href="{rel}/templates/base.css">
<style>
:root {{ --h: 1920px; }}
.sheet {{ padding: 110px 90px 120px; }}
.top img {{ height: 36px; }}
#step {{ font-weight: 600; font-size: 34px; color: var(--cyan); margin-top: 60px; height: 40px; position: relative; z-index: 2; }}
#title {{ font-family: "Bricolage Grotesque"; font-weight: 800; font-stretch: 90%; font-size: 92px; line-height: 1; letter-spacing: -0.025em; margin-top: 22px; min-height: 290px; position: relative; z-index: 2; text-wrap: balance; }}
#art {{ position: absolute; left: 0; top: 560px; width: 1080px; height: 1000px; z-index: 1; overflow: visible; }}
#sub {{ position: absolute; left: 90px; right: 90px; bottom: 150px; z-index: 3; font-size: 40px; line-height: 1.3; font-weight: 600; text-align: center; color: var(--ink); background: rgba(8,19,28,.88); border: 1.5px solid var(--line); border-radius: 18px; padding: 22px 30px; }}
#end {{ position: absolute; inset: 0; z-index: 4; display: flex; flex-direction: column; justify-content: center; padding: 0 90px; background: var(--bg); opacity: 0; }}
#end h2 {{ font-family: "Bricolage Grotesque"; font-weight: 800; font-stretch: 90%; font-size: 108px; line-height: 1; letter-spacing: -0.025em; text-wrap: balance; }}
#end .l {{ font-family: "Bricolage Grotesque"; font-weight: 700; font-size: 70px; margin-top: 70px; color: var(--cyan); }}
#end .s {{ font-size: 40px; color: var(--muted); margin-top: 22px; }}
#end .n {{ font-size: 30px; color: var(--muted); margin-top: 90px; }}
#end img {{ height: 44px; margin-bottom: 90px; align-self: flex-start; }}
text {{ font-family: "Instrument Sans"; }}
</style></head><body>
<div class="frame"></div>
<svg id="art" viewBox="0 0 1080 1000" xmlns="http://www.w3.org/2000/svg">{''.join(scenes_svg)}</svg>
<div class="sheet"><div class="top"><img src="{rel}/brand/logo-on-dark.png" alt=""></div><div id="step"></div><div id="title"></div></div>
<div id="sub"></div>
<div id="end"><img src="{rel}/brand/logo-on-dark.png" alt=""><h2>{html.escape(end['title'])}</h2>
<p class="l">{html.escape(end.get('line', 'aersynk.io'))}</p><p class="s">{html.escape(end.get('sub', 'WhatsApp or call 073 290 4298'))}</p>
<p class="n">{html.escape(note)}</p></div>
<script>
const META = {json.dumps(meta)};
const END = {end_start:.3f};
const clamp = (x,a=0,b=1) => Math.max(a, Math.min(b, x));
const prog = (t,a,b) => b<=a ? (t>=a?1:0) : clamp((t-a)/(b-a));
const ease = x => x<.5 ? 2*x*x : 1-Math.pow(-2*x+2,2)/2;
const pair = s => s.split(',').map(Number);
const scenes = [...document.querySelectorAll('.scene')];
const $ = id => document.getElementById(id);
let last = -2;
window.render = function(t) {{
  let si = META.findIndex(m => t >= m.a && t < m.b);
  if (t >= END) si = -1;
  if (si !== last) {{
    const m = META[si];
    $('step').textContent = m ? m.step : '';
    $('title').textContent = m ? m.title : '';
    $('sub').textContent = m ? m.sub : '';
    last = si;
  }}
  const m = META[si];
  const head = m ? clamp(Math.min((t-m.a)/0.3, (m.b-t)/0.25)) : 0;
  $('title').style.opacity = head; $('step').style.opacity = head;
  $('sub').style.opacity = m ? clamp(Math.min((t-m.a)/0.2, (m.b-t)/0.15)) : 0;
  scenes.forEach((g, i) => {{
    const M = META[i];
    const on = t >= M.a && t < M.b;
    g.style.display = on ? '' : 'none';
    if (!on) return;
    const L = t - M.a;
    g.style.opacity = clamp(Math.min(L/0.3, (M.b-t)/0.3));
    g.querySelectorAll('[data-in],[data-out],[data-draw],[data-move],[data-grow]').forEach(el => {{
      let op = 1;
      if (el.dataset.in) {{ const [a,b] = pair(el.dataset.in); op *= ease(prog(L,a,b)); }}
      if (el.dataset.out) {{ const [a,b] = pair(el.dataset.out); op *= 1 - ease(prog(L,a,b)); }}
      el.style.opacity = op;
      if (el.dataset.draw) {{ const [a,b] = pair(el.dataset.draw); el.style.strokeDasharray = '1'; el.style.strokeDashoffset = String(1 - ease(prog(L,a,b))); }}
      let tf = '';
      if (el.dataset.move) {{ const [a,b,dx,dy] = pair(el.dataset.move); const p = 1 - ease(prog(L,a,b)); tf += `translate(${{dx*p}}px,${{dy*p}}px) `; }}
      if (el.dataset.grow) {{ const [a,b] = pair(el.dataset.grow); tf += `scale(${{ease(prog(L,a,b))}})`; }}
      if (tf) el.style.transform = tf;
    }});
  }});
  $('end').style.opacity = ease(prog(t, END - 0.1, END + 0.5));
}};
window.render(0);
</script></body></html>"""
