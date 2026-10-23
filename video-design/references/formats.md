# Formats

A vertical film is not a crop of a horizontal one. Cropping loses the composition, the type scale
and the reading order; what you rebuild is the same **beat sheet** in a different container.

## Canvas and safe areas

| Format | Canvas | Margin | Content box |
|---|---|---|---|
| 16:9 | 1920×1080 | 96 (5 %) | x 96–1824, y 0–1080 |
| 9:16 | 1080×1920 | 64 (6 %) | x 64–1016, y 220–1600 |
| 1:1 | 1080×1080 | 64 | x 64–1016, y 64–1016 |

Vertical safe areas, because the platform UI owns the edges:

```
┌──────────────────┐  y 0
│   status / top   │  ▒ 0–220   platform header, handle
├──────────────────┤  y 220
│                  │
│   CONTENT BOX    │      x 64–960   ← right 120 px reserved for the like/comment rail
│   952 × 1380     │
│                  │
├──────────────────┤  y 1600
│  caption / CTA   │  ▒ 1600–1920   caption, music, buttons
└──────────────────┘  y 1920
```

Keep type inside 64–960 horizontally: a headline that runs to 1016 sits under the action rail and
looks broken in the app even though the MP4 is fine.

## Type scale per format

| Token | 16:9 | 9:16 | 1:1 |
|---|---|---|---|
| Display | 172 | 104–120 | 128–140 |
| H2 | 74 | 56–64 | 64–72 |
| Big number | 96–132 | 96–130 | 96–120 |
| Body | 21–23 | 22–24 | 21–23 |
| Label (mono) | 17–19 | 15–16 | 16–17 |
| Margin | 96 | 64 | 64 |
| Bar height | 34 | 26 | 30 |

The vertical display is roughly **0.65×** the horizontal one, not 0.5×: fewer words per line, but the
phone screen is physically narrow, so the type must stay large relative to the width.

## Structure adjustments

- **Beats get shorter.** 2–3 s for pure type, up to 3.5 s when there is a chart. Attention is more
  forgiving in a 16:9 presentation than in a feed.
- **Fewer beats.** A 20–25 s vertical holds 5–6 beats; the 16:9 release pattern with 7 beats becomes
  28–30 s, which is too long for a feed. Cut the ecosystem beat or merge specs into the end card.
- **One data point per beat.** The 2×2 counter grid becomes 2×2 with smaller type or a 1×4 stack.
  Charts adapt as: full-width horizontal bars (952 × 26), a single giant number, or a vertical axis
  with two dots — never the 1020×600 scatter.
- **End card holds 1.5–2 s**, not 2.5: the loop point is more important than the aftertaste.
- **Sound matters more.** Most vertical views autoplay with sound: a bed or voiceover is worth the
  extra step here even when the horizontal cut is silent.
- **Text safe from the first frame.** Assume the first 0.3 s is watched with the thumb already moving:
  the hook must be legible before any reveal completes.

## Rebuilding a horizontal cut as vertical

1. Keep `BRIEF`, the beat sheet and the copy deck. Do not keep the composition geometry.
2. Re-derive the type scale from the table above; do not scale the whole film by 0.56.
3. Re-lay every scene against the 952 × 1380 content box.
4. Re-time the beats to 2–3.5 s and drop or merge one.
5. Snapshot the first frame *and* a mid-beat frame at full size — vertical failures are usually
   horizontal collisions (a value over a label) that only appear once the width halves.
6. Render at 1080×1920, 30 fps, same pipeline. A 25 s vertical lands at 2–3 MB with the same settings.

**Worked example** (16.8 s vertical → 16:9, same beats and audio): the recipe card's rows became three
columns with the extraction line running the full width; the date card became two columns ("Obrim" +
time / "Dissabte" + "7 de novembre" + 2026); the motif disc moved from stacking under the wordmark to
flooding the frame and carrying the wordmark at full bleed. Type went from 126 to 152, margin from 64 to
96. Nothing was scaled by a constant — every scene was re-laid out. Then run `deadframe.py` on the new
render: the flood left a 0.23 s hole that the vertical never had.

## Aspect-ratio metadata

Set it once on the root and let the CSS flow from tokens:

```html
<div id="root" data-composition-id="main" data-width="1080" data-height="1920"
     data-duration="22" data-fps="30">
```

Keep one token block per format (`--margin`, `--ds`, `--hs`, `--num`, `--bar-h`) and switch the block,
not the scene markup. A scene built with tokens survives the format change; one built with literals
does not.
