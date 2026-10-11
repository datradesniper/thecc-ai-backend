"""
THECC Supertrend Error Cloud + MOM backtest engine.

Bar-for-bar Python/numba port of tradingview/THECC_Supertrend_MOM.pine (Pine v6).
Historical-bar semantics: barstate.isconfirmed is always true, comparisons with na are
false, nz(x) = 0 for na.

Layering (for grid searches):
    supertrend(...)  -> depends on (lngth, mult, lrate, ml_on)
    mom(...)         -> depends on (source, cycle_min, cycle_max, cycle_mult, squeeze, ...)
    simulate(...)    -> depends on (conf_win, sl_mode, swing_len, buf, rr, exit_mode, close_opp)
Compute the first two once per parameter set, then call simulate() many times.
"""
from __future__ import annotations

import math
from itertools import product
from typing import Iterable

import numpy as np
import pandas as pd
from numba import njit

BASE_COLS = ["time", "open", "high", "low", "close"]

SL_MODES = {"swing": 0, "candle": 1, "st": 2,
            "previous swing": 0, "previous candle": 1, "supertrend line": 2}
EXIT_MODES = {"wick": 0, "close": 1}
REASON_NAMES = {1: "TP", -1: "SL", 0: "opposite"}


# ════════════════════════════════════════════════════════════════════════════
# Data loading
# ════════════════════════════════════════════════════════════════════════════
def load_tv_csv(path: str, tz: str = "America/New_York") -> pd.DataFrame:
    """Load a TradingView 'Export chart data' CSV.

    Returns a DataFrame sorted by time, de-duplicated on time (last row wins),
    with time/open/high/low/close first, any extra plot columns after, and an
    `et` column (tz-aware timestamp of bar open in `tz`).
    """
    df = pd.read_csv(path)
    df.columns = [str(c).strip() for c in df.columns]
    lower = {c.lower(): c for c in df.columns}
    ren = {lower[c]: c for c in BASE_COLS if c in lower and lower[c] != c}
    df = df.rename(columns=ren)
    missing = [c for c in BASE_COLS if c not in df.columns]
    if missing:
        raise ValueError(f"{path}: missing columns {missing}")
    if not np.issubdtype(df["time"].dtype, np.number):
        # ISO strings (some exports) -> unix seconds
        df["time"] = pd.to_datetime(df["time"], utc=True).astype("int64") // 10**9
    df["time"] = df["time"].astype("int64")
    for c in ["open", "high", "low", "close"]:
        df[c] = pd.to_numeric(df[c], errors="coerce").astype("float64")
    df = (df.sort_values("time", kind="mergesort")
            .drop_duplicates("time", keep="last")
            .reset_index(drop=True))
    extras = [c for c in df.columns if c not in BASE_COLS]
    df = df[BASE_COLS + extras]
    df["et"] = pd.to_datetime(df["time"], unit="s", utc=True).dt.tz_convert(tz)
    return df


def source(df_or_o, h=None, l=None, c=None, name: str = "high") -> np.ndarray:
    """Pine input.source equivalents: open/high/low/close/hl2/hlc3/ohlc4/hlcc4."""
    if h is None:
        d = df_or_o
        o, h, l, c = (d["open"].to_numpy(float), d["high"].to_numpy(float),
                      d["low"].to_numpy(float), d["close"].to_numpy(float))
    else:
        o = df_or_o
    name = name.lower()
    if name == "open":
        return np.asarray(o, float)
    if name == "high":
        return np.asarray(h, float)
    if name == "low":
        return np.asarray(l, float)
    if name == "close":
        return np.asarray(c, float)
    if name == "hl2":
        return (h + l) / 2.0
    if name == "hlc3":
        return (h + l + c) / 3.0
    if name == "ohlc4":
        return (o + h + l + c) / 4.0
    if name == "hlcc4":
        return (h + l + c + c) / 4.0
    raise ValueError(name)


