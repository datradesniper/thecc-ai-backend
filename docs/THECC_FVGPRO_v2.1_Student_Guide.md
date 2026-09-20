<!-- ┌─────────────────────────────────────────────────────────────────────┐ -->
<!-- │ THECC INSTITUTIONAL TRADER ACADEMY™ — STANDARD DOCUMENT FRONT-MATTER │ -->
<!-- └─────────────────────────────────────────────────────────────────────┘ -->

# THECC Fair Value Gaps PRO — Student Guide

### THECC Institutional Trader Academy™

#### 📘 Course Metadata

| Field | Value |
|---|---|
| **Academy** | THECC Institutional Trader Academy™ |
| **Course** | Fair Value Gaps PRO |
| **Module** | 1–4 (Core Curriculum) |
| **Lesson** | All |
| **Difficulty** | Beginner → Intermediate |
| **Estimated Time** | 90 minutes |
| **Prerequisites** | None (Market Structure Basics recommended) |
| **Indicator Version** | v2.1 |
| **Document Version** | v2.1.0 |
| **Last Updated** | 2026-09-20 |
| **Instructor** | Dale Batise |
| **Status** | Content Complete — Certification Pending |

**Document control:**

| Field | Value |
|---|---|
| Document ID | THECC-DOC-FVGPRO-SG |
| Document type | Student Guide (Master Curriculum) |
| Indicator | THECC Fair Value Gaps PRO · **Registry ID pending** |
| Version | v2.1.0 |
| Build | 2.1.0+2026-09-20 |
| Release date | 2026-09-20 |
| Compatible indicator versions | FVG PRO v2.1.x |
| Academy Doc Standard | v1.0 |
| Edition | Student / Pro · Status: Beta |
| Platform | TradingView · Pine Script v6 |
| Copyright | © THE CONSISTENCY COLLECTIVE |

> ⚠️ **Registry action required before publication.** This product does not yet hold a permanent `THECC-NNNN` ID. `THECC_INDICATOR_REGISTRY.json` carries an open note under **THECC-0008 (FVG Return Filter)**: *"FVGBPR_v1.7.pine sits in the same folder — unclear whether it is a separate product (FVG+BPR) or an ancestor. Resolve before retrofit; may warrant its own ID."* Once the owner assigns the ID, replace **Registry ID pending** above and in the Document Control block, and move this document into its `THECC-NNNN <CODE>` Academy folder.

[ QR CODE PLACEHOLDER — links to the current version of this guide in the Member Portal ]

**Consistency Creates Freedom.**

---

#### Callout legend

| Symbol | Meaning |
|---|---|
| 💡 | Tip |
| ⚠️ | Warning |
| ✅ | Do this |
| 📸 | Screenshot |
| 📊 | Diagram |
| 📝 | Exercise |
| ❓ | Review Questions |

---

## Table of Contents

