<!-- ┌─────────────────────────────────────────────────────────────────────┐ -->
<!-- │ THECC INSTITUTIONAL TRADER ACADEMY™ — STANDARD DOCUMENT FRONT-MATTER │ -->
<!-- └─────────────────────────────────────────────────────────────────────┘ -->

# THECC Fair Value Gaps PRO — Instructor Answer Key

### THECC Institutional Trader Academy™

> ⚠️ **Instructor copy. Do not distribute to students.**

#### 📘 Course Metadata

| Field | Value |
|---|---|
| **Academy** | THECC Institutional Trader Academy™ |
| **Course** | Fair Value Gaps PRO |
| **Module** | 1–4 (Core Curriculum) |
| **Lesson** | Assessment |
| **Difficulty** | Instructor |
| **Estimated Time** | 20 minutes marking |
| **Prerequisites** | Student Guide `THECC-DOC-FVGPRO-SG` |
| **Indicator Version** | v2.1 |
| **Document Version** | v2.1.0 |
| **Last Updated** | 2026-09-20 |
| **Instructor** | Dale Batise |
| **Status** | Content Complete — Certification Pending |

**Document control:**

| Field | Value |
|---|---|
| Document ID | THECC-DOC-FVGPRO-AK |
| Document type | Instructor Answer Key |
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

## Marking rules

- Pass mark **80% — 16 of 20**.
- One mark per question unless stated. Award the mark for substance, not wording.
- **Questions 16, 17 and 20 are gating.** A student who misses any of those three has not met the course objective even with 16 marks elsewhere. Re-teach Chapter 5 and re-test before sign-off.
- Where a student gives the right answer for the wrong reason, mark it wrong and say why.

---

## Appendix A — Certification Quiz (20 marks)

**1. What must the middle bar of a three-bar sequence do before a zone is drawn?**
Close through the gap edge: above bar 1's high for a bullish gap, below bar 1's low for a bearish one. *Reject "be a big candle" — size is a separate test.*

**2. State the size test applied to the gap, including the role of sensitivity.**
`gap size × sensitivity > ATR`. Sensitivity is a permissiveness multiplier, not a strictness one. (Full marks also for adding the Average Range test on the combined three-bar body size against ATR ÷ 1.5.)

**3. Does Extreme sensitivity admit more zones or fewer than Low?**
More. Extreme = 6.0, Low = 1.0.

**4. What does the percentage in a zone's text measure?**
Volume balance between the zone's two halves — smaller ÷ larger × 100. High means evenly split. *Not quality, not strength, not probability.*

**5. On a bullish zone, which bars' volume is shown in the upper half?**
The two most recent bars of the sequence. Bar 1's volume sits in the lower half. (Mirrored for a bearish zone.)

**6. What does `[Combined]` indicate, and how does it affect invalidation placement?**
Two or more overlapping same-direction zones merged into one, volumes added. Invalidation must sit beyond the whole merged range, which is wider than any original zone.

**7. Define *confirmed* as the Academy uses the term.**
The candle has closed and the result is locked.

**8. Which elements of this indicator can change intrabar, and which cannot?**
Sweep labels can — they are evaluated on the live bar. Zones, MSS, BOS and equal levels cannot; zones are created on confirmed bars and structure requires a close. Half marks if they mention only sweeps without naming what is stable. *Accept as a bonus: zone appearance can change when zones merge on the last bar.*

**9. State the difference between MSS and BOS in one sentence each.**
MSS: a close beyond the most recent **opposing** swing — the established direction has stopped. BOS: a close beyond the most recent swing in the **established** direction — continuation.

**10. Why does a repeated break of the same level not draw a second line?**
Repeat breaks of an already-marked level are suppressed, so each level carries one line rather than a stack.

**11. Why are equal-level lines drawn several bars after the second pivot?**
A pivot needs the required number of bars on **both** sides before it is confirmed. Drawing it earlier would repaint.

**12. Define a buy-side liquidity sweep precisely, and state which direction it is evidence for.**
Price takes out the highest high of the lookback window, excluding the current bar, then closes back **below** that high on a down-closing bar. It is evidence **against higher prices** — context for shorts. *No mark if they say it is a buy signal.*

**13. Does the sweep lookback window include the current bar?**
No.

**14. Which elements follow Fix / Multi-Fix timeframes, and which are always chart-timeframe?**
Zones follow Fix and Multi-Fix. Market structure, equal highs and lows, and liquidity sweeps are always computed on the chart timeframe.

