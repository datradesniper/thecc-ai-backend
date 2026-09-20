<!-- ┌─────────────────────────────────────────────────────────────────────┐ -->
<!-- │ THECC INSTITUTIONAL TRADER ACADEMY™ — STANDARD DOCUMENT FRONT-MATTER │ -->
<!-- └─────────────────────────────────────────────────────────────────────┘ -->

# THECC Fair Value Gaps PRO — Troubleshooting Manual

### THECC Institutional Trader Academy™

#### 📘 Course Metadata

| Field | Value |
|---|---|
| **Academy** | THECC Institutional Trader Academy™ |
| **Course** | Fair Value Gaps PRO |
| **Module** | Reference |
| **Lesson** | Troubleshooting |
| **Difficulty** | Beginner → Intermediate |
| **Estimated Time** | 15 minutes |
| **Prerequisites** | Student Guide Chapters 1–4 |
| **Indicator Version** | v2.1 |
| **Document Version** | v2.1.0 |
| **Last Updated** | 2026-09-20 |
| **Instructor** | Dale Batise |
| **Status** | Content Complete — Certification Pending |

**Document control:**

| Field | Value |
|---|---|
| Document ID | THECC-DOC-FVGPRO-TS |
| Document type | Troubleshooting Manual |
| Indicator | THECC Fair Value Gaps PRO · **Registry ID pending** |
| Version | v2.1.0 |
| Build | 2.1.0+2026-09-20 |
| Release date | 2026-09-20 |
| Compatible indicator versions | FVG PRO v2.1.x |
| Academy Doc Standard | v1.0 |
| Edition | Student / Pro · Status: Beta |
| Platform | TradingView · Pine Script v6 |
| Copyright | © THE CONSISTENCY COLLECTIVE |

**Consistency Creates Freedom.**

---

## 1 · Five checks before anything else

Run these in order. They resolve most reports.

| # | Check | Why |
|---|---|---|
| 1 | Is the script **saved**, and is this the instance you configured? | Alerts and settings attach to a saved instance. Duplicates are the most common cause of "my settings did nothing". |
| 2 | Standard candles? | Heikin Ashi, Renko and Range bars synthesize prices. Everything downstream changes. |
| 3 | In Fix or Multi-Fix, is any timeframe slot **blank**? | A blank slot draws nothing. |
| 4 | Multi-Fix on? What is **Zones kept per timeframe**? | The drawing budget is the single biggest source of display faults. Section 2. |
| 5 | Does the symbol have a real volume feed? | Without one, the volume text and the Volume Threshold filter are meaningless. Use Average Range. |

---

## 2 · The drawing budget

**This is not a bug and it cannot be coded around.** TradingView allows each indicator 500 boxes, 500 lines and 500 labels. The platform then discards the oldest objects **silently**.

| Element | Cost |
|---|---|
| One rendered zone | 4 boxes + 2 lines |
| One MSS or BOS event | 1 line + 1 label |
| One equal-level shelf | 1 line + 1 label |
| One liquidity sweep | 1 label |

**500 boxes ÷ 4 = about 125 zones in total, across every active timeframe — not per timeframe.**

| Active detection timeframes | Set zones kept per timeframe to |
|---|---|
| 1 (Auto or Fix) | 100–125 |
| 2 | 55 |
| 3 | 35 |
| 4 | 30 |
| 5 (four slots + chart) | 25 |

Caps that protect the label ceiling: **Max BOS lines** (50), **Max EQH/EQL drawings** (20), **Max sweep labels to keep** (50). Raising one takes room from the others.

---

## 3 · Display faults

| Symptom | Diagnosis | Fix |
|---|---|---|
| Old zones missing | Box budget exhausted | Lower zones kept per the table in section 2 |
| Zones drawn partly — box but no volume bars, or no text | Budget exhausted mid-zone: some of its four boxes were discarded | As above. This is the clearest signature of the budget fault. |
| Structure or sweep labels disappearing | Label ceiling reached | Lower **Max sweep labels to keep**, or **Max BOS lines** |
| No zones at all | Filter too selective · blank timeframe slot · symbol with no volume on Volume Threshold | Raise Detection Sensitivity toward Extreme · check slots · switch to Average Range |
| Zones only on recent bars | **Max bars back to process** (10000) | Raise it, accepting slower loading |
| Far fewer zones than a colleague | Different sensitivity, filter, detection type, session or symbol | Compare settings side by side before comparing charts |
| Zones changed when you changed chart timeframe | Detection is in **Auto** | Set Fix to your bias timeframe |
| Zone text reads `FVG` with no number | No volume feed | Expected. Use Average Range filtering. |
| Boxes dominate the chart | Presentation, not a fault | Skull Mode, or switch off Show Historic Zones |
| Zone starts earlier than you remember | **Start Zones From = First Bar** | Set to Last Bar, which reflects when the gap was confirmed |

