# Hyperframes Composition Brief: ORU — Watts tee

## Objective

Create a short launch-style brag video for ORU, a one-person e-enduro apparel
brand selling a single $48 tee whose back print is a stock chart that turns into
the word WATTS.

## Output

- Composition directory: `brag-output/composition/`
- Rendered video: `brag-output/brag.mp4`
- Format: landscape — 1920x1080
- Duration: 22.92s

## Source Material

- Project root: the `oru-bike-site` archive supplied by the user (served locally
  at `http://localhost:3000` during capture)
- Primary files read: `index.html`, `about.html`, `product-watts.html`,
  `assets/site.css`, `design/watts-chart.svg`, `CLAUDE-CODE-BRIEF.md`
- Live capture: `brag-output/site-capture/` (8 scroll screenshots, extracted
  tokens, Archivo font manifest)
- Product name: **ORU** — the **Watts tee**, $48
- Tagline / strongest claim: *"Three laps while you did one."*
- Key UI or visual moment to recreate: the `design/watts-chart.svg` lockup — the
  chart path whose final climb **is** the W of WATTS — drawn on progressively.
- Copy that must appear verbatim:
  - `TRAILHEAD · VAN · PUB`
  - `THREE LAPS / WHILE YOU / DID ONE.`
  - `ULTRA-SOFT BLEND · MADE TO ORDER · SHIPPED WORLDWIDE`
  - `WHAT I WILL NOT DO`
  - `Call a t-shirt technical`
  - `Invent reviews`
  - `Run a fake countdown`
  - `YES, IT HAS A MOTOR.`
  - `NO, I AM NOT GOING TO ARGUE ABOUT IT.`
  - `WATTS TEE · $48`
  - `wearoru.com`

## Creative Direction

- **Tone preset:** `deadpan`
- **Creative direction:** *a line going up, explained as little as possible*
- **Interpretation:** Long holds, one thought per scene, slow crossfades, a lot
  of empty near-black. The pace is the joke. Nothing in this video may raise its
  voice, because the brand's own copy never does.
- **Angle:** The line is the product, and you don't know that until it finishes
  drawing. For four seconds the viewer watches what looks like a market chart
  climb; then it stops being a chart and becomes a word. Everything after that
  is the brand refusing to sell you anything, in its own words — because a video
  that behaved like a normal product ad would be lying about the product.
- **Hook:** Near-black. A thin axis. A white line climbing from the bottom left
  in higher highs and higher lows. No title, no logo, no copy.
- **Outro / punchline:** *"Yes, it has a motor. / No, I am not going to argue
  about it."* → ORU mark, `WATTS TEE · $48`, `wearoru.com`, long hold.
- **Avoid:**
  - Generic SaaS language
  - Abstract filler visuals
  - Unrelated visual redesign
  - **Project-specific ban, from the first line of `assets/site.css`:**
    *"Deliberately not: neon on black, italic display type, speed lines."*
    No glow, no neon, no motion streaks, no speed lines anywhere.
  - **No invented product photography.** The repo's `assets/products/*.jpg` are
    grey placeholder tiles and `design/preview-*.jpg` are flat artwork previews,
    not garment shots. The brand brief says "Do not invent product photos or
    measurements." The video therefore shows the print artwork and the real site
    UI, never a mocked-up shirt.

## Visual Identity

Verbatim from `assets/site.css` `:root`.

- **Background:** `#0F1011` (`--ink`)
- **Text:** `#E8E6E1` (`--bone`)
- **Secondary text:** `#8B8A85` (`--smoke`)
- **Accent:** `#D1442B` (`--signal`) — large display only
- **Accent text:** `#E3603F` (`--signal-text`) — small text, the accessible one
- **Rule:** `#272A2D` (`--line`)
- **Display font:** Archivo 700, uppercase, `letter-spacing:-.02em`,
  `line-height:.98` — shipped locally as `assets/fonts/archivo-700.woff2`
- **Body font:** Archivo 400/500/600 — shipped locally
- **Visual references from the project:**
  - `design/watts-chart.svg` — inlined at its true `0 0 3000 1900` geometry
  - the ORU mark from `index.html` (circle `r=47.38` `stroke-width=17.23`
    `#E8E6E1`, rust bar `37.60,51.21 44.80x17.58` `#D1442B`)
  - the hero eyebrow / headline / spec-strip layout

## Storyboard

Use the storyboard in `brag-output/brag-plan.md` as the creative contract.

