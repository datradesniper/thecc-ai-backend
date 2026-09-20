<!-- ┌─────────────────────────────────────────────────────────────────────┐ -->
<!-- │ THECC INSTITUTIONAL TRADER ACADEMY™ — STANDARD DOCUMENT FRONT-MATTER │ -->
<!-- └─────────────────────────────────────────────────────────────────────┘ -->

# THECC Fair Value Gaps PRO — Cheat Sheet

### THECC Institutional Trader Academy™

#### 📘 Course Metadata

| Field | Value |
|---|---|
| **Academy** | THECC Institutional Trader Academy™ |
| **Course** | Fair Value Gaps PRO |
| **Module** | Reference |
| **Lesson** | All |
| **Difficulty** | Beginner → Intermediate |
| **Estimated Time** | 10 minutes |
| **Prerequisites** | Student Guide Chapters 1–3 |
| **Indicator Version** | v2.1 |
| **Document Version** | v2.1.0 |
| **Last Updated** | 2026-09-20 |
| **Instructor** | Dale Batise |
| **Status** | Content Complete — Certification Pending |

**Document control:**

| Field | Value |
|---|---|
| Document ID | THECC-DOC-FVGPRO-CS |
| Document type | Cheat Sheet (Reference) |
| Indicator | THECC Fair Value Gaps PRO · **Registry ID pending** |
| Version | v2.1.0 |
| Build | 2.1.0+2026-09-20 |
| Release date | 2026-09-20 |
| Compatible indicator versions | FVG PRO v2.1.x |
| Academy Doc Standard | v1.0 |
| Edition | Student / Pro · Status: Beta |
| Platform | TradingView · Pine Script v6 |
| Copyright | © THE CONSISTENCY COLLECTIVE |

[ QR CODE PLACEHOLDER — links to the current version of this sheet in the Member Portal ]

**Consistency Creates Freedom.**

---

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
| `$ sweep` above a bar | Buy-side sweep — high taken, closed back below → context for **shorts** |
| `$ sweep` below a bar | Sell-side sweep — low taken, closed back above → context for **longs** |

## Detection in one line each

| Element | Rule |
|---|---|
| **Zone** | Three-bar gap + middle bar closes through the edge + passes the size or volume filter. Confirmed bars only. |
| **MSS** | Close beyond the most recent **opposing** swing → direction stopped |
| **BOS** | Close beyond the most recent swing in the **same** direction → continuation |
| **EQH / EQL** | Two consecutive pivots within tolerance, drawn `Swing length` bars later |
| **Sweep** | Takes out the lookback high or low, then closes back inside, against the run |

## Sensitivity is permissiveness

`gap size × sensitivity > ATR`

| Setting | Multiplier | Result |
|---|---|---|
| Extreme | 6.0 | Most zones |
| High | 2.0 | Fewer, larger |
| Normal | 1.5 | Fewer still |
| Low | 1.0 | Only clearly oversized gaps |

## The reading sequence

**Map → liquidity → sweep → MSS → the zone the shift left → invalidation → size.**

Steps 1–5 are what the indicator shows you. Steps 6–7 are yours, and they are the ones that matter.

## Drawing budget

500 boxes / 500 lines / 500 labels per indicator. **One zone = 4 boxes + 2 lines → about 125 zones in total, across all timeframes.**

| Active detection timeframes | Zones kept per timeframe |
|---|---|
| 1 | 100–125 |
| 2 | 55 |
| 3 | 35 |
| 4 | 30 |
| 5 | 25 |

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

`MSS Bullish` · `MSS Bearish` · `BOS Bullish` · `BOS Bearish` · `MSS (any)` · `BOS (any)` · `MSS or BOS (any)` · `Equal Highs (EQH)` · `Equal Lows (EQL)` · `Buy-side liquidity sweep` · `Sell-side liquidity sweep` · `Liquidity sweep (any)` · `New FVG (Auto/Fix)` · `New FVG TF#1`–`TF#4`

Or one alert on **Any alert() function call**:

```
Bullish BOS | NQ1! | 5 | level 20114.25 | close 20118.50
```

## Three rules that prevent most errors

1. **Everything requires a close.** Wicks are not events.
2. **A sweep without an MSS is one wick with a label on it.**
3. **Invalidation before entry. Size last.**

---

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| v2.1.0 | 2026-09-20 | Dale Batise | First Academy-standard Cheat Sheet for Fair Value Gaps PRO (v2.1, including liquidity sweeps). |

**Educational material only. Not financial advice, not a signal service, and not a claim about future results.**

---

*© THE CONSISTENCY COLLECTIVE — THECC Institutional Trader Academy™ · Consistency Creates Freedom. · Academy Documentation Standard v1.0.*
