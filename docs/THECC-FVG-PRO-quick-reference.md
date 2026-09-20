# THECC FVG PRO — Quick Reference

One page. Full explanations in `THECC-FVG-PRO-student-guide.md`. Educational only.

## On-chart legend

| Mark | Meaning |
|---|---|
| Colored box | Fair value gap (bull / bear) |
| Two bars in the box | Volume split between the zone's halves |
| `12.4K (68%)` | 3-bar volume · how evenly it split (high % = even) |
| `M15 ·` prefix | Multi-Fix zone, tagged with its source timeframe |
| `[Combined]` | Merged overlapping same-direction zones |
| Box ends mid-chart | Invalidated there |
| Solid line + `MSS` | Structure flipped — closed through the last opposing swing |
| Dotted line + `BOS` | Structure continued — closed through the last swing |
| Dashed level + `EQH` / `EQL` | Shelf of two near-equal pivots (stops) |
| `$ sweep` above bar | Buy-side sweep — high taken, closed back below → context for shorts |
| `$ sweep` below bar | Sell-side sweep — low taken, closed back above → context for longs |

## Detection in one line each

- **FVG** — 3-bar gap + middle bar closes through the gap edge + passes the size/volume filter. Confirmed bars only.
- **MSS** — close beyond the most recent **opposing** swing → direction flips.
- **BOS** — close beyond the most recent swing in the **same** direction → continuation.
- **EQH / EQL** — two consecutive pivots within tolerance %, drawn `Swing length` bars late.
- **Sweep** — takes out the lookback high/low, then closes back inside, against the run.

## Sensitivity is permissiveness

`gap × sensitivity > ATR` · Extreme 6.0 (most zones) → High 2.0 → Normal 1.5 → Low 1.0 (fewest, biggest)

## Alert names

`MSS Bullish` `MSS Bearish` `BOS Bullish` `BOS Bearish` `MSS (any)` `BOS (any)` `MSS or BOS (any)` `Equal Highs (EQH)` `Equal Lows (EQL)` `Buy-side liquidity sweep` `Sell-side liquidity sweep` `Liquidity sweep (any)` `New FVG (Auto/Fix)` `New FVG TF#1–#4`

Or one alert on **"Any alert() function call"** →
`Bullish BOS | NQ1! | 5 | level 20114.25 | close 20118.50`

Gotchas: per-signal toggles must be on · BOS alerts need *Show BOS* on · EQH/EQL and sweep alerts default off · keep *Fire on bar close only* ON.

## Drawing budget

500 boxes / 500 lines / 500 labels total. **Each zone = 4 boxes + 2 lines → ~125 zones is the whole box budget across all timeframes.**
Four Multi-Fix timeframes → set *Zones kept per timeframe* ≈ 30. Old drawings vanishing means you are over.

## Reading sequence

Bias (HTF gaps) → liquidity (EQH/EQL, session extremes) → **sweep** → **MSS** → the FVG the shift left → define invalidation → only then size the trade.

## Defaults worth knowing

| Setting | Default |
|---|---|
| Zone Invalidation | Close (body must close through) |
| Zone Filtering | Average Range |
| Detection Sensitivity | Extreme |
| Zones kept per timeframe | 125 |
| Delete untouched zones after | 200 bars |
| Pivot length (MSS/BOS) | 5 |
| EQ swing length / tolerance | 5 / 0.02% |
| Sweep lookback / max labels | 20 / 50 |
| Fire on bar close only | ON |

*Not financial advice. Trade your own plan.*
