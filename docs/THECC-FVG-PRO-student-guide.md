# THECC Fair Value Gaps PRO — Student Guide

**Version:** v2.1 (`pine/thecc-fvg-pro-v2.pine`)
**Educational only. Nothing here is financial advice, a signal service, or a promise of any outcome.** The indicator marks where imbalance and liquidity events happened. It does not know what price will do next, and neither does anyone else.

---

## 1. What this tool is for

Every tool on this indicator answers one question in a different way: **where did participants act with intent, and where did they get trapped?**

- A **fair value gap (FVG)** marks a price range that got skipped because one side was overwhelmed. Unfinished business.
- A **liquidity sweep** marks a level where resting orders were taken and immediately rejected. A failed breakout.
- **MSS / BOS** tell you whether the market is still doing what it was doing, or has just stopped doing it.
- **EQH / EQL** mark the flat levels where stops pile up, which is where sweeps tend to happen.

Used together they form a sequence, not four separate signals. Section 8 walks that sequence.

What this tool will not do for you: pick a direction, size a position, or decide when you are wrong. That is your job, and it is the part that determines whether you survive.

---

## 2. The five components

### 2.1 Fair Value Gaps

**Geometry.** Three consecutive bars. A bullish gap needs bar 3's low above bar 1's high; a bearish gap needs bar 3's high below bar 1's low. The zone spans that untraded range.

**Confirmation.** The middle bar must close beyond the gap edge (`close[1] > high[2]` bullish, `close[1] < low[2]` bearish). A gap that the middle bar could not close through is not treated as displacement.

**Quality filter.** One of two, set by *Zone Filtering*:

| Filter | Test | Use when |
|---|---|---|
| Average Range | Combined body size of the three bars, scaled by sensitivity, must exceed ATR / 1.5 — and the gap itself, scaled by sensitivity, must exceed ATR | Any symbol. Works without a volume feed. |
| Volume Threshold | 5-bar average volume must exceed 15-bar average volume by your percentage | Futures and other symbols with an honest volume feed |

Both filters also reject sequences where the bar-to-bar jump exceeds ATR, unless *Allow Gaps Between Bars* is on. That check throws out session gaps and news holes that only look like displacement.

**Sensitivity is a permissiveness dial, not a strictness dial.** The test is `gap × sensitivity > ATR`. Extreme = 6.0 lets small gaps through; Low = 1.0 demands a genuinely oversized gap. Set it once per symbol and timeframe. Changing it mid-session to make a level appear is bias, not analysis.

**Zones are created on confirmed bars only.** No zone appears and then vanishes intrabar.

### 2.2 The volume profile inside each zone

Each zone carries two volume bars and a number like `12.4K (68%)`.

- The two bars split the three-bar volume between the **upper** and **lower** half of the zone. For a bullish gap, the two most recent bars' volume sits on top and the first bar's volume below; bearish is the mirror.
- The percentage is `smaller ÷ larger × 100`. **High percentage = evenly split.** Low percentage = the volume was concentrated on one side of the gap.
- A lopsided split tells you the participation was front- or back-loaded. It is context for how the gap was built, not a grade.

`[Combined]` in the text means two or more overlapping same-direction zones were merged into that one. A merged zone is a wider, better-attended area than any of its parts — treat it with more respect, not less.

### 2.3 Multi-timeframe modes

| Mode | Behavior |
|---|---|
| Auto | Detects on the chart's own timeframe. Zones change when you change timeframe. |
| Fix | Locks detection to one timeframe. Sit on an M1 chart and still see your M15 gaps at true M15 width. |
| Multi-Fix | Up to four timeframes at once, each zone tagged `M5`, `M15`, `H1`, `D`. |

Multi-Fix exists for one purpose: **finding overlap.** An M5 gap sitting inside an H1 gap is a materially different level from an M5 gap floating on its own. Do not run four timeframes just to fill the screen — read section 10 on the drawing budget first.

### 2.4 Market structure: MSS and BOS

The script maintains a zig-zag of confirmed swing points using pivots of *Pivot length* bars on the left and one bar on the right — so a swing is confirmed one bar after it forms.

