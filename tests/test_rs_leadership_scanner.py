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


if __name__ == "__main__":
    test_combined_cross_fires_when_both_conditions_first_align()
    test_no_fire_when_conditions_already_held_yesterday()
    test_no_fire_when_only_rel_perf_positive_ema_falling()
    test_insufficient_history_returns_false()
    print("OK")