---

## 4 · Structure, equal levels and sweeps

| Symptom | Diagnosis | Fix |
|---|---|---|
| No MSS or BOS lines | **Show Market Structure** off, or pivot length too high for the chart | Enable; lower pivot length toward 5 |
| BOS never appears | **Show BOS** off — this gates detection, not just drawing | Enable it. BOS alerts also depend on it. |
| Structure ignored an obvious break | The break was a wick. Structure requires a **close**. | Working as designed |
| Only one line at a level that broke twice | Duplicate-level suppression | Working as designed |
| All structure lines vanished at once | **Clear previous structure lines on each new MSS** is on | Switch it off to keep history |
| Equal levels appear late | Pivots need bars on both sides to confirm | Working as designed — the alternative repaints |
| No equal levels at all | Tolerance too tight for the symbol | Raise **Equal level tolerance %** gradually |
| Sweep label appeared then vanished | Evaluated on the live bar; the close did not meet the condition | Working as designed. Only closed bars are evidence. |
| Far too many sweeps | Lookback too short for the level you care about | Raise it — 50–200 for long-standing levels |
| A sweep marked where price kept going | Sweeps mark failed breakouts, not reversals | Require an MSS before treating it as a turn |

---

## 5 · Alerts

Work through in this order.

1. **Is the per-signal toggle on?** `⊹ Alerts` has one switch per event. An off switch produces nothing in either alert mechanism.
2. **For BOS alerts, is Show BOS on?** Detection is gated by it.
3. **Is the alert attached to the current saved instance?** Delete and recreate after re-configuring.
4. **Which mechanism did you pick?** A named condition fires only that event. "Any alert() function call" fires every enabled event.
5. **Is the alert still active?** Check TradingView's expiry.

| Symptom | Diagnosis | Fix |
|---|---|---|
| Nothing ever fires | Toggle off, or stale instance | Steps 1 and 3 |
| Fires far too often | Equal-level or sweep alerts enabled | They default off for this reason — disable, or raise the sweep lookback |
| Fired, then price reversed the break | Bar-close gating off | Switch **Fire on bar close only** back on |
| Message has no level | You used a named condition | Use "Any alert() function call" for the dynamic message |
| Webhook rejects the payload | Prefix or format mismatch | Set **Message prefix**; the format is `<direction> <event> \| <ticker> \| <timeframe> \| level <price> \| close <price>` |
| Two alerts for one event | A named condition and the dynamic route both active | Keep one |

---

## 6 · Performance

| Symptom | Diagnosis | Fix |
|---|---|---|
| Script times out or fails to load | Too many timeframes × zones × history | Fewer Multi-Fix slots, lower zones kept, lower max bars back |
| Slow chart when scrolling | Object count | As above; Skull Mode does not reduce object count materially |
| Slow only on one symbol | Very long history or thin data | Lower max bars back to process |

💡 Cost order, highest first: number of active detection timeframes → zones kept per timeframe → max bars back to process. Reduce in that order.

---

## 7 · Escalation

Before raising an issue, capture:

1. Symbol, chart timeframe, session and chart type
2. Detection mode and, for Multi-Fix, every slot value
3. Detection Sensitivity, Zone Filtering, Zone Invalidation, Zones kept per timeframe
4. A screenshot showing the whole chart including the indicator name in the legend
5. The indicator version from the script header, and whether the script is saved
6. For alert issues: which mechanism, which condition name, and the exact message received

⚠️ Two behaviors are frequently reported as faults and are neither: **the drawing budget** discarding old objects, and **equal levels arriving late**. Both are documented above and in the Student Guide.

---

## 8 · Cross references

| Document | ID |
|---|---|
| Student Guide (Chapter 11 covers the same ground in course form) | `THECC-DOC-FVGPRO-SG` |
| Cheat Sheet | `THECC-DOC-FVGPRO-CS` |
| Release Notes — known limitations | `THECC-DOC-FVGPRO-RN` |
| Instructor Guide — student error table | `THECC-DOC-FVGPRO-IG` |

---

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| v2.1.0 | 2026-09-20 | Dale Batise | First Troubleshooting Manual for Fair Value Gaps PRO v2.1: five first checks, the drawing budget, display, structure, alert and performance fault tables, escalation capture list. |

**Educational material only. Not financial advice, not a signal service, and not a claim about future results.**

---

*© THE CONSISTENCY COLLECTIVE — THECC Institutional Trader Academy™ · Consistency Creates Freedom. · Academy Documentation Standard v1.0.*