1. [Chapter 1 — Welcome](#chapter-1--welcome)
2. [Chapter 2 — Installation](#chapter-2--installation)
3. [Chapter 3 — Indicator Walkthrough](#chapter-3--indicator-walkthrough)
4. [Chapter 4 — Timeframe Modes](#chapter-4--timeframe-modes)
5. [Chapter 5 — Reading the Map](#chapter-5--reading-the-map)
6. [Chapter 6 — Alerts](#chapter-6--alerts)
7. [Chapter 7 — Customization](#chapter-7--customization)
8. [Chapter 8 — Best Practices (Top 20)](#chapter-8--best-practices-top-20)
9. [Chapter 9 — Common Mistakes (Top 25)](#chapter-9--common-mistakes-top-25)
10. [Chapter 10 — Frequently Asked Questions (50)](#chapter-10--frequently-asked-questions-50)
11. [Chapter 11 — Troubleshooting](#chapter-11--troubleshooting)
12. [Chapter 12 — Quick Reference (Printable Cheat Sheet)](#chapter-12--quick-reference-printable-cheat-sheet)
13. [Appendix A — Certification Quiz](#appendix-a--certification-quiz)
14. [Appendix B — Glossary](#appendix-b--glossary)
15. [Course Summary](#course-summary)
16. [Document Control](#document-control)

---

## Learning Objectives

By the end of this course you will be able to:

1. Explain what a fair value gap represents in terms of participation and unfinished business.
2. State the exact conditions this indicator requires before it draws a zone, and describe why each filter exists.
3. Read every element on the chart — zone, volume split, percentage, midpoint, timeframe tag, combined tag, structure line, equal-level line and sweep label — without guessing.
4. Choose between Auto, Fix and Multi-Fix timeframe modes for a defined trading style, and explain the cost of each.
5. Distinguish a market structure shift from a break of structure, and state which one changes your bias.
6. Identify the sweep → shift → gap sequence on a live chart and describe where the idea becomes invalid.
7. Configure alerts for structure, equal levels and sweeps, and explain why bar-close gating protects you.
8. Diagnose the four most common display faults, including the drawing budget, without external help.

**Estimated completion time:** 90 minutes · **Difficulty:** Beginner → Intermediate

---

# Chapter 1 — Welcome

## What Fair Value Gaps PRO is

Fair Value Gaps PRO is a **market map**. It records four classes of evidence on your chart and keeps them there for as long as they remain valid:

| Element | Evidence it records |
|---|---|
| Fair value gap zones | Price ranges skipped by one-sided participation — unfinished business |
| Market structure (MSS / BOS) | Whether the market is continuing, or has just stopped continuing |
| Equal highs / equal lows | Flat shelves where protective orders accumulate |
| Liquidity sweeps | Levels where resting orders were taken and immediately rejected |

The indicator also measures the **volume behind each gap** and splits it across the zone, so a level arrives with its participation attached rather than as an anonymous rectangle.

⚠️ **This tool issues no buy or sell signals.** It does not grade probability, it does not rank setups, and it holds no opinion about direction. It is context. Every decision — direction, entry, size, invalidation — remains yours, executed under your own plan.

## Why it exists

Most gap indicators draw every three-bar gap they find. The result is a chart covered in rectangles, most of which mark nothing more than a quiet drift between two bars.

This indicator applies two tests before it accepts a gap:

1. **The middle bar must close through the gap edge.** Intent, not accident.
2. **The move must be large relative to recent range, or backed by above-average volume.** Displacement, not drift.

What survives both tests is a smaller set of levels that were built by real participation. That selectivity is the product.

## How it fits inside the THECC ecosystem

| Role | Product |
|---|---|
| Market map / context (this course) | Fair Value Gaps PRO |
| Market map / structural levels | Support & Resistance Matrix (THECC-0024) |
| Execution and confirmed signals | Precision Execution Engine (THECC-0002) |
| Directional filter | Medium Trend Strategy Suite (THECC-0004) |

A map tells you **where**. An execution tool tells you **when**. Keeping those two jobs in separate tools is deliberate: it stops a level from quietly becoming a trade trigger in your mind before your plan has agreed to it.

💡 **Tip.** If you run this alongside an execution product, decide in advance which tool owns which decision, and write it down. Most tool conflicts are really undocumented role conflicts.

📝 **Exercise 1.** Write one sentence for each of the four elements in the table above, stating what it tells you about *participation*. No price predictions — only evidence.

❓ **Review Questions**
1. Why is a market map deliberately unable to issue a trade signal?
2. Name the two tests a gap must pass before this indicator draws it.
3. Which THECC product owns the entry decision when you pair it with this one?

---

# Chapter 2 — Installation

## Step 1: Add the indicator in TradingView

1. Open TradingView and load your chart.
2. Open **Pine Editor** (bottom panel).
3. Paste the contents of the `.pine` file supplied with your licence.
4. Click **Add to chart**.
5. Confirm the title reads **THECC FVG PRO** in the top-left legend of your chart.

✅ **Do this.** Save the script to your TradingView account (**Save**, then name it). Alerts can only be attached to a saved indicator.

📸 *Screenshot placeholder — Pine Editor with the script loaded and the indicator added to an NQ 5-minute chart.*

## Step 2: Recommended chart

| Setting | Recommendation | Reason |
|---|---|---|
| Symbol | A liquid future or index (for example NQ, ES) | Honest volume and clean gaps |
| Chart type | Standard candles | The detection reads real highs, lows and closes |
| Session | Regular trading hours while learning | Overnight gaps distort the size filters |
| Theme | Either — the zones are semi-transparent by design | — |

⚠️ **Non-standard chart types change what you see.** Heikin Ashi, Renko and Range bars synthesize their own prices, so any gap detected on them is a gap in a derived series, not in the market. Learn on standard candles.

## Step 3: Timeframes

| Trading style | Chart timeframe | Detection mode (Chapter 4) |
|---|---|---|
| Scalping | M1 – M5 | Fix on M15 |
| Intraday | M5 – M15 | Multi-Fix M5 / M15 / H1 |
| Swing | H1 – D | Multi-Fix M15 / H1 / D |

## Step 4: Default settings

The defaults ship deliberately conservative: **Close invalidation**, **Average Range filtering**, **Extreme sensitivity**, structure and equal levels on, sweeps on, and alerts gated to bar close.

✅ **Do this.** Trade the defaults for one full week and keep notes before changing anything. You cannot tell what a setting does for you until you know what the default looked like.

📝 **Exercise 2.** Install the indicator on your primary symbol, set the chart per the table above, and record in your journal: symbol, chart timeframe, detection mode, and the number of live zones visible on screen.

❓ **Review Questions**
1. Why must the script be saved before you can create an alert?
2. Why is a Heikin Ashi chart a poor place to learn gap detection?
3. What are the three defaults that make the shipped configuration conservative?

---

# Chapter 3 — Indicator Walkthrough

📸 *Screenshot placeholder — annotated chart showing every element in this chapter.*

## 3.1 The zones (the main event)

A zone is drawn when three consecutive bars leave an untraded range **and** that range survives both quality tests.

| Direction | Geometry | Confirmation |
|---|---|---|
| Bullish | Bar 3 low is above bar 1 high | Bar 2 must close above bar 1's high |
| Bearish | Bar 3 high is below bar 1 low | Bar 2 must close below bar 1's low |

The box spans the untraded range only — not the bars that created it.

⚠️ **Zones are created on confirmed bars.** A zone never appears mid-bar and then disappears. In the Academy's terminology, *confirmed* means the candle has closed and the result is locked.

## 3.2 The volume split and the percentage

Inside each zone sit two coloured bars and a figure such as `12.4K (68%)`.

- `12.4K` is the **total volume of the three bars** that built the gap.
- The two bars show how that volume **divided between the upper and lower half** of the zone.
- `(68%)` is the smaller side divided by the larger side. **A high percentage means the volume was evenly spread. A low percentage means it was concentrated on one side.**

💡 **Tip.** Read the percentage as *balance*, never as quality or probability. It describes how the level was built, not what it will do.

## 3.3 The midpoint line

The dashed line across a zone marks its **50% level**. Many traders treat the midpoint as the decision point inside a zone: reaction at or before the midpoint is a stronger response than one that requires the whole zone to be consumed.

## 3.4 Combined zones

When two or more same-direction zones overlap, the indicator merges them into one larger zone and tags the text with `[Combined]`. Their volumes are added together.

A combined zone is a **wider, better-attended area** than any of its parts. Treat it as more significant, and remember that its edges are further apart, which changes where invalidation sits.

## 3.5 Historic (invalidated) zones

When price consumes a zone, the box stops at the bar that consumed it and remains on the chart in its historic style.

✅ **Do this.** Keep historic zones on while you are learning. They are the record that lets you audit the levels you did not take. Switch them off only when screen clutter is costing you decisions.

## 3.6 Market structure — MSS and BOS

The indicator tracks confirmed swing highs and lows, then reports two events:

| Event | Condition | Meaning | Default style |
|---|---|---|---|
| **BOS** — Break of Structure | Close beyond the most recent swing **in the direction already established** | Continuation | Dotted line + `BOS` |
| **MSS** — Market Structure Shift | Close beyond the most recent **opposing** swing | The established direction has stopped | Solid line + `MSS` |

Both events require a **close**. A wick through a swing is not a break in this indicator, by design.

⚠️ A repeated break of a level already marked is suppressed, so you see one line per level rather than a stack of identical ones.

## 3.7 Equal highs and equal lows

Two consecutive confirmed pivots within your tolerance percentage draw a dashed line at their average, tagged `EQH` above or `EQL` below.

⚠️ **These levels arrive late, and that is deliberate.** A pivot needs bars on both sides before it is confirmed, so the shelf is drawn `Swing length` bars after the second pivot printed (five bars on the default). The alternative — drawing it immediately — would mean a level that repaints. Use equal levels as **preparation**, never as a trigger.

## 3.8 Liquidity sweeps

| Label position | Condition | Reads as |
|---|---|---|
| Above the bar | Price takes out the highest high of the lookback window, then closes back **below** it on a down-closing bar | Rejection of higher prices — context for shorts |
| Below the bar | Price takes out the lowest low of the lookback window, then closes back **above** it on an up-closing bar | Rejection of lower prices — context for longs |

⚠️ **"Buy-side" names the side of the order book that was taken, not an instruction to buy.** A buy-side sweep is evidence against higher prices.

💡 **Tip.** Sweep labels are evaluated on the live bar, so a label can appear and then vanish before the bar closes. Only a closed bar is evidence. This is why alerts are gated to bar close by default.

## 3.9 Skull Mode

Skull Mode strips each zone to its dotted midpoint line and two very faint grey or black volume bars. The levels stay on the chart; the visual weight does not.

Use it when the boxes are dominating your read of price action, or for screenshots where price must be the subject.

## 3.10 Colors at a glance

| Element | Default |
|---|---|
| Bullish zone | Green, semi-transparent |
| Bearish zone | Red, semi-transparent |
| Zone text | White |
| Combined zone | Same direction color, slightly stronger |
| MSS bullish / bearish | Green / red solid line |
| BOS bullish / bearish | Green / red dotted line |
| EQH / EQL | Red / yellow-green dashed line |
| Sweep labels | Red above, yellow-green below |
| Skull Mode | Light grey, black, grey midpoint |

📝 **Exercise 3.** On a chart with at least twenty visible zones, find one of each: a live zone, a historic zone, a combined zone, a BOS line, an MSS line, and a sweep label. Screenshot each and label it in your journal.

❓ **Review Questions**
1. What must the middle bar do before a gap is accepted?
2. What does a *low* volume percentage tell you about how a zone was built?
3. Why does an equal-level line arrive several bars late, and why is that preferable?
4. State the difference between BOS and MSS in one sentence each.

---

# Chapter 4 — Timeframe Modes

The zones you see do not have to come from the chart you are looking at. This is the single most valuable feature in the product, and the one most often left on its default.

## 4.1 The three modes

| Mode | What it detects on | Use it when |
|---|---|---|
| **Auto** | The chart's own timeframe | You want the tool to follow you as you change timeframe |
| **Fix** | One timeframe you choose, regardless of chart | You execute on a low timeframe but take levels from a higher one |
| **Multi-Fix** | Up to four timeframes at once, plus optionally the chart's own | You want to see which levels agree across timeframes |

## 4.2 Why Fix matters

On an M1 chart in Auto mode, you see M1 gaps: small, numerous, consumed quickly. Set **Fix = M15** and you sit on the same M1 chart while the zones on it are M15 zones, drawn at their true M15 width.

✅ **Do this.** Choose the timeframe your bias actually comes from, fix detection there, then drop to your execution chart. Your levels stop moving every time you change chart timeframe — and levels that move are levels you cannot plan around.

## 4.3 Why Multi-Fix matters: overlap

In Multi-Fix, every zone is tagged with the timeframe that produced it: `M5`, `M15`, `H1`, `D`.

An M5 zone sitting inside an H1 zone is a materially different level from an M5 zone floating on its own. Two or three timeframes marking the same price is the highest-agreement evidence this indicator produces.

📊 *Diagram placeholder — one H1 zone with two M5 zones nested inside it, overlap region shaded.*

💡 **Tip.** Use three timeframes, not four: one for bias, one for the trade, one for execution. The fourth slot usually adds clutter rather than information.

## 4.4 The cost

Each active timeframe is a separate data request and its own set of zones. Four timeframes can ask for four times the drawing objects — and TradingView's limits are fixed. Chapter 11 covers the arithmetic; the short version is that **Multi-Fix requires you to reduce "Zones kept per timeframe"**.

📝 **Exercise 4.** Put your chart on M5. Record the number of zones in Auto mode. Switch to Fix = H1 and record it again. Then Multi-Fix M5/M15/H1. Write one sentence on which configuration you could actually trade from.

❓ **Review Questions**
1. In Fix mode on an M1 chart with Fix = M15, how wide is a zone drawn?
2. What does a timeframe tag tell you in Multi-Fix mode?
3. What must you lower when you enable several Multi-Fix timeframes?

---

# Chapter 5 — Reading the Map

This chapter is the professional core of the course. Everything before it described what appears on screen; this describes how the elements relate.

## 5.1 The four questions

| Question | The element that answers it |
|---|---|
| Where is unfinished business? | Fair value gap zones |
| Where are protective orders sitting? | Equal highs / equal lows |
| Has anyone tried those orders and failed? | Liquidity sweeps |
| Has the market stopped doing what it was doing? | MSS, then BOS for continuation |

## 5.2 The sequence

The elements in this indicator are most informative in one particular order:

1. **Map.** On your bias timeframe, note the unfilled zones above and below price. This is the terrain.
2. **Liquidity.** Mark the equal-level shelves and the obvious session extremes. This is where stops sit.
3. **Sweep.** Wait for price to run one of those levels and close back inside it. An attempt has now failed.
4. **Shift.** Wait for MSS in the direction of that rejection. Until structure confirms, a sweep is one wick.
5. **Level.** The displacement that produced the shift normally leaves a fresh zone behind. That zone, or its midpoint, is the area of interest.
6. **Invalidation.** Decide where the idea is objectively wrong — beyond the sweep extreme, or a body close back through the zone — **before** deciding where you would enter.
7. **Size.** Only now. If the distance from entry to invalidation does not fit your risk limit, there is no trade, however convincing the picture.

⚠️ **Steps 1 to 5 are what this indicator shows you. Steps 6 and 7 are what keep you solvent, and the indicator has no opinion about either.**

## 5.3 Institutional notes

- **Imbalance is not a magnet.** A gap is a record of what happened, not a commitment that price will return. Most unfilled gaps on any chart stay unfilled for a long time.
- **A sweep needs a reason to exist.** Ask what liquidity was worth collecting at that level. A sweep of an obvious shelf before a session open is a different event from a random wick in a quiet hour.
- **Continuation is the base case.** BOS after BOS is the market telling you it is still working. Most MSS events in a strong trend are pauses, not reversals — which is exactly why step 4 requires the close and step 6 comes before step 7.
- **Timeframe agreement outranks zone beauty.** A scruffy zone confirmed by two higher timeframes is worth more than a perfect-looking M1 gap alone.

## 5.4 Worked example A — the full sequence

📸 *Screenshot placeholder — sweep, MSS, retrace into the new zone, with invalidation marked.*

1. `EQH` prints on the bias timeframe: two highs within tolerance, a clear shelf.
2. Price runs above that shelf and closes back below it. A **buy-side sweep** label prints. Higher prices were rejected.
3. Displacement lower follows. Price closes below the most recent swing low: **MSS bearish**.
4. That displacement leaves a fresh **bearish zone** above.
5. Invalidation is defined first: a body close back above the zone, or above the sweep high.
6. Only then is entry and size considered, inside the plan.

## 5.5 Worked example B — the sequence that fails

📸 *Screenshot placeholder — sweep with no shift, price continuing through.*

1. A sell-side sweep prints below an `EQL` shelf.
2. No MSS follows. Structure keeps printing bearish BOS lines.
3. Price continues lower and consumes the zone the sweep created.

**Reading:** the sweep was a pause inside a trend, not a turn. Step 4 exists to keep you out of this trade. The absence of an MSS is information, not a delay.

## 5.6 Where the evidence is weakest

| Situation | Why it degrades |
|---|---|
| Thin overnight session | Size filters compare against a quiet ATR, so marginal gaps pass |
| Immediately after a news release | Gaps are wide, structure flips repeatedly, sweeps fire on both sides |
| Symbols without an honest volume feed | The volume split and percentage carry little meaning — use Average Range filtering |
| Very low timeframes on illiquid symbols | Nearly every bar sequence produces geometry that looks like displacement |

📝 **Exercise 5.** Find two completed sequences in your own history: one where sweep → MSS → zone held, and one where the sweep was a pause. Screenshot both. Write the single observable difference that separated them.

❓ **Review Questions**
1. Which step in the sequence separates a wick from evidence?
2. Why is invalidation defined before entry?
3. Give two conditions under which the volume percentage should be ignored.

---

# Chapter 6 — Alerts

## 6.1 The two mechanisms

**A. Named conditions** — pick one signal by name in TradingView's alert dialog:

| Alert name | Fires when |
|---|---|
| `MSS Bullish` / `MSS Bearish` | Structure shifts in that direction |
| `BOS Bullish` / `BOS Bearish` | Structure continues in that direction |
| `MSS (any)` / `BOS (any)` | Either direction of that event |
| `MSS or BOS (any)` | Any structure event |
| `Equal Highs (EQH)` / `Equal Lows (EQL)` | A confirmed equal-level shelf is drawn |
| `Buy-side liquidity sweep` / `Sell-side liquidity sweep` | A sweep prints on that side |
| `Liquidity sweep (any)` | Either side |
| `New FVG (Auto/Fix)` | A zone forms on the Auto or Fix timeframe |
| `New FVG TF#1` … `TF#4` | A zone forms on that Multi-Fix slot |

**B. One alert for everything** — choose **"Any alert() function call"** and receive every enabled structure, equal-level and sweep event through a single alert, with a dynamic message:

```
Bullish BOS | NQ1! | 5 | level 20114.25 | close 20118.50
```

The fields are: direction, event, symbol, timeframe, the level that was broken, and the closing price. Add a **Message prefix** in the settings when a webhook or bot needs a routing tag at the front.

## 6.2 Setup, in order

1. Save the indicator (Chapter 2, Step 1).
2. In **⊹ Alerts**, switch on only the signals you will act on.
3. Leave **Fire on bar close only** ON.
4. Open the alert dialog, set Condition to **THECC FVG PRO**, and choose a named condition or "Any alert() function call".
5. Set expiry and notification method in TradingView.

## 6.3 Why bar-close gating protects you

With the switch ON, an alert can only fire on a **confirmed** bar. With it OFF, the condition is tested on every tick, so price poking through a level mid-bar can alert you to a break that has failed by the close. The switch is the difference between an alert about what happened and an alert about what nearly happened.

⚠️ **Three faults account for almost every "my alert did not fire":**
1. The per-signal toggle in **⊹ Alerts** is off.
2. **Show BOS** is off, so no BOS is detected to alert on.
3. The alert was created against a different indicator instance than the one you later re-configured.

## 6.4 Default alert states

| Signal | Default | Reason |
|---|---|---|
| MSS bullish / bearish | On | Bias-changing, infrequent |
| BOS bullish / bearish | On | Structure events, moderate frequency |
| EQH / EQL | Off | Fire on every confirmed shelf — chatty by nature |
| Liquidity sweeps | Off | Frequency depends entirely on your lookback |

💡 **Tip.** Every extra alert lowers the value of the ones that matter. Begin with `MSS (any)` only. Add a second alert when the first has earned its place in your routine.

📝 **Exercise 6.** Create two alerts: one named `MSS (any)`, and one on "Any alert() function call" with the prefix `THECC`. Record which arrives first on your next structure event and what each message contained.

❓ **Review Questions**
1. Which mechanism gives you the broken level inside the message?
2. What does "Fire on bar close only" actually change in the calculation?
3. Name the three usual causes of an alert that never fires.

---

# Chapter 7 — Customization

Nothing in this build is locked. Every value that affects what you see is a setting, which makes discipline your responsibility rather than the software's.

## 7.1 Tier 1 — settings you will use weekly

| Group | Settings |
|---|---|
| ⊹ Timeframe Mode | Mode, Fix TF |
| ⊹ Multi-Fix Timeframes | Four slots, include chart timeframe |
| General Configuration | Zone Invalidation, Zone Filtering, Detection Sensitivity, Show Historic Zones |
| ⊹ Market Structure | Show, pivot length, MSS on/off, BOS on/off |
| ⊹ Equal Highs / Lows | Show, swing length, tolerance % |
| ⊹ Liquidity Sweeps | Show, lookback |
| ⊹ Alerts | Per-signal toggles, bar-close gating |

## 7.2 Tier 2 — the Zone Engine (advanced)

These were fixed constants in earlier builds and are now exposed. Every default equals the previous hardcoded value, so an untouched chart renders exactly as it did before.

| Setting | Default | Change it when |
|---|---|---|
| Zones kept per timeframe | 125 | Always lower it for Multi-Fix — see Chapter 11 |
| Combine overlapping zones | On | You want each gap kept separate for study |
| Overlap threshold % | 0 | You only want substantial overlaps merged |
| Minimum zone duration (ms) | 3 | Rarely — this is a timestamp difference, not bars |
| Delete untouched zones / after X bars | On / 200 | You want very old untested levels retained |
| Max bars back to process | 10000 | The script is slow, or you need deeper history |
| ATR length | 10 | The size filter feels too twitchy on your symbol |

⚠️ **Detection Sensitivity is a permissiveness dial, not a strictness dial.** The test is `gap size × sensitivity > ATR`. **Extreme = 6.0** admits the most zones; **Low = 1.0** demands the largest gaps. Read it as *how forgiving the filter is*.

| Setting | Multiplier | Effect |
|---|---|---|
| Extreme | 6.0 | Most zones |
| High | 2.0 | Fewer, larger |
| Normal | 1.5 | Fewer still |
| Low | 1.0 | Only clearly oversized gaps |

## 7.3 Style and presentation

Colors, transparency, border styles, label text, sizes, positions and offsets are all editable for every element, as are zone width, dynamic width, extend-latest count, the combined-zone color and tag, volume-bar side and mirroring, and the three Skull Mode colors.

## 7.4 The two values that cannot be settings

`maxBoxesCount` and the debug flag remain constants in the source. TradingView requires the drawing-limit arguments in the indicator declaration to be compile-time constants, so this is a platform rule, not a design choice.

## 7.5 Changing settings honestly

✅ **Do this.** Change one setting at a time, note the date and reason in your journal, and give it a defined number of sessions before judging it.

⚠️ **Never raise sensitivity until a level appears where you wanted one.** That is asking the tool to confirm a decision you have already made. If you find yourself reaching for the settings panel while in a position, close the panel.

📝 **Exercise 7.** Set Detection Sensitivity to Low, then to Extreme, on the same chart. Count zones at each. Write down which setting you will trade for the next five sessions, and why.

❓ **Review Questions**
1. Does Extreme sensitivity produce more zones or fewer?
2. Which single Zone Engine setting must change when you enable Multi-Fix?
3. Why can the drawing limits not be exposed as inputs?

---

# Chapter 8 — Best Practices (Top 20)

1. **Fix detection to your bias timeframe.** Levels that move when you change chart are levels you cannot plan around.
2. **Trade the defaults for a week** before you change a single value.
3. **Define invalidation before entry**, every time, without exception.
4. **Require the close.** Wicks through zones, swings and shelves are not events in this indicator, and should not be events in your plan.
5. **Wait for the shift.** A sweep without an MSS is one wick with a label on it.
6. **Prefer overlap.** Levels confirmed by two or three timeframes outrank single-timeframe zones.
7. **Respect combined zones as areas**, not lines — and place invalidation beyond the whole merged range.
8. **Use the midpoint as the decision point** inside a zone rather than waiting for full consumption.
9. **Match invalidation method to stop placement.** On Close invalidation, your stop belongs beyond the body-close level.
10. **Keep historic zones on while learning.** They are the audit trail of the levels you skipped.
11. **Size the sweep lookback to the level you actually care about** — session high, prior day high, or local swing.
12. **Alert on the fewest signals you can act on**, starting with `MSS (any)`.
13. **Leave bar-close gating on** for anything you will trade.
14. **Use the Average Range filter** on any symbol whose volume feed you do not trust.
15. **Use three Multi-Fix timeframes, not four** — bias, trade, execution.
16. **Lower "Zones kept per timeframe" before you add timeframes**, not after the chart breaks.
17. **Switch to Skull Mode** when the boxes are dominating your read of price action.
18. **Screenshot completed sequences**, with the map visible, and review them weekly.
19. **Change one setting at a time**, dated, with a reason recorded.
20. **Close the settings panel while in a position.** Tuning under pressure is bias wearing a technical costume.

---

# Chapter 9 — Common Mistakes (Top 25)

1. **Trading a zone because it is on the screen.** A zone is a location, not a reason.
2. **Reading "buy-side sweep" as "buy".** It names the side of the book that was taken. It is evidence against that direction.
3. **Raising sensitivity until a level appears** where you wanted one.
4. **Assuming every gap gets filled.** Many never do.
5. **Treating the volume percentage as a quality score.** It measures balance, nothing else.
6. **Using EQH / EQL as an entry trigger** when they are confirmed several bars late by design.
7. **Acting on an intrabar sweep label** that may vanish before the bar closes.
8. **Mismatching invalidation and stops** — running Close invalidation but stopping out on wicks.
9. **Confusing MSS with reversal.** A shift says the prior direction stopped, not that a new trend has begun.
10. **Ignoring BOS.** Continuation is the base case and BOS is how the market states it.
11. **Trading the first sweep in a strong trend.** Usually a pause.
12. **Running four Multi-Fix timeframes at default zone counts**, then blaming the indicator when old drawings vanish.
13. **Leaving detection in Auto** and wondering why levels change with each timeframe switch.
14. **Learning on Heikin Ashi or Renko charts.**
15. **Using the Volume Threshold filter on a symbol with no honest volume feed.**
16. **Turning on every alert**, then muting all of them a week later.
17. **Disabling bar-close gating** for speed, then acting on failed intrabar breaks.
18. **Forgetting that BOS alerts need "Show BOS" on.**
19. **Re-using an old alert** after re-configuring the indicator instance it was attached to.
20. **Judging a settings change after two trades.** Neither outcome was caused by the setting.
21. **Treating a small zone on a low timeframe as equivalent to a large higher-timeframe zone.**
22. **Trading into the news release** because the map looked clean beforehand.
23. **Stacking this indicator with three other gap tools.** You get agreement by construction, not by evidence.
24. **Sizing the position first** and looking for invalidation afterwards.
25. **Blaming the tool for a plan you did not write down.**

---

# Chapter 10 — Frequently Asked Questions (50)

**Detection**

1. **Why is there no zone on an obvious gap?** It failed a filter: the middle bar did not close through the edge, the move was small against ATR, or the bar-to-bar jump exceeded ATR with Allow Gaps off.
2. **What exactly is the middle-bar rule?** For a bullish gap, bar 2 must close above bar 1's high; for a bearish gap, below bar 1's low.
3. **Does the zone include the bars that made it?** No. Only the untraded range.
4. **Same Type or All?** Same Type requires three bars of the same direction — cleanest. All accepts mixed sequences and produces more zones.
5. **Which filter should I use?** Average Range for any symbol; Volume Threshold only where volume is honest.
6. **What does Volume Threshold % compare?** The 5-bar average volume against the 15-bar average.
7. **Does sensitivity make detection stricter?** No — higher settings are more permissive.
8. **What happens if I untick the sensitivity checkbox?** Both size checks are disabled and every geometric gap is drawn. Useful for study, too noisy to trade.
9. **What is Allow Gaps Between Bars for?** Accepting session and news gaps that the ATR jump check otherwise rejects.
10. **Why does the ATR length matter?** It is the reference for both size tests. Longer is smoother and rejects fewer zones on a single volatile bar.
11. **Can a zone appear and then disappear?** Zones are created on confirmed bars, so no. Their appearance can change when zones merge.
12. **Does the indicator repaint?** Zones and structure do not. Sweep labels are evaluated on the live bar and are only evidence once the bar closes.
13. **Why do some zones stop mid-chart?** They were invalidated there.
14. **What is `[Combined]`?** Two or more overlapping same-direction zones merged into one.
15. **Can I stop zones merging?** Yes — switch off Combine overlapping zones.

**Display**

16. **Why do old zones vanish?** You are past TradingView's drawing budget. See Chapter 11.
17. **How many drawing objects does a zone cost?** Four boxes and two lines.
18. **Why does the volume text read `FVG` with no number?** No volume feed for that symbol.
19. **What is the number in brackets?** Volume balance between the zone's halves — high means evenly split.
20. **What is the dashed line inside a zone?** The 50% midpoint.
21. **Why is there a `M15` prefix on some zones?** Multi-Fix mode tags each zone with its source timeframe.
22. **What is Skull Mode for?** Keeping levels while removing nearly all visual weight.
23. **Can I move the volume bars to the other side?** Yes — Volume bars on left side.
24. **What does Mirror volume bars do?** Controls whether the two bars grow from the same edge or toward each other.
25. **Can I change zone width?** Yes — Extend zones by (bars), measured in the zone's own timeframe.
26. **What does Dynamic width do?** Draws an invalidated zone from its start to the bar that consumed it.
27. **Why do the newest zones reach the current bar?** Extend latest zones to current bar, three by default.
28. **Can I hide invalidated zones?** Switch off Show Historic Zones.
29. **Why is the zone start on the third bar?** Start Zones From defaults to Last Bar, which is honest about when the gap was confirmed. First Bar covers the whole formation.
30. **Are the colors theme-aware?** They are semi-transparent and work on both themes; all are editable.

**Structure, levels and sweeps**

31. **What is the difference between MSS and BOS?** MSS is a close through the most recent *opposing* swing — direction stopped. BOS is a close through the most recent swing in the *same* direction — continuation.
32. **Do wicks count?** No. Both require a close.
33. **What does pivot length change?** How large a swing must be to count. Higher means fewer, more significant events.
34. **Why is the same level not marked twice?** Repeat breaks of a marked level are suppressed.
35. **What does "Clear previous structure lines on each new MSS" do?** Wipes earlier structure drawings on every shift, leaving only the current leg.
36. **Why are equal levels late?** Pivots need bars on both sides to be confirmed. The alternative repaints.
37. **What tolerance should I use for equal levels?** Start at the default and raise it on volatile symbols. It is a percentage of price, so it scales.
38. **What is a liquidity sweep here, precisely?** Price takes out the lookback high or low, excluding the current bar, then closes back inside against the direction of the run.
39. **Does the sweep lookback include the current bar?** No.
40. **What lookback should I use?** 10–20 for local sweeps, 50–200 for long-standing levels.
41. **Why do my sweep labels disappear?** Either the bar closed without meeting the condition, or the label cap removed the oldest.
42. **Are MSS, EQH/EQL and sweeps multi-timeframe?** No. They are computed on the chart timeframe; only the zones follow Fix and Multi-Fix.

**Alerts and operation**

43. **Which alert gives me the broken level?** The dynamic `alert()` route — "Any alert() function call".
44. **What does the message prefix do?** Prepends a routing tag for a webhook or bot.
45. **Why did my BOS alert never fire?** Show BOS is off, so no BOS was detected.
46. **Why are sweep and equal-level alerts off by default?** They fire far more often than structure events.
47. **Can I get one alert for everything?** Yes — "Any alert() function call".
48. **Does the script limit alert frequency?** Yes, once per bar per event.
49. **Is this indicator a signal service?** No. It is a market map and issues no buy or sell signals.
50. **Which build does this guide describe?** FVG PRO v2.1.x. Check the version in the guide header against your script header before relying on any detail.

---

# Chapter 11 — Troubleshooting

## 11.1 The drawing budget — read this first

TradingView allows this indicator **500 boxes, 500 lines and 500 labels** in total. Each rendered zone costs **4 boxes and 2 lines**, so:

> **500 boxes ÷ 4 = about 125 zones across every active timeframe — not per timeframe.**

The default "Zones kept per timeframe" is 125, which is the entire box budget for a single timeframe. Add Multi-Fix timeframes without lowering it and TradingView silently discards the oldest objects, which is what people see as "old zones missing" or "half-drawn boxes".

| Active detection timeframes | Suggested zones kept per timeframe |
|---|---|
| 1 (Auto or Fix) | 100–125 |
| 2 | 55 |
| 3 | 35 |
| 4 | 30 |
| 5 (four slots + chart) | 25 |

Labels are shared between structure, equal levels and sweeps: BOS lines are capped by **Max BOS lines** (50), equal-level drawings by **Max EQH/EQL drawings** (20), and sweeps by **Max sweep labels to keep** (50).

## 11.2 Fault table

| Symptom | Likely cause | Fix |
|---|---|---|
| Old zones missing or partly drawn | Box budget exhausted | Lower Zones kept per timeframe per the table above |
| Structure labels disappearing | Label budget shared with sweeps | Lower Max sweep labels, or Max BOS lines |
| No zones at all | Filter too selective, or an empty timeframe slot | Check sensitivity, filter method, and that Fix / Multi-Fix slots are not blank |
| Zones only on recent bars | Max bars back to process | Raise it, or accept it — it exists to keep the script fast |
| Script times out or is slow | Too many timeframes × zones | Fewer slots, fewer zones, shorter history |
| Volume text shows `FVG` only | Symbol has no volume feed | Expected; use Average Range filtering |
| Too many small zones | Sensitivity too permissive | Move Extreme → High → Normal |
| Too few zones | Sensitivity too strict, or Same Type detection | Raise sensitivity, or set FVG Detection to All |
| Equal levels feel late | Pivot confirmation requires bars on both sides | Working as designed — use them as preparation |
| Sweep labels flicker | Evaluated on the live bar | Wait for the close; alerts are gated for this reason |
| Alert never fires | Toggle off · Show BOS off · stale alert instance | Chapter 6.3 |
| Zones differ from a colleague's chart | Different mode, sensitivity, session or symbol | Compare settings before comparing charts |

📝 **Exercise 8.** Deliberately reproduce the drawing-budget fault: set four Multi-Fix timeframes with 125 zones each and note what happens to the oldest zones. Then apply the table and confirm it resolves.

❓ **Review Questions**
1. How many drawing objects does one zone consume?
2. How many zones can be displayed in total, across all timeframes?
3. Give two causes of a label disappearing that are not a bug.

---

# Chapter 12 — Quick Reference (Printable Cheat Sheet)

## On-chart legend

| Mark | Meaning |
|---|---|
| Coloured box | Fair value gap zone (bullish or bearish) |
| Two bars inside the box | Volume split between the zone's halves |
| `12.4K (68%)` | Three-bar volume · how evenly it split (high % = even) |
| `M15 ·` prefix | Multi-Fix zone, tagged with its source timeframe |
| `[Combined]` | Overlapping same-direction zones merged |
| Box ending mid-chart | Invalidated at that bar |
| Box reaching the current bar | One of the most recent live zones |
| Dashed line inside a box | 50% midpoint |
| Solid line + `MSS` | Structure shifted — closed through the last opposing swing |
| Dotted line + `BOS` | Structure continued — closed through the last swing |
| Dashed level + `EQH` / `EQL` | Shelf of two near-equal pivots |
| `$ sweep` above a bar | Buy-side sweep — high taken, closed back below → context for shorts |
| `$ sweep` below a bar | Sell-side sweep — low taken, closed back above → context for longs |

## Detection, one line each

- **Zone** — three-bar gap + middle bar closes through the edge + passes the size or volume filter. Confirmed bars only.
- **MSS** — close beyond the most recent **opposing** swing. Direction stopped.
- **BOS** — close beyond the most recent swing in the **same** direction. Continuation.
- **EQH / EQL** — two consecutive pivots within tolerance, drawn `Swing length` bars later.
- **Sweep** — takes out the lookback high or low, then closes back inside, against the run.

## Sensitivity

`gap size × sensitivity > ATR` → **Extreme 6.0** (most zones) · High 2.0 · Normal 1.5 · **Low 1.0** (fewest, largest)

## The sequence

Map → liquidity → **sweep** → **MSS** → the zone the shift left → invalidation → size.

## Drawing budget

500 boxes / 500 lines / 500 labels. **One zone = 4 boxes + 2 lines → about 125 zones across all timeframes.** Multi-Fix with four slots → 30 zones per timeframe.

## Defaults worth memorising

| Setting | Default |
|---|---|
| Zone Invalidation | Close (body must close through) |
| Zone Filtering | Average Range |
| Detection Sensitivity | Extreme |
| Zones kept per timeframe | 125 |
| Delete untouched zones after | 200 bars |
| ATR length | 10 |
| Pivot length (MSS / BOS) | 5 |
| Max BOS lines | 50 |
| EQ swing length / tolerance | 5 / 0.02% |
| Sweep lookback / max labels | 20 / 50 |
| Fire on bar close only | On |
| MSS + BOS alerts / EQ + sweep alerts | On / Off |

## Alert names

`MSS Bullish` · `MSS Bearish` · `BOS Bullish` · `BOS Bearish` · `MSS (any)` · `BOS (any)` · `MSS or BOS (any)` · `Equal Highs (EQH)` · `Equal Lows (EQL)` · `Buy-side liquidity sweep` · `Sell-side liquidity sweep` · `Liquidity sweep (any)` · `New FVG (Auto/Fix)` · `New FVG TF#1`–`TF#4` · or **Any alert() function call**

---

# Appendix A — Certification Quiz

**20 questions · pass mark 80% (16 correct) · closed book.**

1. What must the middle bar of a three-bar sequence do before a zone is drawn?
2. State the size test applied to the gap, including the role of sensitivity.
3. Does Extreme sensitivity admit more zones or fewer than Low?
4. What does the percentage in a zone's text measure?
5. On a bullish zone, which bars' volume is shown in the upper half?
6. What does `[Combined]` indicate, and how does it affect invalidation placement?
7. Define *confirmed* as the Academy uses the term.
8. Which elements of this indicator can change intrabar, and which cannot?
9. State the difference between MSS and BOS in one sentence each.
10. Why does a repeated break of the same level not draw a second line?
11. Why are equal-level lines drawn several bars after the second pivot?
12. Define a buy-side liquidity sweep precisely, and state which direction it is evidence for.
13. Does the sweep lookback window include the current bar?
14. Which elements follow Fix / Multi-Fix timeframes, and which are always chart-timeframe?
15. In Fix mode = M15 on an M1 chart, how wide is a zone drawn?
16. Give the seven steps of the reading sequence in order.
17. At which step is position size decided, and why not earlier?
18. How many boxes and lines does one rendered zone consume, and what is the total zone budget?
19. Name the three usual causes of an alert that does not fire.
20. Which two decisions does this indicator never make for you?

*Answers are held in the Instructor Answer Key (`THECC-DOC-FVGPRO-AK`).*

---

# Appendix B — Glossary

| Term | Definition |
|---|---|
| **Fair value gap (FVG)** | A price range skipped by one-sided participation, left untraded between bar 1 and bar 3 of a displacement sequence |
| **Imbalance** | The same event described from the order-flow side: one side was overwhelmed |
| **Displacement** | A fast, one-directional move that is large relative to recent range |
| **Confirmed** | The candle has closed and the result is locked |
| **Repaint** | A drawing or signal that changes after it first appeared |
| **Invalidation** | Price trading back through a zone far enough to use it up, by wick or by body close depending on your setting |
| **Midpoint** | The 50% level of a zone |
| **Combined zone** | Two or more overlapping same-direction zones merged into one |
| **BOS** | Break of Structure — a close through the most recent swing in the established direction |
| **MSS** | Market Structure Shift — a close through the most recent opposing swing |
| **Pivot** | A swing high or low confirmed by a required number of bars on each side |
| **EQH / EQL** | Equal highs / equal lows — a shelf of near-equal pivots where protective orders cluster |
| **Liquidity sweep** | A run through a level that closes back inside it; a failed breakout |
| **Lookback** | How many bars back a calculation measures |
| **Volume split** | How the three-bar volume divided between the upper and lower half of a zone |
| **Skull Mode** | A display mode that reduces each zone to its midpoint line and faint volume bars |
| **Multi-Fix** | Detection across up to four chosen timeframes at once, each zone tagged with its source |
| **Drawing budget** | TradingView's fixed limit of 500 boxes, 500 lines and 500 labels per indicator |

---

# Course Summary

Fair Value Gaps PRO records where participation was one-sided, where protective orders sit, where an attempt on those orders failed, and whether the market has stopped doing what it was doing. It then stays out of your way. The judgement — direction, entry, invalidation, size — is entirely yours, and the tool is built so that nothing in it can pretend otherwise.

## Key Takeaways

1. A zone is evidence of participation, not a prediction, and not an instruction.
2. The middle-bar close and the size filter are what separate this from a generic gap tool.
3. Everything meaningful in this indicator requires a **close**.
4. MSS says the prior direction stopped; BOS says it is continuing. Only one of those changes your bias.
5. Equal levels are preparation, not triggers, because honest pivots arrive late.
6. A sweep without a structure shift is one wick with a label on it.
7. Timeframe agreement outranks how attractive any single zone looks.
8. Invalidation is defined before entry, and size comes last.
9. The drawing budget is real: four boxes and two lines per zone, about 125 zones in total.
10. The tool holds no opinion on risk. That gap is yours to fill, in writing.

## Knowledge Check

1. Which single setting most often needs lowering, and in which mode?
2. Which elements of the indicator are chart-timeframe only?
3. What is the correct reading of a 40% volume balance figure?
4. Why does the guide insist that "buy-side sweep" is not a buy instruction?
5. What is the one step the indicator cannot help you with at all?

## Cross References

| Document | Document ID | Purpose |
|---|---|---|
| Cheat Sheet | `THECC-DOC-FVGPRO-CS` | One-page on-chart legend and defaults |
| Quick Start | `THECC-DOC-FVGPRO-QS` | Installation and first chart in ten minutes |
| Instructor Guide | `THECC-DOC-FVGPRO-IG` | Teaching notes, timings, discussion prompts |
| Answer Key | `THECC-DOC-FVGPRO-AK` | Certification quiz answers |
| Workbook | `THECC-DOC-FVGPRO-WB` | Exercises and journalling templates |
| Release Notes | `THECC-DOC-FVGPRO-RN` | What changed in v2.1 |
| Academy Documentation Standard | `_ACADEMY_DOC_STANDARD_v1.0.md` | The standard governing this document |

⚠️ Documents other than the Student Guide and Cheat Sheet are **not yet authored** for this product. The Academy suite is 20 documents per indicator; this release delivers 2.

---

# Document Control

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| v2.1.0 | 2026-09-20 | Dale Batise | First Academy-standard Student Guide for Fair Value Gaps PRO. Covers zones, volume split, timeframe modes, market structure (MSS / BOS), equal highs and lows, liquidity sweeps, the Zone Engine settings tier, alerts, best practices, mistakes, 50 FAQs, troubleshooting, quiz and glossary. |

## Compatibility

| Item | Value |
|---|---|
| Indicator | THECC Fair Value Gaps PRO |
| Registry ID | **Pending** — see the warning in the front matter |
| Indicator versions | v2.1.x |
| Platform | TradingView · Pine Script v6 |
| Academy Doc Standard | v1.0 |
| Dependencies | None — standalone |
| Companion products | Precision Execution Engine (THECC-0002) · Support & Resistance Matrix (THECC-0024) |

## Certification status

**Content Complete — Certification Pending.** The v2.1 build has not been green-checked on TradingView at the time of writing. Per Academy Documentation Standard v1.0 §2a, `Production Certified` may not be stamped on this material until the build passes the TradingView compile green-check and the owner signs off.

## Copyright and disclaimer

© THE CONSISTENCY COLLECTIVE. All THECC Academy materials and indicators are the property of THE CONSISTENCY COLLECTIVE and distributed under the THECC licence.

**Educational material only.** Nothing in this document is financial advice, a signal service, a solicitation, or a claim about future results. Trading futures and other leveraged instruments carries substantial risk of loss. You are responsible for your own decisions, your own risk limits, and your own compliance with the rules of your broker or prop firm.

## Footer convention

Running footer on rendered formats:
`THECC Institutional Trader Academy™ · Fair Value Gaps PRO Student Guide v2.1.0 · © THE CONSISTENCY COLLECTIVE · Page N of M`

---

*© THE CONSISTENCY COLLECTIVE — THECC Institutional Trader Academy™ · Consistency Creates Freedom. · Academy Documentation Standard v1.0.*
