# THECC Sentiment Tide

`THECC_Sentiment_Tide.pine` — Pine Script **v6** indicator that merges three tools from the
walkthrough into one script with buy/sell signals, a stop loss and three targets at
**1:1, 1:2 and 1:3** risk-to-reward.

## What it combines

| Component | Role | Default |
|---|---|---|
| Average Sentiment Oscillator (ASO) | Market sentiment: blue = % bullish, red = % bearish | Period **34**, method 0 (both) |
| Stochastic | Trend-following entry trigger | **7 / 3 / 3**, bands 80 / 20 |
| EMA ribbon (5 / 8) | Pullback confirmation for reversals | EMA **5** white, EMA **8** orange |

The ASO and Stochastic draw in the indicator pane; the EMAs, BUY/SELL labels and the
SL / Entry / TP1 / TP2 / TP3 levels are pushed onto the price chart with `force_overlay`,
so one script covers both panes.

## Signal rules

**Trend following** (`Strategy = Trend Following` or `Both`)
- Sentiment bearish (red above blue) → wait for %K above 80, then **SELL** when %K closes
  below %D *and* below 80.
- Sentiment bullish (blue above red) → wait for %K below 20, then **BUY** when %K closes
  above %D *and* above 20.

**Reversal** (`Strategy = Reversal` or `Both`)
- ASO crossover red above blue → wait for a pullback (EMA 5 above EMA 8), then **SELL**
  when EMA 5 closes back below EMA 8.
- ASO crossover blue above red → wait for a pullback (EMA 5 below EMA 8), then **BUY**
  when EMA 5 closes back above EMA 8.

## Risk model

- Entry = close of the signal candle.
- Stop = pullback extreme over the last `slLookback` bars (default 10) ± `0.25 × ATR(14)` buffer.
- R = |entry − stop|. TP1 = 1R, TP2 = 2R, TP3 = 3R (all three ratios editable).
- A setup closes when TP3 or the stop is hit, or on an opposite signal (`Close the setup on an
  opposite signal`). `Only one open setup at a time` is on by default.
- Target and stop hits are marked with an ✕ and fire their own alerts.

The video's own trade management (1.5R for trend following, 2R for reversals) is a subset —
just set the three ratios to whatever you run.

## Alerts

`BUY`, `SELL`, sentiment flip bullish/bearish, TP1/TP2/TP3 hit, SL hit, plus a combined
`alert()` on every new signal containing entry, stop and all three targets.

## Install

TradingView → Pine Editor → paste the file → Save → Add to chart. Signals confirm on bar
close; use "Once per bar close" when creating alerts.
