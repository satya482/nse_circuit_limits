"""Institutional footprint scanner helpers and EOD report builder."""

import os
import statistics
from collections.abc import Mapping, Sequence
from datetime import date

import pandas as pd

import ohlc_db
import sector_sync
from capital import regime_throttle
from disclaimer import SEBI_HTML_BANNER, SEBI_HTML_FOOTER, SEBI_MD_FOOTER, SEBI_MD_HEADER

SPARKLINE_BLOCKS = "▁▂▃▄▅▆▇█"
BENCH_SYM = "NIFTY MIDSML 400"
SCANS_DIR = "footprint_scans"
DASHBOARD_PATH = os.path.join("dashboard", "footprint.html")
MIN_BARS = 60


def delivery_sparkline(values: Sequence[float], lookback: int = 20) -> str:
    vals = [float(v) for v in values[-lookback:]]
    if len(vals) < lookback:
        return ""

    low = min(vals)
    high = max(vals)
    if high == low:
        return SPARKLINE_BLOCKS[3] * lookback

    scale = len(SPARKLINE_BLOCKS) - 1
    return "".join(
        SPARKLINE_BLOCKS[round((value - low) / (high - low) * scale)]
        for value in vals
    )


def delivery_percentile(
    values: Sequence[float], lookback: int = 252, min_periods: int = 60
) -> int | None:
    if len(values) < min_periods + 1:
        return None

    latest = float(values[-1])
    previous = [float(v) for v in values[-(lookback + 1) : -1]]
    if len(previous) < min_periods:
        return None

    count = sum(1 for value in previous if value <= latest)
    return int(round(count / len(previous) * 100))


def delivery_zscore(
    values: Sequence[float], lookback: int = 252, min_periods: int = 60
) -> float | None:
    if len(values) < min_periods + 1:
        return None

    latest = float(values[-1])
    previous = [float(v) for v in values[-(lookback + 1) : -1]]
    if len(previous) < min_periods:
        return None

    stdev = statistics.pstdev(previous)
    if not stdev:
        return None
    return round((latest - statistics.mean(previous)) / stdev, 2)


def consecutive_high_delivery_days(
    values: Sequence[float], mult: float = 1.5, baseline_window: int = 20
) -> int:
    vals = [float(v) for v in values]
    if len(vals) < baseline_window + 1:
        return 0

    count = 0
    for i in range(len(vals) - 1, baseline_window - 1, -1):
        baseline = sum(vals[i - baseline_window : i]) / baseline_window
        if baseline <= 0 or vals[i] < baseline * mult:
            break
        count += 1
    return count


def absorption_day(high: pd.Series, low: pd.Series, close: pd.Series, delivery_ratio: float) -> bool:
    """Small range + high delivery + close resilient in upper half of the bar."""
    if len(close) < 20:
        return False

    range_pct = (high - low) / close.replace(0, float("nan"))
    window = range_pct.iloc[-20:]
    today = float(window.iloc[-1])
    threshold = float(window.quantile(0.2))

    latest_close, latest_high, latest_low = float(close.iloc[-1]), float(high.iloc[-1]), float(low.iloc[-1])
    upper_half = latest_high == latest_low or (latest_close - latest_low) >= (latest_high - latest_close)

    return bool(today <= threshold and delivery_ratio >= 1.5 and upper_half)


def failed_breakdown_reclaim(close: pd.Series, low: pd.Series, volume_ratio: float) -> bool:
    """Support (20-day closing low, excluding today) broke intraday in last 3 bars, today reclaims it
    on above-average volume (spec §7.4: "Delivery or volume above average" — without this gate any
    routine dip-and-recover counts, ~21% of a 1300-symbol sample fired in a real-data smoke test)."""
    if len(close) < 21:
        return False

    support = close.rolling(20, min_periods=20).min().shift(1)
    if pd.isna(support.iloc[-1]):
        return False

    broke = any(pd.notna(support.iloc[i]) and low.iloc[i] < support.iloc[i] for i in range(-3, 0))
    return bool(broke and volume_ratio >= 1.2 and float(close.iloc[-1]) > float(support.iloc[-1]))