- **BOS (Break of Structure)** — price closes beyond the most recent swing in the direction it was already going. Continuation. Dotted by default.
- **MSS (Market Structure Shift)** — price closes beyond the most recent opposing swing, flipping the internal direction. This is the "it stopped doing what it was doing" event. Solid by default.

Both fire on **closes**, not wicks. A wick through a swing high is not a break here, by design.

Two behaviors worth knowing:

1. A BOS at a level already marked is suppressed, so you get one line per level rather than a stack.
2. *Clear previous structure lines on each new MSS* (off by default) wipes the drawings on every flip, leaving only the current leg. Turn it on for a clean execution chart, leave it off to audit history.

### 2.5 Equal Highs / Equal Lows

Two consecutive confirmed pivots within *tolerance %* of each other draw a line at their average — a shelf of stops.

**Understand the lag.** EQH/EQL pivots need *Swing length* bars on **both** sides, so the level is drawn `eqLen` bars after the second pivot printed. With the default of 5, you learn about the shelf five bars late. That is honest, not broken: the alternative is a level that repaints. Plan around it — EQH/EQL is context you prepare with, not a trigger you react to.

Tolerance is a percentage of price, so it scales across symbols. Raise it on volatile instruments, lower it for strict double tops and bottoms.

### 2.6 Liquidity sweeps — new in v2.1

A **buy-side sweep** prints above the bar when price takes out the highest high of the lookback window (excluding the current bar) and then closes back **below** that high on a down-closing bar. The buy stops above the old high were filled and price could not hold there. It is context for **shorts**.

A **sell-side sweep** is the mirror below the lowest low, and is context for **longs**.

Do not read the word "buy" as an instruction. It names the side of the book that got taken.

Why sweeps matter here: the rejection wick a sweep leaves behind is exactly the kind of bar that creates a fresh FVG on the other side. Sweep, then shift, then the gap the shift left behind — that is the sequence the whole toolkit is built to show you.

Why sweeps are not a signal: against a strong trend, a sweep is routinely just a pause before continuation. Alone, it is noise with a label on it.

Lookback sizing: 10–20 bars for local sweeps on an execution chart, 50–200 to catch only runs on levels that have stood a long time. Size it to the level in your plan — if your plan is built on the session high, make the window cover the session.

---

## 3. Reading the chart

| What you see | What it means |
|---|---|
| Colored box | An FVG. Bull = up-side imbalance, bear = down-side. |
| Two bars inside the box | The volume split between the zone's halves |
| `12.4K (68%)` | Three-bar volume, and how evenly it split |
| `M15 · 12.4K (68%)` | Same, on a Multi-Fix zone, tagged with its source timeframe |
| `[Combined]` | Merged from overlapping same-direction zones |
| Dashed mid line in a zone | The 50% level of the gap |
| Box that stops mid-chart | The zone was invalidated there |
| Box running to the current bar | One of the most recent live zones |
| Solid line + `MSS` | Structure flipped at that swing |
| Dotted line + `BOS` | Structure continued through that swing |
| Dashed level + `EQH` / `EQL` | A shelf of two near-equal pivots |
| `$ sweep` above a bar | Buy-side sweep — high taken, closed back below |
| `$ sweep` below a bar | Sell-side sweep — low taken, closed back above |

**Skull Mode** strips every zone down to its dotted mid line and faint grey/black volume bars. Use it when you want the levels present but nearly invisible, so the price action drives your read instead of the boxes.

---

## 4. Settings reference

Every group in the settings panel carries its own tooltip with the same detail as below — hover the `ⓘ`.

**⊹ Timeframe Mode** — Auto / Fix / Multi-Fix, plus the fixed timeframe.

**⊹ Multi-Fix Timeframes** — four slots plus an option to include the chart timeframe. Blank a slot to disable it.

**General Configuration**

| Setting | Default | Notes |
|---|---|---|
| Zone Invalidation | Close | Close = body must close through. Your invalidation choice decides where your stop belongs. |
| Zone Filtering | Average Range | Price-based, or volume-based |
| Volume Threshold % | 50 | Only used by the volume filter |
| FVG Detection | Same Type | Three same-direction bars, or mixed |
| Detection Sensitivity | Extreme | Permissiveness. The checkbox disables size checks entirely. |
| Allow Gaps Between Bars | off | On = accept session/news gaps |
| Show Historic Zones | on | Keep invalidated zones for review |

