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
    # Benchmark flat; stock flat for 25 bars then a single up-day. Verified by
    # hand (not just plausible): at n=26 this is exactly the first bar where
    # (rel_perf>=0 AND rel_perf_ema rising) becomes true, having been false
    # every prior bar (both conditions were flat/equal, not rising, before).
    stock_closes = [100.0] * 25 + [101.5]
    bench_closes = [100.0] * len(stock_closes)
    df = _df(stock_closes)
    bench = _bench_series(bench_closes)
    signal, rel_perf, rel_perf_ema = m._rs_leadership_signal(df, bench)
    assert signal is True
    assert rel_perf == 1.5
    assert rel_perf_ema == 0.5


def test_no_fire_when_conditions_already_held_yesterday():
    # Benchmark flat; stock compounds 3%/day for 8 bars after 25 flat bars.
    # Verified by hand: both today's and yesterday's bar already have
    # rel_perf>=0 AND rel_perf_ema rising -- the pair aligned days ago, so
    # this is not a fresh cross despite both conditions currently holding.
    stock_closes = [100.0] * 25 + [100 * (1.03**i) for i in range(1, 9)]
    bench_closes = [100.0] * len(stock_closes)
    df = _df(stock_closes)
    bench = _bench_series(bench_closes)
    signal, _, _ = m._rs_leadership_signal(df, bench)
    assert signal is False


def test_no_fire_when_only_rel_perf_positive_ema_falling():
    # Stock spikes hard (5 bars of +3/day) then flattens for 7 bars. Verified
    # by hand: on the last bar, rel_perf is clearly positive (~5.5, not a
    # boundary value) but rel_perf_ema is falling as the spike ages out of
    # the smoothing window -- exactly the "only one condition true" case.
    stock_closes = [100.0] * 20 + [100 + i * 3.0 for i in range(1, 6)] + [115.0] * 7
    bench_closes = [100.0] * len(stock_closes)
    df = _df(stock_closes)
    bench = _bench_series(bench_closes)
    signal, rel_perf, rel_perf_ema = m._rs_leadership_signal(df, bench)
    assert signal is False
    assert rel_perf > 0


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


def test_leadership_score_strong_when_steadily_outperforming():
    # Stock's daily growth rate itself increases (1.01 + 0.0015*i per day,
    # not a constant compounding rate) for 40 bars, benchmark flat. A constant
    # daily rate gives a mathematically flat 9-day rel_perf (1.02**i /
    # 1.02**(i-9) is identical for every i), which previously made
    # performance_rising true only via ~1e-14 float rounding noise --
    # fragile across pandas/numpy/BLAS builds. This fixture genuinely
    # accelerates: rel_perf.iloc[-1]=72.56 vs rel_perf.iloc[-2]=70.38, a
    # ~2.18 margin, verified by hand (python -c against
    # m._rel_perf_series/m._leadership_score directly). rs_line is strictly
    # increasing off a flat base, so it is above its own EMA(9) from the
    # first rising bar onward and stays there through bar 40 -- an
    # established uptrend, not a fresh cross. Actual output: (5, "strong").
    rates = [1.01 + 0.0015 * i for i in range(40)]
    stock_closes = [100.0]
    for r in rates[1:]:
        stock_closes.append(stock_closes[-1] * r)
    bench_closes = [100.0] * len(stock_closes)
    df = _df(stock_closes)
    bench = _bench_series(bench_closes)
    score, rs_state = m._leadership_score(df, bench)
    assert rs_state == "strong"
    assert score >= 3
    assert score == 5


def test_leadership_score_weak_when_flat_and_matching_benchmark():
    # Stock identical to (flat) benchmark for the whole history. Verified by
    # hand: rs_line = (sc/bc)*1000 is constant from bar 1, so its EMA(9)
    # equals it exactly at every bar (no lag on a constant series) --
    # rs_above_ema, short_rs_bullish, rs_ema_rising, outperforming (rel_perf
    # == 0, not > 0), and performance_rising are all False. Actual output:
    # (0, "weak").
    n = 30
    stock_closes = [100.0] * n
    bench_closes = [100.0] * n
    df = _df(stock_closes)
    bench = _bench_series(bench_closes)
    score, rs_state = m._leadership_score(df, bench)
    assert rs_state == "weak"
    assert score == 0


def test_leadership_score_transition_on_fresh_cross_after_sustained_rise():
    # Bench flat throughout. Stock: flat 15 bars, then declines 5 bars at
    # -7%/day (drags rs_line below its EMA(9), building lag), then rises 9
    # bars at +1%/day -- a genuine multi-day sustained uptrend, not a
    # single-day blip. Verified by hand (python -c against
    # m._leadership_score directly, dumping rs_line/rs_ema_long for the last
    # two bars): rs_line stays below rs_ema_long through bar 28
    # (753.33 < 755.68) and only overtakes it on the final bar, bar 29
    # (760.86 > 756.71) -- a fresh cross on the most recent bar, deep into
    # the 9-day rise rather than on day 1 of it. Actual output: (4,
    # "transition"), with rs_ema_rising/outperforming/performance_rising
    # all True and short_rs_bullish False.
    decl_days, decl_rate, rise_days, rise_rate = 5, 0.93, 9, 1.01
    stock_closes = [100.0] * 15
    for _ in range(decl_days):
        stock_closes.append(stock_closes[-1] * decl_rate)
    base = stock_closes[14 + decl_days]
    for i in range(1, rise_days + 1):
        stock_closes.append(base * (rise_rate**i))
    bench_closes = [100.0] * len(stock_closes)
    df = _df(stock_closes)
    bench = _bench_series(bench_closes)
    score, rs_state = m._leadership_score(df, bench)
    assert rs_state == "transition"
    assert score == 4


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


if __name__ == "__main__":
    test_combined_cross_fires_when_both_conditions_first_align()
    test_no_fire_when_conditions_already_held_yesterday()
    test_no_fire_when_only_rel_perf_positive_ema_falling()
    test_insufficient_history_returns_false()
    test_leadership_score_strong_when_steadily_outperforming()
    test_leadership_score_weak_when_flat_and_matching_benchmark()
    test_leadership_score_transition_on_fresh_cross_after_sustained_rise()
    test_build_markdown_no_findings_has_no_signals_section()
    test_build_markdown_sorts_by_score_then_rel_perf()
    print("OK")
