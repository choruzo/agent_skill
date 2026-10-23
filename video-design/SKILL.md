---
name: video-design
description: >
  Design doctrine for short-form video that must look like a studio made it: launch and product
  promos, model or release announcements, benchmark explainers, data-driven motion graphics, title
  cards, spec strips and end cards, in 16:9, 9:16 or 1:1. Use it whenever the job includes deciding how a
  video should look — palette, type scale, grid, margins, scene order, charts, counters, pacing,
  transitions — not just how to encode it. It adapts to a requested style, brand, era or mood
  (warm, brutalist, cinematic, retro, luxury, Apple-like, a brand's own assets) and falls back to a
  default house style only when the brief gives no signal. Trigger it even when the user gives no
  visual direction ("make a video about X"), asks for something "premium", "clean", "less
  AI-looking", or wants an existing cut restyled. Assumes HyperFrames as the renderer and pairs with
  the hyperframes-* skills; the design rules themselves are renderer-agnostic.
---

# Video Design — invariants first, style second

Two separate things decide whether a video looks authored:

1. **Invariants** — what makes motion typography readable and expensive in *any* style: one idea per
   beat, a single scale hierarchy, real margins, contrast as a gate, honest data.
2. **Style** — temperature, type, texture, motion character. This must come **from the brief**, not
   from the model's habits.

The most expensive mistake in this skill is applying a default look to a brief that asked for
something else. A casino launch, a research lab report and a children's app cannot share a palette.
Read §2 before writing a single token; use §3 only when the brief is silent.

`references/presets.md` — five complete presets plus the axis→token derivation table.
`references/scene-recipes.md` — copy-paste code per beat, all accent usage tokenised.
`references/formats.md` — 16:9 / 9:16 / 1:1 canvases, type scales and vertical safe zones.
`references/qa-loop.md` — the verification loop that catches what eyes miss.
`scripts/deadframe.py` — finds flat stretches with no content in a rendered MP4.
`assets/starter/` — a passing 3-scene skeleton in the default preset (HTML + vendored fonts + GSAP).

```
cp -r <skill>/assets/starter/. <scaffolded-project>/   # then edit index.html
```

## 1. Invariants

These survive every style change. Break them and the piece looks amateur, whatever the palette.

1. **One idea per beat.** Three elements maximum. If deleting something loses nothing, delete it.
2. **One type system.** Two families maximum, and a scale ratio of at least 3× between the smallest
   label and the largest display. Three sizes that are all "medium" read as indecision.
3. **Margins are structural.** One inset, 4–6 % of the short side (96 px on 1920), identical on every
   scene, crossing nothing. Consistency here is most of looking professional.
4. **Contrast is a gate, not a taste.** Body ≥ 4.5:1, large text ≥ 3:1, measured against the actual
   background — including light backgrounds, where the failure flips (your "muted" must get *darker*).
5. **Never fade text over a contrast-critical fill.** An opacity entrance passes through every
   intermediate colour, so a cream line on terracotta that measures 5:1 at rest sits at 1.8:1 mid-fade.
   Reveal text with a mask, a wipe or a hard cut instead — full opacity from its first visible pixel.
6. **One dominant emphasis device.** Accent colour **or** size **or** weight. If colour and size and
   weight all shout, nothing is emphasised.
7. **Beat length 2.5–5 s**, one gesture per element, 0.5–1.2 s, ease-out in and ease-in out. No
   ambient drift, no rotation unless the style calls for it.
8. **Cut, don't dissolve — and never cut to nothing.** Hard cuts are correct. If you fade the
   outgoing wrapper, the incoming beat must be on screen by the time it reaches empty: a gap of even
   0.3 s reads as a hiccup, and it silently eats 5–10 % of a short film. `scripts/deadframe.py` finds
   these holes in the render.
9. **Data gets the biggest type in the film.** A number the viewer has to squint at is not evidence.
10. **Honesty.** Every number traceable to the source; the headline sentence must survive contact with
   the benchmarks you lose. Re-scaling an axis to win is a lie the audience can feel.
11. **The style is one decision, applied everywhere.** Half a preset looks worse than either preset.

## 2. Style intake — decide the look before writing tokens

Work down this list and stop at the first signal that resolves:

1. **An explicit request.** "Cinematic", "brutalist", "like Apple", "años 70", "lujo tranquilo",
   "para adolescentes". Obey it, even when it contradicts the default preset.
2. **Brand assets.** A site, deck, logo or app screenshot. Extract, don't invent: dominant background,
   one accent, the type pairing, corner radius (sharp or soft), density (sparse or packed).
3. **The subject.** A bank, a synth plugin, a research lab, a fashion drop and a developer tool each
   imply a different temperature before anyone says a word.
4. **Nothing?** Use preset A (Technical Editorial).

Then read the brief along five axes and make one choice per axis — full mapping in `presets.md`:

| Axis | Range | Decides |
|---|---|---|
| Temperature | cold ↔ warm | background hue, accent, grain vs. grid |
| Density | sparse ↔ packed | margins, how many elements per beat |
| Era | now ↔ retro | type choice, texture, whether motion snaps or glides |
| Energy | calm ↔ punchy | ease curves, cut length, scale of the type |
| Material | digital ↔ print ↔ film | flat fills vs. rules vs. grain, shadows, blur |

If a request conflicts with an invariant — "use four accent colours", "put a paragraph centred" — keep
the invariant and satisfy the intent (four *tints of one hue*; a centred two-line statement, not a
centred paragraph). Explain the trade-off in one line rather than silently overriding either side.

## 3. Presets

| | Preset | For | Signature |
|---|---|---|---|
| **A** | Technical Editorial (default) | model/infra launches, benchmarks, dev tools | near-black, one electric accent, grotesque + mono, faint grid |
| **B** | Warm Print | brands, culture, food, architecture, editorial | cream paper, ink, serif display, terracotta/oxblood, hairlines |
| **C** | Brutalist / Punch | consumer apps, events, music, youth | off-white or acid, black type, hard shadows, snappy 0.25 s cuts |
| **D** | Cinematic / Luxury | fashion, film, finance-premium, hardware | deep charcoal, one muted metal, wide tracking, slow fades, grain |
| **E** | Terminal | security, OSS, CLI tooling, hacker-adjacent | mono only, one hue on black, typewriter reveals, no gloss |

Full token blocks, font pairings, motion signatures and per-preset do/don't live in
`references/presets.md`. Presets are starting points, not straitjackets: a brand asset always wins
over a preset, and a hybrid (Cinematic palette + Technical Editorial structure) is normal.

## 4. Restyling is a token swap

Every accent usage in the recipes goes through tokens, so changing a preset never touches scene code:

```css
:root{
  --bg; --ink; --muted; --dim; --line;
  --accent;          /* the emphasis hue */
  --accent-mid;      /* accent text on dark bg */
  --accent-soft;     /* 14–18 % fill */
  --accent-line;     /* 35–55 % border */
  --accent-glow;     /* element bloom, 55–70 % */
  --accent-bloom;    /* background wash, 18–22 % */
}
```

Changing style = replace that block, the two `@font-face` pairs, and the texture layers
(`.bg-grid` vs. grain vs. flat). If a scene needs a literal hex to look right, the preset is
under-specified — add a token instead.

## 5. Structure (style-independent)

**A. Release / announcement (20–30 s)** — the flagship pattern:

| Beat | Time | What it does |
|---|---|---|
| Title | 0–4 s | Name at display size, one line of positioning |
| The claim | 4–9 s | The one comparison that states the thesis |
| Proof 1 | 9–15 s | Bars: the biggest numeric jumps |
| Proof 2 | 15–20 s | Counter grid: breadth, four at a glance |
| Specs | 20–23 s | Four facts as giant values |
| Ecosystem | 23–26 s | The second announcement, one line |
| End card | 26–end | Wordmark, version, date. Hold 2 s minimum |

**B. Single-stat explainer (8–12 s)**: hook → the number → what it means → logo.
**C. Feature/product (15–20 s)**: problem → the thing → proof → CTA, told by contrast between beats.

Ordering principle: claim before evidence, magnitude before breadth, one visual metaphor per film.
Never open with a dashboard; open with a sentence. In 9:16, drop one beat and merge specs into the
end card — see `references/formats.md`.

## 6. Formats

The beat sheet is format-independent; the geometry is not. Decide the canvas before the type scale.

| | 16:9 (1920×1080) | 9:16 (1080×1920) | 1:1 (1080×1080) |
|---|---|---|---|
| Margin | 96 | 64 | 64 |
| Display | 172 | 104–120 (≈0.65×, not 0.5×) | 128–140 |
| H2 | 74 | 56–64 | 64–72 |
| Beats | 2.5–5 s | 2–3.5 s | 2.5–4 s |
| Film length | 20–30 s / 7 beats | 15–25 s / 5–6 beats | 15–25 s |
| End card hold | 2 s | 1.5–2 s | 2 s |

Vertical needs **safe areas**: ~220 px at the top and ~320 px at the bottom are covered by platform UI,
and ~120 px on the right by the action rail. Keep type inside `x 64–960, y 220–1600`; an MP4 that looks
fine on the desktop can sit under the caption bar in the app.

A vertical cut is a **re-layout, not a crop**. Keep the beat sheet and the copy, rebuild the geometry
from the 9:16 scale, drop or merge one beat, and re-check for horizontal collisions — halving the width
is what turns a clean frame into overlapping labels. Full tables and the rebuild procedure live in
`references/formats.md`.

## 7. Charts, adapted to the style

The mechanics are constant; the costume changes.

- **Scatter** for trade-offs: two labelled axes, one arrow from old to new, both points labelled with
  value *and* cost. No legend. Works in A, B, D; in C replace the arrow with a hard diagonal rule; in
  E draw it as ASCII if that is the joke.
- **Bars** for magnitude: one shared scale for comparable metrics — a shorter bar that means more is
  a lie the viewer can feel. In B/D make them thin rules rather than blocks.
- **Counters** for breadth: 2×2 maximum; previous small and muted, new large and accent.
- **Spec strips** for facts: four columns, hairline dividers, no icons. In D, drop the dividers.

Never draw an axis you do not label, and never animate a chart before its frame exists.

## 8. Honesty

The design must not outrun the evidence. Every on-screen number comes from the source; the headline
survives the losing benchmarks ("Ahead on agents. Closing on reasoning." reads as confidence, "the
best model" reads as marketing). If a metric is behind, either leave it out of the hero beats or put
it in a footnote band — never quietly re-scale the axis. Specific, defensible claims are also the
better design: they give the type something worth setting large.

## 9. HyperFrames traps that change design decisions

- **A mask carries the type size.** `<h2 class="mask"><span>…</span></h2>` — a plain `div` mask
  silently renders the title at 16 px.
- **Never CSS-translate a node you then GSAP-scale.** `translate(-50%,-50%)` + a `scale` tween is a
  lint conflict; centre with negative margins.
- **Pad the mask** `0.24em` bottom (with the same negative margin) or descenders clip.
- **Vendor fonts and GSAP.** Local `@font-face` files + a local `gsap.min.js`. CDNs break determinism;
  a named family without `@font-face` fails lint. Light presets need their own colour floor.
- **Grey has a floor per background.** On near-black, `--dim` below ~`#7C818E` fails 4.5:1; on cream,
  nothing above ~`#6B665D` passes.
- **Timing lives on the root.** Length is the root `data-duration`; a clip past it is cut.
- **Light backgrounds are a different film.** Glow, shadows and 3 px accent rails that work on black
  look cheap on paper — switch to rules, paper grain and ink.

## 10. Workflow

1. **Harvest the facts.** Every number, unit and qualifier into a table with its source.
2. **Name the style in one sentence**, with its axis choices ("warm print, sparse, retro-serif, calm").
   If you cannot write that sentence, the brief is unresolved — decide, don't drift.
3. **Choose format and structure** (§6, §5) and write the beat sheet as time ranges before any code.
4. **Set tokens + fonts + texture**; scaffold from `assets/starter/` and replace the token block.
5. **Build one scene at a time**, snapshotting it before moving on.
6. **Run the QA loop** (`references/qa-loop.md`): lint → check → snapshots → render → frame grid →
   `scripts/deadframe.py`.
7. **Read rendered frames, not code.** Every defect that matters is visible in a contact sheet.
8. **Sound, if there is any.** A synthesised bed is enough for a 20 s piece: a low drone, a little room
   air, and one soft event per cut, around −18 LUFS with peaks near −10 dBFS. No licences, no network.
   The agent cannot judge how it sounds — ask the person to listen before calling the piece finished.
9. **Hand over the source plus a poster and a note**: MP4, a still PNG for the thumbnail, and a
   `DESIGN.md` of half a page (format and why, palette, type, beat table). The HTML is the deliverable;
   the MP4 is an export.

## 11. Anti-patterns

Universal slop: purple-blue gradient meshes · emoji as iconography · drop shadows on text ·
glassmorphism panels · three families · centred paragraphs · stock footage of people at laptops ·
"AI sparkle" glyphs · animated background blobs · numbers without units · axes without labels · a
different accent per scene · a logo larger than the claim · music that fights the cut.

Style-specific traps: applying preset A to a brief that asked for warmth, playing it "safe" with a
neutral beige that means nothing, importing a preset's texture into a strict brand system, and
treating "minimal" as "empty" instead of "exact".
