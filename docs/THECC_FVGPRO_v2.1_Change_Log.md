<!-- ┌─────────────────────────────────────────────────────────────────────┐ -->
<!-- │ THECC INSTITUTIONAL TRADER ACADEMY™ — STANDARD DOCUMENT FRONT-MATTER │ -->
<!-- └─────────────────────────────────────────────────────────────────────┘ -->

# THECC Fair Value Gaps PRO — Change Log

### THECC Institutional Trader Academy™

#### 📘 Course Metadata

| Field | Value |
|---|---|
| **Academy** | THECC Institutional Trader Academy™ |
| **Course** | Fair Value Gaps PRO |
| **Module** | Reference |
| **Lesson** | Change Log |
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
| Document ID | THECC-DOC-FVGPRO-CL |
| Document type | Change Log |
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

## Versioning policy

Per-product SemVer. Each version is preserved as its own file and never overwritten. Documentation versions track the indicator version they describe (`v2.1` indicator → `v2.1.0` documents).

⚠️ **Baseline note.** The pre-2.0 build carried no version tag in its source header — it is recorded below as *baseline (untagged)* rather than given a retrospective number. Assign one only if the owner decides to.

---

## v2.1.0 — 2026-09-20

**Added**

- Liquidity sweep detection on the chart timeframe. Buy-side: price exceeds the highest high of the lookback window, excluding the current bar, then closes back below it on a down-closing bar. Sell-side mirrors it below the lowest low.
- `⊹ Liquidity Sweeps` settings group: show toggle, lookback (5–200, default 20), and a new **Max sweep labels to keep** (default 50).
- `⊹ Buy-side Sweep (above) label` and `⊹ Sell-side Sweep (below) label` groups: label text, size, style, text colour and background per side.
- Alert conditions `Buy-side liquidity sweep`, `Sell-side liquidity sweep`, `Liquidity sweep (any)`, plus dynamic `alert()` messages. Both per-signal toggles default **off**.
- Educational tooltips on every settings group: timeframe modes, zone invalidation, zone filtering, FVG detection, detection sensitivity, allow-gaps, historic zones, colours, zone start, and all new sweep controls.

**Changed**

- Sweep labels are held in a tracked array and capped, rather than accumulating for the life of the chart. This prevents them from consuming the 500-label ceiling shared with market-structure and equal-level labels, where TradingView would otherwise discard the oldest labels silently.

**Unchanged**

- Fair value gap detection, volume profiling, zone merging, invalidation, Skull Mode, and the Auto / Fix / Multi-Fix engine.

---

## v2.0.0 — 2026-09-20

**Added**

- Market structure on the chart timeframe: MSS (close beyond the most recent opposing swing) and BOS (close beyond the most recent swing in the established direction), built on a pivot zig-zag with duplicate-level suppression.
- `⊹ Market Structure (MSS / BOS)` group: show, pivot length (3–20, default 5), MSS on/off, BOS on/off, max BOS lines (default 50), and **Clear previous structure lines on each new MSS** (default off).
- Four styling groups — MSS Bullish, MSS Bearish, BOS Bullish, BOS Bearish — each with line colour, width and style plus label show, text, size, style, text colour and background.
- Equal highs and equal lows: confirmed-pivot shelves within a tolerance percentage, drawn at the average of the two pivots, with right-side extension and a drawing cap. Separate `⊹ Equal Highs` and `⊹ Equal Lows` styling groups.
- Alerts: `MSS Bullish`, `MSS Bearish`, `BOS Bullish`, `BOS Bearish`, `MSS (any)`, `BOS (any)`, `MSS or BOS (any)`, `Equal Highs (EQH)`, `Equal Lows (EQL)`, plus dynamic `alert()` messages carrying direction, event, symbol, timeframe, broken level and close. New `⊹ Alerts` group with a bar-close gating switch (default on), per-signal toggles and an optional message prefix.
- `⊹ Zone Engine` group exposing values that were previously constants: zones kept per timeframe (125), combine overlapping zones (on), overlap threshold % (0), minimum zone duration in milliseconds (3), delete untouched zones (on) and its bar count (200), max bars back to process (10000), ATR length (10).
- Style additions, also previously hardcoded: extend zones by bars (15), dynamic width (on), extend latest zones to current bar (on) and count (3), recolour combined zones (off) and that colour, tag combined zones in text (on), volume bars on left side (on), mirror volume bars (on).

**Changed**

- Settings menu and code comments translated to English throughout.
- `indicator()` declaration documents its drawing limits; `maxBoxesCount` and the debug flag remain constants because TradingView requires compile-time constants for drawing-limit arguments.

**Unchanged**

- Every default equals the previously hardcoded value, so an upgraded chart with untouched settings renders identically.
- `detectFVG`, `processSlot`, `renderSlot`, `combineFVGsFunc`, the `FVG` type, the volume-bar geometry, Skull Mode and the five `request.security` slots.

---

## Baseline (untagged) — pre-2026-09-20

The build this line descends from provided:

- Three-bar fair value gap detection with middle-bar close confirmation
- Average Range and Volume Threshold quality filters with a four-step sensitivity control
- Volume profiling inside each zone with a balance percentage
- Zone merging, dynamic width, extension of the latest zones, invalidation by wick or body close, and untouched-zone cleanup
- Auto / Fix / Multi-Fix timeframe modes with per-zone timeframe tags, up to four fixed timeframes plus the chart timeframe
- Skull Mode
- `New FVG` alert conditions per timeframe slot

---

## Documentation changes

| Date | Change |
|---|---|
| 2026-09-20 | Documentation set rebuilt to Academy Documentation Standard v1.0. Student Guide, Cheat Sheet, Quick Start, Instructor Guide, Answer Key, Release Notes and this Change Log authored. Metadata JSON, slide outline and video lesson outline produced. Earlier informal guide and quick reference superseded and removed. |

---

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| v2.1.0 | 2026-09-20 | Dale Batise | First Change Log for Fair Value Gaps PRO: v2.1, v2.0 and the untagged baseline. |

**Educational material only. Not financial advice, not a signal service, and not a claim about future results.**

---

*© THE CONSISTENCY COLLECTIVE — THECC Institutional Trader Academy™ · Consistency Creates Freedom. · Academy Documentation Standard v1.0.*
