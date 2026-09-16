# Brag Plan: ORU — Watts tee

## What is this app?

ORU is a one-person e-enduro apparel brand from Haifa selling exactly one thing —
a $48 Bella+Canvas 3001CVC heather tee with a full back print of a stock chart
whose final climb turns into the **W** of WATTS, above ARE OVERRATED. It is a
joke aimed squarely at everyone who has been told an e-bike is cheating, sold on
a site that refuses to run a countdown, invent a review, or call a t-shirt
technical.

## The angle

**The line is the product, and you don't know that until it finishes drawing.**

The site's own strongest asset is `design/watts-chart.svg` — a chart making higher
highs and higher lows where the last zigzag *is* a letter. That's a visual
reveal nobody has to explain: for four seconds the viewer watches what looks like
a market chart climb, and then it stops being a chart and becomes a word.

Everything after that is the brand refusing to sell you anything, in its own
words. No invented photography, no invented claim, no invented review — because
the brand's entire pitch is that it doesn't do that. The video is specific to ORU
because a video that behaved like a normal product ad would be lying about the
product.

## Hook (first 2-3 seconds)

Near-black frame. A thin axis. A white line starts climbing from the bottom left,
one step at a time, higher highs and higher lows. No title, no logo, no copy.
Just a line going up, drawn at a deliberate pace. The question the hook plants is
"what am I looking at" — and the answer arrives at 4.4s when the last climb
resolves into a **W** and ATTS sets beside it.

## Key moments (the middle)

- The chart line's final zigzag landing as the **W**, with `ATTS` setting flush
  beside it — the real production geometry, not a recreation.
- The actual site hero, in real Archivo: **THREE LAPS / WHILE YOU / DID ONE.**
  with `ONE` in the brand rust `#D1442B`.
- The About page's "What I will not do" list, arriving one line at a time:
  *Call a t-shirt technical · Invent reviews · Run a fake countdown.* The three
  things this brand won't do, shown deadpan, in a video that is itself an ad.

## Outro / punchline

Two lines from the About page, the brand's whole position in eleven words:

> **Yes, it has a motor.**
> **No, I am not going to argue about it.**

Then everything clears to the ORU mark, `WATTS TEE · $48`, `wearoru.com`, and a
long hold on empty space.

## User flow worth showing

None — landing-page-only static storefront. The buy flow is a size picker and a
PayPal handoff, and the product cannot currently be bought at all (the Printify
product doesn't exist yet and `/api/checkout` returns 409 by design). Showing a
checkout would be showing something that does not work. The video relies on the
strongest visual instead: the print artwork resolving itself, plus the real hero.

## Tone

- **Preset:** `deadpan`
- **Creative direction:** *a line going up, explained as little as possible*
- **Interpretation:** Long holds, one thought per scene, slow crossfades, and a
  lot of empty near-black. The pace is the joke — the video never raises its
  voice, which is the only register this brand's copy would tolerate.

**Documented deviation from the preset:** `deadpan` calls for mixed-case
typography. ORU's own CSS sets every heading to `text-transform:uppercase` in
Archivo 700, so display lines stay uppercase to remain brand-true. The deadpan
feel is carried by pacing, restraint and empty space instead of by letter case.

## Format: landscape — 1920x1080
## Duration: 22.92s

## Visual identity (from the project)

Taken verbatim from `assets/site.css` `:root`.

- **Background:** `#0F1011` (`--ink`)
- **Raised panel:** `#16181A` (`--carbon`)
- **Accent:** `#D1442B` (`--signal`, "rust. dirt, not neon")
- **Accent text:** `#E3603F` (`--signal-text`, the accessible one for small text)
- **Text:** `#E8E6E1` (`--bone`)
- **Secondary text:** `#8B8A85` (`--smoke`)
- **Rule:** `#272A2D` (`--line`)
- **Display font:** Archivo 700, `letter-spacing:-.02em`, `line-height:.98`, uppercase
- **Body font:** Archivo 400
- **Strongest visual element:** `design/watts-chart.svg` — the chart-into-W
  lockup, used as real vector geometry and drawn on, not redrawn by hand.

**Hard constraint from the source CSS header:** *"Deliberately not: neon on black,
italic display type, speed lines."* No glow, no neon, no motion streaks, no
speed lines anywhere in this video.

## Share copy (draft)

> A chart making higher highs and higher lows, where the last climb turns into
> the W. WATTS ARE OVERRATED — $48, made to order, never on sale. Yes, it has a
> motor. No, I'm not going to argue about it. wearoru.com

## Audio direction

- **Role:** Quiet bed with sparse, dry accents. The audio must never sell.
- **Music:** `happy-beats-business-moves-vol-12-by-ende-dot-app.mp3` (109.96 BPM,
  117.36s). Chosen over vol-10 because its strong cues spread across the whole
  0-25s window instead of clustering at 18-24s.
- **Music treatment:** Start at 0 with a short fade-in, sit low throughout
  (roughly -18 dB posture — present but never foreground), fade out over the last
  ~1.4s so the final lockup lands in near-silence.
- **Music cue guidance:** Preset read from
  `assets/music/cues/happy-beats-business-moves-vol-12-by-ende-dot-app.music-cues.json`.
  Target strong cues: **17.47s** (the motor line), **18.56s** (the refusal line),
  **22.93s** (final frame out). Beat grid spacing is ~0.545s; the three-item
  sequential reveal in Scene 3 snaps to **every other beat** (12.55 / 13.64 /
  14.73 — 1.09s apart) so each line clears the readable floor.
- **Audio-reactive treatment:** None. Reactive glow or breathing presence would
  violate the source CSS's "not neon" rule and the deadpan register.
- **SFX posture:** Sparse. Four cues in the whole video, all dry and quiet.
- **Audio-coupled moments:** the W resolving; the three refusal lines arriving
  one by one; the final lockup.
- **Restraint rule:** No whooshes, no risers, no impact booms, no cinematic
  swells, no build. Nothing that sounds like it is trying to make you buy a
  t-shirt. If a cue draws attention to itself, cut it.

## Storyboard

### Scene 1 — The line — 6.56s (0.00 → 6.56)

Near-black `#0F1011`, full frame, generous margins. The thin axis pair fades up
first (`#E8E6E1`, 12px stroke in the source viewBox). From 1.0s the chart path
draws left to right at a steady rate, stepping up through its higher highs and
higher lows. At ~4.39s the final zigzag completes and *is* the **W**; `ATTS` sets
flush beside it on the same baseline. At ~5.34s `ARE OVERRATED` fades in below
right. Full lockup holds 5.34 → 6.56.

Must use the real geometry from `design/watts-chart.svg` — the W is drawn to
Archivo's actual metrics (cap height 0.69em, stem 0.11em, stroke 40 against a
stem of 34 because diagonals read thinner than verticals). Do not redraw it.