def _ohlc(df):
    return (np.ascontiguousarray(df["open"].to_numpy(np.float64)),
            np.ascontiguousarray(df["high"].to_numpy(np.float64)),
            np.ascontiguousarray(df["low"].to_numpy(np.float64)),
            np.ascontiguousarray(df["close"].to_numpy(np.float64)))


# ════════════════════════════════════════════════════════════════════════════
# Supertrend Error Adaptive Cloud  (supt + mlegn)
# ════════════════════════════════════════════════════════════════════════════
@njit(cache=True)
def _highest(x, length):
    n = x.shape[0]
    out = np.full(n, np.nan)
    for i in range(length - 1, n):
        m = x[i]
        for k in range(i - length + 1, i):
            if x[k] > m:
                m = x[k]
        out[i] = m
    return out


@njit(cache=True)
def _supertrend(o, h, l, c, lngth, mult, lrate, ml_on):
    n = c.shape[0]
    vrng = _highest(h - l, lngth)
    tlin = np.full(n, np.nan)
    cdir = np.zeros(n, np.int64)
    ebias_out = np.zeros(n)
    amult_out = np.zeros(n)

    prdir = 1                 # var int prdir = 1
    param_prev = 0            # nz(dirv[1]) inside mlegn (param of previous call); bar 0 -> 0
    entcl = c[0]              # var float entcl = close (bar 0)
    ebias = 0.0
    ub_prev = np.nan          # final ubnd of previous bar
    lb_prev = np.nan
    tl_prev = np.nan
    for i in range(n):
        # ---- mlegn(ml_on, mult, lrate, lngth, prdir, ...)
        dirv = prdir
        amult = mult
        if i > lngth:
            bcalc = mult * (1.0 + ebias) if ml_on else mult
            amult = bcalc if bcalc > 0.5 else 0.5
        flip = dirv != param_prev
        if flip and i > lngth:
            pdir = param_prev
            exitc = c[i - 1]
            iswin = (pdir == -1 and exitc > entcl) or (pdir == 1 and exitc < entcl)
            errs = 0.0 if iswin else 1.0
            ebias = ebias + lrate * (errs - ebias)
            entcl = c[i]
        param_prev = dirv
        ebias_out[i] = ebias
        amult_out[i] = amult

        # ---- supt(amult)
        src = (c[i] + o[i]) / 2.0
        ub = src + amult * vrng[i]
        lb = src - amult * vrng[i]
        uprev = 0.0 if np.isnan(ub_prev) else ub_prev
        lprev = 0.0 if np.isnan(lb_prev) else lb_prev
        cp = c[i - 1] if i > 0 else np.nan
        if not (lb > lprev or cp < lprev):
            lb = lprev
        if not (ub < uprev or cp > uprev):
            ub = uprev
        if i == 0 or np.isnan(vrng[i - 1]):
            d = 1
        elif tl_prev == uprev:
            d = -1 if c[i] > ub else 1
        else:
            d = 1 if c[i] < lb else -1
        tl = lb if d == -1 else ub
        tlin[i] = tl
        cdir[i] = d
        ub_prev = ub
        lb_prev = lb
        tl_prev = tl
        prdir = d
    return tlin, cdir, ebias_out, amult_out, vrng


def supertrend(o, h, l, c, lngth=50, mult=1.0, lrate=0.5, ml_on=True, full=False):
    """Supertrend Error Adaptive Cloud. Returns (tlin, cdir, ebias).

    cdir == -1 is BULL, 1 is BEAR. ebias is the value after the bar's update.
    full=True additionally returns (amult, vrng).
    """
    o, h, l, c = (np.ascontiguousarray(x, dtype=np.float64) for x in (o, h, l, c))
    tlin, cdir, ebias, amult, vrng = _supertrend(o, h, l, c, int(lngth), float(mult),
                                                  float(lrate), bool(ml_on))
    if full:
        return tlin, cdir, ebias, amult, vrng
    return tlin, cdir, ebias


