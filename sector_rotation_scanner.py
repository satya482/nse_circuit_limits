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

sys.path.insert(0, str(REPO_DIR))
from ohlc_db import load_ohlc, load_ohlc_many


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

    # ── Signals ────────────────────────────────────────────────────────────────

    rot_in:  list[dict] = []
    rot_out: list[dict] = []
    high_conv: list[dict] = []

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
            "| Symbol | Peer Group | RS Rank (now / 4w ago) | Group RS 4W |",
            "|--------|-----------|------------------------|-------------|",
        ]
        for h in high_conv:
            lines.append(
                f"| **{h['symbol']}** | {h['group']} "
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

    md = "\n".join(lines)
    MD_FILE.write_text(md, encoding="utf-8")
    print(f"Written: {MD_FILE}")
    print(f"  Rotating In:  {len(rot_in)} groups")
    print(f"  Rotating Out: {len(rot_out)} groups")
    print(f"  High-conviction: {len(high_conv)} stocks")

    return 0


if __name__ == "__main__":
    sys.exit(main())
