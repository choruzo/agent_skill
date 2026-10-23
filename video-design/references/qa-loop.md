# QA loop

The gates catch different things and none of them replaces looking at frames. Run them in this order;
each is cheaper than the one after.

## 1. Lint (structure)

```bash
npx hyperframes lint            # add --verbose for info findings
```

Catches the structural mistakes that produce silent breakage: wrapped standalone roots, clips without
`class="clip"`, `autoAlpha` on a `.clip`, CSS `transform` + GSAP tween on the same node, `<audio>`
without an `id`, named fonts without `@font-face`, a clip ending past the root duration. Warnings
about "nested structure needs subcomposition" and file length are stylistic — ignore them for a
single-file promo; split into `compositions/*.html` only when you need to iterate on one scene
without re-reading 900 lines.

## 2. Check (runtime, layout, motion, contrast)

```bash
npx hyperframes check
```

Five audits in one pass. Read them in this order:

- **Runtime** — errors mean the timeline never registered or a tween failed.
- **Layout** — `text_box_overflow` / `container_overflow` are real clipping defects; the ones that
  appear *during* a mask reveal (the span is still translated) are transient and acceptable. Fix the
  persistent ones by growing the container, never by shrinking the type.
- **Contrast** — the only gate that will stop a render on aesthetics. On `#05060A`, 4.5:1 needs
  roughly `#7C818E` or lighter; 3:1 for large text needs `#6D7280`. When it fails it prints the exact
  RGB to use — take it.
  **It samples states, not every state.** Text that sits over a shape which slides in later can be
  measured before the shape arrives, and pass. Any copy over a filled disc, panel or image needs a
  pixel check on the *rendered* frame — measure the actual text colour against the actual fill.
- **Motion** — overlaps, dead zones, elements that never appear.
- **Lint errors switch the audits off.** If `check` reports `0 sample(s)` and `0/0 text checks`, a
  lint error is suppressing everything; clear it and run again. A clean-looking "0 samples" is not a
  pass.

## 3. Snapshots (composition, in seconds)

```bash
npx hyperframes snapshot --at 1.6,4.8,8.6,12.6,17.6,22.2,26.5 -o .hyperframes/shots
```

One still per beat, taken *after* the beat's entrances have resolved (add ~1.5 s to the beat start).
Read the contact sheet it writes (`contact-sheet-*.jpg`) at full size, not the thumbnails. What to
look for, in order:

1. Any element that is not where the layout intended (the eye finds this in 2 seconds).
2. Collisions: a label over a curve, a chip over a dot, a value over a rule.
3. Balance: is the bottom third empty? Is the header floating?
4. Type: is the title actually 74 px, or did it inherit 16 px?

## 4. Render

```bash
npx hyperframes render -o renders/<name>.mp4
```

Read the second line of the summary: `beginframe` capture + `hardware gpu` is the fast path;
`screenshot` + `software gpu` is 5–10× slower and usually means the GPU probe failed. Budget roughly
2× realtime at 1080p on a modest discrete GPU (28 s of video ≈ 58 s of render).

## 4b. Dead frames (the hole a contact sheet hides)

```bash
python3 <skill>/scripts/deadframe.py renders/out.mp4          # add --min 0.3 to loosen
```

Flags stretches where the frame is one flat colour with nothing on it — the gap left when a scene fades
out before the next beat arrives. They are invisible in a contact sheet (which is mostly empty space)
and obvious in motion. Aim for zero; a held solid colour is only acceptable when it is a deliberate
beat of at least a second, not a seam.

Calibration from a real piece: a 28.4 s release film had **six holes of 0.30–0.47 s at its cuts** — 1.9 s,
7 % of the runtime — and every other gate passed it. The cause was fading each scene out 0.3 s before the
next one began animating. Leaving them in is a legitimate choice if the pause is deliberate; knowing they
are there is not optional.

## 5. Frame grid from the actual MP4

```bash
ffprobe -v error -show_entries format=duration,size:stream=width,height,r_frame_rate \
        -of default=nw=1 renders/out.mp4

ffmpeg -v error -y -i renders/out.mp4 \
  -vf "select='eq(n\,60)+eq(n\,180)+eq(n\,405)+eq(n\,675)+eq(n\,825)',scale=640:-1,tile=2x3" \
  -frames:v 1 /tmp/grid.jpg
```

This is the only check of the *encoded* artifact — the snapshot tool renders the live DOM, so it will
not show an encoder problem, a wrong duration or a black tail. Sample every ~4 s and one frame near
the end.

## 6. Hand-off

```bash
npx hyperframes check && npx hyperframes preview --background
```

Give the person the MP4 *and* the source. In Studio they can click any element to edit text, drag the
timeline, and re-export — which is usually faster than another round of prompting.

## Failure modes seen in practice

| Symptom | Cause | Fix |
|---|---|---|
| Title renders tiny | the mask is a `div`, not the typed element | put `h2`/`h1` on the masking element |
| Dots drift or lint conflict | CSS `translate(-50%,-50%)` + GSAP `scale` | negative margins for centring |
| Descenders clipped | mask has no bottom padding | `padding-bottom:.24em; margin-bottom:-.24em` |
| Contrast gate fails at 3.2:1 | muted grey too dark | `--dim:#7C818E` (4.5:1) |
| Bars read as tracks | track fill too bright | `rgba(255,255,255,.028)` |
| Small caption invisible on a colour block | cream tint on accent ≈1.8:1, and `check` sampled the frame before the block arrived | use the full cream/ink token, then re-measure on the MP4 frame |
| Text dims for half a second as it enters | opacity fade over a coloured fill | mask/wipe the text in at full opacity — never tween `opacity` on text over a fill |
| A beat of flat colour at every cut | outgoing scene fades out before the incoming one starts | start the next beat on the cut frame, or hard-cut with the outgoing content still full |
| Scene feels empty at the bottom | content ends at 700 on 1080 | add a mono footnote band at 900 |
| Everything animates at once | relative chaining | absolute positions per beat |
| Chart drawn before its frame | tween on the plot before the axes | axes first, then dot, then connector |
| Render silent | audio element has no `id` | give every `<audio>` an `id` |
| Render 10× slower | software GPU fallback | check the summary line, close other GPU users |
