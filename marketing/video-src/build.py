"""Build 9:16 Hyperframes compositions for the ORU TikTok/Reels scripts.

Each video is a list of timed layers in specs/<name>.json. This writes
video-src/<name>/index.html plus its assets; render it with
`npx hyperframes render --quality high --output ../../videos/<name>.mp4`
from inside that folder. Silent on purpose: add a cleared sound in the app.

Layer types (all times in seconds):
  chart    {start, draw_end, w_end, atts_at, overrated_at, end}   the line drawing into WATTS
           {start, draw_end, end, line_only: true, opacity?, y?}   line only, no words (footage stand-in)
  bg       {color, start, end, fade?}                              full-frame colour wash
  split    {srcs: [top, bottom], start, end}                       two stills, top and bottom halves
  text     {text, start, end, y?, size?, color?, band?, sub?}      big centred card text
  label    {text, start, end}                                      small tag, top left ("mockup")
  image    {src, start, end, zoom?, fit?}                          still with slow push-in; fit contain|cover
  video    {src, start, end, media_start?, sound?, position?}      owner's own vertical clip, cover-fit; muted
                                                                    unless sound: true (the owner's own trail sound)
  list     {title, items, start, step, end}                        lines arriving one by one
  endcard  {start, end}                                            ORU mark, WATTS TEE · FROM $56, wearoru.com

Checks (build refuses the spec otherwise): a "mockup" / "AI mockup" label must
start no later and end no earlier than every photoreal mockup it covers, so a
mockup is never on screen without it; and no text sits lower than y 420,
which keeps it clear of TikTok's caption over the bottom fifth.

Owner clips: scripts 02, 06, 07, 09 and 10 can use a faceless POV clip from
the owner in place of the chart-line fallback. Swap the line_only chart layer
for a video layer with the same start/end, then build and render.
"""
import html
import json
from PIL import Image
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BRAG = HERE.parent.parent / 'brag-output' / 'composition' / 'assets'
W, H = 1080, 1920

# Geometry copied from oru-store/design/watts-chart.svg via the brag composition.
CHART_SVG = '''<svg id="chart" viewBox="0 0 3000 1900" xmlns="http://www.w3.org/2000/svg">
  <line id="axis-y" x1="95" y1="140" x2="95" y2="1830" stroke="#E8E6E1" stroke-width="12" />
  <line id="axis-x" x1="95" y1="1830" x2="2900" y2="1830" stroke="#E8E6E1" stroke-width="12" />
  <path id="chart-line" d="M 150.0 1740.0 L 360.0 1545.0 L 455.0 1645.0 L 650.0 1405.0 L 755.0 1515.0 L 960.0 1255.0 L 1075.0 1370.0 L 1240.0 1085.0 L 1320.0 1150.0 L 1380.0 915.4 L 1463.1 1150.0 L 1539.8 995.2 L 1616.5 1150.0 L 1699.6 915.4"
    fill="none" stroke="#E8E6E1" stroke-width="40" stroke-linejoin="miter" stroke-linecap="butt" />
  <text id="atts" x="1710" y="1150" font-family="Archivo" font-weight="500" font-size="340" letter-spacing="10" fill="#E8E6E1">ATTS</text>
  <text id="are-overrated" x="2601" y="1520" text-anchor="end" font-family="Archivo" font-weight="500" font-size="132" letter-spacing="16" fill="#E8E6E1">ARE OVERRATED</text>
</svg>'''

MARK_SVG = '''<svg class="mark" viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">
  <circle cx="60" cy="60" r="47.38" fill="none" stroke="#E8E6E1" stroke-width="17.23" />
  <rect x="37.60" y="51.21" width="44.80" height="17.58" fill="#D1442B" />
</svg>'''