# ════════════════════════════════════════════════════════════════════════════
# MOM - Adaptive Cycle Momentum Oscillator (finalMomentum only)
# ════════════════════════════════════════════════════════════════════════════
@njit(cache=True)
def _atr(h, l, c, length):
    """ta.atr = ta.rma(ta.tr(true), length); rma seeded with SMA at bar length-1."""
    n = c.shape[0]
    tr = np.empty(n)
    for i in range(n):
        if i == 0 or np.isnan(c[i - 1]):
            tr[i] = h[i] - l[i]
        else:
            a = h[i] - l[i]
            b = abs(h[i] - c[i - 1])
            d = abs(l[i] - c[i - 1])
            tr[i] = max(max(a, b), d)
    out = np.full(n, np.nan)
    alpha = 1.0 / length
    prev = np.nan
    for i in range(n):
        if np.isnan(prev):
            if i >= length - 1:
                s = 0.0
                for k in range(i - length + 1, i + 1):
                    s += tr[k]
                prev = s / length
                out[i] = prev
        else:
            prev = alpha * tr[i] + (1.0 - alpha) * prev
            out[i] = prev
    return out


@njit(cache=True)
def _mom(src, h, l, c, cmin, cmax, cmult, squeeze_on, sq_fast, sq_slow,
         adaptive, fixed_len):
    n = src.shape[0]
    pi = math.pi
    # ---------- f_pureACP: roofing filter
    hp_angle = 0.707 * 2.0 * pi / 48.0
    hp_alpha = (math.cos(hp_angle) + math.sin(hp_angle) - 1.0) / math.cos(hp_angle)
    k1 = (1.0 - hp_alpha * 0.5) ** 2.0
    k2 = 2.0 * (1.0 - hp_alpha)
    k3 = (1.0 - hp_alpha) ** 2.0
    a1 = math.exp(-1.414 * pi / 10.0)
    c2 = 2.0 * a1 * math.cos(1.414 * pi / 10.0)
    c3 = -(a1 * a1)
    c1 = 1.0 - c2 - c3
    hp = np.zeros(n)
    filt = np.zeros(n)
    for i in range(n):
        s1 = src[i - 1] if i >= 1 else 0.0
        s2 = src[i - 2] if i >= 2 else 0.0
        if np.isnan(s1):
            s1 = 0.0
        if np.isnan(s2):
            s2 = 0.0
        hp1 = hp[i - 1] if i >= 1 else 0.0
        hp2 = hp[i - 2] if i >= 2 else 0.0
        hp[i] = k1 * (src[i] - 2.0 * s1 + s2) + k2 * hp1 - k3 * hp2
        f1 = filt[i - 1] if i >= 1 else 0.0
        f2 = filt[i - 2] if i >= 2 else 0.0
        filt[i] = c1 * (hp[i] + hp1) * 0.5 + c2 * f1 + c3 * f2

    stride = cmax + 1
    cos_t = np.zeros(stride * stride)
    sin_t = np.zeros(stride * stride)
    for p in range(cmin, cmax + 1):
        for lag in range(3, cmax + 1):
            ang = 2.0 * pi * float(lag) / float(p)
            cos_t[p * stride + lag] = math.cos(ang)
            sin_t[p * stride + lag] = math.sin(ang)
    corr = np.zeros(stride)
    spow = np.zeros(stride)
    npow = np.zeros(stride)
    agc = 0.0

    # ---------- squeeze
    sq_strength = np.zeros(n)
    if squeeze_on:
        fa = _atr(h, l, c, sq_fast)
        sa = _atr(h, l, c, sq_slow)
        ratio = np.full(n, np.nan)
        for i in range(n):
            if (not np.isnan(fa[i])) and (not np.isnan(sa[i])) and sa[i] > 0.0:
                ratio[i] = fa[i] / sa[i]
        rank_len = 144
        prange = max(55.0 - 25.0, 1e-10)
        for i in range(n):
            if i < rank_len or np.isnan(ratio[i]):
                continue
            cnt = 0
            bad = False
            for k in range(1, rank_len + 1):
                v = ratio[i - k]
                if np.isnan(v):
                    bad = True
                    break
                if v <= ratio[i]:
                    cnt += 1
            if bad:
                continue
            rank = 100.0 * cnt / rank_len
            nr = max(0.0, min(1.0, (rank - 25.0) / prange))
            sr = nr * nr * (3.0 - 2.0 * nr)
            sq_strength[i] = 1.0 - sr     # nz(measuredSqueeze, 0) -> 0 elsewhere
    sq_floor_k = 1.0 - 0.30

    # ---------- momentum change series
    pos = np.zeros(n)
    neg = np.zeros(n)
    neg[0] = np.nan                     # ta.change na on bar 0 -> negativeMove = -na
    for i in range(1, n):
        ch = src[i] - src[i - 1]
        if ch >= 0.0:
            pos[i] = ch
            neg[i] = 0.0
        elif np.isnan(ch):
            pos[i] = 0.0
            neg[i] = np.nan
        else:
            pos[i] = 0.0
            neg[i] = -ch

    out = np.full(n, np.nan)
    lookback_out = np.zeros(n, np.int64)
    cycle_out = np.full(n, np.nan)

    hist_need = 2 * cmax + 2
    cycle = np.nan
    invalid = 0
    sm_len = np.nan
    state = np.nan
    smooth_k = 1.0 - 0.9
    for i in range(n):
        cg = np.nan
        peak = np.nan
        dom = 0.0
        dist = np.nan
        edge = False
        if adaptive and i >= hist_need:
            for lag in range(3, cmax + 1):
                sx = 0.0
                sy = 0.0
                sxx = 0.0
                syy = 0.0
                sxy = 0.0
                for cnt in range(lag):
                    x = filt[i - cnt]
                    y = filt[i - cnt - lag]
                    sx += x
                    sy += y
                    sxx += x * x
                    syy += y * y
                    sxy += x * y
                nn = float(lag)
                num = nn * sxy - sx * sy
                den = (nn * sxx - sx * sx) * (nn * syy - sy * sy)
                corr[lag] = num / math.sqrt(den) if den > 1e-10 else 0.0
            for p in range(cmin, cmax + 1):
                cp = 0.0
                sp = 0.0
                for lag in range(3, cmax + 1):
                    cr = corr[lag]
                    cp += cr * cos_t[p * stride + lag]
                    sp += cr * sin_t[p * stride + lag]
                ms = cp * cp + sp * sp
                raw = ms * ms
                spow[p] = 0.2 * raw + (1.0 - 0.2) * spow[p]
            agc = agc * 0.995
            for p in range(cmin, cmax + 1):
                agc = max(agc, spow[p])
            pk_pow = 0.0
            prim = cmin
            for p in range(cmin, cmax + 1):
                nv = spow[p] / agc if agc > 1e-10 else 0.0
                npow[p] = nv
                if nv > pk_pow:
                    pk_pow = nv
                    prim = p
            peak = float(prim)
            edge = prim == cmin or prim == cmax
            wp = 0.0
            ws = 0.0
            for p in range(cmin, cmax + 1):
                pw = npow[p]
                if pw >= 0.5:
                    wp += float(p) * pw
                    ws += pw
            cg = wp / ws if ws > 1e-10 else np.nan
            sec = 0.0
            for p in range(cmin, cmax + 1):
                if p != prim:
                    cur = npow[p]
                    gl = p == cmin or cur > npow[p - 1]
                    gr = p == cmax or cur > npow[p + 1]
                    if gl and gr:
                        sec = max(sec, cur)
            dom = max(0.0, min(1.0, (pk_pow - sec) / pk_pow)) if pk_pow > 1e-10 else 0.0
            dist = abs(cg - peak) if not np.isnan(cg) else np.nan

        # ---------- cycle engine
        if adaptive:
            ready = (not np.isnan(cg)) and (not np.isnan(peak))
            valid = ready and dom >= 0.20 and ((not np.isnan(dist)) and dist <= 3.0) and (not edge)
            if ready:
                if valid:
                    cycle = cg
                    invalid = 0
                else:
                    invalid += 1
                    if invalid > 20:
                        cycle = np.nan
            scaled = cycle * cmult if not np.isnan(cycle) else np.nan
            if np.isnan(scaled):
                sm_len = np.nan
            elif np.isnan(sm_len):
                sm_len = scaled
            else:
                sm_len = 0.9 * sm_len + smooth_k * scaled
            if not np.isnan(sm_len):
                resolved = max(2.0, min(252.0, sm_len))
            else:
                resolved = 14.0
            lb = int(math.floor(resolved + 0.5))   # math.round (half away from zero), resolved > 0
            lb = max(2, min(252, lb))
            cycle_out[i] = cycle
        else:
            lb = fixed_len
        lookback_out[i] = lb

        # ---------- momentum
        mom_def = False
        raw_m = np.nan
        if i - lb + 1 >= 0:
            ps = 0.0
            ns = 0.0
            for k in range(i - lb + 1, i + 1):
                ps += pos[k]
                ns += neg[k]
            tot = ps + ns
            if (not np.isnan(tot)) and tot > 1e-10:
                mom_def = True
                raw_m = 100.0 * (ps - ns) / tot
        if mom_def:
            factor = 1.0 - sq_strength[i] * sq_floor_k
            adj = raw_m * factor
            if not np.isnan(adj):
                state = adj if np.isnan(state) else state + 0.5 * (adj - state)
            if not np.isnan(state):
                out[i] = state
    return out, lookback_out, cycle_out, sq_strength


