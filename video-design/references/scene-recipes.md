# Scene recipes

Copy-paste starting points for every beat in `SKILL.md` §5. All geometry assumes a 1920×1080 root
with 96 px margins. Each snippet is the part that matters — drop it into the scene shell below.

Every accent use goes through the seven tokens (`--accent`, `--accent-mid`, `--accent-soft`,
`--accent-line`, `--accent-glow`, `--accent-bloom`) so switching preset in `presets.md` is a `:root` swap, never a hunt
through scene code. The token block lives in the starter.

## 0. Scene shell

```html
<div id="root" data-composition-id="main" data-start="0"
     data-width="1920" data-height="1080" data-duration="28.4">

  <div class="bg-grid"></div>
  <div class="bg-glow"></div>
  <div class="bg-vignette"></div>

  <div class="chrome left">Product name</div>
  <div class="chrome right">Version / date</div>

  <section id="s1" class="clip scene" data-start="0" data-duration="4.2">
    <div id="s1-inner" class="inner"> … </div>
  </section>

  <div class="progress"><i id="progress-fill"></i></div>
</div>
```

```css
.scene, .inner { position:absolute; inset:0; }
.inner { padding:0 96px; }
.chrome { position:absolute; top:58px; font-family:"JBMono",monospace; font-size:17px;
          letter-spacing:.2em; color:var(--dim); text-transform:uppercase; }
.chrome.left { left:96px } .chrome.right { right:96px; text-align:right }
.bg-grid { position:absolute; inset:0; background-image:
    linear-gradient(to right, rgba(255,255,255,.032) 1px, transparent 1px),
    linear-gradient(to bottom, rgba(255,255,255,.032) 1px, transparent 1px);
  background-size:64px 64px;
  mask-image:radial-gradient(ellipse 75% 65% at 50% 45%, #000 20%, transparent 100%);
  -webkit-mask-image:radial-gradient(ellipse 75% 65% at 50% 45%, #000 20%, transparent 100%); }
.bg-glow { position:absolute; inset:0; background:
    radial-gradient(900px 620px at 78% 8%, var(--accent-glow), transparent 70%),
    radial-gradient(700px 500px at 8% 96%, var(--accent-soft), transparent 70%); }
.progress { position:absolute; left:0; bottom:0; height:3px; width:100%;
            background:rgba(255,255,255,.06); transform-origin:0 50%; }
.progress i { display:block; height:100%; background:var(--accent); transform-origin:0 50%; }
```

The progress rail is a 3 px accent line that fills over the full duration. It is the cheapest way to
make a short film feel authored, and it doubles as chapter position for the viewer.

## 1. Masked display title

```html
<div class="s1-copy">
  <div id="k" class="s1-kicker">Weights released · MIT license</div>
  <h1>
    <span class="mask"><span id="l1">DeepSeek</span></span>
    <span class="mask"><span id="l2">V4.1 Flash <em>1017</em></span></span>
  </h1>
  <div id="sub" class="s1-sub">A minor update. Not a minor jump.</div>
  <div id="rule" class="s1-rule"></div>
</div>
```

```css
h1 { margin:30px 0 0; font-size:172px; line-height:.9; letter-spacing:-.048em; font-weight:700 }
h1 em { font-style:normal; color:var(--accent) }
.mask { display:block; overflow:hidden; padding-bottom:.24em; margin-bottom:-.24em }
.mask > span { display:block }
.s1-rule { width:300px; height:3px; background:var(--accent); transform-origin:0 50% }
```

```js
tl.fromTo("#l1", {yPercent:112}, {yPercent:0,duration:1.05,ease:"power4.out"}, 0.40);
tl.fromTo("#l2", {yPercent:112}, {yPercent:0,duration:1.05,ease:"power4.out"}, 0.54);
tl.fromTo("#sub", {opacity:0,y:18}, {opacity:1,y:0,duration:.8,ease:"power2.out"}, 1.15);
tl.fromTo("#rule",{scaleX:0}, {scaleX:1,duration:.9,ease:"power3.inOut"}, 1.35);
```

Stagger the two lines by 0.14 s: the eye reads it as one gesture, not two. The masked reveal needs
the padding, or descenders (`p`, `j`, the tail of `Q`) get sliced.

## 2. Claim beat — old → new

```html
<div class="micro">Cost per solved task</div>
<div class="price-row">
  <span id="old" class="price-old">$0.50</span>
  <span class="price-arrow">→</span>
  <span id="new" class="price-new">$0.20</span>
</div>
<div id="chip" class="chip">−60% PER TASK</div>
```

```css
.price-old { font-size:88px; font-weight:500; color:#6D7280;      /* ≥3:1 on near-black */
             letter-spacing:-.04em; text-decoration:line-through; text-decoration-thickness:3px }
.price-new { font-size:132px; font-weight:700; color:var(--accent); letter-spacing:-.05em; line-height:1 }
.chip { display:inline-block; padding:10px 18px; border:1px solid var(--accent-line);
        background:var(--accent-soft); color:var(--accent-mid);
        font-family:"JBMono",monospace; font-size:20px; letter-spacing:.08em }
```

