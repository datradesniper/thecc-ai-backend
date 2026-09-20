<!-- ┌─────────────────────────────────────────────────────────────────────┐ -->
<!-- │ THECC INSTITUTIONAL TRADER ACADEMY™ — STANDARD DOCUMENT FRONT-MATTER │ -->
<!-- └─────────────────────────────────────────────────────────────────────┘ -->

# THECC Fair Value Gaps PRO — Instructor Guide

### THECC Institutional Trader Academy™

#### 📘 Course Metadata

| Field | Value |
|---|---|
| **Academy** | THECC Institutional Trader Academy™ |
| **Course** | Fair Value Gaps PRO |
| **Module** | 1–4 (Core Curriculum) |
| **Lesson** | All |
| **Difficulty** | Instructor |
| **Estimated Time** | 90 minutes delivery · 30 minutes preparation |
| **Prerequisites** | Student Guide `THECC-DOC-FVGPRO-SG` read in full |
| **Indicator Version** | v2.1 |
| **Document Version** | v2.1.0 |
| **Last Updated** | 2026-09-20 |
| **Instructor** | Dale Batise |
| **Status** | Content Complete — Certification Pending |

**Document control:**

| Field | Value |
|---|---|
| Document ID | THECC-DOC-FVGPRO-IG |
| Document type | Instructor Guide |
| Indicator | THECC Fair Value Gaps PRO · **Registry ID pending** |
| Version | v2.1.0 |
| Build | 2.1.0+2026-09-20 |
| Release date | 2026-09-20 |
| Compatible indicator versions | FVG PRO v2.1.x |
| Academy Doc Standard | v1.0 |
| Edition | Internal Master · Status: Beta |
| Platform | TradingView · Pine Script v6 |
| Copyright | © THE CONSISTENCY COLLECTIVE |

[ QR CODE PLACEHOLDER — links to the current version of this guide in the Member Portal ]

**Consistency Creates Freedom.**

---

## 1 · What this session must achieve

Students leave able to read the map and state an invalidation before an entry. Nothing else counts as success. A student who can recite the detection rules but still says "there is a gap, so I am long" has not passed the session.

The three ideas that carry the whole course:

1. A zone is **evidence**, not an instruction.
2. Everything requires a **close**.
3. A sweep without a structure shift is **one wick with a label on it**.

⚠️ Do not let the session drift into predicting. If a student asks "so where does it go from here", return the question: "what would tell you the idea is wrong, and how far away is that?"

---

## 2 · Preparation checklist (30 minutes)

| Item | Detail |
|---|---|
| Chart A | NQ or ES, M5, defaults, regular hours, at least one completed sweep → MSS → zone sequence in view |
| Chart B | Same symbol, M1, detection **Fix** on M15 — for the Fix demonstration |
| Chart C | Multi-Fix M5/M15/H1 with **Zones kept = 125** so the drawing-budget fault is visible, plus the same layout fixed at 30 |
| Chart D | A failed sequence: sweep with no shift, price continuing |
| Alert | One `MSS (any)` alert, and one on "Any alert() function call" with prefix `THECC`, ready to show a live message |
| Handouts | Cheat Sheet `-CS`, Quick Start `-QS` |
| Screenshots | The `📸` placeholders in the Student Guide are not yet real captures. Take your own before teaching. |

---

## 3 · Session plan (90 minutes)

| Time | Segment | Method | Watch for |
|---|---|---|---|
| 0–8 | Map vs signal | Chart A, indicator off then on | Students expecting entry arrows. Name the absence early. |
| 8–15 | Install and defaults | Live demo | Anyone on Heikin Ashi or an unsaved script |
| 15–33 | Anatomy of a zone | Chart A zoomed in; switch sensitivity Extreme → Low live | The percentage being read as "quality". Correct it immediately. |
| 33–45 | Timeframe modes | Chart B, then Chart C both ways | The moment levels stop moving in Fix — pause on it |
| 45–50 | 📝 Exercise (Chapter 4) | Students count zones in three modes | Students with no zones at all — check filter and blank slots |
| 50–70 | Structure, liquidity, sequence | Chart A then Chart D | "Buy-side sweep" being read as "buy". Ask them to say it back. |
| 70–80 | Alerts | Live alert dialog | Alerts created against an unsaved or duplicate instance |
| 80–88 | Discipline and the settings panel | Discussion | Tuning under pressure — make the rule explicit |
| 88–90 | Close and quiz brief | — | Remind them the pass mark is 80% |

💡 If you are short of time, cut the alerts segment to five minutes and keep the full twenty on structure and the sequence. Alerts can be self-taught from Chapter 6; judgement cannot.

---

## 4 · Teaching notes, chapter by chapter

