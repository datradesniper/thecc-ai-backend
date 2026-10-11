"""
Smoke test: synthetic random-walk OHLC -> engine timings, stats, cross-check against an
independent plain-Python transcription of the Pine logic, and a parity.py round trip.

    python smoke_test.py [--bars 30000] [--seed 7]

Synthetic data only -- the numbers printed are NOT market results.
"""
from __future__ import annotations

import argparse
import math
import os
import tempfile
import time

import numpy as np
import pandas as pd

import engine as E
import parity

NA = float("nan")


# ─────────────────────────────────────────────────────────────────────────────
# synthetic data
# ─────────────────────────────────────────────────────────────────────────────
def make_synthetic(n, seed=7, tick=0.25, start=18000.0, t0=1_700_000_000, step=60):
    rng = np.random.default_rng(seed)
    vol = np.exp(np.cumsum(rng.normal(0, 0.02, n)))  # slowly varying volatility regime
    vol = 1.0 + 3.0 * vol / vol.mean()
    drift = np.repeat(rng.normal(0, 0.3, n // 500 + 1), 500)[:n]
    ret = rng.normal(drift, vol)
    close = start + np.cumsum(ret)
    open_ = np.empty(n)
    open_[0] = start
    open_[1:] = close[:-1] + rng.normal(0, 0.3, n - 1) * (rng.random(n - 1) < 0.1)
    hi = np.maximum(open_, close) + np.abs(rng.normal(0, vol * 0.6))
    lo = np.minimum(open_, close) - np.abs(rng.normal(0, vol * 0.6))
    r = lambda x: np.round(x / tick) * tick
    return pd.DataFrame({"time": t0 + step * np.arange(n), "open": r(open_), "high": r(hi),
                         "low": r(lo), "close": r(close)})


# ─────────────────────────────────────────────────────────────────────────────
# independent reference (plain Python, written literally from the Pine source)
# ─────────────────────────────────────────────────────────────────────────────
def isna(x):
    return x is None or (isinstance(x, float) and math.isnan(x))


def nz(x):
    return 0.0 if isna(x) else x


def lt(a, b):  # Pine comparison: na -> false
    return (not isna(a)) and (not isna(b)) and a < b


def gt(a, b):
    return lt(b, a)


def ref_supertrend(o, h, l, c, lngth, mult, lrate, ml_on=True):
    n = len(c)
    vr = [NA] * n
    for i in range(lngth - 1, n):
        vr[i] = max(h[k] - l[k] for k in range(i - lngth + 1, i + 1))
    ubh, lbh, tlh, cd, eb, dirv_hist = [], [], [], [], [], []
    entcl, ebias, prdir = c[0], 0.0, 1
    for i in range(n):
        # mlegn
        dirv_hist.append(prdir)
        amult = mult
        if i > lngth:
            amult = max(mult * (1.0 + ebias) if ml_on else mult, 0.5)
        prev_param = dirv_hist[i - 1] if i >= 1 else None
        flip = prdir != nz(prev_param)
        if flip and i > lngth:
            pdir = nz(prev_param)
            exitc = c[i - 1]
            iswin = (pdir == -1 and exitc > entcl) or (pdir == 1 and exitc < entcl)
            ebias = nz(ebias) + lrate * ((0.0 if iswin else 1.0) - nz(ebias))
            entcl = c[i]
        eb.append(ebias)
        # supt
        src = (c[i] + o[i]) / 2.0
        ub = src + amult * vr[i]
        lb = src - amult * vr[i]
        uprev = nz(ubh[i - 1] if i >= 1 else None)
        lprev = nz(lbh[i - 1] if i >= 1 else None)
        c1 = c[i - 1] if i >= 1 else NA
        lb = lb if (gt(lb, lprev) or lt(c1, lprev)) else lprev
        ub = ub if (lt(ub, uprev) or gt(c1, uprev)) else uprev
        pstr = tlh[i - 1] if i >= 1 else NA
        if i == 0 or isna(vr[i - 1]):
            d = 1
        elif (not isna(pstr)) and pstr == uprev:
            d = -1 if gt(c[i], ub) else 1
        else:
            d = 1 if lt(c[i], lb) else -1
        tl = lb if d == -1 else ub
        ubh.append(ub); lbh.append(lb); tlh.append(tl); cd.append(d)
        prdir = d
    return np.array(tlh, float), np.array(cd), np.array(eb)


def ref_simulate(o, h, l, c, tlin, cdir, mom, conf_win, sl_mode, swing_len, buf, rr, exit_mode, close_opp):
    n = len(c)
    pend_dir, pend_bar = 0, None
    t_dir, t_entry, t_sl, t_tp, t_risk, t_ent = 0, NA, NA, NA, NA, None
    trades, sig = [], np.zeros(n, np.int8)
    for i in range(n):
        flip = i >= 1 and cdir[i] != cdir[i - 1]
        st_bull = cdir[i] == -1
        if flip:
            pend_dir = 1 if st_bull else -1
            pend_bar = i
        if pend_dir != 0 and ((pend_dir == 1) != st_bull or (pend_bar is not None and i - pend_bar >= conf_win)):
            pend_dir = 0
        mu = (not isna(mom[i])) and mom[i] > 0
        md = (not isna(mom[i])) and mom[i] < 0
        buy = pend_dir == 1 and mu and c[i] > o[i]
        sell = pend_dir == -1 and md and c[i] < o[i]
        swlo = min(l[i - swing_len + 1:i + 1]) if i >= swing_len - 1 else NA
        swhi = max(h[i - swing_len + 1:i + 1]) if i >= swing_len - 1 else NA
        base_b = swlo if sl_mode == "swing" else (l[i - 1] if i >= 1 else NA) if sl_mode == "candle" else tlin[i]
        base_s = swhi if sl_mode == "swing" else (h[i - 1] if i >= 1 else NA) if sl_mode == "candle" else tlin[i]
        bsl, ssl = base_b - buf, base_s + buf
        buy = buy and not isna(bsl) and bsl < c[i]
        sell = sell and not isna(ssl) and ssl > c[i]
        if buy or sell:
            pend_dir = 0
        if t_dir != 0 and i > t_ent:
            oc = exit_mode == "close"
            slh = (c[i] <= t_sl if t_dir == 1 else c[i] >= t_sl) if oc else (l[i] <= t_sl if t_dir == 1 else h[i] >= t_sl)
            tph = (not slh) and ((c[i] >= t_tp if t_dir == 1 else c[i] <= t_tp) if oc else (h[i] >= t_tp if t_dir == 1 else l[i] <= t_tp))
            if slh or tph:
                px = c[i] if oc else (t_sl if slh else t_tp)
                trades.append((t_ent, i, t_dir, (px - t_entry) * t_dir / t_risk, -1 if slh else 1))
                t_dir = 0
        if t_dir != 0 and close_opp and ((buy and t_dir == -1) or (sell and t_dir == 1)):
            trades.append((t_ent, i, t_dir, (c[i] - t_entry) * t_dir / t_risk, 0))
            t_dir = 0
        if (buy or sell) and t_dir == 0:
            t_dir = 1 if buy else -1
            t_entry = c[i]
            t_sl = bsl if buy else ssl
            t_risk = abs(t_entry - t_sl)
            t_tp = t_entry + t_dir * t_risk * rr
            t_ent = i
            sig[i] = t_dir
    return trades, sig


def ref_mom(src, h, l, c, cmin=8, cmax=20, cmult=0.8):
    """Second MOM transcription using a different structure (numpy per-bar slices, pandas
    for ATR / percentrank) -- used to catch transcription slips in the numba version."""
    n = len(src)
    ang = 0.707 * 2.0 * math.pi / 48.0
    al = (math.cos(ang) + math.sin(ang) - 1.0) / math.cos(ang)
    a1 = math.exp(-1.414 * math.pi / 10.0)
    C2 = 2.0 * a1 * math.cos(1.414 * math.pi / 10.0); C3 = -(a1 * a1); C1 = 1.0 - C2 - C3
    HP, F = [], []
    g = lambda arr, k: nz(arr[k]) if k >= 0 else 0.0
    for i in range(n):
        HP.append(math.pow(1.0 - al * 0.5, 2.0) * (src[i] - 2.0 * g(src, i - 1) + g(src, i - 2))
                  + 2.0 * (1.0 - al) * g(HP, i - 1) - math.pow(1.0 - al, 2.0) * g(HP, i - 2))
        F.append(C1 * (HP[i] + g(HP, i - 1)) * 0.5 + C2 * g(F, i - 1) + C3 * g(F, i - 2))
    sp = {p: 0.0 for p in range(cmin, cmax + 1)}
    agc = 0.0
    cyc, inv, sml, state = NA, 0, NA, NA
    # squeeze via pandas
    def atr(L):
        pc = pd.Series(c).shift(1)
        tr = pd.concat([pd.Series(h - l), (pd.Series(h) - pc).abs(), (pd.Series(l) - pc).abs()], axis=1).max(axis=1)
        tr.iloc[0] = h[0] - l[0]
        out = np.full(n, NA)
        out[L - 1] = tr.iloc[:L].mean()
        for i in range(L, n):
            out[i] = (1.0 / L) * tr.iloc[i] + (1.0 - 1.0 / L) * out[i - 1]
        return out
    ratio = atr(8) / atr(34)
    pr = np.full(n, NA)
    for i in range(144, n):
        w = ratio[i - 144:i]
        if not np.isnan(ratio[i]) and not np.isnan(w).any():
            pr[i] = 100.0 * np.sum(w <= ratio[i]) / 144
    out = np.full(n, NA)
    lbs = np.zeros(n, int)
    for i in range(n):
        cg = pk = NA; dom = 0.0; dist = NA; edge = False
        if i >= 2 * cmax + 2:
            corr = {}
            for lag in range(3, cmax + 1):
                X = np.array([F[i - k] for k in range(lag)]); Y = np.array([F[i - k - lag] for k in range(lag)])
                N = float(lag)
                num = N * float(np.dot(X, Y)) - X.sum() * Y.sum()
                den = (N * float(np.dot(X, X)) - X.sum() ** 2) * (N * float(np.dot(Y, Y)) - Y.sum() ** 2)
                corr[lag] = num / math.sqrt(den) if den > 1e-10 else 0.0
            for p in range(cmin, cmax + 1):
                cs = sum(corr[lag] * math.cos(2.0 * math.pi * float(lag) / float(p)) for lag in range(3, cmax + 1))
                sn = sum(corr[lag] * math.sin(2.0 * math.pi * float(lag) / float(p)) for lag in range(3, cmax + 1))
                sp[p] = 0.2 * (cs * cs + sn * sn) ** 2 + 0.8 * sp[p]
            agc = max([agc * 0.995] + list(sp.values()))
            npw = {p: (sp[p] / agc if agc > 1e-10 else 0.0) for p in sp}
            pp, prim = 0.0, cmin
            for p in range(cmin, cmax + 1):
                if npw[p] > pp:
                    pp, prim = npw[p], p
            pk = float(prim); edge = prim in (cmin, cmax)
            sig = [p for p in npw if npw[p] >= 0.5]
            ws = sum(npw[p] for p in sig)
            cg = sum(p * npw[p] for p in sig) / ws if ws > 1e-10 else NA
            sec = 0.0
            for p in range(cmin, cmax + 1):
                if p != prim and (p == cmin or npw[p] > npw[p - 1]) and (p == cmax or npw[p] > npw[p + 1]):
                    sec = max(sec, npw[p])
            dom = max(0.0, min(1.0, (pp - sec) / pp)) if pp > 1e-10 else 0.0
            dist = abs(cg - pk) if not isna(cg) else NA
        ready = not isna(cg) and not isna(pk)
        if ready:
            if dom >= 0.2 and (not isna(dist) and dist <= 3.0) and not edge:
                cyc, inv = cg, 0
            else:
                inv += 1
                if inv > 20:
                    cyc = NA
        sc = cyc * cmult if not isna(cyc) else NA
        sml = (sc if isna(sml) else 0.9 * sml + (1.0 - 0.9) * sc) if not isna(sc) else NA
        res = max(2.0, min(252.0, sml)) if not isna(sml) else 14.0
        lb = max(2, min(252, int(math.floor(res + 0.5))))
        lbs[i] = lb
        if i >= lb:
            ch = [src[k] - src[k - 1] for k in range(i - lb + 1, i + 1)]
            ps = sum(x if x >= 0 else 0.0 for x in ch)
            ns = sum(0.0 if x >= 0 else -x for x in ch)
            tot = ps + ns
            if tot > 1e-10:
                raw = 100.0 * (ps - ns) / tot
                strength = 0.0
                if not isna(pr[i]):
                    nr = max(0.0, min(1.0, (pr[i] - 25.0) / 30.0))
                    strength = 1.0 - nr * nr * (3.0 - 2.0 * nr)
                adj = raw * (1.0 - strength * (1.0 - 0.3))
                state = adj if isna(state) else state + 0.5 * (adj - state)
                out[i] = state
    return out, lbs


# ─────────────────────────────────────────────────────────────────────────────
def timeit(fn, reps=5):
    best = float("inf")
    for _ in range(reps):
        t = time.perf_counter()
        r = fn()
        best = min(best, time.perf_counter() - t)
    return best, r


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bars", type=int, default=30000)
    ap.add_argument("--seed", type=int, default=7)
    ap.add_argument("--ref-bars", type=int, default=4000)
    a = ap.parse_args()
    tmp = tempfile.mkdtemp(prefix="thecc_smoke_")

    # 1) synthetic CSV -> load_tv_csv
    path = os.path.join(tmp, "synthetic.csv")
    syn = make_synthetic(a.bars, a.seed)
    shuffled = pd.concat([syn, syn.iloc[100:110]]).sample(frac=1.0, random_state=1)  # dup + unsorted
    shuffled.to_csv(path, index=False)
    df = E.load_tv_csv(path)
    assert len(df) == a.bars and df["time"].is_monotonic_increasing
    print(f"[data] {path}: {len(df)} bars, ET {df['et'].iloc[0]} .. {df['et'].iloc[-1]}")
    o, h, l, c = E._ohlc(df)

    # 2) JIT warm-up
    t = time.perf_counter()
    res, ind = E.run_thecc(df.iloc[:1000])
    print(f"[jit] first call (compile or cache load): {time.perf_counter() - t:.2f}s")

    # 3) timings on N bars and on 100k bars
    big = make_synthetic(100_000, a.seed + 1)
    bo, bh, bl, bc = E._ohlc(big)
    for label, (O, H, L, C) in ((f"{len(df)} bars", (o, h, l, c)), ("100k bars", (bo, bh, bl, bc))):
        ts, (tl, cd, eb) = timeit(lambda: E.supertrend(O, H, L, C, 50, 1.0, 0.5), 3)
        tm, fm = timeit(lambda: E.mom(H, H, L, C), 3)
        tsim, res = timeit(lambda: E.simulate(O, H, L, C, tl, cd, fm), 50)
        tsim2, _ = timeit(lambda: E._simulate(O, H, L, C, tl, cd, fm, 3, 0, 20, 0.0, 1.5, False, True), 50)
        tst, _ = timeit(lambda: E.stats(res), 20)
        print(f"[time {label}] supertrend {ts*1e3:.1f} ms | mom {tm*1e3:.1f} ms | "
              f"simulate {tsim*1e3:.2f} ms (raw core {tsim2*1e3:.2f} ms) | stats {tst*1e3:.2f} ms | "
              f"closed trades {len(res['R'])}")

    # 4) grid search timing (on the N-bar set)
    t = time.perf_counter()
    g = E.grid_search(df, st_grid=[(50, 1.0, 0.5), (34, 1.5, 0.3)], mom_grid=[("high", 20, 0.8), ("close", 34, 1.1)],
                      conf_wins=[1, 2, 3, 5], sl_modes=["swing", "candle", "st"], swing_lens=[5, 10, 20, 40],
                      rrs=[1.0, 1.5, 2.0, 3.0], exit_modes=["wick", "close"])
    dt = time.perf_counter() - t
    print(f"[grid] {len(g)} combos (4 indicator sets) in {dt:.2f}s ({dt / max(len(g), 1) * 1e3:.2f} ms/combo incl. stats)")

    # 5) default THECC run on the N-bar synthetic set
    res, ind = E.run_thecc(df)
    tdf = E.trades_df(res, df)
    print(f"[run] flips {int((np.diff(ind['cdir']) != 0).sum())}, BUY {int((res['signals'] == 1).sum())}, "
          f"SELL {int((res['signals'] == -1).sum())}, closed {len(tdf)}, open {res['open']}")
    print("[trades head]\n" + tdf.head(5).to_string())
    st = E.stats(tdf)
    print("[stats all]", {k: (round(v, 4) if isinstance(v, float) else v) for k, v in st.items()})
    st500 = E.stats(tdf, last_n=500)
    print("[stats last 500]", {k: (round(v, 4) if isinstance(v, float) else v) for k, v in st500.items()})

    # 6) cross-check vs independent plain-Python reference on the first ref_bars bars
    m = a.ref_bars
    so, sh, sl_, sc = o[:m], h[:m], l[:m], c[:m]
    rt, rc, re_ = ref_supertrend(list(so), list(sh), list(sl_), list(sc), 50, 1.0, 0.5)
    et, ec, ee = E.supertrend(so, sh, sl_, sc, 50, 1.0, 0.5)
    st_ok = np.array_equal(rc, ec) and np.allclose(rt, et, rtol=0, atol=0, equal_nan=True) and np.array_equal(re_, ee)
    rm, rl = ref_mom(sh, sh, sl_, sc)
    em, el, _, _ = E.mom(sh, sh, sl_, sc, full=True)
    both = ~np.isnan(rm) & ~np.isnan(em)
    mom_na_ok = np.array_equal(np.isnan(rm), np.isnan(em))
    mom_maxrel = float(np.max(np.abs(rm[both] - em[both]) / np.maximum(np.abs(rm[both]), 1e-12))) if both.any() else 0.0
    lb_ok = np.array_equal(rl, el)
    print(f"[ref] supertrend exact: {st_ok} | mom na-pattern equal: {mom_na_ok}, lookback equal: {lb_ok}, "
          f"max rel diff {mom_maxrel:.2e} (lookback distinct values {sorted(set(el.tolist()))[:12]})")
    sim_ok = True
    for cw, slm, sw, rr, ex, co in [(3, "swing", 20, 1.5, "wick", True), (1, "candle", 20, 2.0, "close", True),
                                    (5, "st", 20, 1.0, "wick", False), (2, "swing", 5, 3.0, "close", False)]:
        rtr, rsig = ref_simulate(so, sh, sl_, sc, et, ec, em, cw, slm, sw, 0.5, rr, ex, co)
        er = E.simulate(so, sh, sl_, sc, et, ec, em, cw, slm, sw, 0.5, rr, ex, co)
        etr = list(zip(er["entry_idx"].tolist(), er["exit_idx"].tolist(), er["dir"].tolist(),
                       er["R"].tolist(), er["exit_reason"].tolist()))
        ok = etr == rtr and np.array_equal(rsig, er["signals"])
        sim_ok &= ok
        print(f"[ref] simulate conf={cw} sl={slm} sw={sw} rr={rr} exit={ex} opp={co}: "
              f"{len(etr)} trades, identical={ok}")

    # 7) parity.py round trip: write a fake export carrying engine plot columns
    exp = df[E.BASE_COLS].copy()
    flip = np.r_[False, np.diff(ind["cdir"]) != 0]
    exp["Supertrend"] = ind["tlin"]
    exp["Dot"] = np.where(flip, ind["tlin"], np.nan)
    exp["Momentum"] = ind["mom"]
    exp["THECC BUY"] = np.where(res["signals"] == 1, 1.0, np.nan)
    exp["THECC SELL"] = np.where(res["signals"] == -1, 1.0, np.nan)
    ppath = os.path.join(tmp, "fake_export.csv")
    exp.to_csv(ppath, index=False, float_format="%.10g")
    print("[parity round trip on engine-generated columns, expect 0 mismatches]")
    out = parity.run(ppath, show=3)
    ok_all = st_ok and mom_na_ok and lb_ok and mom_maxrel < 1e-9 and sim_ok and sum(out.values()) == 0
    print("SMOKE TEST", "PASSED" if ok_all else "FAILED")
    return 0 if ok_all else 1


if __name__ == "__main__":
    raise SystemExit(main())
