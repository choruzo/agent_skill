# Presets and style derivation

Five complete looks. A preset is a **starting token block**, not a rule: brand assets beat presets,
and hybrids are normal (Cinematic palette + Technical Editorial structure works well).

All contrast ratios below were measured against the preset's own background. Re-check after any
tweak — `hyperframes check` will catch it, but knowing the floor saves a cycle.

## Axis → token derivation

When the brief names a feeling instead of a look, translate it on these five axes. One choice each.

| Axis | Low end | High end | What it changes |
|---|---|---|---|
| **Temperature** | cold (blue-grey, steel) | warm (cream, oxblood, amber) | background hue, accent family, grain vs. grid |
| **Density** | sparse (3 elements, 40 % empty) | packed (tables, 6+ elements) | margins, type scale, how much per beat |
| **Era** | now (grotesque, flat) | retro (serif, texture, rounded) | families, corner radius, texture |
| **Energy** | calm (0.9–1.2 s eases, holds) | punchy (0.25–0.45 s, hard cuts) | durations, ease curves, overshoot |
| **Material** | digital (flat, glow) | print / film (rules, grain, no glow) | shadows, borders, background layers |

Adjective → choices, as used in practice:

| The user says | Temperature | Type | Motion | Material |
|---|---|---|---|---|
| "premium", "lujo", "Apple-like" | cold, very low saturation | one grotesque, tight tracking, huge sizes | slow fades 0.8–1.2 s, no bounce | flat, no shadows, vast space |
| "editorial", "revista", "cultural" | warm cream | serif display + grotesque body | 0.6–0.9 s, soft | hairlines, paper grain |
| "brutal", "punk", "para jóvenes" | acid or off-white | one heavy grotesque, mono labels | 0.2–0.4 s, hard cuts, overshoot | hard offset shadows, no gradients |
| "cinematográfico", "film", "moda" | deep charcoal, one metal | wide-tracked light grotesque or serif caps | 1.0–1.5 s dissolves, slow scale | grain, vignette, letterbox |
| "técnico", "dev", "seguridad" | black + one hue | mono only, or grotesque + mono | 0.4–0.8 s, typewriter | grid, scanlines, glow |
| "divertido", "colorido" | light bg, 1 saturated hue | rounded or heavy grotesque | 0.3–0.5 s, bounce allowed | flat shapes, thick outlines |

Two accents is the maximum in any preset, and the second must mean something.

---

## A · Technical Editorial (default)

Model/infra launches, benchmarks, dev tooling. Reads as a lab notebook laid out by an art director.

```css
:root{
  --bg:#05060A;          --ink:#F5F6F8;      /* 18.7:1 */
  --muted:#9196A3;       /* 6.8:1 */         --dim:#7C818E;   /* 5.2:1 */
  --line:rgba(255,255,255,.09);
  --accent:#4D6BFE;      /* 4.7:1 */         --accent-mid:#B9C4FF;  /* 12:1 */
  --accent-soft:rgba(77,107,254,.16);
  --accent-line:rgba(77,107,254,.38);
  --accent-glow:rgba(77,107,254,.65);
  --accent-bloom:rgba(77,107,254,.20);
}
```

**Type** Inter (variable, tight −0.048em) + JetBrains Mono. Display 172, h2 74, number 96–132,
label 18 uppercase/0.24em, footnote 17.
**Texture** 64 px grid masked to an ellipse, one blue bloom top-right, vignette.
**Motion** mask reveal 1.05 s `power4.out`, scaleX draws, count-ups, one `back.out(2.4)` pop.
**Charts** scatter with a drawn connector, bars on a 0–100 scale, 2×2 counters.
**Do** numbers ≥ 90 px · mono for every unit · footnotes at y≈900.
**Don't** add a second accent · use glow on light elements · let a chart exist without axes labels.

---

## B · Warm Print

Brands, culture, food, architecture, editorial. Paper, not screen.