Scene summary:
1. **The line** — 6.56s — the axis, then the chart drawing itself left to right,
   the final climb resolving into the **W**, `ATTS` setting beside it, then
   `ARE OVERRATED`. Must use the real SVG geometry, not a redraw.
2. **Three laps** — 4.90s — the real hero: rust eyebrow, then
   `THREE LAPS / WHILE YOU / DID ONE.` with `ONE` in rust, then the spec strip.
3. **What I will not do** — 4.92s — three verbatim refusals arriving one at a
   time on every other beat, each holding to the end of the scene.
4. **The motor** — 6.54s — the two-line punchline on consecutive strong cues,
   then a full clear to the ORU mark, `WATTS TEE · $48`, `wearoru.com`.

## Audio

- **Audio role:** sparse professional accents over a deliberately quiet bed.
- **Audio arc:** a low bed fades in under a line drawing itself, carries four dry
  cues across twenty-three seconds without once swelling, and leaves before the
  last frame does.
- **Music:** `assets/music/happy-beats-business-moves-vol-12-by-ende-dot-app.mp3`
- **Music treatment:** volume `0.15` (the `deadpan` band is 0.12–0.18), fade in
  over the first ~1.2s, fade out across the final ~1.4s so the lockup lands in
  near-silence. Never allowed to drive the edit.
- **Music cue guidance:** bundled preset,
  `assets/music/cues/happy-beats-business-moves-vol-12-by-ende-dot-app.music-cues.json`
  (109.96 BPM, beat spacing ~0.545s). Strong-cue locks: **17.47s** (motor line),
  **18.56s** (refusal line). Beat-grid windows: W resolve at **4.39s**;
  headline lines at **6.56 / 7.09 / 7.64**; refusal list at **12.55 / 13.64 /
  14.73** (every *other* beat — 1.09s apart — so each line clears the readable
  floor).
- **Audio-reactive treatment:** **none, deliberately.** `audio.md` exempts tones
  that ask for stillness ("unless the tone asks for stillness or deadpan
  restraint"), and every good audio-reactive target — glow, breathing presence,
  background warmth — is banned outright by the source CSS's "not neon, no speed
  lines" rule. Extraction is available; it is declined on creative grounds, not
  skipped for a missing dependency.
- **Audio-coupled moments:**
  - Scene 1, W resolves at 4.39s — one dry low cue, the only reveal sound
  - Scene 3, three refusals — one identical quiet tick per arrival, no escalation
  - Scene 4, ORU mark at 21.28s — one warm accent, then silence
- **SFX selection guidance:** all picks are **low high-frequency risk** per
  `sfx-analysis.md`, since two of the three are repeated or land on a long hold:
  - `assets/sfx/impact/impactSoft_medium_002.ogg` — 0.14s, warm, low HF,
    transient — "major reveal" family; the W resolving
  - `assets/sfx/ui/rollover2.ogg` — 0.06s, balanced, low HF — "general accent";
    repeated three times unchanged for the refusal list
  - `assets/sfx/interface/bong_001.ogg` — 0.12s, warm, low HF, textured —
    "safest general pick"; the final mark
- **SFX volume:** 0.28–0.42. Below the 0.55–0.85 default band, because `deadpan`
  asks for softer values and these must sit under the bed, not on top of it.
- **Restraint rule:** no whooshes, risers, impact booms, swells or builds. If a
  cue draws attention to itself, cut it.

## Hyperframes Instructions

Built against `hyperframes-core` (composition contract + `data-*` timing),
`hyperframes-animation` (motion), `hyperframes-creative` (design spec),
`hyperframes-keyframes` (seek-safe keyframes) and `hyperframes-cli` (check /
render). `/brag` is its own workflow — the `hyperframes` entry-point intent
interview and its generic promo / launch-video workflow are deliberately not
entered.

Requirements met:

- Real project material: the actual `watts-chart.svg` geometry, the actual hero
  copy and layout, the actual ORU mark, the actual Archivo type, the actual
  palette.
- All text holds past the readable floor (short line ≥0.8s settled, sentence
  ≥0.3s/word).
- Duration 22.92s — inside 15–25s.
- Music + SFX present; audio-reactive declined on documented creative grounds.
- ≥1 major tween beat-locked within ±0.15s (`// beat-locked` at 17.47 and 18.56).
- Sequential reveals snapped to the beat grid (`// beat-grid` at 12.55 / 13.64 /
  14.73 and 6.56 / 7.09 / 7.64).
- All audio and fonts are local files under `composition/assets/`; no absolute
  paths, no runtime network dependency except the pinned GSAP CDN.
- `npx hyperframes check` is the single gate before render.
