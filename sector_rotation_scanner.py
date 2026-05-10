#!/usr/bin/env python3
"""
Sector Rotation Scanner — daily, run after fetch_data.py (4:45 PM IST).

Reads peer_groups.json (built monthly by tools/peer_group_builder.py) and
OHLC data from market.db to produce two signals per peer group:

  Signal A — Group RS trend:  avg RS of group vs 20 trading days ago
  Signal B — Individual rank: RS rank within group vs 20 trading days ago

High-conviction = stock is in ROTATING IN group AND is a RISING LEADER.

Output: sector_rotation_scans/sector_rotation_latest.md
"""

import json
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path

_LABELS_FILE = Path(__file__).parent / "tools" / "stock_labels.json"
_LABELS: dict = json.loads(_LABELS_FILE.read_text(encoding="utf-8")) if _LABELS_FILE.exists() else {}

import pandas as pd

sys.stdout.reconfigure(encoding="utf-8")

REPO_DIR     = Path(__file__).parent
SCANS_DIR    = REPO_DIR / "sector_rotation_scans"
GROUPS_FILE  = REPO_DIR / "peer_groups.json"
MD_FILE      = SCANS_DIR / "sector_rotation_latest.md"
TODAY        = datetime.now().strftime("%Y-%m-%d")

BENCHMARK    = "NIFTY MIDSML 400"
LOOKBACK     = 60    # trading days of history needed
WINDOW       = 20   # 4 calendar weeks ≈ 20 trading days

ROT_IN_PCT   = 0.08  # group avg RS up ≥ 8% over WINDOW bars → Rotating In
ROT_OUT_PCT  = 0.08  # group avg RS down ≥ 8% → Rotating Out
RANK_RISE    = 1     # rank improved by ≥ N places → Rising Leader
RANK_FALL    = 1     # rank dropped by ≥ N places → Falling Laggard
MIN_GROUP    = 3     # skip groups smaller than this (too few to rank)
ZL_TURN_CAP  = 60   # cap ZL days lookback
ZL_CLUSTER_WINDOW = 2   # bars — turns within ±N bars = "cluster"
ZL_CLUSTER_MIN    = 2   # min members turning together to flag a cluster
ZL_BREADTH_MIN    = 0.40  # only show groups with ≥40% ZL rising in breadth table

sys.path.insert(0, str(REPO_DIR))
from ohlc_db import load_ohlc, load_ohlc_many


# ── ZL helpers ─────────────────────────────────────────────────────────────────

def _ema(s: pd.Series, n: int) -> pd.Series:
    return s.ewm(span=n, adjust=False).mean()

def _zlema25(s: pd.Series) -> pd.Series:
    e = _ema(s, 25)
    return 2 * e - _ema(e, 25)

def _zl25_turn_stats(zl25: pd.Series, closes: pd.Series) -> tuple[int, float]:
    """Return (bars_since_last_turn_up, pct_gain_since_turn)."""
    n     = len(zl25)
    limit = max(2, n - ZL_TURN_CAP)
    for i in range(n - 1, limit - 1, -1):
        if zl25.iloc[i] > zl25.iloc[i - 1] and zl25.iloc[i - 1] <= zl25.iloc[i - 2]:
            bars = (n - 1) - i + 1
            pct  = (closes.iloc[-1] / closes.iloc[i - 1] - 1) * 100
            return bars, round(pct, 2)
    cap_idx = max(0, n - ZL_TURN_CAP)
    return ZL_TURN_CAP, round((closes.iloc[-1] / closes.iloc[cap_idx] - 1) * 100, 2)


# ── RS helpers ─────────────────────────────────────────────────────────────────

def compute_rs(stock_df: pd.DataFrame, bm_df: pd.DataFrame) -> pd.Series:
    """
    Return RS series (stock_close / benchmark_close * 1000), date-aligned.
    Date is the index.
    """
    s = stock_df.set_index("date")["close"]
    b = bm_df.set_index("date")["close"]
    aligned = pd.concat([s, b], axis=1, join="inner")
    aligned.columns = ["stock", "bm"]
    return (aligned["stock"] / aligned["bm"] * 1000).rename("rs")


