"""Make a contact sheet of frames from a reel: python3 tools/contact_sheet.py reel.mp4 out.jpg t1 t2 ..."""
import subprocess, sys, tempfile
from PIL import Image
mp4, out, *ts = sys.argv[1:]
ims = []
with tempfile.TemporaryDirectory() as d:
    for i, t in enumerate(ts):
        p = f"{d}/{i}.jpg"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", t, "-i", mp4, "-frames:v", "1", p], check=True)
        ims.append(Image.open(p).resize((270, 480)))
sheet = Image.new("RGB", (280 * len(ims), 480), "#333")
for i, im in enumerate(ims):
    sheet.paste(im, (i * 280, 0))
sheet.save(out)