```css
:root{
  --bg:#F4EFE6;          --ink:#1A1714;      /* 15.6:1 */
  --muted:#5F5A52;       /* 6.0:1 */         --dim:#6E675C;   /* 4.9:1 */
  --line:rgba(26,23,20,.16);
  --accent:#B34424;      /* 4.9:1 */         --accent-mid:#8A3A20;  /* 6.8:1 */
  --accent-soft:rgba(179,68,36,.10);
  --accent-line:rgba(179,68,36,.35);
  --accent-glow:rgba(179,68,36,0);
  --accent-bloom:rgba(179,68,36,.06);
}
```

**Type** `InstrumentSerif.woff2` (shipped) at 168 / lh .96 / tracking −.012em, + Inter for body and
labels. Instrument Serif only has a 400 weight — that is the point; do not fake a bold. Display 140–190 with normal tracking (serifs hate −0.05em); h2 64; numbers 90–120.
**Texture** paper grain at 4–6 % over the cream, hairline rules, generous top/bottom margins, a page
number in mono bottom-right instead of a progress rail.
**Motion** 0.6–0.9 s `power2.out`; fades and slow slides, **no scale pops, no glow**. Words can rise
line by line.
**Charts** thin rules and dots, ink strokes 1.5 px, no filled bars — use underlined values.
**Do** leave wide margins · set text in one column · use rules to separate.
**Don't** use electric accents, drop shadows or glow — they destroy the paper illusion.

---

## C · Brutalist / Punch

Consumer apps, events, music, youth. Loud on purpose, still disciplined.

```css
:root{
  --bg:#F2F0E9;          --ink:#0B0B0B;      /* 17.3:1 */
  --muted:#4A4A46;       /* 7.8:1 */         --dim:#57574F;   /* 6.4:1 */
  --line:#0B0B0B;
  --accent:#D42B00;      /* 4.4:1 — large text only */
  --accent-mid:#A31F00;  /* safe for body */
  --accent-soft:rgba(212,43,0,.12);
  --accent-line:#0B0B0B;
  --accent-glow:rgba(0,0,0,0);
  --accent-bloom:rgba(212,43,0,.10);
}
```

**Type** `ArchivoBlack.woff2` (shipped) at 206 / lh .86 / tracking −.02em, uppercase, + mono labels.
All-caps is not optional here: mixed case loses the poster weight. Numbers allowed to bleed off the frame edge.
**Texture** hard 8 px offset shadows, thick 3 px rules, flat blocks of accent, no gradients, no blur.
**Motion** 0.2–0.4 s, `power4.out` or steps; hard cuts, occasional 2–3° rotation, overshoot allowed on
one element.
**Charts** giant numerals with hard rules; bars as solid black blocks; no axes, label the values only.
**Do** embrace asymmetry · repeat one shape · let type touch the edges.
**Don't** soften it with rounded corners or pastel tints — commit or pick another preset.

---

## D · Cinematic / Luxury

Fashion, film, premium hardware, finance. Slow, dark, quiet.

```css
:root{
  --bg:#0A0A0B;          --ink:#F2F0EC;      /* 17.4:1 */
  --muted:#A39C92;       /* 7.3:1 */         --dim:#857E75;   /* 4.9:1 */
  --line:rgba(242,240,236,.14);
  --accent:#C8A97E;      /* 8.9:1 */         --accent-mid:#E3C69B;  /* 12:1 */
  --accent-soft:rgba(200,169,126,.12);
  --accent-line:rgba(200,169,126,.40);
  --accent-glow:rgba(200,169,126,.35);
  --accent-bloom:rgba(200,169,126,.14);
}
```

**Type** Inter 300, uppercase, 118 / lh 1.08, tracking **+.06em** (positive — this is the one preset
where tight tracking looks cheap). Labels 14–16, 0.34em.
**Texture** film grain 6 %, vignette, letterbox bars if the subject earns it, no grid, no glow rings.
**Motion** 1.0–1.5 s dissolves, slow 1.02→1.0 scale on images, no bounce, no snap.
**Charts** avoid them. One number, centred, with a thin underline; or a single horizontal rule whose
length is the value.
**Do** hold shots longer than feels comfortable · keep one idea per frame · let black be black.
**Don't** use bar charts, chips or badges — they read as a dashboard, not a film.