The struck old value must stay legible (3:1, not 1.8:1). A price you cannot read reads as a design
mistake, not as emphasis.

## 3. Scatter — the trade-off plot

Container is `position:relative; width:1020px; height:600px`. Axes in an SVG with `viewBox="0 0 1020 600"`.

```html
<svg viewBox="0 0 1020 600" fill="none">
  <line id="ax-x" x1="60" y1="520" x2="980" y2="520" stroke="rgba(255,255,255,.22)" stroke-width="1.5"/>
  <line id="ax-y" x1="60" y1="520" x2="60"  y2="60"  stroke="rgba(255,255,255,.22)" stroke-width="1.5"/>
  <line x1="60" y1="405" x2="980" y2="405" stroke="rgba(255,255,255,.06)"/>
  <line x1="60" y1="290" x2="980" y2="290" stroke="rgba(255,255,255,.06)"/>
  <line x1="60" y1="175" x2="980" y2="175" stroke="rgba(255,255,255,.06)"/>
  <path id="s2-path" d="M 862 394 Q 560 214 292 232" stroke="var(--accent)" stroke-width="3"
        pathLength="1" stroke-dasharray="1" stroke-dashoffset="1" stroke-linecap="round"/>
</svg>
<div id="dot-old" class="dot old" style="left:862px; top:394px"></div>
<div id="dot-new" class="dot new" style="left:292px; top:232px"></div>
```

Map data to pixels once, in your head, and hard-code it:

```
x(cost)  = 60 + (cost  - minCost ) / (maxCost  - minCost ) * 860     // cheaper → further right? no:
         = 60 + (maxCost - cost) / (maxCost - minCost) * 860          // cheaper → further LEFT
y(score) = 520 - (score - minScore) / (maxScore - minScore) * 400     // better → higher
```

```css
.dot { position:absolute; border-radius:50% }
.dot.old { width:18px; height:18px; margin:-9px 0 0 -9px; background:#4A4F5B; border:2px solid #6A707D }
.dot.new { width:30px; height:30px; margin:-15px 0 0 -15px; background:var(--accent);
           box-shadow:0 0 0 10px var(--accent-soft), 0 0 46px var(--accent-glow) }
```

```js
tl.fromTo("#ax-x",{scaleX:0,transformOrigin:"0% 50%"},{scaleX:1,duration:.7,ease:"power2.inOut"},4.70);
tl.fromTo("#ax-y",{scaleY:0,transformOrigin:"50% 100%"},{scaleY:1,duration:.7,ease:"power2.inOut"},4.70);
tl.fromTo("#s2-path",{opacity:0,strokeDashoffset:1},{opacity:1,strokeDashoffset:0,duration:1.0,ease:"power2.inOut"},5.65);
tl.fromTo("#dot-new",{opacity:0,scale:.2},{opacity:1,scale:1,duration:.7,ease:"back.out(2.4)"},6.55);
```

`pathLength="1"` + `stroke-dasharray="1"` is the draw-on trick: normalised length, no measuring.
Do not animate `stroke-dashoffset` on a dashed pattern — it slides the dashes instead of drawing.

## 4. Benchmark bars

```html
<div class="bench b1">
  <div class="bench-head"><span class="bench-name">Terminal-Bench 4.0</span>
                          <span class="bench-note">Claude Code harness</span></div>
  <div class="bar-row"><span class="bar-tag">prev</span>
    <div class="track"><div id="p1" class="bar prev" style="width:31.2%"></div></div>
    <span class="bar-val dim">31.2</span></div>
  <div class="bar-row"><span class="bar-tag hot">now</span>
    <div class="track"><div id="b1" class="bar next" style="width:42.3%"></div></div>
    <span class="bar-val">42.3</span><span id="d1" class="delta">+11.1</span></div>
</div>
```

```css
.bench-head { display:flex; justify-content:space-between; align-items:baseline;
              padding-bottom:16px; border-bottom:1px solid var(--line) }
.bench-name { font-size:36px; font-weight:600; letter-spacing:-.02em }
.bench-note { font-family:"JBMono",monospace; font-size:17px; letter-spacing:.14em;
              color:var(--dim); text-transform:uppercase }
.track { position:relative; width:1230px; height:34px; background:rgba(255,255,255,.028) }
.bar { position:absolute; inset:0 auto 0 0; border-radius:2px; transform-origin:0 50% }
.bar.prev { background:#3B404C }
.bar.next { background:var(--accent); box-shadow:0 0 34px var(--accent-glow) }
.bar-val { font-family:"JBMono",monospace; font-size:30px; width:108px; text-align:right }
.delta { font-family:"JBMono",monospace; font-size:22px; font-weight:700; color:var(--accent-mid);
         background:var(--accent-soft); border:1px solid var(--accent-line); padding:6px 12px; width:104px; text-align:center }
```

```js
tl.fromTo("#p1",{scaleX:0},{scaleX:1,duration:.55,ease:"power2.out"},10.25);
tl.fromTo("#b1",{scaleX:0},{scaleX:1,duration:.95,ease:"power3.out"},10.55);
```

