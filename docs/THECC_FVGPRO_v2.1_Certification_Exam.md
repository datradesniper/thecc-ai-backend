<!-- ┌─────────────────────────────────────────────────────────────────────┐ -->
<!-- │ THECC INSTITUTIONAL TRADER ACADEMY™ — STANDARD DOCUMENT FRONT-MATTER │ -->
<!-- └─────────────────────────────────────────────────────────────────────┘ -->

# THECC Fair Value Gaps PRO — Certification Exam

### THECC Institutional Trader Academy™

#### 📘 Course Metadata

| Field | Value |
|---|---|
| **Academy** | THECC Institutional Trader Academy™ |
| **Course** | Fair Value Gaps PRO |
| **Module** | Assessment |
| **Lesson** | Certification Exam |
| **Difficulty** | Intermediate |
| **Estimated Time** | 45 minutes |
| **Prerequisites** | Student Guide, Workbook, Practical Exercises |
| **Indicator Version** | v2.1 |
| **Document Version** | v2.1.0 |
| **Last Updated** | 2026-09-20 |
| **Instructor** | Dale Batise |
| **Status** | Content Complete — Certification Pending |

**Document control:**

| Field | Value |
|---|---|
| Document ID | THECC-DOC-FVGPRO-EX |
| Document type | Certification Exam (Student copy) |
| Indicator | THECC Fair Value Gaps PRO · **Registry ID pending** |
| Version | v2.1.0 |
| Build | 2.1.0+2026-09-20 |
| Release date | 2026-09-20 |
| Compatible indicator versions | FVG PRO v2.1.x |
| Academy Doc Standard | v1.0 |
| Edition | Student |
| Platform | TradingView · Pine Script v6 |
| Copyright | © THE CONSISTENCY COLLECTIVE |

**Consistency Creates Freedom.**

---

## Instructions

- **40 marks. Pass mark 80% — 32 marks.** 45 minutes. Closed book.
- Section A: 20 multiple choice, one mark each. Section B: 12 short answer, one mark each. Section C: 4 applied questions, two marks each.
- Questions marked **[G]** are gating: you must answer these correctly to pass, regardless of total.
- Answers and marking guidance are held in `THECC-DOC-FVGPRO-EX-AK` (instructor copy).

Candidate name: ______________________  Date: ____________  Score: ____ / 40

---

## Section A — Multiple choice (20 marks)

**A1.** A bullish zone requires the middle bar to close:
a) above its own open · b) above bar 1's high · c) below bar 3's low · d) anywhere inside the gap

**A2.** Detection Sensitivity at Extreme means:
a) the strictest filter · b) the most permissive filter · c) volume filtering only · d) no filtering at all

**A3.** The size test applied to the gap is:
a) gap ÷ sensitivity > ATR · b) gap × sensitivity > ATR · c) gap > ATR × 2 always · d) gap > the three-bar body sum

**A4.** `12.4K (68%)` tells you:
a) a 68% chance of a fill · b) the zone is 68% consumed · c) the volume split between the zone's halves was fairly even · d) 68% of volume was buying

**A5.** `[Combined]` means:
a) two timeframes agree · b) overlapping same-direction zones merged · c) the zone was invalidated twice · d) volume and range filters both passed

**A6.** With Zone Invalidation on Close, a zone retires when:
a) any wick pierces it · b) a body closes fully through it · c) three bars trade inside it · d) the session ends

**A7.** MSS is:
a) a close beyond the most recent swing in the same direction · b) a close beyond the most recent opposing swing · c) any wick through a swing · d) two equal highs

**A8.** BOS indicates:
a) reversal · b) continuation · c) a liquidity sweep · d) an invalidated zone

**A9.** Equal highs are confirmed:
a) immediately · b) on the next bar · c) `Swing length` bars after the second pivot · d) only at session close

**A10.** A buy-side sweep is evidence against:
a) higher prices · b) lower prices · c) the volume filter · d) the current structure direction

**A11.** The sweep lookback window:
a) includes the current bar · b) excludes the current bar · c) is fixed at 20 · d) follows Multi-Fix

**A12.** Which elements follow Fix and Multi-Fix?
a) everything · b) zones only · c) structure only · d) sweeps only

**A13.** One rendered zone consumes:
a) 1 box · b) 2 boxes and 1 line · c) 4 boxes and 2 lines · d) 6 boxes

**A14.** The approximate total zone capacity across all timeframes is:
a) 125 · b) 250 · c) 500 · d) unlimited

**A15.** With four Multi-Fix timeframes active, Zones kept per timeframe should be about:
a) 125 · b) 60 · c) 30 · d) 10

**A16.** "Fire on bar close only" switched off means:
a) alerts never fire · b) alerts fire once per session · c) alerts can fire on breaks that later fail · d) alerts become more reliable

**A17.** A BOS alert will not fire if:
a) Show BOS is off · b) Show MSS is off · c) the chart is on M1 · d) Skull Mode is on

**A18.** Skull Mode:
a) hides structure · b) reduces each zone to its midpoint and faint volume bars · c) deletes invalidated zones · d) doubles the drawing budget

**A19.** Zones are created:
a) on every tick · b) on confirmed bars only · c) only on the last bar · d) at session open

**A20.** This indicator issues:
a) buy and sell signals · b) probability grades · c) no trade signals · d) position sizes

---

## Section B — Short answer (12 marks)

**B1.** State the middle-bar rule for a bearish zone.

**B2.** Why is the Average Range filter the right choice on a symbol with no reliable volume feed?

**B3.** What does a 35% balance figure tell you about how a zone was built?

**B4.** Define *confirmed* as the Academy uses the term.

**B5.** Give one element that can change intrabar and one that cannot.

**B6.** Why does a level broken twice carry only one structure line?

**B7.** Why would drawing equal levels immediately be worse than drawing them late? **[G]**

**B8.** In Fix mode on an M1 chart with Fix = M15, how wide is a zone drawn, and in whose bars?

**B9.** Name the three usual causes of an alert that does not fire.

**B10.** What is the signature on screen of the drawing budget being exhausted?

**B11.** State what a sweep is, in one sentence, without using the word "reversal".

**B12.** Why is "the gap will get filled" an unsafe assumption?

---

## Section C — Applied (8 marks, 2 each)

**C1. [G]** List the seven steps of the reading sequence in order, and state which of them this indicator performs for you.

**C2. [G]** Price sweeps the session high and closes back below it. Structure does not shift; the next three structure events are bullish BOS lines. State your read, and what would have to change it.

**C3.** Your bias timeframe shows an unfilled bearish zone 40 points above price. A sweep and a bearish MSS have just completed, leaving a fresh zone 12 points above price. Your risk limit permits 15 points of invalidation distance. Describe how you would decide whether a trade exists — without stating a direction to trade.

**C4.** A student reports that zones "keep disappearing" on a Multi-Fix chart with four timeframes. Diagnose it, give the arithmetic, and give the fix.

---

## Declaration

I completed this exam without assistance and understand that this course is educational material only.

Signed: ______________________  Date: ____________

---

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| v2.1.0 | 2026-09-20 | Dale Batise | First Certification Exam for Fair Value Gaps PRO v2.1: 40 marks across multiple choice, short answer and applied sections, with gating questions identified. |

**Educational material only. Not financial advice, not a signal service, and not a claim about future results.**

---

*© THE CONSISTENCY COLLECTIVE — THECC Institutional Trader Academy™ · Consistency Creates Freedom. · Academy Documentation Standard v1.0.*