def failed_breakout(close: pd.Series, high: pd.Series, low: pd.Series, volume_ratio: float) -> bool:
    """Resistance (20-day closing high, excluding today) broke in last 2 bars, today gives it back."""
    if len(close) < 21:
        return False

    level = close.rolling(20, min_periods=20).max().shift(1)
    if pd.isna(level.iloc[-1]):
        return False

    broke = any(pd.notna(level.iloc[i]) and close.iloc[i] > level.iloc[i] for i in range(-2, 0))
    latest_high, latest_low, latest_close = float(high.iloc[-1]), float(low.iloc[-1]), float(close.iloc[-1])
    wick_ratio = (latest_high - latest_close) / (latest_high - latest_low) if latest_high > latest_low else 0.0

    return bool(broke and wick_ratio > 0.5 and volume_ratio >= 1.5 and latest_close <= float(level.iloc[-1]))


def resistance_touch_count(close: pd.Series, window: int = 20) -> int:
    """Closes within 1.5% of the 60-day closing high, over the last `window` bars."""
    if len(close) < 60:
        return 0

    resistance = close.rolling(60, min_periods=60).max()
    tail = min(window, len(close))
    touches = 0
    for i in range(-tail, 0):
        r = resistance.iloc[i]
        if pd.notna(r) and r > 0 and abs(float(close.iloc[i]) / float(r) - 1) <= 0.015:
            touches += 1
    return touches


def assign_rating(ics: float) -> str:
    if ics >= 95:
        return "ELITE"
    if ics >= 85:
        return "STRONG"
    if ics >= 70:
        return "BUILDING"
    if ics >= 55:
        return "WATCH"
    return "IGNORE"


def calculate_ics(row: Mapping[str, object]) -> float:
    score = 0.0

    score += 6 if row.get("latest_delivery_above_avg20") else 0
    score += 6 if _num(row, "delivery_ratio") >= 1.5 else 0
    score += 6 if _num(row, "delivery_percentile") >= 90 else 0
    score += 6 if _num(row, "consecutive_high_delivery_days") >= 3 else 0
    score += 6 if row.get("delivery_slope_positive") else 0

    score += 6 if _num(row, "volume_ratio") >= 1.5 else 0
    score += 6 if _num(row, "turnover_ratio") >= 1.5 else 0
    score += 4 if _num(row, "turnover_cr") >= 5 else 0
    score += 4 if row.get("up_day_volume_above_avg") else 0

    score += 4 if row.get("close_gt_ema20") else 0
    score += 4 if row.get("close_gt_ema50") else 0
    score += 4 if row.get("close_gt_ema200") else 0
    score += 4 if row.get("breakout20") else 0
    score += 4 if row.get("within_15pct_52w_high") else 0

    cmf20 = _num(row, "cmf20")
    score += 5 if cmf20 > 0 else 0
    score += 5 if cmf20 > 0.05 else 0
    score += 5 if row.get("obv_slope20_positive", row.get("cmf_rising")) else 0

    score += 8 if _num(row, "rs_percentile") >= 90 else 0
    score += 4 if row.get("rs_trend") == "UP" else 0
    score += 3 if row.get("outperform_benchmark_50d") else 0

    score += 6 if row.get("absorption_day") else 0
    score += 8 if row.get("failed_breakdown_reclaim") else 0
    score += 6 if _num(row, "resistance_touches") >= 3 else 0
    score -= 10 if row.get("failed_breakout") else 0

    return min(100.0, max(0.0, score))


def assign_lifecycle(row: Mapping[str, object]) -> str:
    cmf20 = _num(row, "cmf20")
    weakening = (
        _num(row, "obv_slope20") < 0
        or row.get("cmf_rising") is False
        or row.get("obv_slope20_positive") is False
    )
    if row.get("price_down") and _num(row, "volume_ratio") >= 1.5 and cmf20 < 0 and weakening:
        return "DISTRIBUTION"

    if row.get("breakout20") and _num(row, "delivery_percentile") >= 90 and _num(row, "volume_ratio") >= 1.5:
        return "BREAKOUT"

    if row.get("close_gt_ema20") and row.get("close_gt_ema50") and _num(row, "rs_percentile") >= 90 and _num(row, "ics") >= 85:
        return "MARKUP"

    if _num(row, "ics") >= 70 and row.get("delivery_slope_positive") and cmf20 > 0 and not row.get("breakout20"):
        return "BUILDING"

    if _num(row, "delivery_percentile") >= 85 and not row.get("breakout20"):
        return "SEED"

    return "NONE"


