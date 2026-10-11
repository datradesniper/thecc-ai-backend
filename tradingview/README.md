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

## Session stats table (last 100 trades)
A third table (bottom left by default) splits the last **100** closed trades into **Premarket** (entries outside NY regular hours) and **NY Regular** (entries 9:30am–4:30pm ET). Each column shows:
- trades and wins / losses
- win rate
- net R and average R per trade
- profit factor
- net and average P/L in $
- max drawdown and longest losing streak
- total costs paid

Every trade has a **fixed cost per contract** (default **$5.00** round turn, **1 contract**) subtracted. Dollar values use the symbol's point value ($20/pt NQ, $50/pt ES). You can change N, the session window, the contract count and the cost under *THECC Session Stats*.

Alerts: THECC Buy, THECC Sell, Take Profit Hit, Stop Loss Hit, plus all of the original MOM alerts.

*THECC AI Coach. For education only, not financial advice.*

## Backtest on your own chart (strategy version)
`THECC_Supertrend_MOM_Strategy.pine` is the same script declared as a **strategy**. Add it to the chart and open **Strategy Tester** to get TradingView's own backtest of the exact BUY/SELL signals and brackets on that chart.
- Entries fill at the signal candle's close. The SL and TP are stop/limit orders. Each trade is 1 contract.
- Commission is **$2.50 per contract per side = $5.00 round turn**. Change it in the strategy's *Properties* tab.
- **Trade sessions** = *Premarket only* or *NY Regular only* makes the Strategy Tester report one session on its own. Run it once with each setting, on each timeframe.
- Set *Last N trades per session* to 500 to make the on-chart session table cover 500 trades.
- How much history you get depends on your TradingView plan. Turn on **Deep Backtesting** in Strategy Tester (Premium and above) to test beyond the loaded bars.
- The strategy version has no alerts, because TradingView doesn't allow `alertcondition` in strategies. Use the indicator version for alerts.