def mom(src, h, l, c, cycle_min=8, cycle_max=20, cycle_mult=0.8, squeeze_on=True,
        fast=8, slow=34, length_mode="Adaptive", fixed_len=14, full=False):
    """MOM finalMomentum. `src` is the source series (default THECC: high).

    full=True returns (finalMomentum, lookback, cyclePeriod, squeezeStrength).
    """
    src, h, l, c = (np.ascontiguousarray(x, dtype=np.float64) for x in (src, h, l, c))
    adaptive = str(length_mode).lower() == "adaptive"
    if adaptive and cycle_min >= cycle_max:
        raise ValueError("cycle_min must be < cycle_max")
    if squeeze_on and fast >= slow:
        raise ValueError("fast ATR must be < slow ATR")
    res = _mom(src, h, l, c, int(cycle_min), int(cycle_max), float(cycle_mult),
               bool(squeeze_on), int(fast), int(slow), adaptive, int(fixed_len))
    return res if full else res[0]


# ════════════════════════════════════════════════════════════════════════════
# THECC signals & bracket simulation
# ════════════════════════════════════════════════════════════════════════════
@njit(cache=True)
def _simulate(o, h, l, c, tlin, cdir, mom, conf_win, sl_mode, swing_len, buf, rr,
              exit_close, close_opp):
    n = c.shape[0]
    nflip = 0
    for i in range(1, n):
        if cdir[i] != cdir[i - 1]:
            nflip += 1
    cap = nflip + 1
    e_idx = np.empty(cap, np.int64)
    x_idx = np.empty(cap, np.int64)
    t_dir = np.empty(cap, np.int64)
    e_px = np.empty(cap)
    t_sl = np.empty(cap)
    t_tp = np.empty(cap)
    x_px = np.empty(cap)
    t_r = np.empty(cap)
    reason = np.empty(cap, np.int64)
    sig = np.zeros(n, np.int8)      # +1 newBuy, -1 newSell (THECC BUY / SELL plotshapes)

    pend_dir = 0
    pend_bar = -1
    tdir = 0
    entry = 0.0
    sl = 0.0
    tp = 0.0
    risk = 0.0
    ent_bar = -1
    k = 0
    for i in range(n):
        cd = cdir[i]
        if i > 0 and cd != cdir[i - 1]:
            pend_dir = 1 if cd == -1 else -1
            pend_bar = i
        if pend_dir != 0 and (((pend_dir == 1) != (cd == -1)) or (i - pend_bar >= conf_win)):
            pend_dir = 0
        m = mom[i]
        buy = pend_dir == 1 and m > 0.0 and c[i] > o[i]
        sell = pend_dir == -1 and m < 0.0 and c[i] < o[i]
        buy_sl = np.nan
        sell_sl = np.nan
        if buy:
            if sl_mode == 0:
                if i >= swing_len - 1:
                    v = l[i]
                    for j in range(i - swing_len + 1, i):
                        if l[j] < v:
                            v = l[j]
                    buy_sl = v - buf
            elif sl_mode == 1:
                if i > 0:
                    buy_sl = l[i - 1] - buf
            else:
                buy_sl = tlin[i] - buf
            buy = buy_sl < c[i]           # na -> false
        if sell:
            if sl_mode == 0:
                if i >= swing_len - 1:
                    v = h[i]
                    for j in range(i - swing_len + 1, i):
                        if h[j] > v:
                            v = h[j]
                    sell_sl = v + buf
            elif sl_mode == 1:
                if i > 0:
                    sell_sl = h[i - 1] + buf
            else:
                sell_sl = tlin[i] + buf
            sell = sell_sl > c[i]
        if buy or sell:
            pend_dir = 0

        # 4) SL / TP check
        if tdir != 0 and i > ent_bar:
            if exit_close:
                if tdir == 1:
                    sl_hit = c[i] <= sl
                    tp_hit = (not sl_hit) and c[i] >= tp
                else:
                    sl_hit = c[i] >= sl
                    tp_hit = (not sl_hit) and c[i] <= tp
            else:
                if tdir == 1:
                    sl_hit = l[i] <= sl
                    tp_hit = (not sl_hit) and h[i] >= tp
                else:
                    sl_hit = h[i] >= sl
                    tp_hit = (not sl_hit) and l[i] <= tp
            if sl_hit or tp_hit:
                if exit_close:
                    px = c[i]
                else:
                    px = sl if sl_hit else tp
                x_idx[k] = i
                x_px[k] = px
                t_r[k] = (px - entry) * tdir / risk
                reason[k] = -1 if sl_hit else 1
                k += 1
                tdir = 0
        # 5) opposite signal
        if tdir != 0 and close_opp and ((buy and tdir == -1) or (sell and tdir == 1)):
            x_idx[k] = i
            x_px[k] = c[i]
            t_r[k] = (c[i] - entry) * tdir / risk
            reason[k] = 0
            k += 1
            tdir = 0
        # 6) new trade
        if (buy or sell) and tdir == 0:
            tdir = 1 if buy else -1
            entry = c[i]
            sl = buy_sl if buy else sell_sl
            risk = abs(entry - sl)
            tp = entry + tdir * risk * rr
            ent_bar = i
            e_idx[k] = i
            t_dir[k] = tdir
            e_px[k] = entry
            t_sl[k] = sl
            t_tp[k] = tp
            sig[i] = tdir
    # open trade (slot k, not counted in the closed set)
    open_r = np.nan
    if tdir != 0:
        open_r = (c[n - 1] - entry) * tdir / risk
        x_idx[k] = -1
        x_px[k] = np.nan
        t_r[k] = open_r
        reason[k] = -2
    return (e_idx, x_idx, t_dir, e_px, t_sl, t_tp, x_px, t_r, reason, k, tdir, sig)