**15. In Fix mode = M15 on an M1 chart, how wide is a zone drawn?**
At true M15 width — the zone-width setting is counted in bars of the zone's own timeframe (15 M15 bars by default), not in M1 bars.

**16. Give the seven steps of the reading sequence in order. — GATING**
Map → liquidity → sweep → shift (MSS) → the zone the shift left → invalidation → size. *All seven, in order, for the mark.*

**17. At which step is position size decided, and why not earlier? — GATING**
Last, step 7. Until invalidation is defined there is no risk distance to size against; sizing first makes risk a consequence of what the trader wants rather than what the chart allows. If the distance from entry to invalidation does not fit the risk limit, there is no trade.

**18. How many boxes and lines does one rendered zone consume, and what is the total zone budget?**
Four boxes and two lines. 500 boxes ÷ 4 ≈ **125 zones in total across all active timeframes**, not per timeframe.

**19. Name the three usual causes of an alert that does not fire.**
The per-signal toggle is off; **Show BOS** is off so no BOS is detected; the alert is attached to a different or unsaved indicator instance.

**20. Which two decisions does this indicator never make for you? — GATING**
Whether to trade (direction and entry) and how much to risk (size). Equivalent answers naming invalidation and risk are full marks. *It is a map; it holds no opinion on either.*

---

## Chapter Review Questions — model answers

**Chapter 1** · (1) Because a map's job is to state where evidence exists; merging that with a trigger hides the decision the trader must own. (2) The middle bar must close through the gap edge, and the move must be large against ATR or volume-backed. (3) The execution product — Precision Execution Engine (THECC-0002) — or the trader's own plan.

**Chapter 2** · (1) TradingView can only attach alerts to a saved script. (2) Heikin Ashi synthesizes prices, so a gap found there is a gap in a derived series, not the market. (3) Body-close invalidation, Average Range filtering, and bar-close-gated alerts. *(Accept structure/equal levels defaulting on.)*

**Chapter 3** · (1) Close through the gap edge. (2) That the volume was concentrated on one side of the zone rather than spread across it. (3) Pivots need bars on both sides to confirm; the alternative is a repainting level, and a late honest level is more useful than an early unreliable one. (4) MSS = closed through the last opposing swing, direction stopped. BOS = closed through the last swing in the same direction, continuation.

**Chapter 4** · (1) At true M15 width. (2) Which timeframe produced that zone, so overlap between timeframes becomes visible. (3) Zones kept per timeframe.

**Chapter 5** · (1) Step 4, the structure shift. (2) Because invalidation sets the risk distance, and risk decides whether the trade exists at all. (3) A symbol with no honest volume feed, and a thin or news-distorted session. *(Accept: any symbol where Average Range filtering is the appropriate choice.)*

**Chapter 6** · (1) The dynamic `alert()` route — "Any alert() function call". (2) It restricts evaluation to confirmed bars, so a break that fails before the close cannot alert. (3) Toggle off; Show BOS off; stale or unsaved instance.

**Chapter 7** · (1) More. (2) Zones kept per timeframe. (3) TradingView requires the drawing-limit arguments in the indicator declaration to be compile-time constants.

**Chapter 11** · (1) Four boxes and two lines. (2) About 125, across all timeframes together. (3) The sweep-label cap removing the oldest, and the shared 500-label ceiling being reached by structure and equal-level labels.

---

## Knowledge Check (Course Summary) — model answers

1. **Zones kept per timeframe**, in Multi-Fix mode.
2. Market structure (MSS / BOS), equal highs and lows, and liquidity sweeps.
3. The volume was concentrated on one side of the zone — roughly a 40:60 split between halves. It describes construction, not strength.
4. Because it names the side of the order book that was taken. Those buy stops were filled and price could not hold, which is evidence against higher prices.
5. Deciding whether to take the trade and how much to risk — the plan, not the map.

---

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| v2.1.0 | 2026-09-20 | Dale Batise | First Answer Key for Fair Value Gaps PRO v2.1: quiz answers with marking notes, gating questions identified, chapter review and knowledge-check model answers. |

**Educational material only. Not financial advice, not a signal service, and not a claim about future results.**

---

*© THE CONSISTENCY COLLECTIVE — THECC Institutional Trader Academy™ · Consistency Creates Freedom. · Academy Documentation Standard v1.0.*
