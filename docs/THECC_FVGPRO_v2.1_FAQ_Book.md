<!-- ┌─────────────────────────────────────────────────────────────────────┐ -->
<!-- │ THECC INSTITUTIONAL TRADER ACADEMY™ — STANDARD DOCUMENT FRONT-MATTER │ -->
<!-- └─────────────────────────────────────────────────────────────────────┘ -->

# THECC Fair Value Gaps PRO — FAQ Book

### THECC Institutional Trader Academy™

#### 📘 Course Metadata

| Field | Value |
|---|---|
| **Academy** | THECC Institutional Trader Academy™ |
| **Course** | Fair Value Gaps PRO |
| **Module** | Reference |
| **Lesson** | FAQ |
| **Difficulty** | All |
| **Estimated Time** | 25 minutes |
| **Prerequisites** | Quick Start `THECC-DOC-FVGPRO-QS` |
| **Indicator Version** | v2.1 |
| **Document Version** | v2.1.0 |
| **Last Updated** | 2026-09-20 |
| **Instructor** | Dale Batise |
| **Status** | Content Complete — Certification Pending |

**Document control:**

| Field | Value |
|---|---|
| Document ID | THECC-DOC-FVGPRO-FAQ |
| Document type | FAQ Book |
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

## A · Getting started (1–8)

**1. What does this indicator actually do?** Marks fair value gaps with the volume behind them, market structure shifts and breaks, equal highs and lows, and liquidity sweeps. It is a map of evidence.

**2. Does it tell me when to buy or sell?** No. It issues no signals of any kind and holds no view on direction.

**3. Can I use it on stocks, crypto and forex?** Yes. On symbols without an honest volume feed, use Average Range filtering and ignore the volume figures.

**4. Which timeframe should I start on?** M5 with defaults. Then set detection to Fix on M15 and keep executing where you like.

**5. Do I need other THECC products for this to work?** No, it is standalone. It pairs naturally with an execution tool because it deliberately does not execute.

**6. Why must I save the script?** TradingView only attaches alerts to saved indicators.

**7. Can I run two copies with different settings?** Yes — one Fix on H1 for bias and one in Auto for execution is a common layout. Mind the drawing budget; each instance has its own 500-object allowance.

**8. Does it work on replay?** Yes. Zones form on confirmed bars, which makes replay honest practice.

## B · Detection (9–22)

**9. Why did an obvious gap not draw?** The middle bar did not close through the gap edge, the move was too small against ATR, or the bar-to-bar jump exceeded ATR with Allow Gaps off.

**10. What is the middle-bar rule?** Bullish: bar 2 closes above bar 1's high. Bearish: bar 2 closes below bar 1's low.

**11. Does the zone cover the three bars?** No — only the untraded range between bar 1 and bar 3.

**12. Same Type versus All?** Same Type needs three bars of one direction: cleanest and fewest. All accepts mixed sequences and produces more zones.

**13. Average Range or Volume Threshold?** Average Range for anything; Volume Threshold only where volume is trustworthy.

**14. What does Volume Threshold % compare?** 5-bar average volume against 15-bar average volume.

**15. Is higher sensitivity stricter?** No. `gap × sensitivity > ATR` — Extreme (6.0) admits the most zones, Low (1.0) the fewest.

**16. What does the sensitivity checkbox do when unticked?** Disables both size tests. Every geometric gap draws. Study only.

**17. Why does ATR length matter?** It is the yardstick for both size tests. Longer is steadier and rejects fewer zones after one volatile bar.

**18. Can a zone vanish after appearing?** Not from detection — zones form on confirmed bars. Appearance changes when zones merge.

**19. What is Allow Gaps Between Bars?** It permits session and news gaps that the ATR jump check would otherwise reject.

**20. Why are there more zones on lower timeframes?** More bars, more sequences, smaller ATR. Lower timeframes always produce more.

**21. Does it detect inverted or inverse gaps?** Not in this product. This build detects and tracks fair value gaps, their invalidation and their merging.

**22. Does the indicator look ahead?** No. Higher-timeframe data is requested without lookahead, and zones are created on confirmed bars.

## C · Reading the chart (23–34)

**23. What is `12.4K (68%)`?** Total volume of the three bars, and how evenly it split between the zone's halves. High percentage means even.

**24. Is a high percentage better?** It is not a quality score. It describes how the level was built.

**25. What is the dashed line inside a box?** The 50% midpoint.

**26. What does `[Combined]` mean?** Overlapping same-direction zones merged into one, volumes added.

**27. Why is one zone much wider than the others?** Either it is combined, or it is one of the latest zones extended to the current bar.

**28. What does a box that stops mid-chart mean?** It was invalidated at that bar.

**29. What is the `M15 ·` prefix?** The source timeframe in Multi-Fix mode.

**30. What is Skull Mode for?** Keeping levels while removing nearly all visual weight.

**31. Why do the newest zones reach the current bar?** Extend latest zones to current bar — three by default.

