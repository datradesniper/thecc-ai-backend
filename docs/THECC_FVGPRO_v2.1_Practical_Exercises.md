<!-- ┌─────────────────────────────────────────────────────────────────────┐ -->
<!-- │ THECC INSTITUTIONAL TRADER ACADEMY™ — STANDARD DOCUMENT FRONT-MATTER │ -->
<!-- └─────────────────────────────────────────────────────────────────────┘ -->

# THECC Fair Value Gaps PRO — Practical Exercises

### THECC Institutional Trader Academy™

#### 📘 Course Metadata

| Field | Value |
|---|---|
| **Academy** | THECC Institutional Trader Academy™ |
| **Course** | Fair Value Gaps PRO |
| **Module** | 2–4 |
| **Lesson** | Practical Exercises |
| **Difficulty** | Beginner → Intermediate |
| **Estimated Time** | 12 drills, 10–25 minutes each |
| **Prerequisites** | Student Guide Chapters 1–6 |
| **Indicator Version** | v2.1 |
| **Document Version** | v2.1.0 |
| **Last Updated** | 2026-09-20 |
| **Instructor** | Dale Batise |
| **Status** | Content Complete — Certification Pending |

**Document control:**

| Field | Value |
|---|---|
| Document ID | THECC-DOC-FVGPRO-PE |
| Document type | Practical Exercises |
| Indicator | THECC Fair Value Gaps PRO · **Registry ID pending** |
| Version | v2.1.0 |
| Build | 2.1.0+2026-09-20 |
| Release date | 2026-09-20 |
| Compatible indicator versions | FVG PRO v2.1.x |
| Academy Doc Standard | v1.0 |
| Edition | Student / Pro |
| Platform | TradingView · Pine Script v6 |
| Copyright | © THE CONSISTENCY COLLECTIVE |

**Consistency Creates Freedom.**

---

## How these drills work

Each drill has an objective, a method, and a **success criterion you can verify yourself**. Use TradingView's Bar Replay for anything that involves waiting.

⚠️ **No drill in this document requires a live position.** Every one can be completed on replay or on historical charts. If you catch yourself wanting to "test it with a small trade", you have swapped a learning task for a gambling one.

---

## Drill 1 — Prove the middle-bar rule (10 min)

**Objective:** see the rule reject something.
**Method:** find three consecutive bars that leave a visible gap but carry **no** zone. Inspect bar 2's close against bar 1's high or low.
**Success:** you can name which specific condition failed — the close, the size test, or the ATR jump check.

## Drill 2 — The sensitivity count (15 min)

**Objective:** internalise that sensitivity is permissiveness.
**Method:** on one fixed chart, count visible zones at Low, Normal, High and Extreme.
**Success:** your four counts increase monotonically, and you can state the formula `gap × sensitivity > ATR` from memory.

## Drill 3 — Balance reading (10 min)

**Objective:** stop reading the percentage as quality.
**Method:** find one zone above 80% and one below 40%. Write what each says about the construction of the level.
**Success:** neither sentence contains a prediction.

## Drill 4 — Invalidation methods, side by side (15 min)

**Objective:** connect the setting to your stop placement.
**Method:** find a zone that a wick pierced but no body closed through. Switch Zone Invalidation from Close to Wick and watch the zone retire.
**Success:** you can state where your stop belongs under each setting, and which you will use.

## Drill 5 — The Fix demonstration (10 min)

**Objective:** feel the difference between moving levels and stable ones.
**Method:** in Auto, change chart timeframe three times and watch the zones change. Set Fix to your bias timeframe and repeat.
**Success:** you can explain in one sentence why stable levels are a planning requirement, not a preference.

## Drill 6 — Overlap hunt (20 min)

**Objective:** find agreement between timeframes.
**Method:** Multi-Fix M5 / M15 / H1, zones kept at 35. Identify three prices where two or more timeframes overlap. Note what price did on arrival.
**Success:** three documented overlaps with outcomes, and no claim that overlap guarantees anything.

## Drill 7 — Reproduce the drawing-budget fault (15 min)

**Objective:** recognise the fault on sight, forever.
**Method:** four Multi-Fix timeframes with zones kept at 125. Scroll back and find zones drawn without volume bars or text. Then set zones kept to 30 and reload.
**Success:** you can describe the signature of the fault and the arithmetic behind it — 4 boxes per zone, 500 boxes total.

## Drill 8 — Structure classification (20 min)

**Objective:** separate continuation from a shift.
**Method:** find five structure events. Before reading the label, decide whether each is MSS or BOS from the swing it broke. Then check.
**Success:** four of five correct, and the misses explained.

## Drill 9 — Wick versus close (10 min)

**Objective:** trust the close requirement.
**Method:** find a swing high pierced by a wick with no structure line, and one broken by a close with a line.
**Success:** screenshots of both, captioned with why one counted.

## Drill 10 — Sweep survey (25 min)

**Objective:** measure how often a sweep alone means anything.
**Method:** log ten sweeps on replay. For each, record whether an MSS followed within ten bars, and what price did over twenty.
**Success:** a ratio in your journal, and a sentence on what it implies for trading sweeps alone.

## Drill 11 — Full sequence on replay (25 min)

**Objective:** run the seven steps without hindsight.
**Method:** Bar Replay. Pause at the sweep. Write your invalidation **before** advancing. Advance bar by bar through the shift and the retrace.
**Success:** a completed sequence worksheet where the invalidation was written before the outcome was known.

## Drill 12 — Alert verification (15 min)

**Objective:** confirm your alerting actually works before you rely on it.
**Method:** create `MSS (any)` and one "Any alert() function call" alert with prefix `THECC`. Wait for a structure event on a fast timeframe.
**Success:** both messages received and archived; you can identify the level field in the dynamic message.

---

## Drill record

| Drill | Date | Result | What surprised me |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |
| 6 | | | |
| 7 | | | |
| 8 | | | |
| 9 | | | |
| 10 | | | |
| 11 | | | |
| 12 | | | |

---

## Instructor notes

- Drills 2, 7 and 10 produce the biggest behavioural change per minute spent. If you can only run three in a session, run those.
- Drill 11 is the assessment-grade exercise. Ask to see the worksheet where invalidation was written before the outcome; a student who cannot produce one has not met the course objective.
- Drill 10's ratio varies by symbol and session. Do not publish a target figure — the point is that each student measures their own market.

---

## Cross references

| Document | ID |
|---|---|
| Student Guide | `THECC-DOC-FVGPRO-SG` |
| Student Workbook | `THECC-DOC-FVGPRO-WB` |
| Live Trading Lab Manual | `THECC-DOC-FVGPRO-LM` |
| Instructor Guide | `THECC-DOC-FVGPRO-IG` |

---

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| v2.1.0 | 2026-09-20 | Dale Batise | First Practical Exercises for Fair Value Gaps PRO v2.1: 12 verifiable drills with success criteria, drill record and instructor notes. |

**Educational material only. Not financial advice, not a signal service, and not a claim about future results.**

---

*© THE CONSISTENCY COLLECTIVE — THECC Institutional Trader Academy™ · Consistency Creates Freedom. · Academy Documentation Standard v1.0.*