**⊹ Zone Engine** — zones kept per timeframe (125), combining and overlap threshold, minimum zone duration in milliseconds, untouched-zone cleanup (200 bars), max bars back to process, ATR length.

**Style** — bull/bear/text colors, zone start bar, zone width and dynamic width, extend-latest count, combined-zone color and tag, volume bar side and mirroring.

**💀 Skull Mode** — enable, plus the three discreet colors.

**⊹ Market Structure** — show, pivot length, MSS on/off, BOS on/off, max BOS lines, clear-on-shift. Then four styling groups: MSS Bullish, MSS Bearish, BOS Bullish, BOS Bearish — each with line color/width/style and label text/size/style/colors.

**⊹ Equal Highs / Lows** — show, swing length, tolerance %, extension, drawing cap, then EQH and EQL styling groups.

**⊹ Liquidity Sweeps** — show, lookback, max labels kept, then buy-side and sell-side label styling.

**⊹ Alerts** — fire-on-close switch, one toggle per signal, optional message prefix.

---

## 5. Alerts

Two mechanisms. Use whichever fits.

**A. Named conditions** — in TradingView's alert dialog, set Condition to the indicator and pick one entry:

`MSS Bullish` · `MSS Bearish` · `BOS Bullish` · `BOS Bearish` · `MSS (any)` · `BOS (any)` · `MSS or BOS (any)` · `Equal Highs (EQH)` · `Equal Lows (EQL)` · `Buy-side liquidity sweep` · `Sell-side liquidity sweep` · `Liquidity sweep (any)` · `New FVG (Auto/Fix)` · `New FVG TF#1`…`TF#4`

**B. One alert for everything** — set Condition to the indicator and choose **"Any alert() function call"**. You get one alert covering structure, EQH/EQL and sweeps, with a dynamic message:

```
Bullish BOS | NQ1! | 5 | level 20114.25 | close 20118.50
```

Add a *Message prefix* in the settings to route it — a bot name, a channel tag, whatever your webhook expects.

**Setup checklist**

1. Set your per-signal toggles in **⊹ Alerts** first. A toggle that is off produces no alert, whichever mechanism you use.
2. Leave **Fire on bar close only** ON for anything you trade. With it off, the condition is evaluated every tick, so an intrabar poke through a level can alert on a break that fails before the close.
3. **BOS alerts need "Show BOS" ON** — the detection branch itself is gated by that toggle.
4. EQH/EQL and sweep alerts default to **off**. They fire more often than structure events; turn them on deliberately.
5. Set the alert's own expiry and frequency in TradingView's dialog. The script already limits itself to once per bar.

---

## 6. What repaints and what does not

Be precise about this. It decides whether your backtest means anything.

| Element | Timing |
|---|---|
| FVG zones | Created on **confirmed** bars only. Never appear then vanish intrabar. |
| Zone invalidation | Evaluated on confirmed bars |
| Zone rendering (combining, extension) | Redrawn on the last bar — appearance can change, the underlying zones do not |
| MSS / BOS | Evaluated on close, using swings confirmed one bar after they form |
| EQH / EQL | Confirmed `Swing length` bars late, by design |
| Liquidity sweeps | Evaluated on the live bar, so the label can appear and disappear intrabar until the bar closes |
| Alerts | Gated to confirmed bars when *Fire on bar close only* is on — leave it on |

---

## 7. Common mistakes

1. **Trading a zone because it is on the screen.** A zone is a location, not a reason. No structure, no sweep, no plan — no trade.
2. **Turning sensitivity up until a level appears where you want one.** That is asking the tool to agree with you.
3. **Mismatching invalidation and stop placement.** If you run Close invalidation, a wick through the zone is not your exit; a body close is.
4. **Reading "buy-side sweep" as "buy".** It names the side that was taken, and it is context for the opposite direction.
5. **Reacting to EQH/EQL as a trigger.** It arrives late. It is preparation.
6. **Running four Multi-Fix timeframes at 125 zones each,** then wondering why old drawings disappear. See section 10.
7. **Alerting on everything.** Every extra alert lowers the value of the ones that matter.

---

## 8. A worked sequence