CSS = '''
@font-face { font-family: "Archivo"; src: url("assets/fonts/archivo-500.woff2") format("woff2"); font-weight: 500; font-display: block; }
@font-face { font-family: "Archivo"; src: url("assets/fonts/archivo-600.woff2") format("woff2"); font-weight: 600; font-display: block; }
@font-face { font-family: "Archivo"; src: url("assets/fonts/archivo-700.woff2") format("woff2"); font-weight: 700; font-display: block; }
:root { --ink: #0f1011; --bone: #e8e6e1; --smoke: #8b8a85; --signal: #d1442b; --signal-text: #e3603f; }
body { margin: 0; background: var(--ink); }
#root { position: relative; width: 100%; height: 100%; overflow: hidden; background: var(--ink);
  color: var(--bone); font-family: "Archivo", sans-serif; }
.layer { position: absolute; inset: 0; opacity: 0; }
/* TikTok's buttons sit on the right edge and its caption over the bottom fifth,
   so everything readable stays inside x 80-900 and y 220-1480. */
.card { display: flex; align-items: center; justify-content: center; }
.card p { margin: 0; width: 820px; margin-right: 100px; text-align: center; font-weight: 700;
  line-height: 1.04; letter-spacing: -0.01em; text-transform: uppercase; }
.chart-wrap { display: flex; align-items: center; justify-content: center; }
/* 870 wide + 98 right margin puts the artwork (axis end included) at x 84-897. */
#chart { width: 870px; height: 551px; margin-right: 98px; overflow: visible; }
.vid { width: 100%; height: 100%; object-fit: cover; }
.img { background-size: cover; background-position: center; }
.tag { position: absolute; left: 80px; top: 220px; padding: 10px 18px; background: rgba(15,16,17,.82);
  font-size: 40px; font-weight: 600; letter-spacing: .16em; text-transform: uppercase; color: var(--bone); }
.list { display: flex; flex-direction: column; justify-content: center; padding: 0 80px; }
.list h2 { margin: 0 0 48px; font-size: 40px; font-weight: 600; letter-spacing: .22em; text-transform: uppercase; color: var(--signal-text); }
.list p { margin: 0; padding: 30px 0; width: 820px; border-bottom: 2px solid #272a2d; font-size: 76px;
  font-weight: 600; line-height: 1.08; opacity: 0; }
.end { display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 44px; padding-right: 100px; }
.end .mark { width: 190px; height: 190px; }
.end .product { margin: 0; font-size: 58px; font-weight: 700; letter-spacing: .14em; text-transform: uppercase; }
.end .price { margin: 0; font-size: 58px; font-weight: 700; letter-spacing: .06em; color: var(--signal-text); }
.end .url { margin: 0; font-size: 44px; font-weight: 500; letter-spacing: .1em; color: var(--smoke); }
'''

FADE = 0.3


def check_labels(spec):
    """Every photoreal mockup (anything from assets/products) must sit under a
    label for its whole time on screen, fades included."""
    labels = [(l['start'], l['end']) for l in spec['layers'] if l['type'] == 'label']
    for l in spec['layers']:
        srcs = l.get('srcs') or [l.get('src', '')]
        if l['type'] in ('image', 'split') and any('/assets/products/' in s for s in srcs):
            if not any(a <= l['start'] and b >= l['end'] for a, b in labels):
                raise ValueError(f"{spec['name']}: mockup {srcs} {l['start']}-{l['end']} is not fully labelled")
    for l in spec['layers']:
        if l['type'] == 'text' and l.get('y', 0) > 420:
            raise ValueError(f"{spec['name']}: text {l['text']!r} sits too low (y {l['y']} > 420)")