Bars are `width:%` at rest and `scaleX` for the animation — never tween `width`. Keep the track fill
at ~3 % white; at 4.5 % it reads as a second bar and the chart loses its meaning.

## 5. Counter grid

```html
<div class="cards">
  <div class="card"><div class="card-name">Automation-Bench v1.0.6</div>
    <div class="card-vals"><span class="v-old">54.8</span><span class="arr">→</span>
      <span id="v1" class="v-new">60.5</span><span class="card-delta">+5.7</span></div></div>
  …
</div>
```

```css
.cards { display:grid; grid-template-columns:840px 840px; grid-column-gap:48px; grid-row-gap:58px }
.card { border-top:1px solid rgba(255,255,255,.16); padding-top:22px }
.v-old { font-family:"JBMono",monospace; font-size:46px; color:#767C89 }
.v-new { font-size:102px; font-weight:700; letter-spacing:-.045em; color:var(--accent); line-height:1 }
.card-delta { align-self:center; font-family:"JBMono",monospace; font-size:21px; color:var(--accent-mid);
              background:var(--accent-soft); border:1px solid var(--accent-line); padding:5px 11px }
```

```js
// seek-safe counter: the tween drives the text from the timeline, not from a timer
function countUp(id, from, to, at, dur = 1.1) {
  const o = { v: from };
  tl.to(o, { v: to, duration: dur, ease: "power2.out",
             onUpdate: () => { document.getElementById(id).textContent = o.v.toFixed(1); } }, at);
}
```

Set the element's initial text to the *previous* value so the frame before the tween is correct.

## 6. Spec strip

```html
<div class="specs">
  <div class="spec"><div class="spec-v">1M</div><div class="spec-l">Context window</div>
                   <div class="spec-s">tokens in · up to 256K out</div></div>
  <div class="spec"><div class="spec-v hot">¼</div><div class="spec-l">KV cache HBM</div>
                   <div class="spec-s">⅛ the SSD footprint</div></div>
</div>
```

```css
.specs { display:flex }
.spec { flex:1; padding:0 40px; border-left:1px solid var(--line) }
.spec:first-child { padding-left:0; border-left:0 }
.spec-v { font-size:132px; font-weight:700; letter-spacing:-.05em; line-height:.95 }
.spec-v.hot { color:var(--accent) }
.spec-l { margin-top:22px; font-size:23px; color:#C2C7D2; font-weight:500 }
.spec-s { margin-top:10px; font-family:"JBMono",monospace; font-size:17px; color:var(--dim) }
```

```js
[1,2,3,4].forEach((n,i)=>
  tl.fromTo("#sp"+n,{opacity:0,y:34},{opacity:1,y:0,duration:.7,ease:"power3.out"},20.85+i*.14));
```

## 7. End card

```html
<div class="endcard">
  <div class="end-brand">DEEPSEEK</div>
  <div class="end-title"><span class="ln">V4.1 Flash</span><span class="ln hot">1017</span></div>
  <div class="end-date">17 · 10 · 2026</div>
</div>
```

```css
.endcard { position:absolute; inset:0; display:flex; flex-direction:column;
           align-items:center; justify-content:center }
.end-brand { font-family:"JBMono",monospace; font-size:20px; letter-spacing:.42em; color:var(--muted) }
.end-title { margin-top:26px; font-size:128px; font-weight:700; letter-spacing:-.05em;
             line-height:.95; text-align:center }
.end-title .ln { display:block } .end-title .hot { color:var(--accent) }
.end-date { margin-top:40px; font-family:"JBMono",monospace; font-size:18px;
            letter-spacing:.3em; color:var(--dim) }
```

Two stacked `span`s, not `<br>` — line breaks inside a block break text-fit auditing and are banned
by the HyperFrames determinism rules.

## 8. Timeline skeleton

```js
const tl = gsap.timeline({ paused: true });          // exactly one, registered at the end
tl.fromTo("#progress-fill",{scaleX:0},{scaleX:1,duration:28.4,ease:"none"},0);
// … every scene's tweens at absolute times …
window.__timelines["main"] = tl;                      // key must equal data-composition-id
```

Absolute-positioned tweens (`…, 5.65)`) make the beat sheet and the code the same document. Avoid
relative chaining: when a beat needs to move, one number changes instead of ten.

## 9. Fonts

```css
@font-face{ font-family:"Inter"; src:url("fonts/Inter-latin.woff2") format("woff2");
            font-weight:100 900; font-display:block }
@font-face{ font-family:"JBMono"; src:url("fonts/JetBrainsMono-Regular.ttf") format("truetype");
            font-weight:400; font-display:block }
```

Download the variable Inter Latin subset (~48 KB) from `fonts.googleapis.com/css2?family=Inter:wght@100..900`
and take the `/* latin */` block's `.woff2` URL. JetBrains Mono ships with most Linux distros
(`/usr/share/fonts/truetype/jetbrains-mono/`). Vendor `gsap.min.js` next to them — a CDN dependency
makes the render non-deterministic and fails offline.
