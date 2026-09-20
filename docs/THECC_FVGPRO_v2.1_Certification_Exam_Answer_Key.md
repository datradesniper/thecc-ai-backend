<!-- ┌─────────────────────────────────────────────────────────────────────┐ -->
<!-- │ THECC INSTITUTIONAL TRADER ACADEMY™ — STANDARD DOCUMENT FRONT-MATTER │ -->
<!-- └─────────────────────────────────────────────────────────────────────┘ -->

# THECC Fair Value Gaps PRO — Certification Exam Answer Key

### THECC Institutional Trader Academy™

> ⚠️ **Instructor copy. Do not distribute to students.**

#### 📘 Course Metadata

| Field | Value |
|---|---|
| **Academy** | THECC Institutional Trader Academy™ |
| **Course** | Fair Value Gaps PRO |
| **Module** | Assessment |
| **Lesson** | Exam marking |
| **Difficulty** | Instructor |
| **Estimated Time** | 15 minutes marking |
| **Prerequisites** | Certification Exam `THECC-DOC-FVGPRO-EX` |
| **Indicator Version** | v2.1 |
| **Document Version** | v2.1.0 |
| **Last Updated** | 2026-09-20 |
| **Instructor** | Dale Batise |
| **Status** | Content Complete — Certification Pending |

**Document control:**

| Field | Value |
|---|---|
| Document ID | THECC-DOC-FVGPRO-EX-AK |
| Document type | Certification Exam Answer Key |
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

## Marking summary

**Pass: 32 / 40 (80%) AND all three gating questions correct — B7, C1, C2.**

| Section | Marks |
|---|---|
| A · Multiple choice | 20 |
| B · Short answer | 12 |
| C · Applied | 8 |

---

## Section A — answer row

| Q | A1 | A2 | A3 | A4 | A5 | A6 | A7 | A8 | A9 | A10 |
|---|---|---|---|---|---|---|---|---|---|---|
| **Ans** | b | b | b | c | b | b | b | b | c | a |

| Q | A11 | A12 | A13 | A14 | A15 | A16 | A17 | A18 | A19 | A20 |
|---|---|---|---|---|---|---|---|---|---|---|
| **Ans** | b | b | c | a | c | c | a | b | b | c |

**Notes on common wrong answers**

- **A2/A3** — a student choosing "strictest" for Extreme has the sensitivity model inverted. Re-teach with the zone count demonstration before sign-off.
- **A4** — option a or d indicates the percentage is being read as a prediction or as buy/sell pressure. Correct immediately; it is the most consequential misreading in the course.
- **A10** — the answer is *higher prices*. A student answering b) has the sweep logic backwards and will trade it the wrong way.
- **A14** — 125 across all timeframes, not per timeframe. A student answering 500 has confused zones with boxes.

---

## Section B — model answers (1 mark each)

**B1.** Bar 2 must close **below bar 1's low**.

**B2.** Because it tests displacement using price and ATR rather than volume, so it remains valid where the volume feed is absent or unreliable.

**B3.** The volume was concentrated on one side — roughly a 35:65 split between the zone's halves. It describes construction, not strength or likelihood.

**B4.** The candle has closed and the result is locked.

**B5.** Changes intrabar: a liquidity sweep label. Does not: zones, MSS, BOS or equal levels. *(Either direction stated correctly earns the mark.)*

**B6.** Duplicate-level suppression — a repeat break of an already-marked level does not draw a second line.

**B7. [G]** Because the pivot would not yet be confirmed, so the level could change or vanish as later bars print — it would repaint. A level that arrives late but stays put can be planned around; one that arrives early and moves cannot.

**B8.** At true M15 width — the zone-width setting counts bars of the zone's own timeframe, so 15 M15 bars by default, not 15 M1 bars.

**B9.** Per-signal toggle off; Show BOS off for BOS alerts; the alert attached to a different or unsaved instance.

**B10.** Old zones missing, or zones drawn incompletely — a box with no volume bars or no text — because some of the four boxes per zone were discarded.

**B11.** Price trades through a recent high or low and then closes back inside it, against the direction of the run — a failed breakout. *(Any answer using "reversal" scores zero, per the question.)*

**B12.** Many gaps are never filled; a zone records what happened, and carries no commitment that price returns.

---

## Section C — model answers (2 marks each)

**C1. [G]** Map → liquidity → sweep → shift (MSS) → the zone the shift left → invalidation → size.
The indicator performs **steps 1 to 5** — it marks zones, equal levels, sweeps and structure. **Steps 6 and 7, invalidation and size, are the trader's** and the indicator has no opinion on them.
*1 mark for the seven steps in order; 1 mark for correctly splitting 1–5 from 6–7. Both required for the gate.*

**C2. [G]** The sweep was a pause inside an ongoing move, not a turn: the absence of an MSS means structure never confirmed the rejection, and continued bullish BOS lines say the established direction is intact. What would change it: a close beyond the most recent opposing swing — a bearish MSS — ideally with a fresh zone left by that displacement.
*1 mark for reading the sweep as a pause because no shift followed; 1 mark for naming the MSS close as the condition that would change it. Reject any answer that treats the sweep alone as a short trigger.*

**C3.** Full marks require the decision to be made in this order: define invalidation first — a body close back above the fresh zone, or above the sweep high — then measure that distance. If invalidation sits beyond the 15-point limit, there is no trade regardless of how good the sequence looks; the 40-point zone is context for a target or a higher-timeframe idea, not a reason to widen risk. Award 1 mark for invalidation-before-size, 1 mark for concluding that the risk limit, not the setup, decides whether the trade exists.
*Deduct both marks if the student proposes widening the limit or "sizing down to fit" without addressing where invalidation actually sits.*

**C4.** Diagnosis: the drawing budget. Arithmetic: each rendered zone costs 4 boxes and 2 lines against a 500-box ceiling, so about 125 zones in total across all active timeframes — four timeframes at 125 each asks for roughly 2000 boxes and TradingView discards the oldest silently. Fix: lower Zones kept per timeframe to about 30 with four timeframes active, or run fewer timeframes.
*1 mark for the diagnosis with the arithmetic, 1 mark for the corrective setting.*

---

## Sign-off

| Requirement | Met? |
|---|---|
| 32 / 40 or better | |
| B7 correct | |
| C1 correct | |
| C2 correct | |
| Drill 11 worksheet seen, invalidation recorded before outcome | |

⚠️ Certification for this product remains **pending** at the Academy level until the v2.1 build passes the TradingView compile green-check and the owner signs off. Do not issue certificates describing the course as certified before that.

---

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| v2.1.0 | 2026-09-20 | Dale Batise | First Certification Exam Answer Key for Fair Value Gaps PRO v2.1: answer row, model answers, marking notes and sign-off checklist. |

**Educational material only. Not financial advice, not a signal service, and not a claim about future results.**

---

*© THE CONSISTENCY COLLECTIVE — THECC Institutional Trader Academy™ · Consistency Creates Freedom. · Academy Documentation Standard v1.0.*
