# UGC ad — Watts tee

Customer-voice UGC for Arcads / Seedance 2.0. 9:16, 15s (Seedance's maximum).
Written to the pack's 9-layer formula (`seedance-2-ugc.md`).

**Direction chosen by the owner:** full AI UGC, customer voice. Two guardrails
kept: every product claim below exists on the site, and the finished ad carries
an `Ad · AI-generated` label.

## Reference image

`@(img1)` = `img1-print-on-heather.jpg` — the real back print (from
`design/preview-on-heather.jpg`), white on dark grey heather.

**Confirm before generating:** the catalog doesn't name a colour. This assumes
dark grey heather because that's the site's own preview. Swap the image and the
word "dark grey heather" in the prompt if the shirt will be a different colour.

## Seedance prompt

```
15 seconds UGC style honest review video, filmed on smartphone, late
afternoon light at a dirt trailhead car park, phone in one hand at a casual
selfie angle. A man in his early 30s with short messy brown hair and a
few days of stubble, natural skin with visible texture, a hint of shine on
his forehead, a light dusting of trail dust on his forearms, wearing the
@(img1) (dark grey heather t-shirt, blank front, full back print of a white
line chart whose last climb turns into the W of "WATTS" above the words
"ARE OVERRATED"), in a gravel car park — an electric mountain bike leaning
against the open side door of a van, a helmet hanging off the handlebar, a
water bottle on the van step, pine trees behind, dusty and real.

The video opens with him looking into the camera, deadpan, slightly out of
breath: "Guy at the trailhead told me my bike's cheating."

Quick jump cut — he turns his back to the camera and looks over his
shoulder so the full back print fills the frame. He says nothing for a
beat, then: "So I bought the shirt."

Jump cut — close-up, he pinches the fabric at his chest between two fingers
and rubs it: "Feels broken in straight away. Doesn't go clammy."

Final shot — back to the original angle, he glances over at the bike, then
back to camera, half-smiling: "Size up though. It runs slim." He laughs
under his breath and the clip ends mid-laugh.

Throughout the video, the tone is dry, unbothered and quietly amused — he
isn't selling anything, he's telling a mate a story. The pacing is natural
and unhurried — he leaves a beat of silence after each sentence and takes a
breath before the next line, never rushing. Each jump cut is slightly
closer or at a different angle, as if he filmed multiple takes and edited
the best bits together.

The lighting is low golden sun from one side — one side of his face in
shadow, no ring light, no filters. The image is slightly imperfect —
natural phone quality, not colour graded, slight motion blur when he
turns, auto white balance shift between cuts. The sound is direct from the
phone mic — his natural voice, light wind, distant car door, no music
underneath.

The overall feel is dry, relatable, real — a rider sending a clip to the
group chat after someone had a go at his e-bike.
```

## Timing check (read aloud, relaxed pace)

| Beat | Line | ~Time |
|---|---|---|
| 1 Hook | "Guy at the trailhead told me my bike's cheating." | 0–3.5s |
| 2 Show | *(silent back-print hold)* "So I bought the shirt." | 3.5–7s |
| 3 Proof | "Feels broken in straight away. Doesn't go clammy." | 7–11s |
| 4 Verdict | "Size up though. It runs slim." *(laugh)* | 11–15s |

About 25 spoken words, plus one silent beat. It fits 15s without rushing.

## Every claim, and where it comes from

| Line in the ad | Source on the site |
|---|---|
| "Feels broken in straight away" | index.html: "already feels broken in. No stiff first wash" |
| "Doesn't go clammy" | index.html: "without the clammy feel of a gym shirt" |
| "Size up, it runs slim" | product page: "Runs slimmer than Gildan or Hanes… take an XL" |
| e-bike / "cheating" | the print's own FAQ: "If you have ever been told your bike is cheating" |

Deliberately left out: "softest tee I own", "best shirt ever", anything about
riding a long climb in it. The site says a jersey wins there.

## After generation

Seedance renders text unreliably, so the end card goes on afterwards, not in
the prompt. Planned as a Hyperframes/ffmpeg overlay on the last ~2s:

- `WATTS TEE · $48`
- `wearoru.com`
- `Ad · AI-generated` (small, bottom corner, visible the whole clip)

Also check the back print in the output against `img1`. AI video often
garbles lettering. If "WATTS" or "ARE OVERRATED" comes out misspelled,
re-roll it or composite the real artwork over that shot.

## Before spending money on it

- The Arcads skill pack isn't installed in this session yet (blocked pending
  approval), and there's no Arcads API key here.
- Checkout returns 409 until the Printify product exists, and wearoru.com
  still runs the previous brand. Don't run paid traffic until both are fixed.
