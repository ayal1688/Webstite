# UGC ad — Watts tee

Customer-voice UGC for Arcads / Seedance 2.0. 9:16, 15s (Seedance's maximum).
Written to the pack's 9-layer formula (`seedance-2-ugc.md`).

**Owner's direction:** full AI UGC in a customer's voice. The character talks
about the shirt as ORU's fabric and calls it premium. The neck label is never
shown.

## Reference images

Cropped from the owner's mockups. The label close-up tile is left out.

| Token | File | Shows |
|---|---|---|
| `@(img1)` | `img1-front-black.jpg` | black tee, ORU mark on the left chest |
| `@(img2)` | `img2-back-black.jpg` | black tee, WATTS / ARE OVERRATED back print |
| — | `img3-front-navy.jpg` | navy colourway — see [Navy version](#navy-version) |

Pass them in this order in `referenceImages`: index 0 = `@(img1)`, 1 = `@(img2)`.

## Seedance prompt — black

```
15 seconds UGC style honest review video, filmed on smartphone, late
afternoon light at a dirt trailhead car park, phone in one hand at a casual
selfie angle. The woman from @(img1) — long dark brown hair, natural skin
with visible texture, light freckles, a hint of shine on her forehead,
small hoop earrings, a light dusting of trail dust on her forearms —
wearing the black t-shirt from @(img1) with the small ORU circle mark on
the left chest, and the full back print from @(img2): a white line chart
whose last climb turns into the W of "WATTS" above "ARE OVERRATED". The
shirt from @(img1) and @(img2) must remain visually unchanged in every
shot. The collar is always framed from the outside — the inside neck label
is never visible. She stands in a gravel car park — an electric mountain
bike leaning against the open side door of a van, a helmet hanging off
the handlebar, a water bottle on the van step, pine trees behind, dusty
and real.

The video opens with her looking into the camera, deadpan, slightly out of
breath: "Guy at the trailhead told me my bike's cheating."

Quick jump cut — she turns her back to the camera and looks over her
shoulder so the full back print fills the frame. She says nothing for a
beat, then: "So I got the shirt."

Jump cut — close-up at chest height, she pinches the fabric below the ORU
mark between two fingers and rubs it, collar out of frame: "And honestly?
ORU's fabric is premium. So soft."

Final shot — back to the original angle, she glances over at the bike,
then back to camera, half-smiling: "Three laps to his one, by the way."
She laughs under her breath and the clip ends mid-laugh.

Throughout the video, the tone is dry, unbothered and quietly amused — she
isn't selling anything, she's telling a friend a story. The pacing is
natural and unhurried — she leaves a beat of silence after each sentence
and takes a breath before the next line, never rushing. Each jump cut is
slightly closer or at a different angle, as if she filmed multiple takes
and edited the best bits together.

The lighting is low golden sun from one side — one side of her face in
shadow, no ring light, no filters. The image is slightly imperfect —
natural phone quality, not colour graded, slight motion blur when she
turns, auto white balance shift between cuts. The sound is direct from the
phone mic — her natural voice, light wind, distant car door, no music
underneath.

The overall feel is dry, relatable, real — a rider sending a clip to the
group chat after someone had a go at her e-bike.
```

## Navy version

Same script, setting and timing as the black version, so the two work as an
A/B colour test. Only the shirt changes.

| Token | File | Used for |
|---|---|---|
| `@(img1)` | `img3-front-navy.jpg` | shirt colour, front mark, the person |
| `@(img2)` | `img2-back-black.jpg` | **print artwork only** — this is the black shirt |

There's no navy back mockup, so the prompt tells the model to take only the
artwork from `@(img2)` and keep the shirt navy. Check the turn-around shot: if
the back comes out black, re-roll it. A navy back mockup would fix this for good.

```
15 seconds UGC style honest review video, filmed on smartphone, late
afternoon light at a dirt trailhead car park, phone in one hand at a casual
selfie angle. The woman from @(img1) — long dark brown hair, natural skin
with visible texture, light freckles, a hint of shine on her forehead,
small hoop earrings, a light dusting of trail dust on her forearms —
wearing the navy blue t-shirt from @(img1) with the small ORU circle mark
on the left chest. The back of the same navy shirt carries the full back
print shown in @(img2): a white line chart whose last climb turns into the
W of "WATTS" above "ARE OVERRATED". Use @(img2) only for the print
artwork — the shirt is navy blue on the front and the back, never black.
The navy shirt and its prints must remain visually unchanged in every
shot. The collar is always framed from the outside — the inside neck label
is never visible. She stands in a gravel car park — an electric mountain
bike leaning against the open side door of a van, a helmet hanging off
the handlebar, a water bottle on the van step, pine trees behind, dusty
and real.

The video opens with her looking into the camera, deadpan, slightly out of
breath: "Guy at the trailhead told me my bike's cheating."

Quick jump cut — she turns her back to the camera and looks over her
shoulder so the full back print on the navy shirt fills the frame. She
says nothing for a beat, then: "So I got the shirt."

Jump cut — close-up at chest height, she pinches the navy fabric below the
ORU mark between two fingers and rubs it, collar out of frame: "And
honestly? ORU's fabric is premium. So soft."

Final shot — back to the original angle, she glances over at the bike,
then back to camera, half-smiling: "Three laps to his one, by the way."
She laughs under her breath and the clip ends mid-laugh.

Throughout the video, the tone is dry, unbothered and quietly amused — she
isn't selling anything, she's telling a friend a story. The pacing is
natural and unhurried — she leaves a beat of silence after each sentence
and takes a breath before the next line, never rushing. Each jump cut is
slightly closer or at a different angle, as if she filmed multiple takes
and edited the best bits together.

The lighting is low golden sun from one side — one side of her face in
shadow, no ring light, no filters. The image is slightly imperfect —
natural phone quality, not colour graded, slight motion blur when she
turns, auto white balance shift between cuts. The sound is direct from the
phone mic — her natural voice, light wind, distant car door, no music
underneath.

The overall feel is dry, relatable, real — a rider sending a clip to the
group chat after someone had a go at her e-bike.
```

## Timing check (read aloud, relaxed pace, both versions)

| Beat | Line | ~Time |
|---|---|---|
| 1 Hook | "Guy at the trailhead told me my bike's cheating." | 0–3.5s |
| 2 Show | *(silent back-print hold)* "So I got the shirt." | 3.5–7s |
| 3 Fabric | "And honestly? ORU's fabric is premium. So soft." | 7–11.5s |
| 4 Verdict | "Three laps to his one, by the way." *(laugh)* | 11.5–15s |

About 26 spoken words, plus one silent beat. It fits 15s without rushing.

## Claims

- **"ORU's fabric", "premium", "so soft"** — brand ownership and subjective
  feel. Fine as written.
- **Not said, on purpose:** "custom", "developed", "exclusive", "our own
  blend", or any material or performance claim. The blank is a stock Hanes
  Cool Dri, so an origin claim is disproved by flipping the collar. Material
  and performance lines can be added once they're checked against the live
  wearoru.com description, which this environment can't reach yet.
- **No price in the dialogue.** It goes on the end card, taken from the live
  site.

## After generation

- **Check the print.** AI video often garbles lettering. If "WATTS" or "ARE
  OVERRATED" comes out wrong, re-roll the clip, or composite the real artwork
  over that shot.
- **Check the collar.** If a label shows up in any frame, re-roll or crop.
- **End card** (overlay, last ~2s): `WATTS TEE · $62.00` and
  `wearoru.com`, plus a small `Ad · AI-generated` in a corner for the whole
  clip. Seedance renders text badly, so this goes on afterwards.

## To generate

1. Allow `external-api.arcads.ai` (and `wearoru.com`) in the environment's
   network access settings.
2. Add the Arcads key as an environment variable named `ARCADS_BASIC_AUTH`.
3. Start a new session and re-run the Arcads pack install
   (`/home/user/arcads-claude-code`, lost when this container resets). Then
   send each prompt with its references:
   - **black:** `img1-front-black.jpg`, `img2-back-black.jpg`
   - **navy:** `img3-front-navy.jpg`, `img2-back-black.jpg`

## Free route: talking photo + local edit

Built without Arcads, in `edit/` (black) and `edit-navy/` (navy), 1080×1920, 14.6s.

- **Voiceover:** `edit/assets/vo/vo-full.wav`, local Kokoro TTS, voice `af_heart`.
  Voice samples to compare are in `edit/assets/vo/test-af_*.wav`.
- **Previews:** `ugc-watts-black-preview.mp4`, `ugc-watts-navy-preview.mp4`.
  The talking slot currently shows the still mockup.

To finish:
1. Upload the front mockup (`img1-front-black.jpg` / `img3-front-navy.jpg`)
   plus `vo-full.wav` to a talking-photo tool. Export it 9:16, full length,
   with the audio starting at 0.
2. Save it as `edit/assets/talk.mp4`, and in `index.html` replace
   `<img id="front-img" …>` with
   `<video id="front-img" src="assets/talk.mp4" muted playsinline></video>`.
   Keep `vo-full.wav` as the audio track.
3. Run `npx hyperframes check`, then `npx hyperframes render`.

The navy edit cuts to the black back mockup until there's a navy one.
