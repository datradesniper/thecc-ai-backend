# THECC backtest engine

A Python port of `tradingview/THECC_Supertrend_MOM.pine` (Pine v6) that aims to match it bar for bar. It uses numpy and numba.
It runs on historical bars with these rules: `barstate.isconfirmed` is always true, any comparison with `na` is false, and `nz(na)` is 0.

```
pip install numpy pandas numba
python smoke_test.py            # synthetic data: timings, stats, reference cross-check, parity round trip
python parity.py export.csv     # compare against a TradingView export that has THECC plot columns
```

## engine.py

| Function | Purpose |
|---|---|
| `load_tv_csv(path, tz="America/New_York")` | Loads a TradingView "Export chart data" CSV. Sorts by time, drops duplicate `time` rows (the last one wins) and orders the columns `time, open, high, low, close`, then any extra plot columns. Adds `et`, the bar-open time in Eastern Time (tz-aware). `time` is UNIX seconds in UTC. |
| `source(o,h,l,c,name)` / `source(df, name=...)` | Builds a Pine source series: `open, high, low, close, hl2, hlc3, ohlc4, hlcc4`. |
| `supertrend(o,h,l,c, lngth=50, mult=1.0, lrate=0.5, ml_on=True, full=False)` | Returns `(tlin, cdir, ebias)`. `cdir == -1` means bull and `1` means bear. `ebias` is the value after that bar's update. With `full=True` it also returns `amult, vrng`. |
| `mom(src,h,l,c, cycle_min=8, cycle_max=20, cycle_mult=0.8, squeeze_on=True, fast=8, slow=34, length_mode='Adaptive', fixed_len=14, full=False)` | Returns `finalMomentum`. With `full=True` it also returns `lookback` (the "Adaptive Length" plot), `cyclePeriod` and `squeezeStrength`. |
| `simulate(o,h,l,c, tlin, cdir, mom, conf_win=3, sl_mode='swing'\|'candle'\|'st', swing_len=20, buf=0.0, rr=1.5, exit_mode='wick'\|'close', close_opp=True)` | Runs the THECC signal and bracket state machine. Returns a dict of arrays for **closed** trades: `entry_idx, exit_idx, dir, entry, sl, tp, exit_px, R, exit_reason` (1 = TP, -1 = SL, 0 = opposite signal). It also returns `open` (None, or a dict for the open trade with `R_at_last_close`) and `signals` (an int8 per bar: +1 for THECC BUY and -1 for THECC SELL, matching the plotshapes). **`buf` is in price units**, which is Pine's `ticks * syminfo.mintick`. |
| `trades_df(res, df=None)` | Turns a `simulate()` result into a DataFrame. It adds `bars_held` and `exit_name`, plus ET entry and exit times when you pass `df`. |
| `stats(trades, last_n=None)` | Takes a `trades_df()` DataFrame or a `simulate()` dict. Reports trades, wins, losses, win_pct, net_R, avg_R (expectancy), profit_factor, max_dd_R (peak to trough of cumulative R, starting at 0), max_consec_losses, pct_tp/sl/opposite, long and short counts, long_win_pct, short_win_pct and avg_bars_held. A win is `R > 0`, as in the Pine panel. Use `last_n=500` to tally the last 500 trades. |
| `run_thecc(df, **overrides)` | Runs the full pipeline with `THECC_DEFAULTS`. Returns `(simulate_result, indicators)`. |
| `grid_search(df, st_grid, mom_grid, conf_wins, sl_modes, swing_lens, rrs, exit_modes, buf, close_opp, last_n, min_trades)` | Computes the Supertrend once for each `(lngth, mult, lrate)` and MOM once for each `(src, cycle_max, cycle_mult)`, then runs `simulate()` for every other combination. Returns one row of `stats()` per combination. |

The low-level numba kernels are `_supertrend`, `_mom` and `_simulate`. In a tight optimisation loop you can call `_simulate` directly, with `sl_mode` set to 0, 1 or 2 and `exit_close` as a bool.

## parity.py

`python parity.py export.csv [--warmup 600] [--rtol 1e-6] [--lngth 50 ... any THECC_DEFAULTS key]`

Compares the engine with the indicator's own plot columns, using whichever of these the export contains:

- `Supertrend` is compared with tlin.
- `Dot` is compared with the cdir flip bars and their value.
- `Momentum` is compared with finalMomentum, both its value and its sign.
- `Adaptive Length` is compared with the MOM lookback.
- `THECC BUY` and `THECC SELL` are compared with the newBuy and newSell bars.

It prints mismatch counts and the first bars that differ. Bars before `--warmup` are ignored. Floats use a relative tolerance of 1e-6. The script exits with a non-zero code if any count is above 0. It treats the first CSV row as the indicator's `bar_index 0`, as described in the caveats below.

## smoke_test.py

This script uses synthetic random-walk OHLC (tick 0.25) only. It does five things:

1. Loads a CSV that is shuffled and contains duplicate rows.
2. Times the engine on N bars and on 100k bars.
3. Runs a grid search of 768 combinations.
4. Prints stats for a default run.
5. Cross-checks `supertrend`, `mom` and `simulate` against a separate plain-Python transcription of the Pine code, then round-trips the parity checker.

Its numbers are **not market results**.

## Known caveats

- **Starting bar.** `ebias` (the Supertrend's adaptive error memory) and every `var` state depend on the bar where TradingView started calculating. If the export's first row is not the indicator's `bar_index 0`, the values can differ for a long time after the warm-up. For parity runs, export the full chart history that was loaded.
- **`math.sum` with a variable `lookback`.** The engine sums the window directly and returns na when the window contains na. TradingView may keep a running sum, which would give rounding differences of about 1e-12. That only matters when momentum is almost exactly 0.
- **`ta.percentrank`.** The engine returns na unless the current value and all 144 previous ratio values are non-na. This only affects the first roughly 177 bars.