def simulate(o, h, l, c, tlin, cdir, mom, conf_win=3, sl_mode="swing", swing_len=20,
             buf=0.0, rr=1.5, exit_mode="wick", close_opp=True):
    """Run the THECC signal + bracket state machine.

    buf is in PRICE units (Pine: ticks * syminfo.mintick).
    Returns a dict of numpy arrays for CLOSED trades:
        entry_idx, exit_idx, dir, entry, sl, tp, exit_px, R, exit_reason (1=TP,-1=SL,0=opposite)
    plus 'open' (dict or None: entry_idx, dir, entry, sl, tp, R_at_last_close)
    and 'signals' (int8 array per bar: +1 THECC BUY, -1 THECC SELL, i.e. newBuy/newSell).
    """
    slm = SL_MODES[sl_mode.lower()] if isinstance(sl_mode, str) else int(sl_mode)
    exm = EXIT_MODES[exit_mode.lower()] if isinstance(exit_mode, str) else int(exit_mode)
    (e_idx, x_idx, t_dir, e_px, t_sl, t_tp, x_px, t_r, reason, k, tdir, sig) = _simulate(
        o, h, l, c, tlin, cdir, mom, int(conf_win), slm, int(swing_len), float(buf),
        float(rr), bool(exm), bool(close_opp))
    res = {
        "entry_idx": e_idx[:k], "exit_idx": x_idx[:k], "dir": t_dir[:k],
        "entry": e_px[:k], "sl": t_sl[:k], "tp": t_tp[:k], "exit_px": x_px[:k],
        "R": t_r[:k], "exit_reason": reason[:k], "signals": sig, "open": None,
    }
    if tdir != 0:
        res["open"] = {"entry_idx": int(e_idx[k]), "dir": int(t_dir[k]), "entry": float(e_px[k]),
                       "sl": float(t_sl[k]), "tp": float(t_tp[k]), "R_at_last_close": float(t_r[k])}
    return res