def rs_at(rs: pd.Series, bars_back: int) -> float | None:
    """Return RS value bars_back positions from end. None if not enough history."""
    if len(rs) <= bars_back:
        return None
    return float(rs.iloc[-(bars_back + 1)])


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    SCANS_DIR.mkdir(exist_ok=True)

    if not GROUPS_FILE.exists():
        print(f"ERROR: {GROUPS_FILE} not found. Run tools/peer_group_builder.py first.")
        return 1

    groups_data = json.loads(GROUPS_FILE.read_text(encoding="utf-8"))
    groups      = groups_data["groups"]
    sym_to_grp  = groups_data["stock_to_group"]

    # Only non-singleton groups with enough members
    active_groups = {
        gid: g for gid, g in groups.items()
        if g["size"] >= MIN_GROUP and not gid.startswith("singleton_")
    }
    print(f"Peer groups: {len(groups)} total, {len(active_groups)} with >= {MIN_GROUP} members")

    all_symbols = list({sym for g in active_groups.values() for sym in g["members"]})
    all_symbols_with_bm = all_symbols + [BENCHMARK]

    print(f"Loading OHLC for {len(all_symbols)} stocks + benchmark...")
    ohlc = load_ohlc_many(all_symbols_with_bm, lookback=LOOKBACK)

    bm_df = ohlc.get(BENCHMARK)
    if bm_df is None or bm_df.empty:
        print("ERROR: Benchmark not in DB. Run fetch_data.py first.")
        return 1

    # Compute RS for each stock
    print("Computing RS lines...")
    rs_map: dict[str, pd.Series] = {}
    for sym in all_symbols:
        df = ohlc.get(sym)
        if df is not None and not df.empty:
            try:
                rs_map[sym] = compute_rs(df, bm_df)
            except Exception:
                pass

    # Compute ZL stats for each stock
    print("Computing ZL stats...")
    zl_map: dict[str, dict] = {}   # sym -> {rising, days, pct, turn_bar_idx}
    for sym in all_symbols:
        df = ohlc.get(sym)
        if df is None or len(df) < 30:
            continue
        try:
            c     = df["close"].astype(float)
            zl25  = _zlema25(c)
            rising = bool(zl25.iloc[-1] > zl25.iloc[-2])
            days, pct = _zl25_turn_stats(zl25, c)
            # find the bar index (from series end) of the last turn-up
            n = len(zl25)
            turn_bar = None
            limit = max(2, n - ZL_TURN_CAP)
            for i in range(n - 1, limit - 1, -1):
                if zl25.iloc[i] > zl25.iloc[i - 1] and zl25.iloc[i - 1] <= zl25.iloc[i - 2]:
                    turn_bar = (n - 1) - i   # bars ago
                    break
            zl_map[sym] = {"rising": rising, "days": days, "pct": pct, "turn_bar": turn_bar}
        except Exception:
            pass

    # ── Signals ────────────────────────────────────────────────────────────────

    rot_in:     list[dict] = []
    rot_out:    list[dict] = []
    high_conv:  list[dict] = []
    zl_breadth: list[dict] = []

    for gid, group in active_groups.items():
        members    = group["members"]
        label      = group["label"]
        valid_syms = [s for s in members if s in rs_map]

        if len(valid_syms) < MIN_GROUP:
            continue

        # Latest RS per member and RS 20 days ago
        rs_now  = {}
        rs_past = {}
        for sym in valid_syms:
            rs = rs_map[sym]
            if len(rs) < 2:
                continue
            rs_now[sym]  = float(rs.iloc[-1])
            past         = rs_at(rs, WINDOW)
            if past is not None:
                rs_past[sym] = past

        if not rs_now:
            continue

        # ── Signal A: group avg RS trend ────────────────────────────────────
        avg_rs_now  = sum(rs_now.values()) / len(rs_now)
        past_syms   = [s for s in rs_now if s in rs_past]
        avg_rs_past = (sum(rs_past[s] for s in past_syms) / len(past_syms)) if past_syms else None
        rs_chg_pct  = ((avg_rs_now / avg_rs_past) - 1) if avg_rs_past else None

        is_rot_in  = rs_chg_pct is not None and rs_chg_pct >= ROT_IN_PCT
        is_rot_out = rs_chg_pct is not None and rs_chg_pct <= -ROT_OUT_PCT

        # ── Signal B: individual RS rank within group ─────────────────────
        rank_now  = {sym: rank for rank, sym in enumerate(
            sorted(rs_now, key=rs_now.__getitem__, reverse=True), start=1
        )}
        rank_past = {sym: rank for rank, sym in enumerate(
            sorted(rs_past, key=rs_past.__getitem__, reverse=True), start=1
        ) if sym in rs_past} if rs_past else {}

        leaders  = []
        laggards = []
        for sym in valid_syms:
            rn = rank_now.get(sym)
            rp = rank_past.get(sym)
            if rn is None or rp is None:
                continue
            improvement = rp - rn  # positive = improved rank
            if improvement >= RANK_RISE:
                leaders.append((sym, rn, rp, improvement))
            elif improvement <= -RANK_FALL:
                laggards.append((sym, rn, rp, improvement))

        leaders.sort(key=lambda x: x[1])    # best rank first
        laggards.sort(key=lambda x: x[1], reverse=True)

        # ── ZL Breadth + Cluster ─────────────────────────────────────────────
        zl_members   = [s for s in valid_syms if s in zl_map]
        zl_rising_syms = [s for s in zl_members if zl_map[s]["rising"]]
        breadth_pct  = len(zl_rising_syms) / len(zl_members) if zl_members else 0.0
        avg_zl_days  = (sum(zl_map[s]["days"] for s in zl_rising_syms) / len(zl_rising_syms)
                        if zl_rising_syms else None)
        avg_zl_pct   = (sum(zl_map[s]["pct"]  for s in zl_rising_syms) / len(zl_rising_syms)
                        if zl_rising_syms else None)

        # Cluster: find turn_bar values for rising members that just turned (turn_bar < ZL_TURN_CAP)
        recent_turns = [(s, zl_map[s]["turn_bar"]) for s in zl_rising_syms
                        if zl_map[s]["turn_bar"] is not None and zl_map[s]["turn_bar"] < ZL_TURN_CAP]
        cluster_syms: list[str] = []
        if len(recent_turns) >= ZL_CLUSTER_MIN:
            # group by proximity: any two turns within ZL_CLUSTER_WINDOW bars of each other
            recent_turns.sort(key=lambda x: x[1])
            best_cluster: list[str] = []
            for j in range(len(recent_turns)):
                anchor = recent_turns[j][1]
                group_j = [s for s, tb in recent_turns if abs(tb - anchor) <= ZL_CLUSTER_WINDOW]
                if len(group_j) > len(best_cluster):
                    best_cluster = group_j
            if len(best_cluster) >= ZL_CLUSTER_MIN:
                cluster_syms = best_cluster

        if breadth_pct >= ZL_BREADTH_MIN and zl_members:
            zl_breadth.append({
                "gid":          gid,
                "label":        label,
                "size":         len(valid_syms),
                "zl_count":     len(zl_rising_syms),
                "zl_total":     len(zl_members),
                "breadth_pct":  breadth_pct,
                "avg_zl_days":  avg_zl_days,
                "avg_zl_pct":   avg_zl_pct,
                "cluster_syms": cluster_syms,
                "rising_syms":  zl_rising_syms,
            })

        chg_str = f"{rs_chg_pct * 100:+.1f}%" if rs_chg_pct is not None else "n/a"
        grp_entry = {
            "gid":        gid,
            "label":      label,
            "size":       len(valid_syms),
            "rs_chg_pct": rs_chg_pct,
            "chg_str":    chg_str,
            "leaders":    leaders,
            "laggards":   laggards,
            "top_by_rs":  sorted(rs_now, key=rs_now.__getitem__, reverse=True)[:5],
        }

        if is_rot_in:
            rot_in.append(grp_entry)
            for sym, rn, rp, imp in leaders:
                high_conv.append({
                    "symbol":    sym,
                    "group":     label,
                    "rank_now":  rn,
                    "rank_past": rp,
                    "rs_chg":    chg_str,
                    "group_size": len(valid_syms),
                })
        elif is_rot_out:
            rot_out.append(grp_entry)

    # Sort by magnitude of RS change
    rot_in.sort(key=lambda x: x["rs_chg_pct"] or 0, reverse=True)
    rot_out.sort(key=lambda x: x["rs_chg_pct"] or 0)
    high_conv.sort(key=lambda x: x["rank_now"])
    # ZL breadth: cluster groups first, then by breadth % desc
    zl_breadth.sort(key=lambda x: (-len(x["cluster_syms"]), -x["breadth_pct"]))

    # ── Markdown output ────────────────────────────────────────────────────────
    lines = [
        f"# Sector Rotation — {TODAY}",
        "",
        f"Universe: {len(all_symbols)} stocks  |  "
        f"Active groups: {len(active_groups)}  |  "
        f"Rotating In: {len(rot_in)}  |  Rotating Out: {len(rot_out)}",
        "",
    ]

    # High-conviction
    if high_conv:
        lines += [
            "## High-Conviction (Rotating Group + Rising Leader)",
            "",
            "| Symbol | Label | Peer Group | RS Rank (now / 4w ago) | Group RS 4W |",
            "|--------|-------|-----------|------------------------|-------------|",
        ]
        for h in high_conv:
            lbl = _LABELS.get(h["symbol"], "")
            lines.append(
                f"| **{h['symbol']}** | {lbl} | {h['group']} "
                f"| {h['rank_now']} / {h['rank_past']} of {h['group_size']} "
                f"| {h['rs_chg']} |"
            )
        lines.append("")

    # Rotating In
    if rot_in:
        lines += [
            "## Rotating In",
            "",
            "| Group | Size | RS Change (4W) | Leaders | Top by RS |",
            "|-------|------|----------------|---------|-----------|",
        ]
        for g in rot_in:
            leader_str = ", ".join(f"{s}↑" for s, _, _, _ in g["leaders"][:3]) or "—"
            top_str    = ", ".join(g["top_by_rs"][:4])
            lines.append(
                f"| {g['label']} | {g['size']} | {g['chg_str']} | {leader_str} | {top_str} |"
            )
        lines.append("")

    # Rotating Out
    if rot_out:
        lines += [
            "## Rotating Out",
            "",
            "| Group | Size | RS Change (4W) | Laggards |",
            "|-------|------|----------------|---------|",
        ]
        for g in rot_out:
            laggard_str = ", ".join(f"{s}↓" for s, _, _, _ in g["laggards"][:3]) or "—"
            lines.append(
                f"| {g['label']} | {g['size']} | {g['chg_str']} | {laggard_str} |"
            )
        lines.append("")

    if not rot_in and not rot_out:
        lines += ["*No strong rotation signals today.*", ""]

    # ZL Breadth per group
    if zl_breadth:
        lines += [
            "## ZL Breadth per Group",
            "",
            "_Groups where ≥40% of members have ZLEMA25 rising. "
            "⚡ = coordinated cluster (≥2 members turned ZL within ±2 bars)._",
            "",
            "| Group | ZL Rising | Breadth | Avg ZL Days | Avg ZL Chg% | Cluster | Members |",
            "|-------|-----------|---------|------------|-------------|---------|---------|",
        ]
        for z in zl_breadth:
            cluster_str = ", ".join(z["cluster_syms"]) if z["cluster_syms"] else "—"
            cluster_flag = "⚡ " + cluster_str if z["cluster_syms"] else "—"
            rising_str   = ", ".join(z["rising_syms"][:6])
            if len(z["rising_syms"]) > 6:
                rising_str += f" +{len(z['rising_syms']) - 6}"
            avg_days_str = f"{z['avg_zl_days']:.0f}d" if z["avg_zl_days"] is not None else "—"
            avg_pct_str  = f"{z['avg_zl_pct']:+.1f}%" if z["avg_zl_pct"] is not None else "—"
            lines.append(
                f"| {z['label']} "
                f"| {z['zl_count']}/{z['zl_total']} "
                f"| {z['breadth_pct'] * 100:.0f}% "
                f"| {avg_days_str} "
                f"| {avg_pct_str} "
                f"| {cluster_flag} "
                f"| {rising_str} |"
            )
        lines.append("")
    else:
        lines += ["## ZL Breadth per Group", "", "*No groups with ≥40% ZL rising today.*", ""]

    md = "\n".join(lines)
    MD_FILE.write_text(md, encoding="utf-8")
    dated_file = SCANS_DIR / f"sector_rotation_{TODAY}.md"
    dated_file.write_text(md, encoding="utf-8")
    print(f"Written: {MD_FILE}  +  {dated_file.name}")
    print(f"  Rotating In:  {len(rot_in)} groups")
    print(f"  Rotating Out: {len(rot_out)} groups")
    print(f"  High-conviction: {len(high_conv)} stocks")
    print(f"  ZL breadth groups: {len(zl_breadth)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