**Chapter 1 — Welcome.** Establish the map/execution split in the first two minutes. Ask each student which tool in their setup currently owns the entry decision. Most cannot answer, and that is the lesson.

**Chapter 2 — Installation.** Do it live, slowly, including **Save**. Roughly a third of alert problems in support come from unsaved or duplicated instances.

**Chapter 3 — Walkthrough.** Teach the middle-bar close rule with your cursor on the actual candle. Then run the sensitivity demonstration: set **Low**, count what remains, set **Extreme**, count again. State the formula out loud — `gap × sensitivity > ATR` — and let them hear that a *higher* setting is *more* permissive. This is the single most misread control in the product.

**Chapter 4 — Timeframe modes.** The Fix demonstration is the highest-value ninety seconds of the session. Switch chart timeframes twice in Auto and let them watch the levels move; switch to Fix and do it again.

**Chapter 5 — Reading the map.** Walk the seven steps on Chart A, then walk the *same* seven steps on Chart D where step 4 never arrives. Students learn the sequence from the failure faster than from the success.

**Chapter 6 — Alerts.** Show a real message. Point at the level field and explain that it is the swing that broke, not the entry.

**Chapter 7 — Customization.** State plainly: nothing is locked in this build, so the discipline is theirs. Give the rule — one change at a time, dated, with a reason — and the prohibition — never during a position.

**Chapters 8–12.** Assign as reading. Pull three mistakes from Chapter 9 that you have seen in that cohort's journals and discuss those only.

---

## 5 · Discussion prompts

1. A zone has sat unfilled for three weeks. What, if anything, does that tell you?
2. Two zones overlap on different timeframes. Why might that matter more than either alone?
3. Price sweeps the session high, closes back inside, and structure does not shift. What is your read, and what would change it?
4. Your invalidation is 40 points away and your risk limit allows 15. What is the trade?
5. A student raises sensitivity mid-session and a level appears where they wanted one. What has happened?
6. Why would an honest tool deliberately show a level several bars late?

---

## 6 · Errors students make, and the correction

| Error | Correction |
|---|---|
| "Extreme sensitivity is the strictest" | Say the formula. Demonstrate the zone count both ways. |
| "Buy-side sweep means buy" | Have them restate it as "the buy stops above were taken and price could not hold". |
| "The percentage is a strength score" | It is balance. Show a 90% and a 30% zone and ask what differed in how they were built. |
| "EQH is late, so it is broken" | Show what an immediate version would do — repaint. Then ask which they would rather plan around. |
| "MSS means reverse" | Show Chart D. Continuation is the base case. |
| "The indicator is deleting my zones" | Drawing budget. Do the arithmetic on the board: 500 ÷ 4. |
| "No zones appear" | Filter, sensitivity, or a blank Multi-Fix slot. In that order. |

---

## 7 · Assessment

| Instrument | Where | Pass mark |
|---|---|---|
| Chapter Review Questions | Student Guide, each chapter | Formative — discuss, do not score |
| 📝 Exercises 1–8 | Student Guide | Completion, journal evidence |
| Certification Quiz (20 questions) | Student Guide Appendix A | **80% — 16 of 20** |

Marking guidance is in the Answer Key, `THECC-DOC-FVGPRO-AK`. Questions 16, 17 and 20 are the ones that matter most: the sequence, why size comes last, and what the indicator never decides. A student who misses those three has not met the objective even if they clear 16 marks elsewhere — re-teach Chapter 5 before signing them off.

⚠️ Certification status for this product is **Content Complete — Certification Pending** until the v2.1 build passes the TradingView compile green-check and the owner signs off. Do not describe the course as certified in any cohort communication before then.

---

## 8 · Cross references

| Document | ID |
|---|---|
| Student Guide | `THECC-DOC-FVGPRO-SG` |
| Quick Start | `THECC-DOC-FVGPRO-QS` |
| Cheat Sheet | `THECC-DOC-FVGPRO-CS` |
| Answer Key | `THECC-DOC-FVGPRO-AK` |
| Troubleshooting Manual | `THECC-DOC-FVGPRO-TS` |
| Practical Exercises | `THECC-DOC-FVGPRO-PE` |
| Academy Documentation Standard | `_ACADEMY_DOC_STANDARD_v1.0.md` |

---

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| v2.1.0 | 2026-09-20 | Dale Batise | First Instructor Guide for Fair Value Gaps PRO v2.1: session plan, chapter notes, discussion prompts, student-error table and assessment guidance. |

**Educational material only. Not financial advice, not a signal service, and not a claim about future results.**

---

*© THE CONSISTENCY COLLECTIVE — THECC Institutional Trader Academy™ · Consistency Creates Freedom. · Academy Documentation Standard v1.0.*