def delivery_visual_tag(row: Mapping[str, object]) -> str:
    if _num(row, "delivery_ratio") < 1.5:
        return ""

    parts = [f"DEL{_num(row, 'latest_delivery_pct'):.0f}%"]
    if row.get("delivery_sparkline"):
        parts.append(str(row["delivery_sparkline"]))
    if row.get("delivery_percentile") is not None:
        parts.append(f"P{int(_num(row, 'delivery_percentile'))}")
    if row.get("delivery_zscore") is not None:
        parts.append(f"Z{_num(row, 'delivery_zscore'):+.1f}")
    if _num(row, "consecutive_high_delivery_days") >= 2:
        parts.append(f"{int(_num(row, 'consecutive_high_delivery_days'))}D")
    return " ".join(parts)


def structure_tag(row: Mapping[str, object]) -> str:
    parts = []
    if row.get("absorption_day"):
        parts.append("ABS")
    if row.get("failed_breakdown_reclaim"):
        parts.append("RECLAIM")
    if row.get("failed_breakout"):
        parts.append("TRAP")
    touches = _num(row, "resistance_touches")
    if touches >= 3:
        parts.append(f"R{int(touches)}")
    return " ".join(parts)


def assign_trade_action(row: Mapping[str, object], regime: str) -> tuple[str, str]:
    ics = _num(row, "ics")
    stage = str(row.get("stage", "NONE"))
    rs_pct = _num(row, "rs_percentile")
    delivery_ratio = _num(row, "delivery_ratio")
    volume_ratio = _num(row, "volume_ratio")

    is_trigger_near = stage in {"BREAKOUT", "MARKUP"} or volume_ratio >= 1.5
    has_footprint = delivery_ratio >= 1.5 or rs_pct >= 90

    if ics >= 85 and is_trigger_near and has_footprint:
        rank = "A"
    elif ics >= 70:
        rank = "B"
    else:
        rank = "C"

    if regime == "RED":
        return rank, "NO_DEPLOY"
    if regime == "NEUTRAL":
        return rank, "WATCH_FOR_ENTRY" if rank == "A" else "WAIT"
    if regime == "GREEN":
        return rank, "WATCH_FOR_ENTRY" if rank in {"A", "B"} else "WATCHLIST"
    return rank, "WAIT"


def regime_info_for(as_of: str) -> dict:
    try:
        return regime_throttle.regime_for_date(as_of)
    except Exception:
        return {"regime": "NEUTRAL", "max_slots": 3, "time_stop_mode": "bar3_only"}


