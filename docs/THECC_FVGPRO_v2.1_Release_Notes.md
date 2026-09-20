<!-- ┌─────────────────────────────────────────────────────────────────────┐ -->
<!-- │ THECC INSTITUTIONAL TRADER ACADEMY™ — STANDARD DOCUMENT FRONT-MATTER │ -->
<!-- └─────────────────────────────────────────────────────────────────────┘ -->

# THECC Fair Value Gaps PRO — Release Notes v2.1

### THECC Institutional Trader Academy™

#### 📘 Course Metadata

| Field | Value |
|---|---|
| **Academy** | THECC Institutional Trader Academy™ |
| **Course** | Fair Value Gaps PRO |
| **Module** | Reference |
| **Lesson** | Release Notes |
| **Difficulty** | All |
| **Estimated Time** | 5 minutes |
| **Prerequisites** | None |
| **Indicator Version** | v2.1 |
| **Document Version** | v2.1.0 |
| **Last Updated** | 2026-09-20 |
| **Instructor** | Dale Batise |
| **Status** | Content Complete — Certification Pending |

**Document control:**

| Field | Value |
|---|---|
| Document ID | THECC-DOC-FVGPRO-RN |
| Document type | Release Notes |
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

## Summary

v2.1 adds liquidity sweeps and educational tooltips to the v2.0 release, which itself added market structure, equal highs and lows, an English settings menu and a fully configurable Zone Engine. **No change was made to fair value gap detection, volume profiling, Skull Mode or the multi-timeframe engine in either release.** An existing chart upgraded to v2.1 with untouched settings draws the same zones it drew before.

⚠️ **Compile status: not green-checked.** This build has not yet passed the TradingView compile verification, so the documentation set carries `Content Complete — Certification Pending` per Academy Documentation Standard v1.0 §2a.

---

## New in v2.1

### Liquidity sweeps

Marks a bar that runs a recent high or low and then closes back inside it, against the direction of the run — a failed breakout.

| Detail | Value |
|---|---|
| Buy-side | Price exceeds the highest high of the lookback window, excluding the current bar, then closes back **below** it on a down-closing bar |
| Sell-side | Mirror of the above, below the lowest low |
| Lookback | 5–200 bars, default 20 |
| Timeframe | Chart timeframe |
| Labels | Independent styling per side: text, size, style, text and background colour |
| Label cap | New setting, default 50 |
| Alerts | `Buy-side liquidity sweep`, `Sell-side liquidity sweep`, `Liquidity sweep (any)`, plus dynamic `alert()` messages. Both default **off**. |

💡 The label cap is new behavior worth knowing about: sweep labels are now tracked and the oldest removed past your limit, so they cannot silently consume the 500-label ceiling shared with the market-structure and equal-level labels.

### Educational tooltips

Every settings group now carries an in-panel explanation covering the mechanism, what the default does and the counter-case — the same style used elsewhere in the range. The tooltip on **Detection Sensitivity** states explicitly that the control is a *permissiveness* multiplier (`gap × sensitivity > ATR`), which is the most commonly misread setting in the product.

---

## New in v2.0

| Feature | Detail |
|---|---|
| Market structure | MSS (structure shift) and BOS (break of structure) on the chart timeframe, close-based, with duplicate-level suppression. Full per-direction styling of lines and labels, pivot length, max BOS lines, and an optional clear-on-shift switch. |
| Equal highs / lows | Confirmed-pivot shelves within a tolerance percentage, with extension, drawing cap and full styling. |
| Alerts | 9 named conditions plus dynamic `alert()` messages carrying direction, event, symbol, timeframe, broken level and close. Bar-close gating on by default; per-signal toggles; optional message prefix. |
| English settings menu | Every input title, tooltip and code comment. |
| Zone Engine | The values that were previously hardcoded are now settings: zones kept per timeframe, combine overlapping zones, overlap threshold, minimum zone duration, untouched-zone cleanup, max bars processed, ATR length — plus zone width, dynamic width, extend-latest count, combined-zone colour and tag, and volume-bar side and mirroring in Style. **Every default equals the old hardcoded value.** |

---

## Unchanged

The following are byte-for-byte identical to the pre-2.0 baseline:

- Three-bar gap detection, the middle-bar close confirmation and both quality filters
- The volume split, the balance percentage and the zone text
- Zone merging, extension, invalidation and cleanup logic
- Skull Mode
- Auto / Fix / Multi-Fix timeframe resolution and the five detection slots
- The original `New FVG` alert conditions

---

## Upgrade steps

1. Copy the v2.1 `.pine` source over your existing script in the Pine Editor and **Save**.
2. Re-add to chart if you keep separate saved instances.
3. Open settings and confirm your zone, style and timeframe choices survived. They should: no existing input was renamed or removed.
4. **If you run Multi-Fix**, set *Zones kept per timeframe* per the table below before judging the display.
5. Re-check your alerts. Existing `New FVG` alerts continue to work. New structure, equal-level and sweep alerts must be created, and their per-signal toggles switched on.

| Active detection timeframes | Zones kept per timeframe |
|---|---|
| 1 | 100–125 |
| 2 | 55 |
| 3 | 35 |
| 4 | 30 |
| 5 | 25 |

---

## Known limitations

| Limitation | Detail |
|---|---|
| Structure is chart-timeframe only | MSS, BOS, equal levels and sweeps do not follow Fix or Multi-Fix. Their drawings anchor to chart bars. |
| Drawing budget | TradingView allows 500 boxes, 500 lines and 500 labels. One zone costs 4 boxes and 2 lines, so about 125 zones total. Past that, the platform discards the oldest objects silently. |
| BOS alerts depend on a display toggle | BOS detection is gated by **Show BOS**; with it off, no BOS alert can fire. |
| Sweep labels are live-bar | A sweep label can appear and vanish before the bar closes. Alerts are bar-close gated by default for this reason. |
| Equal levels are confirmed late | By design — `Swing length` bars after the second pivot. The alternative repaints. |
| Two drawing-limit values cannot be settings | The indicator declaration requires compile-time constants. |
| Screenshots in the documentation | Still placeholders. Real captures are outstanding across the product range. |

---

## Documentation

| Document | ID | State |
|---|---|---|
| Student Guide | `THECC-DOC-FVGPRO-SG` | Delivered |
| Cheat Sheet | `THECC-DOC-FVGPRO-CS` | Delivered |
| Quick Start | `THECC-DOC-FVGPRO-QS` | Delivered |
| Instructor Guide | `THECC-DOC-FVGPRO-IG` | Delivered |
| Answer Key | `THECC-DOC-FVGPRO-AK` | Delivered |
| Release Notes | `THECC-DOC-FVGPRO-RN` | This document |
| Remaining suite | — | See `_DOCUMENTATION_INDEX_FVGPRO_v2.1.md` |

---

## Outstanding before publication

1. Registry ID assignment — this product has none; the registry raises the question under **THECC-0008**.
2. `_SOURCE_OF_TRUTH.json` creation, per Academy Documentation Standard §2.
3. TradingView compile green-check, then owner sign-off before any `Production Certified` stamp.
4. Real screenshots and portal QR URLs.

---

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| v2.1.0 | 2026-09-20 | Dale Batise | Release notes for v2.1 (liquidity sweeps, educational tooltips) and v2.0 (market structure, equal highs and lows, English menu, Zone Engine settings). |

**Educational material only. Not financial advice, not a signal service, and not a claim about future results.**

---

*© THE CONSISTENCY COLLECTIVE — THECC Institutional Trader Academy™ · Consistency Creates Freedom. · Academy Documentation Standard v1.0.*