def trades_df(res: dict, df: pd.DataFrame | None = None) -> pd.DataFrame:
    """Closed trades from simulate() as a DataFrame (adds ET entry/exit times if df given)."""
    cols = ["entry_idx", "exit_idx", "dir", "entry", "sl", "tp", "exit_px", "R", "exit_reason"]
    t = pd.DataFrame({k: res[k] for k in cols})
    t["bars_held"] = t["exit_idx"] - t["entry_idx"]
    t["exit_name"] = t["exit_reason"].map(REASON_NAMES)
    if df is not None and "et" in df.columns and len(t):
        et = df["et"].to_numpy()
        t.insert(0, "entry_time_et", et[t["entry_idx"].to_numpy()])
        t.insert(1, "exit_time_et", et[t["exit_idx"].to_numpy()])
    return t


# ════════════════════════════════════════════════════════════════════════════
# Statistics
# ════════════════════════════════════════════════════════════════════════════
def stats(trades, last_n: int | None = None) -> dict:
    """Performance summary in R. `trades` is a trades_df() DataFrame or simulate() dict.
    last_n keeps only the most recent N closed trades (e.g. 500). Win = R > 0 (as in Pine)."""
    if isinstance(trades, dict):
        r = np.asarray(trades["R"], float)
        reason = np.asarray(trades["exit_reason"])
        d = np.asarray(trades["dir"])
        held = np.asarray(trades["exit_idx"]) - np.asarray(trades["entry_idx"])
    else:
        r = trades["R"].to_numpy(float)
        reason = trades["exit_reason"].to_numpy()
        d = trades["dir"].to_numpy()
        held = (trades["exit_idx"] - trades["entry_idx"]).to_numpy()
    if last_n is not None:
        r, reason, d, held = r[-last_n:], reason[-last_n:], d[-last_n:], held[-last_n:]
    n = len(r)
    if n == 0:
        return {"trades": 0}
    win = r > 0
    gp = r[r > 0].sum()
    gl = -r[r < 0].sum()
    eq = np.concatenate(([0.0], np.cumsum(r)))
    dd = float((np.maximum.accumulate(eq) - eq).max())
    streak = best = 0
    for w in win:
        streak = 0 if w else streak + 1
        best = max(best, streak)
    longs, shorts = d == 1, d == -1
    pct = lambda m: float(100.0 * m.sum() / n)
    return {
        "trades": n,
        "wins": int(win.sum()),
        "losses": int(n - win.sum()),
        "win_pct": float(100.0 * win.mean()),
        "net_R": float(r.sum()),
        "avg_R": float(r.mean()),
        "profit_factor": float(gp / gl) if gl > 0 else float("inf"),
        "max_dd_R": dd,
        "max_consec_losses": int(best),
        "pct_tp": pct(reason == 1),
        "pct_sl": pct(reason == -1),
        "pct_opposite": pct(reason == 0),
        "long_trades": int(longs.sum()),
        "short_trades": int(shorts.sum()),
        "long_win_pct": float(100.0 * win[longs].mean()) if longs.any() else float("nan"),
        "short_win_pct": float(100.0 * win[shorts].mean()) if shorts.any() else float("nan"),
        "avg_bars_held": float(held.mean()),
    }