def build(spec_path):
    spec = json.loads(Path(spec_path).read_text(encoding='utf-8'))
    check_labels(spec)
    name = spec['name']
    out = HERE / name
    if out.exists():
        shutil.rmtree(out)
    (out / 'assets' / 'fonts').mkdir(parents=True)
    (out / 'assets' / 'vendor').mkdir(parents=True)
    (out / 'assets' / 'img').mkdir(parents=True)
    for w in ('500', '600', '700'):
        shutil.copy(BRAG / 'fonts' / f'archivo-{w}.woff2', out / 'assets' / 'fonts')
    shutil.copy(BRAG / 'vendor' / 'gsap.min.js', out / 'assets' / 'vendor')

    duration = spec['duration']
    body, js, clips = [], [], []
    for i, layer in enumerate(spec['layers']):
        lid = f'L{i}'
        kind = layer['type']
        start, end = layer['start'], layer['end']
        if kind == 'chart':
            # line_only: the line draws (W shape included) with no words, as a
            # stand-in for owner footage. opacity < 1 makes it a faint backdrop.
            peak = layer.get('opacity', 1)
            shift = layer.get('y', 0)  # px; a faint backdrop sits low, clear of the words
            body.append(f'<div id="{lid}" class="layer chart-wrap" style="transform:translateY({shift}px)">{CHART_SVG}</div>')
            js.append(f'''
  {{ const line = document.getElementById("chart-line");
    const total = line.getTotalLength();
    const cum = cumulative(PTS);
    const atW = total * (1 - cum[9] / cum[cum.length - 1]);
    line.style.strokeDasharray = total; line.style.strokeDashoffset = total;
    tl.set("#atts, #are-overrated", {{ opacity: 0 }}, 0);
    tl.to("#{lid}", {{ opacity: {peak}, duration: 0.01 }}, {start});''')
            if layer.get('line_only'):
                js.append(f'''
    tl.to("#chart-line", {{ strokeDashoffset: 0, duration: {layer["draw_end"] - start - 0.2}, ease: "none" }}, {start + 0.2});''')
            else:
                js.append(f'''
    tl.to("#chart-line", {{ strokeDashoffset: atW, duration: {layer["draw_end"] - start - 0.2}, ease: "none" }}, {start + 0.2});
    tl.to("#chart-line", {{ strokeDashoffset: 0, duration: {layer["w_end"] - layer["draw_end"]}, ease: "power1.inOut" }}, {layer["draw_end"]});
    tl.to("#atts", {{ opacity: 1, duration: 0.34, ease: "power2.out" }}, {layer["atts_at"]});
    tl.to("#are-overrated", {{ opacity: 1, duration: 0.36, ease: "power2.out" }}, {layer["overrated_at"]});''')
            js.append(f'''
    tl.to("#{lid}", {{ opacity: 0, duration: {FADE} }}, {end - FADE}); }}''')
        elif kind == 'bg':
            body.append(f'<div id="{lid}" class="layer" style="background:{layer["color"]}"></div>')
            js.append(f'''
  tl.to("#{lid}", {{ opacity: 1, duration: {layer.get("fade", 0.6)}, ease: "power1.inOut" }}, {start});
  tl.to("#{lid}", {{ opacity: 0, duration: 0.2 }}, {end - 0.2});''')
        elif kind == 'split':
            halves = []
            for j, s in enumerate(layer['srcs']):
                src = Path(s)
                shutil.copy(src, out / 'assets' / 'img' / src.name)
                halves.append(f'<div style="position:absolute;left:0;right:0;top:{j * 50}%;height:50%;'
                              f'background:url(assets/img/{src.name}) center/cover no-repeat"></div>')
            body.append(f'<div id="{lid}" class="layer">{"".join(halves)}</div>')
            js.append(f'''
  tl.to("#{lid}", {{ opacity: 1, duration: {FADE} }}, {start});
  tl.to("#{lid}", {{ opacity: 0, duration: {FADE} }}, {end - FADE});''')
        elif kind == 'text':
            size = layer.get('size', 112)
            y = layer.get('y', 0)  # px offset from centre, negative = up
            color = layer.get('color', 'var(--bone)')
            # band: a dark strip behind the words when they sit over a photo.
            band = 'background:rgba(15,16,17,.8);padding:26px 30px;' if layer.get('band') else ''
            sub = ''
            if layer.get('sub'):
                sub = (f'<span style="display:block;margin-top:28px;font-size:{round(size * 0.6)}px;'
                       f'color:var(--smoke)">{html.escape(layer["sub"])}</span>')
            body.append(f'<div id="{lid}" class="layer card"><p style="font-size:{size}px;color:{color};{band}transform:translateY({y}px)">'
                        f'{html.escape(layer["text"]).replace(chr(10), "<br>")}{sub}</p></div>')
            js.append(f'''
  tl.fromTo("#{lid}", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.25, ease: "power2.out" }}, {start});
  tl.to("#{lid}", {{ opacity: 0, duration: 0.2 }}, {end - 0.2});''')
        elif kind == 'label':
            body.append(f'<div id="{lid}" class="layer"><span class="tag">{html.escape(layer["text"])}</span></div>')
            js.append(f'''
  tl.to("#{lid}", {{ opacity: 1, duration: 0.2 }}, {start});
  tl.to("#{lid}", {{ opacity: 0, duration: 0.2 }}, {end - 0.2});''')
        elif kind == 'image':
            src = Path(layer['src'])
            shutil.copy(src, out / 'assets' / 'img' / src.name)
            zoom = layer.get('zoom', 1.08)
            pos = layer.get('position', 'center')
            # "contain" keeps a print close-up whole; "cover" fills the frame with a body shot.
            size = 'contain' if layer.get('fit') == 'contain' else 'cover'
            # Fill the bars around a contained image with its own corner colour,
            # so the photo doesn't sit in a visible box on the ink.
            r, g, b = Image.open(src).convert('RGB').getpixel((2, 2))
            body.append(f'<div id="{lid}" class="layer img" style="background-image:url(assets/img/{src.name});'
                        f'background-color:rgb({r},{g},{b});background-position:{pos};background-size:{size};background-repeat:no-repeat"></div>')
            js.append(f'''
  tl.fromTo("#{lid}", {{ opacity: 0, scale: 1 }}, {{ opacity: 1, duration: {FADE}, ease: "power1.out" }}, {start});
  tl.to("#{lid}", {{ scale: {zoom}, duration: {end - start}, ease: "none" }}, {start});
  tl.to("#{lid}", {{ opacity: 0, duration: {FADE} }}, {end - FADE});''')
        elif kind == 'video':
            # The owner's own clip. Muted unless the owner wants their own
            # trail sound on it; never anyone else's audio.
            # Re-encoded with a keyframe every 30 frames so the renderer can seek
            # it cleanly. It sits outside the timed <section> (hyperframes
            # resolves a nested video's start without the wrapper's offset),
            # below every other layer.
            src = Path(layer['src'])
            (out / 'assets' / 'clip').mkdir(exist_ok=True)
            dst = out / 'assets' / 'clip' / (src.stem + '.mp4')
            subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', str(src), '-c:v', 'libx264', '-r', '30',
                            '-g', '30', '-keyint_min', '30', '-pix_fmt', 'yuv420p', '-movflags', '+faststart',
                            '-c:a', 'aac', str(dst)], check=True)
            pos = layer.get('position', 'center')
            sound = 'data-has-audio="true"' if layer.get('sound') else 'muted'
            clips.append(f'<video id="{lid}" class="layer clip vid" src="assets/clip/{dst.name}" '
                        f'data-start="{start}" data-duration="{round(end - start, 3)}" '
                        f'data-media-start="{layer.get("media_start", 0)}" {sound} playsinline '
                        f'style="object-position:{pos}"></video>')
            js.append(f'''
  tl.fromTo("#{lid}", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.2 }}, {start});
  tl.to("#{lid}", {{ opacity: 0, duration: {FADE} }}, {end - FADE});''')
        elif kind == 'list':
            items = ''.join(f'<p id="{lid}i{j}">{html.escape(t)}</p>' for j, t in enumerate(layer['items']))
            body.append(f'<div id="{lid}" class="layer list"><h2>{html.escape(layer["title"])}</h2>{items}</div>')
            js.append(f'''
  tl.to("#{lid}", {{ opacity: 1, duration: 0.25 }}, {start});''')
            for j in range(len(layer['items'])):
                t = start + 0.4 + j * layer['step']
                js.append(f'''
  tl.fromTo("#{lid}i{j}", {{ opacity: 0, y: 24 }}, {{ opacity: 1, y: 0, duration: 0.35, ease: "power3.out" }}, {t:.2f});''')
            js.append(f'''
  tl.to("#{lid}", {{ opacity: 0, duration: 0.2 }}, {end - 0.2});''')
        elif kind == 'endcard':
            body.append(f'<div id="{lid}" class="layer end">{MARK_SVG}<p class="product">Watts tee</p>'
                        f'<p class="price">from $56</p><p class="url">wearoru.com</p></div>')
            js.append(f'''
  tl.to("#{lid}", {{ opacity: 1, duration: 0.35, ease: "power2.out" }}, {start});''')
            if end < duration:
                js.append(f'''
  tl.to("#{lid}", {{ opacity: 0, duration: 0.2 }}, {end - 0.2});''')
        else:
            raise ValueError(f'unknown layer type {kind}')

    page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width={W}, height={H}" />
