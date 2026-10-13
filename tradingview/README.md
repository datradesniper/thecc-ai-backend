# THECC Supertrend Error Cloud + MOM Strategy (TradingView)

`THECC_Supertrend_MOM.pine` puts the **Supertrend Error Adaptive Cloud** and the **MOM - Adaptive Cycle Momentum Oscillator** into one THECC-branded Pine v6 indicator. It adds its own BUY/SELL signals and an Entry / Stop Loss / Take Profit bracket on top.

## Install
In TradingView, open the Pine Editor, paste the file contents, then click **Add to chart**. The MOM oscillator shows in its own pane. The Supertrend cloud, signals, brackets and tables show on the price chart.

## Default settings (from the strategy walkthrough)
| Setting | Original | THECC default |
|---|---|---|
| Supertrend: Learning Rate | 0.1 | **0.5** |
| Supertrend: Bull Color | green | **blue** |
| MOM: Source | close | **high** |
| MOM: Maximum Cycle Period | 34 | **20** |
| MOM: Period Multiplier | 1.1 | **0.8** |
| MOM: momentum line thickness | 2 | **3** |
| Risk : Reward | – | **1 : 1.5** |

Every other setting keeps the original indicator's default. One exception: the Supertrend dashboard moves to Top Right so it doesn't sit on top of the MOM table.

## Signals
- **SELL:** the Supertrend circle flips to **Bear**, the MOM red line is **below zero**, and a **bearish candle** closes. The stop goes at the **previous high**.
- **BUY:** the Supertrend circle flips to **Bull**, the MOM green line is **above zero**, and a **bullish candle** closes. The stop goes at the **previous low**.
- **Target:** 1.5 × the stop distance.

The confirmation candle can come on the flip bar or within the next few bars (*Confirmation window*, default 3 bars). "Previous high/low" means the highest high or lowest low of the last 20 bars (*Swing lookback*). You can switch it to the previous candle or the Supertrend line instead.

## Bracket and THECC panel
Each trade gets a teal target zone, a red stop zone and an entry line. The bracket is cut at the exit bar, and a ✓ / ✗ label shows the result in R. The THECC panel shows:
- the Supertrend direction and error bias
- the MOM value against zero
- the setup status
- the stop and R:R settings
- closed trades, win rate, net R and the open trade

Alerts: THECC Buy, THECC Sell, Take Profit Hit, Stop Loss Hit, plus all of the original MOM alerts.

*THECC AI Coach. For education only, not financial advice.*

---

# TCC TradeOS Plan Loader v2.0.0

`TradeOS_Plan_Loader.pine` draws a TradeOS plan on the chart from one Plan Code, for example:

```
TCC1|2026-10-13|AMLUNCH|CL|GO|A|LONG|93.09|93.34|93.22|92.59|94|94.36|94.8|93.76|92.73|91.7
```

**Install once:** Pine Editor → paste the file → **Add to chart**.
**Each session:** Settings → paste into **TradeOS Plan Code** → **press Enter** → **OK**.

What's new in v2.0.0:
- **Three market groups:** Equity (NQ, ES, YM), Energy (CL, HO, RB) and Metals (GC, SI, HG). The micro and mini contracts are accepted too.
- **Live session tracking:** from the start of the routine window (New York time, editable), the status table moves through Watching → In Zone → Entry Filled → TP1 → TP2 → TP3, or ends at Stopped, Expired, Invalidated or Missed.
- **Alerts:** one fixed alert for each event, plus detailed `alert()` messages that carry the price levels. To get those, choose *Any alert() function call* when you create the alert.

The Plan Code format and the input title haven't changed, so a plan saved in v1.x still loads.
