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

# THECC Q-Trend + P&D Zones + Adaptive MACD Strategy (TradingView)

`THECC_QTrend_PD_MACD.pine` puts **Q-Trend**, **Dynamic Premium & Discount Zones** and **Adaptive MACD** into one THECC-branded Pine v6 indicator. It adds a combined BUY/SELL signal and an Entry / Stop Loss / Take Profit bracket on top.

## Install
In TradingView, open the Pine Editor, paste the file contents, then click **Add to chart**. The Adaptive MACD shows in its own pane. Q-Trend, the zones, signals, brackets and panels show on the price chart.

## Default settings (from the strategy walkthrough)
| Setting | Original | THECC default |
|---|---|---|
| Q-Trend: Smooth source with EMA? | No | **No** |
| Q-Trend: ATR Multiplier | 1.0 | **0.8** |
| P&D: Equilibrium line | Smooth | **Stepped** |
| Adaptive MACD: R2 Period | 20 | **18** |
| Adaptive MACD: Histogram style | Columns | **Histogram** |
| Adaptive MACD: MACD line | chart text colour, width 1 | **blue, width 2** |
| Risk : Reward | – | **1 : 1.5** |

Every other setting keeps the original indicator's default.

## Signals
- **SELL:** Q-Trend prints a **SELL or STRONG SELL** label, the MACD **orange (signal) line is above the blue (MACD) line**, and a **bearish candle** closes. The stop goes at the **previous high**.
- **BUY:** Q-Trend prints a **BUY or STRONG BUY** label, the MACD **blue line is above the orange line**, and a **bullish candle** closes. The stop goes at the **previous low**.
- **Target:** 1.5 × the stop distance.

The MACD and candle confirmation can come on the label bar or within the next few bars (*Confirmation window*, default 3). The setup is cancelled if Q-Trend flips the other way. "Previous high/low" means the highest high or lowest low of the last 10 bars (*Swing lookback*). You can switch it to the previous candle instead. Optional settings: take STRONG labels only, or require BUYs in discount and SELLs in premium (*Premium/Discount filter*, off by default).

THECC signals show as **THECC BUY / THECC SELL** labels, one ATR beyond the candle so they don't cover the Q-Trend labels.

Alerts: THECC Buy, THECC Sell, THECC Signal, Take Profit Hit, Stop Loss Hit, plus all of the original Q-Trend and Premium & Discount alerts.

*THECC AI Coach. For education only, not financial advice.*

## Strategy version (backtesting)
`THECC_QTrend_PD_MACD_Strategy.pine` uses the same signals and bracket but runs as a TradingView **strategy**, so results show in the **Strategy Tester**.
- Orders fill at the close of the signal candle. SL/TP are stop/limit orders at the bracket levels (or market closes when *Exit trigger* is *Close*). An opposite signal reverses the trade.
- **Position size:** risk 1% of equity per trade by default (*THECC Backtest → Risk per trade*), or switch to *Strategy properties* to use the Properties tab order size.
- Optional *Trade direction* (long/short only) and *date range* filters.
- Commission and slippage default to 0; set them on the Properties tab for realistic results.
- The MACD lines are hidden in the strategy (they would squash the price scale). Their values are still in the Data Window. Add the indicator version alongside to see the MACD pane.
- Alerts: create an alert on the strategy and pick *alert() function calls only* (THECC BUY/SELL with entry, SL and TP) or *Order fills*.