# ════════════════════════════════════════════════════════════════════════════
# Convenience: full pipeline + grid search
# ════════════════════════════════════════════════════════════════════════════
THECC_DEFAULTS = dict(lngth=50, mult=1.0, lrate=0.5, ml_on=True,
                      src="high", cycle_min=8, cycle_max=20, cycle_mult=0.8,
                      squeeze_on=True, fast=8, slow=34, length_mode="Adaptive", fixed_len=14,
                      conf_win=3, sl_mode="swing", swing_len=20, buf=0.0, rr=1.5,
                      exit_mode="wick", close_opp=True)


def run_thecc(df: pd.DataFrame, **params):
    """Compute everything with THECC defaults (overridable). Returns (res, ind) where
    res is the simulate() dict and ind holds tlin/cdir/ebias/mom/lookback arrays."""
    p = {**THECC_DEFAULTS, **params}
    o, h, l, c = _ohlc(df)
    tlin, cdir, ebias = supertrend(o, h, l, c, p["lngth"], p["mult"], p["lrate"], p["ml_on"])
    fm, lbk, cyc, sq = mom(source(o, h, l, c, p["src"]), h, l, c, p["cycle_min"], p["cycle_max"],
                           p["cycle_mult"], p["squeeze_on"], p["fast"], p["slow"],
                           p["length_mode"], p["fixed_len"], full=True)
    res = simulate(o, h, l, c, tlin, cdir, fm, p["conf_win"], p["sl_mode"], p["swing_len"],
                   p["buf"], p["rr"], p["exit_mode"], p["close_opp"])
    ind = dict(tlin=tlin, cdir=cdir, ebias=ebias, mom=fm, lookback=lbk, cycle=cyc, squeeze=sq)
    return res, ind


