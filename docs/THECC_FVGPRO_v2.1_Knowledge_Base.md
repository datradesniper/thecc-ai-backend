<!-- ┌─────────────────────────────────────────────────────────────────────┐ -->
<!-- │ THECC INSTITUTIONAL TRADER ACADEMY™ — STANDARD DOCUMENT FRONT-MATTER │ -->
<!-- └─────────────────────────────────────────────────────────────────────┘ -->

# THECC Fair Value Gaps PRO — Knowledge Base

### THECC Institutional Trader Academy™

*The single reference table set for this product. Every figure quoted in the other documents comes from here.*

#### 📘 Course Metadata

| Field | Value |
|---|---|
| **Academy** | THECC Institutional Trader Academy™ |
| **Course** | Fair Value Gaps PRO |
| **Module** | Reference |
| **Lesson** | Knowledge Base |
| **Difficulty** | All |
| **Estimated Time** | Reference |
| **Prerequisites** | None |
| **Indicator Version** | v2.1 |
| **Document Version** | v2.1.0 |
| **Last Updated** | 2026-09-20 |
| **Instructor** | Dale Batise |
| **Status** | Content Complete — Certification Pending |

**Document control:**

| Field | Value |
|---|---|
| Document ID | THECC-DOC-FVGPRO-KB |
| Document type | Knowledge Base |
| Indicator | THECC Fair Value Gaps PRO · **Registry ID pending** |
| Version | v2.1.0 |
| Build | 2.1.0+2026-09-20 |
| Release date | 2026-09-20 |
| Compatible indicator versions | FVG PRO v2.1.x |
| Academy Doc Standard | v1.0 |
| Edition | Internal Master |
| Platform | TradingView · Pine Script v6 |
| Copyright | © THE CONSISTENCY COLLECTIVE |

**Consistency Creates Freedom.**

---

## KB-01 · Detection formulas

| Element | Formula |
|---|---|
| Bullish gap geometry | `low > high[2]` |
| Bearish gap geometry | `high < low[2]` |
| Bullish middle-bar close | `close[1] > high[2]` |
| Bearish middle-bar close | `close[1] < low[2]` |
| Average Range filter | three-bar body sum × sensitivity > ATR ÷ 1.5 |
| Volume Threshold filter | `sma(volume,5) > sma(volume,15) × (threshold ÷ 100)` |
| Jump check | `max(abs(close[2]−open[1]), abs(close[1]−open)) ≤ ATR` unless Allow Gaps |
| Gap size test | `gapSize × sensitivity > ATR` |
| Volume balance % | `min(highVol, lowVol) ÷ max(highVol, lowVol) × 100` |
| Equal-level tolerance | `abs(a − b) ≤ lastPivot × tolerance ÷ 100` |
| Buy-side sweep | `high > highest(high[1], lookback) and close < that high and close < open` |
| Sell-side sweep | `low < lowest(low[1], lookback) and close > that low and close > open` |

## KB-02 · Sensitivity map

| Setting | Multiplier |
|---|---|
| Extreme | 6.0 |
| High | 2.0 |
| Normal | 1.5 |
| Low | 1.0 |

Higher = more permissive. Unticking the checkbox disables both size tests entirely.

## KB-03 · Every default

| Group | Setting | Default |
|---|---|---|
| Timeframe | Mode | Auto |
| Timeframe | Fix TF | 15 |
| Multi-Fix | TF #1–#4 | 5 · 15 · 60 · blank |
| Multi-Fix | Include chart timeframe | Off |
| General | Zone Invalidation | Close |
| General | Zone Filtering | Average Range |
| General | Volume Threshold % | 50 |
| General | FVG Detection | Same Type |
| General | Detection Sensitivity | Extreme (enabled) |
| General | Allow Gaps Between Bars | Off |
| General | Show Historic Zones | On |
| Zone Engine | Zones kept per timeframe | 125 |
| Zone Engine | Combine overlapping zones | On |
| Zone Engine | Overlap threshold % | 0 |
| Zone Engine | Minimum zone duration (ms) | 3 |
| Zone Engine | Delete untouched zones / after | On / 200 bars |
| Zone Engine | Max bars back to process | 10000 |
| Zone Engine | ATR length | 10 |
| Style | Start zones from | Last Bar |
| Style | Extend zones by (bars) | 15 |
| Style | Dynamic width | On |
| Style | Extend latest zones / count | On / 3 |
| Style | Recolour combined zones | Off |
| Style | Tag combined zones in text | On |
| Style | Volume bars on left side | On |
| Style | Mirror volume bars | On |
| Skull | Enable | Off |
| Structure | Show market structure | On |
| Structure | Pivot length | 5 |
| Structure | Show MSS / Show BOS | On / On |
| Structure | Max BOS lines | 50 |
| Structure | Clear previous lines on MSS | Off |
| Equal levels | Show | On |
| Equal levels | Swing length | 5 |
| Equal levels | Tolerance % | 0.02 |
| Equal levels | Extend bars | 10 |
| Equal levels | Max drawings | 20 |
| Sweeps | Show | On |
| Sweeps | Lookback | 20 |
| Sweeps | Max labels | 50 |
| Alerts | Fire on bar close only | On |
| Alerts | MSS / BOS toggles | On |
| Alerts | EQH / EQL / sweep toggles | Off |
| Alerts | Message prefix | empty |