def analyse_symbol(
    symbol: str,
    df: pd.DataFrame,
    bench_df: pd.DataFrame,
    delivery_df: pd.DataFrame | None,
) -> dict | None:
    if df is None or bench_df is None or len(df) < MIN_BARS or len(bench_df) < MIN_BARS:
        return None

    close = df["close"].astype(float)
    high = df["high"].astype(float)
    low = df["low"].astype(float)
    volume = df["volume"].astype(float)
    latest_close = float(close.iloc[-1])
    prev_close = float(close.iloc[-2])
    latest_high = float(high.iloc[-1])
    latest_low = float(low.iloc[-1])
    latest_open = float(df["open"].astype(float).iloc[-1])

    row = {
        "symbol": symbol,
        "close": latest_close,
        "open": latest_open,
        "high": latest_high,
        "low": latest_low,
        "price_down": latest_close < prev_close,
        "close_gt_ema20": latest_close > float(close.ewm(span=20, adjust=False).mean().iloc[-1]),
        "close_gt_ema50": latest_close > float(close.ewm(span=50, adjust=False).mean().iloc[-1]),
        "close_gt_ema200": latest_close > float(close.ewm(span=200, adjust=False).mean().iloc[-1]),
        "breakout20": latest_close >= float(close.rolling(20, min_periods=20).max().iloc[-1]),
        "within_15pct_52w_high": latest_close >= float(close.rolling(252, min_periods=60).max().iloc[-1]) * 0.85,
    }

    avg_volume20 = float(volume.iloc[-21:-1].mean()) if len(volume) >= 21 else float(volume.mean())
    today_volume = float(volume.iloc[-1])
    turnover = latest_close * today_volume / 1e7
    turnover20 = float((close * volume / 1e7).iloc[-21:-1].mean()) if len(df) >= 21 else turnover
    row.update(
        {
            "volume_ratio": today_volume / avg_volume20 if avg_volume20 else 0.0,
            "turnover_cr": turnover,
            "turnover_ratio": turnover / turnover20 if turnover20 else 0.0,
            "up_day_volume_above_avg": latest_close > prev_close and today_volume > avg_volume20,
        }
    )

    cmf = ohlc_db.cmf_series(df, n=20)
    cmf20 = float(cmf.iloc[-1]) if len(cmf) else 0.0
    row["cmf20"] = cmf20
    row["cmf_rising"] = len(cmf) >= 2 and cmf20 > float(cmf.iloc[-2])

    if delivery_df is not None and len(delivery_df) >= 21:
        vals = [float(v) for v in delivery_df["deliv_pct"].tolist()]
        prior20 = vals[-21:-1]
        latest_delivery = vals[-1]
        avg20 = sum(prior20) / len(prior20)
        row.update(
            {
                "latest_delivery_pct": latest_delivery,
                "latest_delivery_above_avg20": latest_delivery > avg20,
                "delivery_ratio": latest_delivery / avg20 if avg20 else 0.0,
                "delivery_percentile": delivery_percentile(vals),
                "delivery_zscore": delivery_zscore(vals),
                "consecutive_high_delivery_days": consecutive_high_delivery_days(vals),
                "delivery_slope_positive": len(vals) >= 40 and sum(vals[-20:]) / 20 > sum(vals[-40:-20]) / 20,
                "delivery_sparkline": delivery_sparkline(vals),
            }
        )
    else:
        row.update(
            {
                "latest_delivery_pct": 0.0,
                "latest_delivery_above_avg20": False,
                "delivery_ratio": 0.0,
                "delivery_percentile": None,
                "delivery_zscore": None,
                "consecutive_high_delivery_days": 0,
                "delivery_slope_positive": False,
                "delivery_sparkline": "",
            }
        )

    row["absorption_day"] = absorption_day(high, low, close, _num(row, "delivery_ratio"))
    row["failed_breakdown_reclaim"] = failed_breakdown_reclaim(close, low, _num(row, "volume_ratio"))
    row["failed_breakout"] = failed_breakout(close, high, low, _num(row, "volume_ratio"))
    row["resistance_touches"] = resistance_touch_count(close)

    row["stock_return_20d"] = _return(close, 20)
    row["stock_return_50d"] = _return(close, 50)
    bench_close = bench_df["close"].astype(float)
    row["rs_raw_20"] = row["stock_return_20d"] - _return(bench_close, 20)
    row["rs_raw_50"] = row["stock_return_50d"] - _return(bench_close, 50)
    row["rs_trend"] = "UP" if row["rs_raw_20"] > row["rs_raw_50"] else "FLAT"
    row["outperform_benchmark_50d"] = row["rs_raw_50"] > 0
    return row


def run(universe_df, as_of, ohlc_map=None, delivery_map=None, bench_df=None, regime_info=None):
    symbols = universe_df["symbol"].tolist()
    regime_info = regime_info or regime_info_for(as_of)
    regime = regime_info["regime"]
    if ohlc_map is None:
        loaded = ohlc_db.load_ohlc_many(symbols + [BENCH_SYM], lookback=300)
        bench_df = loaded.pop(BENCH_SYM, None)
        ohlc_map = loaded
    if bench_df is None:
        bench_df = ohlc_map.get(BENCH_SYM) if ohlc_map else None

    rows = []
    for symbol in symbols:
        delivery_df = (
            delivery_map.get(symbol)
            if delivery_map is not None
            else ohlc_db.load_delivery(symbol, lookback=300)
        )
        row = analyse_symbol(symbol, ohlc_map.get(symbol), bench_df, delivery_df)
        if row:
            rows.append(row)

    if not rows:
        return pd.DataFrame()

    sector_map = (
        dict(zip(universe_df["symbol"], universe_df["sector"]))
        if "sector" in universe_df.columns
        else None
    )

    _rank_rs(rows)
    for row in rows:
        row["ics"] = calculate_ics(row)
        row["rating"] = assign_rating(row["ics"])
        row["stage"] = assign_lifecycle(row)
        row["delivery_tag"] = delivery_visual_tag(row)
        row["regime"] = regime
        row["action_rank"], row["action"] = assign_trade_action(row, regime)
        row["reason"] = _reason(row)

    df = sector_sync.add_sector_scores(pd.DataFrame(rows), sector_map)
    return df.sort_values(["action_rank", "ics", "rs_percentile"], ascending=[True, False, False]).reset_index(drop=True)


