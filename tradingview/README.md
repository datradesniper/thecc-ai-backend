# THECC OC + Spread RSI Strategy (TradingView)

`THECC_OC_SpreadRSI.pine` puts the **OC Buy/Sell Signals** and **Spread RSI** indicators into one THECC-branded Pine v6 script.

## Install
1. In TradingView, open the Pine Editor, paste the file contents, then click **Add to chart**.
2. The Spread RSI line shows in its own pane. BUY/SELL labels, Entry/SL/TP lines, the info box and the THECC logo show on the price chart.

## Default settings (from the strategy walkthrough)
| Setting | Original | THECC default |
|---|---|---|
| OC: Average body length | 50 | **39** |
| OC: Min body vs average | 3.0 | **2.0** |
| OC: Min volume vs average | 0.0 | **0.5** |
| Spread RSI: Upper threshold (red line) | 90 | **57** |
| Spread RSI: Lower threshold (green line) | 10 | **38** |
| Stop loss mode | Candle wick | Candle wick (the red SL line) |
| Take profit (x SL) / R:R | 2.0 | **1.8** (the trades in the walkthrough used 1:1.72 to 1:1.84) |

Everything else keeps the original defaults: RSI length 2, comparison symbol AMEX:SPY, non-repaint ON, alternate signals ON, wick exits, ATR 14.

## Rules
- **BUY:** an OC BUY signal, then the Spread RSI line above the upper (red) line, then a bullish confirmation candle closes. Entry is that candle's close.
- **SELL:** an OC SELL signal, then the Spread RSI line below the lower (green) line, then a bearish confirmation candle closes.
- **Stop loss:** the OC signal candle's wick. **Take profit:** 1.8 × risk.

`Confirmation candle` sets whether confirmation comes from the **Next candle** (default) or the **Signal candle** itself. Small triangles mark raw OC signals that never got confirmed.

Alerts: THECC Buy/Sell Entry, raw OC Buy/Sell, TP Hit, SL Hit.

*THECC AI Coach. For education only, not financial advice.*
