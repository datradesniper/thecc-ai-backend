<!-- ┌─────────────────────────────────────────────────────────────────────┐ -->
<!-- │ THECC INSTITUTIONAL TRADER ACADEMY™ — STANDARD DOCUMENT FRONT-MATTER │ -->
<!-- └─────────────────────────────────────────────────────────────────────┘ -->

# THECC Fair Value Gaps PRO — Quick Start

### THECC Institutional Trader Academy™

#### 📘 Course Metadata

| Field | Value |
|---|---|
| **Academy** | THECC Institutional Trader Academy™ |
| **Course** | Fair Value Gaps PRO |
| **Module** | 1 (Onboarding) |
| **Lesson** | Quick Start |
| **Difficulty** | Beginner |
| **Estimated Time** | 10 minutes |
| **Prerequisites** | None |
| **Indicator Version** | v2.1 |
| **Document Version** | v2.1.0 |
| **Last Updated** | 2026-09-20 |
| **Instructor** | Dale Batise |
| **Status** | Content Complete — Certification Pending |

**Document control:**

| Field | Value |
|---|---|
| Document ID | THECC-DOC-FVGPRO-QS |
| Document type | Quick Start |
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

## Callout legend

💡 Tip · ⚠️ Warning · ✅ Do this · 📸 Screenshot · 📝 Exercise

---

## In one paragraph

Fair Value Gaps PRO marks where price moved so hard it left an untraded gap, and keeps that level on your chart until price uses it up. It adds the volume behind each gap, whether market structure has shifted or continued, where equal highs and lows have stacked protective orders, and where a run on those orders failed. **It issues no buy or sell signals.** It tells you where; your plan decides whether.

---

## Ten minutes, six steps

### 1 · Add it (2 min)

Open TradingView → **Pine Editor** → paste the `.pine` file from your licence → **Add to chart** → **Save**.

✅ Saving is not optional. An unsaved script cannot carry alerts.

### 2 · Set the chart (1 min)

| Setting | Use |
|---|---|
| Symbol | Something liquid — NQ, ES, a major index |
| Candles | **Standard** only |
| Timeframe | M5 to start |
| Session | Regular hours while you learn |

⚠️ Heikin Ashi, Renko and Range bars invent their own prices. Gaps found on them are not gaps in the market.

### 3 · Leave the defaults alone (0 min)

They are already conservative: body-close invalidation, range-based filtering, structure and equal levels on, sweeps on, alerts gated to bar close.

⚠️ The one number worth changing early is **Zones kept per timeframe** — and only if you turn on Multi-Fix. See step 6.

### 4 · Learn the six marks (4 min)

| On your chart | What it means |
|---|---|
| Coloured box | A fair value gap — an untraded range left by a hard move |
| Two bars + `12.4K (68%)` inside it | The volume that built it, and how evenly it split (high % = even) |
| Dashed line across the box | The 50% midpoint |
| Solid line + `MSS` | Structure **shifted** — the prior direction stopped |
| Dotted line + `BOS` | Structure **continued** |
| `$ sweep` label | A level was run and price closed back inside — a failed breakout |

💡 A `$ sweep` **above** a bar is evidence against higher prices. The word names the side of the order book that was taken, not a direction to trade.

### 5 · Set one alert (2 min)

Alert dialog → Condition = **THECC FVG PRO** → choose **`MSS (any)`** → save.

One alert. That is the whole recommendation for week one. Structure shifts are infrequent and they are the events that change a bias.

### 6 · If you turn on Multi-Fix (1 min)

Multi-Fix draws zones from several timeframes at once, each tagged `M5`, `M15`, `H1`. It is the best feature in the product and it has a cost: TradingView allows 500 boxes and each zone uses four.

| Timeframes you switch on | Set "Zones kept per timeframe" to |
|---|---|
| 1 | 100–125 |
| 2 | 55 |
| 3 | 35 |
| 4 | 30 |

Skip this and the oldest zones silently vanish.

---

## Your first week

| Day | Task |
|---|---|
| 1 | Install, defaults, M5 chart. Screenshot one zone and write what the volume figure says. |
| 2 | Switch detection to **Fix** on M15. Note that your levels stop moving when you change chart timeframe. |
| 3 | Find one `MSS` and one `BOS`. Write the difference in your own words. |
| 4 | Find one `$ sweep`. Check what happened next: shift, or continuation? |
| 5 | Find a full sequence: sweep → MSS → the fresh zone it left. Mark where the idea would have been wrong. |
| 6–7 | Review your screenshots. No trades taken from this tool until you can name the invalidation before the entry. |

---

## The three rules that matter most

1. **Everything needs a close.** Wicks through zones, swings and shelves are not events.
2. **A sweep without a structure shift is one wick with a label on it.**
3. **Invalidation before entry. Size last.**

---

## Where to go next

| Document | ID | Why |
|---|---|---|
| Student Guide | `THECC-DOC-FVGPRO-SG` | The full course — detection rules, the reading sequence, alerts, 50 FAQs |
| Cheat Sheet | `THECC-DOC-FVGPRO-CS` | One page beside your chart |
| Troubleshooting Manual | `THECC-DOC-FVGPRO-TS` | When something looks wrong on screen |

---

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| v2.1.0 | 2026-09-20 | Dale Batise | First Quick Start for Fair Value Gaps PRO v2.1. |

**Educational material only. Not financial advice, not a signal service, and not a claim about future results.**

---

*© THE CONSISTENCY COLLECTIVE — THECC Institutional Trader Academy™ · Consistency Creates Freedom. · Academy Documentation Standard v1.0.*
