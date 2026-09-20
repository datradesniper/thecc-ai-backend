<!-- ┌─────────────────────────────────────────────────────────────────────┐ -->
<!-- │ THECC INSTITUTIONAL TRADER ACADEMY™ — STANDARD DOCUMENT FRONT-MATTER │ -->
<!-- └─────────────────────────────────────────────────────────────────────┘ -->

# THECC Fair Value Gaps PRO — Feature Roadmap

### THECC Institutional Trader Academy™

> ⚠️ **Proposals, not commitments.** Nothing in this document is a promised release date or a claim that any item will ship. Items become real only when the owner schedules them.

#### 📘 Course Metadata

| Field | Value |
|---|---|
| **Academy** | THECC Institutional Trader Academy™ |
| **Course** | Fair Value Gaps PRO |
| **Module** | Operations |
| **Lesson** | Roadmap |
| **Difficulty** | Instructor / Engineering |
| **Estimated Time** | 10 minutes |
| **Prerequisites** | Developer Guide `THECC-DOC-FVGPRO-DG` |
| **Indicator Version** | v2.1 |
| **Document Version** | v2.1.0 |
| **Last Updated** | 2026-09-20 |
| **Instructor** | Dale Batise |
| **Status** | Content Complete — Certification Pending |

**Document control:**

| Field | Value |
|---|---|
| Document ID | THECC-DOC-FVGPRO-RM |
| Document type | Feature Roadmap |
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

## 0 · Before any new feature

These are not features and they outrank everything below.

| Item | Why it blocks |
|---|---|
| Registry ID assignment | Every document carries "pending" until it is resolved |
| `_SOURCE_OF_TRUTH.json` | The factory pipeline reads from it |
| TradingView compile green-check | No `Production Certified` stamp without it |
| Real screenshots and portal QR | The suite ships with placeholders today |
| DOCX renders | One of the seven required formats is still missing |

---

## 1 · Candidates, ranked by value per unit of risk

### 1.1 Zone proximity alert · *low risk*

Alert when price comes within a configurable distance of a live zone, rather than only when a zone forms. The most requested behaviour for a map tool, because a level that formed 200 bars ago is the one you want telling you it is close.
**Cost:** one loop over the live zones per bar, two inputs, one alert condition. **Risk:** alert frequency — must default off with a sensible distance unit.

### 1.2 Zone-touch and midpoint-touch events · *low risk*

Distinguish first touch, midpoint touch and full invalidation, each with its own alert. Teaches the midpoint concept that Chapter 3 already covers.
**Cost:** state per zone, three alert conditions. **Risk:** per-zone state grows; no new drawings.

### 1.3 Higher-timeframe market structure · *high risk*

Run MSS/BOS from a chosen timeframe instead of the chart.
**Cost:** `request.security` plus bar-index translation, because structure drawings currently anchor to chart bars.
**Risk:** the drawings are the hard part, not the detection. Prototype before promising.

### 1.4 Session-anchored liquidity levels · *medium risk*

Mark the prior session high and low explicitly, so sweeps reference a named level rather than a rolling lookback window.
**Cost:** session detection plus two lines and labels per session. **Risk:** drawing budget on long histories; needs a "sessions kept" cap.

### 1.5 Zone-age display · *low risk*

Optional bar count or age tag on each zone. Answers "how long has this been unfilled" without counting.
**Cost:** text only, no new objects. **Risk:** text clutter at small sizes.

### 1.6 Per-timeframe styling in Multi-Fix · *low risk*

Distinct colours per timeframe slot rather than by direction only, so overlap reads at a glance.
**Cost:** four colour pairs. **Risk:** doubles the Style section; consider a simple "colour by timeframe" toggle instead.

### 1.7 Compact mode for the zone text · *low risk*

Volume figure without the balance percentage, or tag only, for crowded charts.
**Cost:** one input. **Risk:** none material.

---

## 2 · Explicitly out of scope

| Item | Why |
|---|---|
| Buy / sell signals, or any direction call | This product is a map. Adding a trigger would break the role split with the execution products and the course's whole argument. |
| Probability or "strength" grades on zones | The balance percentage is already misread as quality. A score would make that worse and could not be honestly derived. |
| Position sizing or stop placement | Risk belongs in the trader's plan, not in a context tool. |
| Automatic settings tuning per symbol | Encourages exactly the behaviour the course prohibits. |
| More per-zone drawings | Capacity is 125 zones; each new drawing cuts it. |

---

## 3 · Documentation roadmap

| Item | State |
|---|---|
| Full video scripts from the lesson outline | Outline delivered; scripts outstanding |
| PowerPoint deck from the slide outline | Outline delivered; deck outstanding |
| Real chart screenshots and the overlap diagram | Outstanding |
| DOCX renders of all documents | Outstanding |
| PDF renders of all documents | Delivered — `make_pdf.py` |
| Translated editions | Not planned |

---

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| v2.1.0 | 2026-09-20 | Dale Batise | First Feature Roadmap for Fair Value Gaps PRO v2.1: blocking items, seven ranked candidates with cost and risk, explicit out-of-scope list, documentation roadmap. |

**Educational material only. Not financial advice, not a signal service, and not a claim about future results.**

---

*© THE CONSISTENCY COLLECTIVE — THECC Institutional Trader Academy™ · Consistency Creates Freedom. · Academy Documentation Standard v1.0.*