<title>ORU — {html.escape(spec.get("title", name))}</title>
<script src="assets/vendor/gsap.min.js"></script>
<style>{CSS}</style>
</head>
<body>
<div id="root" data-composition-id="oru" data-start="0" data-width="{W}" data-height="{H}" data-duration="{duration}">
{chr(10).join(clips)}
<section id="scene" class="clip" data-start="0" data-duration="{duration}" data-track-index="0" style="position:absolute;inset:0">
{chr(10).join(body)}
</section>
</div>
<script>
const PTS = [[150,1740],[360,1545],[455,1645],[650,1405],[755,1515],[960,1255],[1075,1370],[1240,1085],[1320,1150],[1380,915.4],[1463.1,1150],[1539.8,995.2],[1616.5,1150],[1699.6,915.4]];
function cumulative(pts) {{ const o = [0]; for (let i = 1; i < pts.length; i++) o.push(o[i-1] + Math.hypot(pts[i][0]-pts[i-1][0], pts[i][1]-pts[i-1][1])); return o; }}
function build() {{
  const tl = gsap.timeline({{ paused: true }});
{"".join(js)}
  tl.set({{}}, {{}}, {duration});
  window.__timelines = window.__timelines || {{}};
  window.__timelines["oru"] = tl;
}}
if (document.fonts && document.fonts.ready) {{ document.fonts.ready.then(build); }} else {{ build(); }}
</script>
</body>
</html>
'''
    (out / 'index.html').write_text(page, encoding='utf-8')
    return out


if __name__ == '__main__':
    for p in sys.argv[1:]:
        print(build(p))