---

## E · Terminal

Security, OSS, CLI tooling, hacker-adjacent products. Deliberately spare.

```css
:root{
  --bg:#000000;          --ink:#E8FFE8;      /* 19.9:1 */
  --muted:#9DBF9D;       /* 10.4:1 */        --dim:#83A683;   /* 7.8:1 */
  --line:rgba(232,255,232,.12);
  --accent:#33FF88;      /* 15.8:1 */        --accent-mid:#B4FFD0;  /* 18:1 */
  --accent-soft:rgba(51,255,136,.10);
  --accent-line:rgba(51,255,136,.35);
  --accent-glow:rgba(51,255,136,.35);
  --accent-bloom:rgba(51,255,136,.10);
}
```

**Type** JetBrains Mono only: 104 for display, 26 for body, 20 for labels. No second face — mixing in
a grotesque collapses the illusion instantly.
**Texture** pure black, optional scanlines at 3 %, a blinking 2 px cursor. Never gloss.
**Motion** typewriter or line-by-line reveal, 0.3–0.6 s, stepped eases (`steps(8)` reads as a
terminal), no smooth scale.
**Charts** ASCII bars (`█████░░░░`), or values in a monospaced table.
**Do** keep the whole frame monospaced · use lowercase labels · let it be austere.
**Don't** mix in a sans display face — it collapses the illusion instantly.

---

## Applying a preset

1. Replace the `:root` block and the two `@font-face` pairs.
2. Swap the background layers (grid / grain / flat) and the progress rail for the preset's equivalent.
3. Adjust the type scale by the preset's ratio (Brutalist ×1.35, Cinematic ×0.8) rather than by eye.
4. Re-run `hyperframes check` — light presets fail contrast differently than dark ones.
5. Snapshot one scene and look at it before building the rest. If the preset does not survive a single
   frame, it will not survive the film.


---

## Validated: one title beat, five presets

A 17-second test composition built the same title beat (kicker / two-line display / sub / rule) in all
five presets and rendered a still per look. Every preset survives a frame; these are the values that
were tuned on screen rather than on paper.

| | Display | Margin | Copy top | Texture that actually reads |
|---|---|---|---|---|
| A | Inter 172 / −.048em | 96 | 322 | grid 64 px masked + one accent bloom at 20 % |
| B | Instrument 168 / −.012em | 110 | 300 | paper noise: `feTurbulence` 0.9, `opacity .55`, `mix-blend: multiply` |
| C | Archivo 206 / −.02em caps | 80 | 250 | flat + 26 px accent edge bar right + 10 px ink bar bottom |
| D | Inter 300 / +.06em caps | 140 | 360 | film grain 0.85 / `.22` on `screen` + vignette to 75 % |
| E | JBMono 104 / −.02em | 96 | 330 | scanlines 1 px every 4 px at 3.5 % + 22×42 cursor block |

Three things failed on the first render and are now part of the presets:

- **B's grain was invisible** at `opacity .55` on the layer *and* `.35` inside the turbulence. It needs
  the noise rect at `.55` with no extra layer opacity, multiplied — subtle is not the same as absent.
- **C's accent column** started as a 22 %-wide background band and read as a mistake, not a graphic.
  A hard 26 px edge bar plus a 10 px bottom bar does the same job with intent. The offset shadow also
  only works with **accent text over an ink shadow**; ink text over a red shadow looks like
  misregistration.
- **E's cursor** at 44×76 read as a stray block attached to the number. 22×42, 16 px gap, `.9` opacity.

Fonts shipped in `assets/starter/fonts/`: `Inter-latin.woff2` (variable 100–900),
`JetBrainsMono-{Regular,Medium}.ttf`, `InstrumentSerif.woff2`, `ArchivoBlack.woff2`. All four families
are covered offline; nothing needs downloading at render time.