def build_markdown(rows, as_of: str) -> str:
    records = rows.to_dict("records") if hasattr(rows, "to_dict") else list(rows)
    records = [
        row for row in records
        if row.get("rating") != "IGNORE" and _num(row, "ics") >= 55
    ]
    records = sorted(
        records,
        key=lambda r: (str(r.get("action_rank", "Z")), -_num(r, "ics"), r.get("symbol", "")),
    )

    lines = [f"## Institutional Footprint Scan - {as_of}", ""]
    if not records:
        lines.append("*No signals.*")
    else:
        cols = [
            "Symbol",
            "Reason / Delivery",
            "ICS",
            "Rating",
            "Stage",
            "Regime",
            "Rank",
            "Action",
            "RS",
            "CMF20",
            "Vol",
            "Turnover",
            "Sector",
            "Structure",
        ]
        lines.append("| " + " | ".join(cols) + " |")
        lines.append("|" + "---|" * len(cols))
        for row in records:
            tv = f"https://in.tradingview.com/chart/?symbol=NSE:{row['symbol']}"
            symbol = f"[{row['symbol']}]({tv})"
            rs = f"{_num(row, 'rs_percentile'):.0f} {row.get('rs_trend', '')}".strip()
            lines.append(
                "| "
                + " | ".join(
                    [
                        symbol,
                        _reason_delivery(row),
                        f"{_num(row, 'ics'):.0f}",
                        str(row.get("rating", "")),
                        str(row.get("stage", "")),
                        str(row.get("regime", "")),
                        str(row.get("action_rank", "")),
                        str(row.get("action", "")),
                        rs,
                        f"{_num(row, 'cmf20'):.2f}",
                        f"{_num(row, 'volume_ratio'):.1f}x",
                        f"{_num(row, 'turnover_cr'):.1f}Cr",
                        f"{row.get('sector', '')} ({_num(row, 'sector_score'):.0f})".strip(),
                        structure_tag(row),
                    ]
                )
                + " |"
            )
    return SEBI_MD_HEADER + "\n".join(lines) + SEBI_MD_FOOTER


def build_html(rows, as_of: str) -> str:
    records = rows.to_dict("records") if hasattr(rows, "to_dict") else list(rows)
    records = [r for r in records if r.get("rating") != "IGNORE" and _num(r, "ics") >= 55]
    records = sorted(records, key=lambda r: (str(r.get("action_rank", "Z")), -_num(r, "ics")))

    cards = "\n".join(
        f'<div class="card" data-q="{row.get("symbol","")} {row.get("stage","")} {row.get("action","")}">'
        f'<div class="hdr"><a href="https://in.tradingview.com/chart/?symbol=NSE:{row.get("symbol","")}" '
        f'target="_blank">{row.get("symbol","")}</a><span class="ics">{_num(row,"ics"):.0f}</span></div>'
        f'<div class="tags">{row.get("rating","")} · {row.get("stage","")} · {row.get("action","")}</div>'
        f'<div class="del">{row.get("delivery_tag","")}</div>'
        f'<div class="struct">{row.get("sector","")} ({_num(row,"sector_score"):.0f}) · {structure_tag(row)}</div>'
        f'<div class="reason">{row.get("reason","")}</div>'
        f"</div>"
        for row in records
    )
    if not records:
        cards = '<p class="empty">No signals.</p>'

    return f"""<!doctype html>
<html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Institutional Footprint — {as_of}</title>
<style>
:root{{color-scheme:dark}}
body{{background:#0d1117;color:#e6edf3;font-family:system-ui,sans-serif;margin:0;padding:12px}}
h1{{font-size:1.1rem}}
#q{{width:100%;box-sizing:border-box;padding:8px;margin:8px 0;background:#161b22;color:#e6edf3;border:1px solid #30363d;border-radius:6px}}
#cards{{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:10px}}
.card{{background:#161b22;border:1px solid #30363d;border-radius:8px;padding:10px}}
.hdr{{display:flex;justify-content:space-between;font-weight:600}}
.hdr a{{color:#58a6ff;text-decoration:none}}
.ics{{color:#3fb950}}
.tags{{color:#8b949e;font-size:.85rem;margin-top:4px}}
.del{{font-size:.85rem;margin-top:4px}}
.struct{{font-size:.8rem;color:#8b949e;margin-top:2px}}
.reason{{font-size:.8rem;color:#8b949e;margin-top:4px}}
.empty{{color:#8b949e}}
</style></head>
<body>
{SEBI_HTML_BANNER}
<h1>Institutional Footprint — {as_of}</h1>
<input id="q" placeholder="Filter by symbol / stage / action">
<div id="cards">
{cards}
</div>
{SEBI_HTML_FOOTER}
<script>
document.getElementById('q').addEventListener('input', function(e) {{
  var q = e.target.value.toLowerCase();
  document.querySelectorAll('#cards .card').forEach(function(c) {{
    c.style.display = c.dataset.q.toLowerCase().includes(q) ? '' : 'none';
  }});
}});
</script>
</body></html>
"""