This is a study framework for reading the chart, not a system, and not a recommendation.

1. **Bias** — Fix or Multi-Fix on your higher timeframe. Where are the unfilled gaps above and below? That is the map.
2. **Liquidity** — mark the EQH/EQL shelves and obvious session highs/lows. That is where stops sit.
3. **Sweep** — wait for price to run one of those levels and close back inside. Now you know an attempt failed.
4. **Shift** — wait for MSS in the direction of the rejection. Until structure confirms, the sweep is just a wick.
5. **Level** — the displacement that caused the shift usually leaves a fresh FVG. That gap, or its 50% mid line, is your area of interest.
6. **Invalidation first** — decide where the idea is objectively wrong (beyond the sweep extreme, or a body close back through the zone) **before** you decide where you enter. If the distance from entry to invalidation does not fit your risk, there is no trade — however good the setup looks.
7. **Record it.** Screenshot the sequence with the zones and structure visible. Historic zones being left on the chart is what makes that review honest.

Steps 1–5 are what this indicator shows you. Step 6 is what keeps you in the game, and the indicator has no opinion about it.

---

## 9. Choosing settings by style

Starting points to test on your own symbol, not prescriptions.

| | Scalping (M1–M5) | Intraday (M5–M15) | Swing (H1–D) |
|---|---|---|---|
| Mode | Fix on M15 | Multi-Fix M5/M15/H1 | Multi-Fix M15/H1/D |
| Sensitivity | High | Extreme | Extreme |
| Invalidation | Close | Close | Close |
| Zones kept per TF | 40 | 30 | 25 |
| Pivot length (MSS/BOS) | 5 | 5–8 | 8–12 |
| EQ swing length | 5 | 5 | 8 |
| Sweep lookback | 10–20 | 20–40 | 50–100 |
| Show Historic Zones | off while trading, on for review | on | on |

---

## 10. Drawing budget and troubleshooting

TradingView allows this indicator **500 boxes, 500 lines and 500 labels** in total. The script asks for the maximum of each, but the ceiling is hard.

**Each rendered FVG costs 4 boxes and 2 lines** (zone, text panel, two volume bars; mid line and text separator). So roughly **125 zones is the whole box budget** — across every active timeframe, not per timeframe.

| Symptom | Cause | Fix |
|---|---|---|
| Old zones missing or half-drawn | Box budget exhausted | Lower *Zones kept per timeframe*. With four Multi-Fix timeframes, ~30 each is the honest maximum. |
| Structure labels disappearing | Label budget shared with sweeps | Lower *Max sweep labels to keep* or *Max BOS lines* |
| Nothing draws at all | Filter too selective, or a blank timeframe slot | Check Detection Sensitivity, Zone Filtering, and that your Fix/Multi-Fix slots are not blank |
| Zones only on recent bars | *Max bars back to process* | Raise it, or accept it — it exists to keep the script fast |
| Script times out | Too many timeframes and zones | Fewer Multi-Fix slots, lower zone count, raise minimum sizes |
| No alerts firing | Per-signal toggle off, or BOS with *Show BOS* off | Section 5, checklist items 1 and 3 |
| Volume text reads `FVG` with no number | No volume feed for that symbol | Expected. Use the Average Range filter. |
| EQH/EQL feels late | Pivot confirmation needs bars on both sides | Working as designed. Section 2.5. |

---

## 11. Glossary

**FVG** — fair value gap; a skipped price range left by displacement.
**Imbalance** — the same idea described from the order-flow side: one side was overwhelmed.
**Displacement** — a fast, one-directional move large relative to recent range.
**Mitigation / invalidation** — price trading back through a zone, using it up.
**BOS** — break of structure; continuation through the last swing in the same direction.
**MSS** — market structure shift; a close through the last opposing swing, flipping direction.
**EQH / EQL** — equal highs / equal lows; a shelf of near-equal pivots where stops cluster.
**Liquidity sweep** — a run through a level that closes back inside; a failed breakout.
**Pivot** — a swing high or low confirmed by a set number of bars on each side.
**Lookback** — how far back a calculation measures.

---

*Educational material only. Not financial advice, not a signal service, and not a claim about future results. Trade your own plan, manage your own risk.*