**32. Should I keep historic zones on?** While learning, yes. They are the audit trail.

**33. What is the difference between MSS and BOS again?** MSS: closed through the last **opposing** swing, direction stopped. BOS: closed through the last swing in the **same** direction, continuation.

**34. Why is a `$ sweep` label above the bar bearish context?** It names the side of the book that was taken. Buy stops above were filled and price could not hold.

## D · Structure, levels, sweeps (35–44)

**35. Why did structure ignore a break?** It was a wick. Structure requires a close.

**36. What does pivot length change?** How large a swing must be to qualify. Higher gives fewer, more significant events.

**37. Why only one line at a level broken twice?** Duplicate-level suppression.

**38. Why did all my structure lines disappear?** Clear previous structure lines on each new MSS is switched on.

**39. Why are equal levels late?** Pivots need bars on both sides to confirm. The alternative repaints.

**40. No equal levels at all?** Tolerance too tight for the symbol. Raise it gradually.

**41. What exactly is a sweep here?** Price exceeds the lookback high or low, excluding the current bar, then closes back inside against the run.

**42. Why so many sweeps?** Short lookback. Raise it to 50–200 for long-standing levels.

**43. A sweep printed and price kept going — is it broken?** No. A sweep is a failed breakout, not a reversal. Require an MSS before treating it as a turn.

**44. Do structure and sweeps follow Multi-Fix?** No. Chart timeframe only. Only zones follow Fix and Multi-Fix.

## E · Alerts (45–52)

**45. How many alerts should I run?** Start with one: `MSS (any)`.

**46. Which route gives the broken level?** The dynamic route — "Any alert() function call".

**47. What is the message format?** `<direction> <event> | <ticker> | <timeframe> | level <price> | close <price>`.

**48. What is the prefix for?** Routing to a bot or webhook.

**49. Why did my BOS alert never fire?** Show BOS is off, which gates detection.

**50. Why are sweep and equal-level alerts off by default?** They fire far more often than structure events.

**51. Should I disable bar-close gating for speed?** No, not for anything you trade. Without it you will be alerted to breaks that fail before the close.

**52. Can one alert cover several timeframes?** The `New FVG TF#1`–`TF#4` conditions are per slot; the dynamic route covers structure, equal levels and sweeps on the chart timeframe.

## F · Display and performance (53–58)

**53. Why did my old zones disappear?** The drawing budget: 4 boxes per zone against a 500-box ceiling, about 125 zones in total.

**54. How do I fix it?** Lower Zones kept per timeframe — roughly 30 when four timeframes are active.

**55. Why is a zone drawn without its volume bars?** The budget ran out mid-zone. Same fix.

**56. The script times out. What do I cut first?** Active timeframes, then zones kept, then max bars back to process.

**57. Can I raise the 500-object limit?** No. It is a TradingView platform limit and the declaration requires compile-time constants.

**58. Does Skull Mode make it faster?** Not materially. It changes appearance, not object count.

## G · Expectations and risk (59–64)

**59. What win rate does this produce?** None — it produces no trades. Any figure attached to it would be a claim about a plan, not about the indicator.

**60. Do gaps always get filled?** No. Many never do.

**61. Is a bigger zone a better zone?** Bigger means more displacement, and also a wider invalidation distance. Whether that is better depends entirely on your risk limit.

**62. Can I automate from the webhook messages?** The messages are structured enough to route, but automating an entry from a map is a decision about your plan and your risk, not a feature of this tool.

**63. Where does risk management live?** Outside this indicator, in your written plan. The tool deliberately has no view.

**64. Is this financial advice?** No. Every document in this suite is educational material only.

## H · Documentation and versions (65–70)

**65. Which version do these documents describe?** FVG PRO v2.1.x. Check the script header against the document header.

**66. Is the course certified?** Not yet. Status is Content Complete — Certification Pending until the build passes the TradingView compile green-check and the owner signs off.

**67. Why do the guides show screenshot placeholders?** Real captures are outstanding across the product range.

**68. Where is the full course?** Student Guide `THECC-DOC-FVGPRO-SG`.

**69. Where do I look when something on screen looks wrong?** Troubleshooting Manual `THECC-DOC-FVGPRO-TS`.

**70. Why does this product have no THECC-NNNN number?** The registry has not assigned one. It raises the question under THECC-0008, and IDs are assigned once and never change, so the documents say "Registry ID pending" rather than guessing.

---

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| v2.1.0 | 2026-09-20 | Dale Batise | First FAQ Book for Fair Value Gaps PRO v2.1: 70 questions across getting started, detection, chart reading, structure, alerts, display, expectations and documentation. |

**Educational material only. Not financial advice, not a signal service, and not a claim about future results.**

---

*© THE CONSISTENCY COLLECTIVE — THECC Institutional Trader Academy™ · Consistency Creates Freedom. · Academy Documentation Standard v1.0.*
