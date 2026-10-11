"""
Parity check: engine vs. the THECC indicator's own plot columns in a TradingView export.

    python parity.py export.csv [--warmup 600] [--lngth 50 --mult 1.0 --lrate 0.5 ...]

Columns used when present (TradingView names them after the plot titles):
    Supertrend            -> tlin                     (float, rel tol 1e-6)
    Dot                   -> tlin on cdir flip bars    (flip-bar set + value)
    Momentum              -> finalMomentum            (float, rel tol 1e-6)
    Adaptive Length       -> MOM lookback              (int)
    THECC BUY / THECC SELL-> newBuy / newSell bars     (non-na and != 0 => signal)
The engine is run from the first CSV row, i.e. it assumes the export's first bar is the
indicator's bar_index 0. Bars before --warmup are ignored.
"""
from __future__ import annotations

import argparse
import sys

import numpy as np
import pandas as pd

import engine as E


def _find(df, name):
    """Exact match first, then case-insensitive, then 'name.1' style duplicates excluded."""
    if name in df.columns:
        return name
    low = {c.lower(): c for c in df.columns}
    return low.get(name.lower())


def _float_mismatch(eng, tv, rtol, atol=1e-9):
    e_na, t_na = np.isnan(eng), np.isnan(tv)
    both = ~e_na & ~t_na
    diff = np.zeros_like(eng, dtype=bool)
    diff[both] = np.abs(eng[both] - tv[both]) > np.maximum(rtol * np.abs(tv[both]), atol)
    na_mis = e_na != t_na
    bad = diff | na_mis
    return bad, int(diff.sum()), int(na_mis.sum())


def _flag(x):
    x = pd.to_numeric(pd.Series(x), errors="coerce").to_numpy(float)
    return ~np.isnan(x) & (x != 0)


def run(path, warmup=600, rtol=1e-6, show=5, **params):
    df = E.load_tv_csv(path)
    n = len(df)
    res, ind = E.run_thecc(df, **params)
    mask = np.arange(n) >= warmup
    t = df["time"].to_numpy()
    print(f"{path}: {n} bars, comparing bars {warmup}..{n - 1} ({mask.sum()} bars)")
    out = {}

    def report(label, bad, extra=""):
        bad = bad & mask
        cnt = int(bad.sum())
        out[label] = cnt
        print(f"  {label:<22} mismatches: {cnt:>6} {extra}")
        if cnt and show:
            idx = np.flatnonzero(bad)[:show]
            print(f"      first at bar_index {list(idx)} (time {list(t[idx])})")
        return bad

    found = False
    col = _find(df, "Supertrend")
    if col:
        found = True
        tv = df[col].to_numpy(float)
        bad, nv, nn = _float_mismatch(ind["tlin"], tv, rtol)
        report("Supertrend line", bad, f"(value {nv}, na {nn})")
        if (bad & mask).any():
            i = np.flatnonzero(bad & mask)[0]
            print(f"      bar {i}: engine={ind['tlin'][i]!r} tv={tv[i]!r}")

    cdir = ind["cdir"]
    eng_flip = np.zeros(n, bool)
    eng_flip[1:] = cdir[1:] != cdir[:-1]
    col = _find(df, "Dot")
    if col:
        found = True
        tv = df[col].to_numpy(float)
        report("cdir flips (Dot)", eng_flip != ~np.isnan(tv),
               f"(engine flips {int((eng_flip & mask).sum())}, tv {int((~np.isnan(tv) & mask).sum())})")
        both = eng_flip & ~np.isnan(tv)
        dv = np.zeros(n, bool)
        dv[both] = np.abs(ind["tlin"][both] - tv[both]) > rtol * np.abs(tv[both])
        report("Dot value", dv)

    col = _find(df, "Momentum")
    if col:
        found = True
        tv = df[col].to_numpy(float)
        bad, nv, nn = _float_mismatch(ind["mom"], tv, rtol)
        report("finalMomentum", bad, f"(value {nv}, na {nn})")
        if (bad & mask).any():
            i = np.flatnonzero(bad & mask)[0]
            print(f"      bar {i}: engine={ind['mom'][i]!r} tv={tv[i]!r}")
        sign = np.sign(np.nan_to_num(ind["mom"])) != np.sign(np.nan_to_num(tv))
        report("finalMomentum sign", sign)

    col = _find(df, "Adaptive Length")
    if col:
        tv = df[col].to_numpy(float)
        report("MOM lookback", ~np.isnan(tv) & (ind["lookback"] != tv))

    sig = res["signals"]
    for name, val in (("THECC BUY", 1), ("THECC SELL", -1)):
        col = _find(df, name)
        if col:
            found = True
            tvf = _flag(df[col])
            ef = sig == val
            report(f"{name} bars", ef != tvf,
                   f"(engine {int((ef & mask).sum())}, tv {int((tvf & mask).sum())})")

    if not found:
        print("  no THECC plot columns found (Supertrend / Dot / Momentum / THECC BUY / THECC SELL)")
    s = E.stats(E.trades_df(res))
    print("  engine stats (all closed trades):", {k: (round(v, 4) if isinstance(v, float) else v)
                                                  for k, v in s.items()})
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("csv", nargs="+")
    ap.add_argument("--warmup", type=int, default=600)
    ap.add_argument("--rtol", type=float, default=1e-6)
    for k, v in E.THECC_DEFAULTS.items():
        if isinstance(v, bool):
            ap.add_argument(f"--{k}", type=lambda s: s.lower() in ("1", "true", "yes", "on"), default=v)
        else:
            ap.add_argument(f"--{k}", type=type(v), default=v)
    a = vars(ap.parse_args(argv))
    paths, warmup, rtol = a.pop("csv"), a.pop("warmup"), a.pop("rtol")
    total = 0
    for p in paths:
        total += sum(run(p, warmup, rtol, **a).values())
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