def grid_search(df: pd.DataFrame,
                st_grid: Iterable[tuple] = ((50, 1.0, 0.5),),
                mom_grid: Iterable[tuple] = (("high", 20, 0.8),),
                conf_wins: Iterable[int] = (3,),
                sl_modes: Iterable[str] = ("swing",),
                swing_lens: Iterable[int] = (20,),
                rrs: Iterable[float] = (1.5,),
                exit_modes: Iterable[str] = ("wick",),
                buf: float = 0.0, close_opp: bool = True, last_n: int | None = None,
                min_trades: int = 1) -> pd.DataFrame:
    """Grid search. st_grid items: (lngth, mult, lrate); mom_grid items: (src, cycle_max, cycle_mult).
    Supertrend / MOM are computed once per item; simulate() runs for every remaining combo.
    swing_len is only varied for sl_mode='swing'. Returns one row per combo with stats()."""
    o, h, l, c = _ohlc(df)
    sts = {k: supertrend(o, h, l, c, *k)[:2] for k in st_grid}
    moms = {k: mom(source(o, h, l, c, k[0]), h, l, c, cycle_max=k[1], cycle_mult=k[2])
            for k in mom_grid}
    rows = []
    for (sk, (tlin, cdir)), (mk, fm) in product(sts.items(), moms.items()):
        for cw, slm, rr, ex in product(conf_wins, sl_modes, rrs, exit_modes):
            for sw in (swing_lens if slm == "swing" else (0,)):
                res = simulate(o, h, l, c, tlin, cdir, fm, cw, slm, max(sw, 1), buf, rr, ex, close_opp)
                s = stats(res, last_n)
                if s["trades"] < min_trades:
                    continue
                rows.append({"lngth": sk[0], "mult": sk[1], "lrate": sk[2], "src": mk[0],
                             "cycle_max": mk[1], "cycle_mult": mk[2], "conf_win": cw,
                             "sl_mode": slm, "swing_len": sw if slm == "swing" else None,
                             "rr": rr, "exit_mode": ex, **s})
    return pd.DataFrame(rows)