Sequential/interaction: yes — the path draws progressively as a single stroke
reveal, then `ATTS` and `ARE OVERRATED` arrive in that order.
Audio intent: almost nothing. Music enters under the axis, very low. The draw
itself is silent — the line climbing should feel matter-of-fact.
Audio-coupled idea: one dry, quiet tick at ~4.39s when the W resolves and `ATTS`
sets. Single cue, no layering.
Music: low bed, fading in from 0.
Transition mood: slow crossfade (0.9s) → Scene 2

### Scene 2 — Three laps — 4.90s (6.56 → 11.46)

The real site hero, rebuilt crisply in Archivo rather than scaled from a
screenshot. Rust eyebrow `TRAILHEAD · VAN · PUB` in `#E3603F`, then the headline
in three lines, left-aligned, `#E8E6E1`:

```
THREE LAPS
WHILE YOU
DID ONE.
```

`ONE` in `#D1442B`, exactly as the site marks it. Lines arrive quickly (6.56 /
7.09 / 7.64, one beat apart) and then the **whole set holds 7.64 → 11.46**, which
is what earns the read. At the 10.93s strong cue the spec strip fades in small
and quiet beneath: `ULTRA-SOFT BLEND · MADE TO ORDER · SHIPPED WORLDWIDE`.

Sequential/interaction: yes — three headline lines one beat apart, then a long
settled hold on the complete headline.
Audio intent: the bed continues, unchanged. Nothing marks the headline — it
should feel like the video simply cut to a page.
Audio-coupled idea: none. Deliberately unscored.
Music: low bed, steady.
Transition mood: clean cut → Scene 3

### Scene 3 — What I will not do — 4.92s (11.46 → 16.38)

Rust eyebrow `WHAT I WILL NOT DO` at 11.46. Then three lines arrive one at a
time on every other beat — 12.55 / 13.64 / 14.73 — each in `#E8E6E1`, stacked
with a hairline `#272A2D` rule between them:

```
Call a t-shirt technical
Invent reviews
Run a fake countdown
```

Verbatim from `about.html`. The full set holds 14.73 → 16.38.

Sequential/interaction: yes — three items, 1.09s apart (every other beat), each
holding to the end of the scene so the earliest line is on screen for 3.8s.
Audio intent: dry and administrative. Three identical quiet ticks, like items
being checked off a list by someone who isn't enjoying it.
Audio-coupled idea: one quiet tick per item arrival, same file each time, no
escalation in pitch or volume.
Music: low bed, steady.
Transition mood: slow crossfade (0.9s) → Scene 4

### Scene 4 — The motor — 6.54s (16.38 → 22.92)

Empty near-black. At the 17.47s strong cue, centred and large:

```
YES, IT HAS A MOTOR.
```

At the 18.56s strong cue, beneath it, quieter and in `#8B8A85`:

```
NO, I AM NOT GOING TO ARGUE ABOUT IT.
```

Both hold to 21.28 — the second line gets 2.72s settled, which is the readable
floor for nine words. Everything clears, and at 21.28 the ORU mark (the circle
and rust bar from the site's inline SVG) fades up centred with, beneath it:

```
WATTS TEE · $48
wearoru.com
```

Long hold on mostly-empty frame, 21.28 → 22.92. Music fades out across the last
~1.4s so the final second is effectively silent.

Sequential/interaction: yes — two lines on consecutive strong cues, then a full
clear to the lockup.
Audio intent: the bed thins and leaves. The last frame should be quiet enough
that it reads as the end of a statement rather than the end of an ad.
Audio-coupled idea: one dry, low cue on the ORU mark at 21.28. Nothing on the
two text lines — they land in the music, unmarked.
Music: low bed through 21.28, then fade to silence by 22.92.
Transition mood: hold to black → end

**Music mood for this video:** deadpan — an upbeat track deliberately held low
and never allowed to drive the edit.
**Audio summary:** A quiet bed fades in under a line drawing itself, carries four
dry ticks across twenty seconds without once swelling, and leaves before the last
frame does.
