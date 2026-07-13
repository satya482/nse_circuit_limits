# RS Leadership Scanner Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build `rs_leadership_scanner.py`, a standalone daily scanner that fires when a stock's Relative Performance % (vs NIFTY MIDSML 400) is non-negative AND its EMA is rising, on the day these two conditions first align together (combined cross).

**Architecture:** TV screener (reused from `rs_highline_scanner.py`) → `load_ohlc_many()` + benchmark load → pure-function signal check (`_rs_leadership_signal`) per stock → context enrichment (leadership score, RS state, ZLEMA25 direction, squeeze) → markdown output (dated + latest). PS1 runner + `run_all_scanners.ps1` + `CLAUDE.md` integration.

**Tech Stack:** Python 3.13, pandas, `tradingview_screener`, SQLite via `ohlc_db.py`, PowerShell 5.1 runner script.

## Global Constraints

- Source spec: `docs/superpowers/specs/2026-07-13-rs-leadership-scanner-design.md`
- No look-ahead bias: signal at bar N uses only bars 0..N ([[backtesting-integrity]] rule)
- All scanners read OHLCV exclusively via `load_ohlc()` / `load_ohlc_many()` from `ohlc_db.py` — never CSV/yfinance/API directly in scanner logic
- Every generated `.md` file must include the SEBI disclaimer (`SEBI_MD_HEADER` / `SEBI_MD_FOOTER` from `disclaimer.py`)
- Every scanner writes both a dated file (`*_YYYY-MM-DD.md`) and `*_latest.md`, in the same run
- Zero-result run → `*No signals.*` section, never an empty file
- Signal rank / gate constants: no existing external contract to preserve here (new scanner) — define fresh
- PowerShell script strings: ASCII only, no em dashes/curly quotes ([[pine-script-conventions]] applies repo-wide to `.ps1` too, per `CLAUDE.md`)
- Git commits in this repo: always `git commit --no-verify` (pre-commit hooks disabled here)
- Never commit `market.db`, `*.pyc`, or `.env` files
- Params: `rs_ema_long_len=9`, `rs_ema_short_len=5`, `perf_lookback=9`, `perf_smooth=5` (screenshot-saved values, not the .txt's coded defaults)
- No benchmark trend filter applied (explicit design decision, differs from screenshot's checked checkbox)

---

### Task 1: Signal logic + leadership score (pure functions, TDD)

**Files:**
- Create: `rs_leadership_scanner.py`
- Test: `tests/test_rs_leadership_scanner.py`

**Interfaces:**
- Consumes: nothing (first task, pure pandas)
- Produces:
  - `_ema(s: pd.Series, n: int) -> pd.Series`
  - `_zlema(s: pd.Series, n: int) -> pd.Series`
  - `_bb_kc_squeeze(df: pd.DataFrame) -> bool`
  - `_rs_leadership_signal(df: pd.DataFrame, bench: pd.Series) -> tuple[bool, float, float]` — `(signal, rel_perf, rel_perf_ema)`
  - `_leadership_score(df: pd.DataFrame, bench: pd.Series) -> tuple[int, str]` — `(score 0-5, rs_state)` where `rs_state` is `"strong"` / `"weak"` / `"transition"`
  - Module constants: `RS_EMA_LONG_LEN=9`, `RS_EMA_SHORT_LEN=5`, `PERF_LOOKBACK=9`, `PERF_SMOOTH=5`, `BENCH_SYM="NIFTY MIDSML 400"`

- [ ] **Step 1: Write failing tests for `_rs_leadership_signal`**

Create `tests/test_rs_leadership_scanner.py`:

```python
import os
import sys

import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import rs_leadership_scanner as m


def _df(closes, highs=None, lows=None, vols=None, start="2024-01-01"):
    n = len(closes)
    dates = pd.date_range(start, periods=n, freq="D")
    highs = highs or [c * 1.01 for c in closes]
    lows = lows or [c * 0.99 for c in closes]
    vols = vols or [1_000_000] * n
    return pd.DataFrame(
        {
            "date": dates,
            "open": closes,
            "high": highs,
            "low": lows,
            "close": closes,
            "volume": vols,
        }
    )


def _bench_series(values, start="2024-01-01"):
    n = len(values)
    dates = pd.date_range(start, periods=n, freq="D")
    return pd.Series(values, index=dates)


def test_combined_cross_fires_when_both_conditions_first_align():
    n = 40
    # Benchmark flat; stock flat then accelerates up in the last 10 bars so
    # relative performance turns positive and its EMA turns up on the same
    # recent bar, having been negative/falling before.
    stock_closes = [100.0] * 25 + [100 + i * 1.5 for i in range(1, 16)]
    bench_closes = [100.0] * n
    df = _df(stock_closes)
    bench = _bench_series(bench_closes)
    signal, rel_perf, rel_perf_ema = m._rs_leadership_signal(df, bench)
    assert isinstance(signal, bool)
    assert isinstance(rel_perf, float)
    assert isinstance(rel_perf_ema, float)


def test_no_fire_when_conditions_already_held_yesterday():
    n = 60
    # Stock has been outperforming steadily for a long stretch -- both
    # conditions are true both today and yesterday, so no fresh cross.
    stock_closes = [100 + i * 1.0 for i in range(n)]
    bench_closes = [100.0] * n
    df = _df(stock_closes)
    bench = _bench_series(bench_closes)
    signal, _, _ = m._rs_leadership_signal(df, bench)
    assert signal is False


def test_no_fire_when_only_rel_perf_positive_ema_falling():
    n = 40
    # Stock spikes hard then flattens: relative performance stays positive
    # but its EMA is falling (smoothing catching up to the spike ending).
    stock_closes = [100.0] * 20 + [100 + i * 3.0 for i in range(1, 6)] + [115.0] * 14
    bench_closes = [100.0] * n
    df = _df(stock_closes)
    bench = _bench_series(bench_closes)
    signal, rel_perf, rel_perf_ema = m._rs_leadership_signal(df, bench)
    # Whatever the state, if it fires, both conditions must actually hold today.
    if signal:
        assert rel_perf >= 0


def test_insufficient_history_returns_false():
    n = 10
    stock_closes = [100.0] * n
    bench_closes = [100.0] * n
    df = _df(stock_closes)
    bench = _bench_series(bench_closes)
    signal, rel_perf, rel_perf_ema = m._rs_leadership_signal(df, bench)
    assert signal is False
    import math
    assert math.isnan(rel_perf)
    assert math.isnan(rel_perf_ema)


if __name__ == "__main__":
    test_combined_cross_fires_when_both_conditions_first_align()
    test_no_fire_when_conditions_already_held_yesterday()
    test_no_fire_when_only_rel_perf_positive_ema_falling()
    test_insufficient_history_returns_false()
    print("OK")
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python tests/test_rs_leadership_scanner.py`
Expected: `ModuleNotFoundError: No module named 'rs_leadership_scanner'`

- [ ] **Step 3: Implement `rs_leadership_scanner.py` signal logic**

```python
#!/usr/bin/env python3
"""
NSE RS Leadership Scanner
Mirrors pine_scripts/Satya RS Relative Leadership.txt: fires when a stock's
Relative Performance % vs NIFTY MIDSML 400 is non-negative AND its EMA is
rising, on the bar these two conditions first align together (combined cross).
Run after 4:05 PM IST on trading days (after run_fetch_data.ps1).
"""

import sys
import os
import json
from math import nan, isnan
from datetime import datetime

import pandas as pd
from tradingview_screener import Query, col

from ohlc_db import load_ohlc_many, get_names, liq_tag, cmf_tag, deliv_tag
from disclaimer import SEBI_MD_HEADER, SEBI_MD_FOOTER

sys.stdout.reconfigure(encoding="utf-8")

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
SCANS_DIR = os.path.join(REPO_DIR, "rs_leadership_scans")
_LABELS_FILE = os.path.join(REPO_DIR, "tools", "stock_labels.json")

TODAY = datetime.now().strftime("%Y-%m-%d")
MD_LATEST = os.path.join(SCANS_DIR, "rs_leadership_latest.md")
MD_DATED = os.path.join(SCANS_DIR, f"rs_leadership_{TODAY}.md")

MC_LOW = 8_000 * 1_00_00_000  # 8B INR = 800 Cr
MC_HIGH = 5_00_000 * 1_00_00_000  # 5T INR = 5 lakh Cr
BENCH_SYM = "NIFTY MIDSML 400"

RS_EMA_LONG_LEN = 9
RS_EMA_SHORT_LEN = 5
PERF_LOOKBACK = 9
PERF_SMOOTH = 5


def _load_labels() -> dict:
    if not os.path.exists(_LABELS_FILE):
        return {}
    with open(_LABELS_FILE, encoding="utf-8") as fh:
        return json.loads(fh.read())


_LABELS: dict = _load_labels()


# ── Indicators ────────────────────────────────────────────────────────────────


def _ema(s: pd.Series, n: int) -> pd.Series:
    return s.ewm(span=n, adjust=False).mean()


def _zlema(s: pd.Series, n: int) -> pd.Series:
    e = _ema(s, n)
    return 2 * e - _ema(e, n)


def _bb_kc_squeeze(df: pd.DataFrame) -> bool:
    """True if BB(20,2.0,SMA) is fully inside KC(20,1.5,SMA ATR) on the last bar."""
    if len(df) < 21:
        return False
    c = df["close"].astype(float)
    h = df["high"].astype(float)
    l = df["low"].astype(float)
    bb_basis = c.rolling(20).mean()
    bb_std = c.rolling(20).std()
    bb_upper = bb_basis + 2.0 * bb_std
    bb_lower = bb_basis - 2.0 * bb_std
    tr = pd.concat([h - l, (h - c.shift(1)).abs(), (l - c.shift(1)).abs()], axis=1).max(
        axis=1
    )
    kc_atr = tr.rolling(20).mean()
    kc_basis = c.rolling(20).mean()
    kc_upper = kc_basis + 1.5 * kc_atr
    kc_lower = kc_basis - 1.5 * kc_atr
    return bool(
        bb_upper.iloc[-1] < kc_upper.iloc[-1] and bb_lower.iloc[-1] > kc_lower.iloc[-1]
    )


# ── Core signal ───────────────────────────────────────────────────────────────


def _rel_perf_series(
    stock_close: pd.Series, bench_close: pd.Series
) -> tuple[pd.Series, pd.Series]:
    """Aligned (rel_perf, rel_perf_ema) over the overlap of the two series."""
    bench_aligned = bench_close.reindex(stock_close.index)
    valid = bench_aligned.notna()
    sc = stock_close[valid]
    bc = bench_aligned[valid]
    stock_ret = sc / sc.shift(PERF_LOOKBACK)
    bench_ret = bc / bc.shift(PERF_LOOKBACK)
    rel_perf = ((stock_ret / bench_ret) - 1) * 100
    rel_perf_ema = rel_perf.ewm(span=PERF_SMOOTH, adjust=False).mean()
    return rel_perf, rel_perf_ema


def _rs_leadership_signal(
    df: pd.DataFrame, bench: pd.Series
) -> tuple[bool, float, float]:
    """
    (signal, rel_perf_today, rel_perf_ema_today)

    signal = combined cross: (rel_perf>=0 AND rel_perf_ema rising) true today,
    NOT both true yesterday. Returns (False, nan, nan) on insufficient data.
    """
    min_bars = PERF_LOOKBACK + PERF_SMOOTH + 3
    if len(df) < min_bars:
        return False, nan, nan

    stock_close = df.set_index("date")["close"].astype(float)
    rel_perf, rel_perf_ema = _rel_perf_series(stock_close, bench)

    valid_count = rel_perf_ema.notna().sum()
    if valid_count < 3:
        return False, nan, nan

    rel_perf = rel_perf.dropna()
    rel_perf_ema = rel_perf_ema.dropna()
    if len(rel_perf) < 2 or len(rel_perf_ema) < 2:
        return False, nan, nan

    perf_positive = rel_perf >= 0
    ema_rising = rel_perf_ema > rel_perf_ema.shift(1)

    if len(ema_rising.dropna()) < 2:
        return False, nan, nan

    combined = perf_positive & ema_rising
    combined = combined.dropna()
    if len(combined) < 2:
        return False, nan, nan

    combined_today = bool(combined.iloc[-1])
    combined_yesterday = bool(combined.iloc[-2])
    signal = combined_today and not combined_yesterday

    return signal, round(float(rel_perf.iloc[-1]), 2), round(float(rel_perf_ema.iloc[-1]), 2)


def _leadership_score(df: pd.DataFrame, bench: pd.Series) -> tuple[int, str]:
    """(score 0-5, rs_state) mirroring the .txt's leadershipScore formula."""
    if len(df) < RS_EMA_LONG_LEN + 3:
        return 0, "weak"

    stock_close = df.set_index("date")["close"].astype(float)
    bench_aligned = bench.reindex(stock_close.index)
    valid = bench_aligned.notna()
    if valid.sum() < RS_EMA_LONG_LEN + 3:
        return 0, "weak"

    sc = stock_close[valid]
    bc = bench_aligned[valid]
    rs_line = (sc / bc) * 1000
    rs_ema_long = _ema(rs_line, RS_EMA_LONG_LEN)
    rs_ema_short = _ema(rs_line, RS_EMA_SHORT_LEN)

    rel_perf, _ = _rel_perf_series(stock_close, bench)
    rel_perf = rel_perf.reindex(rs_line.index)

    rs_above_ema = bool(rs_line.iloc[-1] > rs_ema_long.iloc[-1])
    short_rs_bullish = bool(rs_ema_short.iloc[-1] > rs_ema_long.iloc[-1])
    rs_ema_rising = bool(rs_ema_long.iloc[-1] > rs_ema_long.iloc[-2])
    outperforming = bool(rel_perf.iloc[-1] > 0) if not pd.isna(rel_perf.iloc[-1]) else False
    performance_rising = (
        bool(rel_perf.iloc[-1] > rel_perf.iloc[-2])
        if not pd.isna(rel_perf.iloc[-1]) and not pd.isna(rel_perf.iloc[-2])
        else False
    )

    score = sum(
        [rs_above_ema, short_rs_bullish, rs_ema_rising, outperforming, performance_rising]
    )

    now_strong = rs_above_ema
    was_strong = bool(rs_line.iloc[-2] > rs_ema_long.iloc[-2])
    if now_strong and not was_strong:
        rs_state = "transition"
    elif now_strong:
        rs_state = "strong"
    else:
        rs_state = "weak"

    return score, rs_state
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python tests/test_rs_leadership_scanner.py`
Expected: `OK` printed, exit code 0

- [ ] **Step 5: Commit**

```bash
git add rs_leadership_scanner.py tests/test_rs_leadership_scanner.py
git commit --no-verify -m "$(cat <<'EOF'
feat: RS leadership scanner signal logic

Combined cross of RelPerf%>=0 and its EMA rising, vs NIFTY MIDSML 400.
Mirrors pine_scripts/Satya RS Relative Leadership.txt.
EOF
)"
```

---

### Task 2: Watchlist, per-stock analysis, markdown output, main()

**Files:**
- Modify: `rs_leadership_scanner.py` (append to file from Task 1)

**Interfaces:**
- Consumes: `_rs_leadership_signal`, `_leadership_score`, `_zlema`, `_bb_kc_squeeze`, `BENCH_SYM`, `MD_LATEST`, `MD_DATED`, `SCANS_DIR` from Task 1
- Produces:
  - `get_watchlist() -> list[str]`
  - `get_circuit_limits() -> dict[str, tuple[str, str]]`
  - `analyse(symbol: str, df: pd.DataFrame, bench: pd.Series | None) -> dict | None`
  - `build_markdown(findings: list[dict], circuit: dict, names: dict[str, str]) -> str`
  - `main() -> None`

- [ ] **Step 1: Append watchlist + circuit limits helpers**

Append to `rs_leadership_scanner.py`:

```python
# ── Watchlist ─────────────────────────────────────────────────────────────────


def get_watchlist() -> list[str]:
    """TV screener: NSE common equity passing price/MCap/EMA/notional filters.
    Same filters as rs_highline_scanner.get_watchlist()."""
    _, df = (
        Query()
        .set_markets("india")
        .select("name", "close", "market_cap_basic", "Perf.W")
        .where(
            col("exchange") == "NSE",
            col("type") == "stock",
            col("typespecs").has(["common"]),
            col("close") > 20,
            col("Perf.W") > 3,
            col("market_cap_basic").between(MC_LOW, MC_HIGH),
            col("close") > col("EMA10"),
            col("close") > col("EMA20"),
            col("Value.Traded") > 200e6,
        )
        .limit(2000)
        .get_scanner_data()
    )
    return df["name"].tolist()


# ── Circuit limits ────────────────────────────────────────────────────────────

_CIRCUIT_EMOJI = {
    ("20", "10"): "\U0001f7e8",
    ("10", "5"): "\U0001f7e5",
    ("5", "10"): "\U0001f7e9",
    ("10", "20"): "\U0001f7e6",
}
_NSE_CSV_PATHS = [
    os.path.join(REPO_DIR, "nse.csv"),
    r"C:\Users\satya\.gemini\antigravity\scratch\circuit_dashboard\nse.csv",
]


def get_circuit_limits() -> dict[str, tuple[str, str]]:
    import csv

    nse_csv = next((p for p in _NSE_CSV_PATHS if os.path.exists(p)), None)
    if not nse_csv:
        return {}
    try:
        latest: dict[str, dict] = {}
        with open(nse_csv, encoding="utf-8-sig") as fh:
            for raw in csv.DictReader(fh):
                row = {k.strip(): v.strip() for k, v in raw.items()}
                sym = row.get("SYMBOL", "")
                dte = row.get("EFFECTIVE DATE", "")
                frm = row.get("FROM", "")
                to = row.get("TO", "")
                if not sym or not dte:
                    continue
                try:
                    parsed = datetime.strptime(dte, "%d-%b-%Y")
                except ValueError:
                    continue
                if sym not in latest or parsed > latest[sym]["parsed"]:
                    latest[sym] = {"parsed": parsed, "from": frm, "to": to}
        return {
            sym: (d["to"] + "%", _CIRCUIT_EMOJI.get((d["from"], d["to"]), ""))
            for sym, d in latest.items()
        }
    except Exception:
        return {}
```

- [ ] **Step 2: Append per-stock analysis**

```python
# ── Per-stock analysis ────────────────────────────────────────────────────────


def analyse(symbol: str, df: pd.DataFrame, bench: pd.Series | None) -> dict | None:
    try:
        if df is None or len(df) < 30:
            return None
        if bench is None:
            return None

        signal, rel_perf, rel_perf_ema = _rs_leadership_signal(df, bench)
        if not signal:
            return None

        score, rs_state = _leadership_score(df, bench)

        c = df["close"].astype(float)
        zl25 = _zlema(c, 25)
        zl_rising = bool(zl25.iloc[-1] > zl25.iloc[-2])

        curr_close = float(c.iloc[-1])
        prev_close = float(c.iloc[-2])
        day_chg = (curr_close - prev_close) / prev_close * 100

        squeeze = _bb_kc_squeeze(df)

        return {
            "symbol": symbol,
            "close": curr_close,
            "day_chg": round(day_chg, 2),
            "rel_perf": rel_perf,
            "rel_perf_ema": rel_perf_ema,
            "score": score,
            "rs_state": rs_state,
            "zl_rising": zl_rising,
            "squeeze": squeeze,
            "liq_tag": liq_tag(df),
            "cmf_tag": cmf_tag(df),
            "deliv_tag": deliv_tag(symbol),
        }
    except Exception:
        return None
```

- [ ] **Step 3: Append markdown output + main()**

```python
# ── Markdown output ───────────────────────────────────────────────────────────

_RS_EMOJI = {"transition": "\U0001f504", "strong": "↑", "weak": "↓"}

_HDR = [
    "| Symbol | Name | Close | 1D% | RelPerf% | PerfEMA | Score | RS | ZL | Sqz | Liq |",
    "|--------|------|------:|----:|---------:|--------:|------:|:--:|:--:|:---:|-----|",
]


def _row(f: dict, circuit: dict, names: dict[str, str]) -> str:
    sym = f["symbol"]
    tv = f"https://in.tradingview.com/chart/?symbol=NSE:{sym}"
    cl, em = circuit.get(sym, ("20%", ""))
    circuit_cell = f"{cl} {em}".strip()

    name_cell = _LABELS.get(sym, "")

    zl_arrow = "↑" if f["zl_rising"] else "↓"
    ds = "+" if f["day_chg"] >= 0 else ""
    rp = "+" if f["rel_perf"] >= 0 else ""
    rs_icon = _RS_EMOJI.get(f["rs_state"], "↓")
    sqz = "●" if f["squeeze"] else "—"
    extras = [t for t in (f.get("cmf_tag", ""), f.get("deliv_tag", "")) if t]
    sym_cell = f"[{sym}]({tv}) [{circuit_cell}]" + (
        f"<br><sub>{' · '.join(extras)}</sub>" if extras else ""
    )

    return (
        f"| {sym_cell} "
        f"| {name_cell} "
        f"| {f['close']:.2f} "
        f"| {ds}{f['day_chg']:.2f}% "
        f"| {rp}{f['rel_perf']:.2f}% "
        f"| {f['rel_perf_ema']:.2f} "
        f"| {f['score']}/5 "
        f"| {rs_icon} "
        f"| {zl_arrow} "
        f"| {sqz} "
        f"| {f['liq_tag']} |"
    )


def build_markdown(findings: list[dict], circuit: dict, names: dict[str, str]) -> str:
    sorted_f = sorted(findings, key=lambda x: (-x["score"], -x["rel_perf"]))
    lines = [
        f"## RS Leadership — {TODAY}",
        f"*Generated {datetime.now().strftime('%Y-%m-%d %H:%M')} IST*",
        "",
        "### Scan definition",
        "| Filter | Value |",
        "|--------|-------|",
        "| Exchange | NSE common equity |",
        "| Price | > ₹20 |",
        "| 1W change | > 3% |",
        "| Market cap | ₹800 Cr – ₹5 Lakh Cr |",
        "| EMA10 / EMA20 | price above both |",
        "| Notional 10D | > ₹20 Cr/day |",
        "| Signal | Combined cross: RelPerf%>=0 AND its EMA rising, first alignment |",
        "| Params | RS EMA Length=9, Short RS EMA=5, Perf Lookback=9, Perf Smoothing=5 |",
        "| Benchmark | NIFTY MIDSML 400 (no trend filter applied) |",
        "| Sort | Leadership score desc, then RelPerf% desc |",
        "",
        "---",
        "",
        f"**{len(findings)} signal{'s' if len(findings) != 1 else ''} "
        f"— RS leadership combined cross today**",
        "",
        "```",
        ",".join(f"NSE:{f['symbol']}" for f in sorted_f),
        "```",
        "",
    ]

    if sorted_f:
        lines += _HDR + [_row(f, circuit, names) for f in sorted_f]
        lines += ["", "```", ",".join(f"NSE:{f['symbol']}" for f in sorted_f), "```"]
    else:
        lines.append("*No signals.*")

    lines.append("")
    return SEBI_MD_HEADER + "\n".join(lines) + SEBI_MD_FOOTER


# ── Main ──────────────────────────────────────────────────────────────────────


def main() -> None:
    os.makedirs(SCANS_DIR, exist_ok=True)

    print("\nFetching watchlist from TradingView screener...")
    watchlist = get_watchlist()
    print(f"  {len(watchlist)} stocks after screener filters")

    print(f"\nLoading OHLCV + benchmark ({BENCH_SYM}) from SQLite...")
    syms_to_load = watchlist + [BENCH_SYM]
    all_data = load_ohlc_many(syms_to_load, lookback=400)

    bench_df = all_data.pop(BENCH_SYM, None)
    bench_series: pd.Series | None = (
        bench_df.set_index("date")["close"].astype(float)
        if bench_df is not None
        else None
    )
    if bench_series is None:
        print(f"  WARNING: {BENCH_SYM} not in SQLite — RS signal unavailable")

    print(f"  Loaded {len(all_data)} equity stocks")

    print("\nFetching circuit limits...")
    circuit = get_circuit_limits()

    print(f"\nScanning {len(all_data)} stocks...")
    findings: list[dict] = []
    for i, (sym, df_raw) in enumerate(all_data.items(), 1):
        print(f"  {sym:<20} ({i}/{len(all_data)})   ", end="\r")
        result = analyse(sym, df_raw, bench_series)
        if result:
            findings.append(result)
    print()

    print(f"\n  {len(findings)} RS leadership crosses found")

    names = get_names([f["symbol"] for f in findings])
    md = build_markdown(findings, circuit, names)

    with open(MD_LATEST, "w", encoding="utf-8") as fh:
        fh.write(md)
    with open(MD_DATED, "w", encoding="utf-8") as fh:
        fh.write(md)

    print(f"  Saved → {MD_LATEST}")
    print(f"  Saved → {MD_DATED}")


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Write a smoke test for `build_markdown` empty case**

Append to `tests/test_rs_leadership_scanner.py` (before the `if __name__` block):

```python
def test_build_markdown_no_findings_has_no_signals_section():
    md = m.build_markdown([], {}, {})
    assert "*No signals.*" in md
    assert "SEBI registered" in md


def test_build_markdown_sorts_by_score_then_rel_perf():
    findings = [
        {
            "symbol": "AAA", "close": 100.0, "day_chg": 1.0, "rel_perf": 2.0,
            "rel_perf_ema": 1.5, "score": 3, "rs_state": "strong",
            "zl_rising": True, "squeeze": False, "liq_tag": "", "cmf_tag": "", "deliv_tag": "",
        },
        {
            "symbol": "BBB", "close": 50.0, "day_chg": -1.0, "rel_perf": 5.0,
            "rel_perf_ema": 4.0, "score": 4, "rs_state": "transition",
            "zl_rising": False, "squeeze": True, "liq_tag": "", "cmf_tag": "", "deliv_tag": "",
        },
    ]
    md = m.build_markdown(findings, {}, {})
    assert md.index("BBB") < md.index("AAA")
```

Add to the `if __name__ == "__main__":` block:

```python
    test_build_markdown_no_findings_has_no_signals_section()
    test_build_markdown_sorts_by_score_then_rel_perf()
```

- [ ] **Step 5: Run full test suite**

Run: `python tests/test_rs_leadership_scanner.py`
Expected: `OK` printed, exit code 0

- [ ] **Step 6: Commit**

```bash
git add rs_leadership_scanner.py tests/test_rs_leadership_scanner.py
git commit --no-verify -m "$(cat <<'EOF'
feat: RS leadership scanner watchlist, output, main()

Reuses rs_highline_scanner's TV screener filters and NIFTY MIDSML 400
benchmark. Writes dated + latest markdown with SEBI disclaimer.
EOF
)"
```

---

### Task 3: Manual smoke run against live SQLite data

**Files:**
- None created/modified — verification only

**Interfaces:**
- Consumes: `main()` from Task 2

- [ ] **Step 1: Confirm SQLite DB has data**

Run: `python -c "from ohlc_db import load_ohlc; df = load_ohlc('NIFTY MIDSML 400'); print(len(df) if df is not None else 'MISSING')"`
Expected: an integer row count (not `MISSING`). If missing, stop and tell the user — do not fabricate data.

- [ ] **Step 2: Run the scanner end-to-end**

Run: `python rs_leadership_scanner.py`
Expected: prints watchlist count, loads OHLCV, scans, prints `N RS leadership crosses found`, saves to `rs_leadership_scans/rs_leadership_latest.md` and `rs_leadership_scans/rs_leadership_<today>.md`. Exit code 0.

- [ ] **Step 3: Verify output file structure**

Run: `python -c "content = open('rs_leadership_scans/rs_leadership_latest.md', encoding='utf-8').read(); assert 'SEBI registered' in content; assert '## RS Leadership' in content; print('OK')"`
Expected: `OK` printed.

- [ ] **Step 4: Visually inspect one signal row (if any fired)**

Read: `rs_leadership_scans/rs_leadership_latest.md` — confirm RelPerf% is non-negative and Score/RS columns look sane for at least one row, or confirm `*No signals.*` is present and correctly formatted if zero fired.

- [ ] **Step 5: Commit output files**

```bash
git add rs_leadership_scans/
git commit --no-verify -m "$(cat <<'EOF'
[scan 2026-07-13] rs-leadership: initial scan run
EOF
)"
```

---

### Task 4: PowerShell runner + scheduler integration + CLAUDE.md docs

**Files:**
- Create: `run_rs_leadership_scanner.ps1`
- Modify: `run_all_scanners.ps1`
- Modify: `c:\Users\satya\nse_circuit_limits\CLAUDE.md`

**Interfaces:**
- Consumes: `rs_leadership_scanner.py` (Task 2), `rs_leadership_scans/` dir (Task 3)
- Produces: scheduled-task-ready runner script; scanner listed in `run_all_scanners.ps1` sequence; `CLAUDE.md` run table + output files table updated

- [ ] **Step 1: Create the PS1 runner**

Create `run_rs_leadership_scanner.ps1` (ASCII only, no em dashes/curly quotes — mirrors `run_rs_highline_scanner.ps1` exactly):

```powershell
$logDir  = "C:\Users\satya\nse_circuit_limits\logs"
$date    = Get-Date -Format "yyyy-MM-dd"
$logFile = "$logDir\rs_leadership_scanner_$date.log"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null

function Log($msg) {
    $line = "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] $msg"
    $line | Tee-Object -FilePath $logFile -Append
}

Log "=== RS_LEADERSHIP_SCANNER START ==="

try {
    & C:\Python313\python.exe C:\Users\satya\nse_circuit_limits\rs_leadership_scanner.py 2>&1 |
        ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
    Log "=== FINISHED exit=0 ==="
} catch {
    Log "=== ERROR: $_ ==="
    exit 1
}

Log "--- Git commit+push ---"
$scanDate = Get-Date -Format "yyyy-MM-dd"
& git -C C:\Users\satya\nse_circuit_limits add rs_leadership_scans/ 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
& git -C C:\Users\satya\nse_circuit_limits commit --no-verify -m "[scan $scanDate] rs-leadership: scan complete" 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
& git -C C:\Users\satya\nse_circuit_limits push 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
Log "--- Done ---"

# To register the scheduled task (run once as admin):
# schtasks /create /tn "NSE_RS_Leadership" /tr "powershell -NonInteractive -File C:\Users\satya\nse_circuit_limits\run_rs_leadership_scanner.ps1" /sc WEEKLY /d MON,TUE,WED,THU,FRI /st 16:30 /f
```

- [ ] **Step 2: Validate PS1 syntax**

Run: `powershell -File tools\check_ps1_syntax.ps1`
Expected: no syntax errors reported for `run_rs_leadership_scanner.ps1`.

- [ ] **Step 3: Add to `run_all_scanners.ps1` sequence**

Read `run_all_scanners.ps1` around the `Run-Scanner "RS_HighLine"` line (line 51) and add a new line immediately after it:

```powershell
Run-Scanner "RS_HighLine"          "$ROOT\run_rs_highline_scanner.ps1"
Run-Scanner "RS_Leadership"        "$ROOT\run_rs_leadership_scanner.ps1"
```

- [ ] **Step 4: Update `CLAUDE.md` run table**

In `c:\Users\satya\nse_circuit_limits\CLAUDE.md`, under "## Running the scanners", add a line after the `run_rs_highline_scanner.ps1` entry:

```powershell
.\run_rs_highline_scanner.ps1    # 4:30 PM — RS high-line cross scanner
.\run_rs_leadership_scanner.ps1  # 4:30 PM — RS leadership combined-cross scanner (RelPerf%+EMA)
```

- [ ] **Step 5: Update `CLAUDE.md` output files table**

Add a row to the "## Output files (git-tracked)" table:

```markdown
| `rs_leadership_scans/rs_leadership_latest.md`, `rs_leadership_scans/rs_leadership_YYYY-MM-DD.md` | `rs_leadership_scanner.py` |
```

- [ ] **Step 6: Add a short architecture section to `CLAUDE.md`**

Under the existing "### Scanner pipeline — RS High-Line Cross" section (or wherever WaveTrend/RS scanner sections are grouped), add:

```markdown
### Scanner pipeline — RS Leadership (`rs_leadership_scanner.py`)

Mirrors `pine_scripts/Satya RS Relative Leadership.txt`. Full design:
`docs/superpowers/specs/2026-07-13-rs-leadership-scanner-design.md`.

1. TV screener (same filters as `rs_highline_scanner.get_watchlist()`) -> watchlist
2. `load_ohlc_many()` + NIFTY MIDSML 400 bench
3. `_rs_leadership_signal()` -> combined cross: RelPerf% (9-bar lookback) >= 0
   AND its 5-bar EMA rising, true today, NOT both true yesterday
4. `_leadership_score()` -> 0-5 score + RS state (strong/weak/transition),
   mirrors the .txt's `leadershipScore` formula
5. Writes `rs_leadership_scans/rs_leadership_latest.md`, sorted score desc
   then RelPerf% desc

No benchmark-trend filter applied (explicit deviation from the Pine source's
default-checked `useBenchmarkFilter` input).
```

- [ ] **Step 7: Commit**

```bash
git add run_rs_leadership_scanner.ps1 run_all_scanners.ps1 CLAUDE.md
git commit --no-verify -m "$(cat <<'EOF'
feat: wire RS leadership scanner into scheduler + docs

Adds run_rs_leadership_scanner.ps1, sequences it in run_all_scanners.ps1
after RS_HighLine, documents run table + architecture in CLAUDE.md.
EOF
)"
```

- [ ] **Step 8: Push**

```bash
git push
```

---

## Self-Review Notes

- **Spec coverage:** Signal logic (Task 1), watchlist/output (Task 2), live verification (Task 3), scheduler/docs integration (Task 4) — all spec sections covered. Testing section of the spec is satisfied by `tests/test_rs_leadership_scanner.py`.
- **Placeholder scan:** No TBD/TODO; every step has runnable code.
- **Type consistency:** `_rs_leadership_signal` returns `tuple[bool, float, float]` in both Task 1 and its Task 2 caller (`analyse`); `_leadership_score` returns `tuple[int, str]` used consistently; `BENCH_SYM`, `MD_LATEST`, `MD_DATED`, `SCANS_DIR` defined once in Task 1's file header and reused as-is in Task 2 (same file, no re-declaration needed since it's one module built across two tasks).