def get_universe() -> pd.DataFrame:
    """Returns `symbol`/`sector` — sector straight from the same TradingView query used
    to build the universe, so coverage is 100% of what's scanned (a static sector CSV
    join only covered ~69% of this universe in practice)."""
    from tradingview_screener import Query, col

    mc_low = 1_000 * 1_00_00_000
    mc_high = 5_00_000 * 1_00_00_000
    _, df = (
        Query()
        .set_markets("india")
        .select("name", "sector")
        .where(
            col("exchange") == "NSE",
            col("type") == "stock",
            col("typespecs").has(["common"]),
            col("close") > 50,
            col("market_cap_basic").between(mc_low, mc_high),
        )
        .limit(2000)
        .get_scanner_data()
    )
    return df.rename(columns={"name": "symbol"})[["symbol", "sector"]]


def main() -> None:
    as_of = date.today().isoformat()
    os.makedirs(SCANS_DIR, exist_ok=True)
    os.makedirs(os.path.dirname(DASHBOARD_PATH), exist_ok=True)
    rows = run(get_universe(), as_of)

    md = build_markdown(rows, as_of)
    latest = os.path.join(SCANS_DIR, "footprint_latest.md")
    dated = os.path.join(SCANS_DIR, f"footprint_{as_of}.md")
    with open(latest, "w", encoding="utf-8") as fh:
        fh.write(md)
    with open(dated, "w", encoding="utf-8") as fh:
        fh.write(md)

    with open(DASHBOARD_PATH, "w", encoding="utf-8") as fh:
        fh.write(build_html(rows, as_of))

    # ponytail: CSV snapshot is the signal-history store (spec Phase 5) — a real
    # DB table only if repeated cross-day queries over this history get painful.
    if not rows.empty:
        rows.to_csv(os.path.join(SCANS_DIR, f"footprint_{as_of}.csv"), index=False)


def _num(row: Mapping[str, object], key: str) -> float:
    value = row.get(key)
    if value is None:
        return 0.0
    return float(value)


def _return(close: pd.Series, bars: int) -> float:
    if len(close) <= bars or float(close.iloc[-bars - 1]) == 0:
        return 0.0
    return float(close.iloc[-1] / close.iloc[-bars - 1] - 1)


def _rank_rs(rows: list[dict]) -> None:
    ordered = sorted(rows, key=lambda r: r["rs_raw_50"])
    denom = max(1, len(ordered) - 1)
    for rank, row in enumerate(ordered):
        row["rs_percentile"] = round(rank / denom * 100)


def _reason(row: Mapping[str, object]) -> str:
    reasons = []
    if row.get("delivery_percentile") is not None and _num(row, "delivery_percentile") >= 90:
        reasons.append(f"Delivery P{_num(row, 'delivery_percentile'):.0f}")
    if _num(row, "consecutive_high_delivery_days") >= 2:
        reasons.append(f"{_num(row, 'consecutive_high_delivery_days'):.0f}D high delivery")
    if _num(row, "cmf20") > 0:
        reasons.append("CMF positive")
    if _num(row, "rs_percentile") >= 90:
        reasons.append("RS leader")
    return ", ".join(reasons[:4]) or "No standout factor"


def _reason_delivery(row: Mapping[str, object]) -> str:
    reason = str(row.get("reason", ""))
    tag = row.get("delivery_tag")
    tag = "" if tag is None or pd.isna(tag) else str(tag)
    return f"{reason} · {tag}" if tag else reason


if __name__ == "__main__":
    main()