## KB-04 · Alert inventory

| # | Name | Type |
|---|---|---|
| 1–4 | `MSS Bullish` · `MSS Bearish` · `BOS Bullish` · `BOS Bearish` | Named |
| 5–7 | `MSS (any)` · `BOS (any)` · `MSS or BOS (any)` | Named |
| 8–9 | `Equal Highs (EQH)` · `Equal Lows (EQL)` | Named |
| 10–12 | `Buy-side liquidity sweep` · `Sell-side liquidity sweep` · `Liquidity sweep (any)` | Named |
| 13–17 | `New FVG (Auto/Fix)` · `New FVG TF#1`–`TF#4` | Named |
| — | Any alert() function call | Dynamic, once per bar |

Dynamic message format:
`<direction> <event> | <ticker> | <timeframe> | level <price> | close <price>`

## KB-05 · Timeframe scope

| Element | Follows Fix / Multi-Fix? |
|---|---|
| Fair value gap zones | Yes |
| Volume split and text | Yes |
| MSS / BOS | No — chart timeframe |
| Equal highs / lows | No — chart timeframe |
| Liquidity sweeps | No — chart timeframe |

## KB-06 · Repaint status

| Element | Behaviour |
|---|---|
| Zones | Created on confirmed bars — no repaint |
| Zone appearance | Merging and extension redraw on the last bar |
| MSS / BOS | Close-based, pivots confirmed one bar later — no repaint |
| Equal levels | Confirmed `Swing length` bars after the second pivot — no repaint, but late by design |
| Sweep labels | Evaluated on the live bar — can appear and vanish before the close |
| Alerts | Confirmed-bar gated while "Fire on bar close only" is on |

## KB-07 · Drawing budget

| Element | Boxes | Lines | Labels |
|---|---|---|---|
| One zone | 4 | 2 | 0 |
| One MSS / BOS | 0 | 1 | 1 |
| One equal level | 0 | 1 | 1 |
| One sweep | 0 | 0 | 1 |
| **Ceiling** | **500** | **500** | **500** |

**Total zone capacity ≈ 125 across all active timeframes.**

| Active timeframes | Zones kept per timeframe |
|---|---|
| 1 | 100–125 |
| 2 | 55 |
| 3 | 35 |
| 4 | 30 |
| 5 | 25 |

## KB-08 · Fault signatures

| Signature | Cause |
|---|---|
| Zone box with no volume bars or text | Box budget exhausted mid-zone |
| Oldest zones absent | Box budget |
| Labels vanishing while lines remain | Label ceiling |
| `FVG` text with no number | No volume feed |
| No zones after a settings change | Sensitivity, filter, or blank slot |
| Structure line missing at an obvious break | The break was a wick |
| All structure gone at once | Clear-on-shift enabled |
| Sweep label flickering intrabar | Live-bar evaluation |

## KB-09 · Terminology lock

| Term | Locked meaning |
|---|---|
| Confirmed | The candle has closed and the result is locked |
| Repaint | A drawing or signal that changes after it first appeared |
| Sensitivity | A permissiveness multiplier, not a strictness one |
| Balance % | Volume split evenness, never quality or probability |
| Buy-side sweep | The side of the book taken — evidence against higher prices |
| Map | A context tool that issues no trade signals |

## KB-10 · Open items

| Item | State |
|---|---|
| Registry ID | Not assigned — question raised under THECC-0008 |
| `_SOURCE_OF_TRUTH.json` | Not created |
| TradingView compile green-check | Not performed |
| Screenshots and diagrams | Placeholders |
| Portal QR URLs | Not issued |
| DOCX renders | Not produced — see the Documentation Index |
| PDF renders | Produced by `make_pdf.py` at v2.1.0 |

---

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| v2.1.0 | 2026-09-20 | Dale Batise | First Knowledge Base for Fair Value Gaps PRO v2.1: formulas, sensitivity map, complete defaults, alert inventory, timeframe scope, repaint status, drawing budget, fault signatures, terminology lock and open items. |

**Educational material only. Not financial advice, not a signal service, and not a claim about future results.**

---

*© THE CONSISTENCY COLLECTIVE — THECC Institutional Trader Academy™ · Consistency Creates Freedom. · Academy Documentation Standard v1.0.*
