import pandas as pd
import pytest
from pandas.testing import assert_series_equal

import backtest_daily_zlema25_weekly_rs as m


def _ohlc(closes, start="2024-01-01"):
    dates = pd.bdate_range(start, periods=len(closes))
    return pd.DataFrame({"date": dates, "close": closes})


def test_zlema_matches_double_ema_formula():
    close = pd.Series([100.0 + i for i in range(40)])
    ema = close.ewm(span=25, adjust=False).mean()
    expected = 2 * ema - ema.ewm(span=25, adjust=False).mean()
    assert_series_equal(m.zlema(close), expected)


def test_weekly_rs_ema_does_not_look_ahead_within_week():
    stock = _ohlc([100.0 + i for i in range(70)])
    bench = _ohlc([200.0 + i * 0.2 for i in range(70)])
    cutoff = stock.loc[62, "date"]
    early = m.build_indicator_frame(stock.iloc[:63], bench.iloc[:63])
    full = m.build_indicator_frame(stock, bench)
    cols = ["weekly_rs_ema9", "prior_week_rs_ema9", "rs_ema9_rising"]
    pd.testing.assert_frame_equal(
        early.set_index("date")[cols],
        full.loc[full["date"] <= cutoff].set_index("date")[cols],
    )


def test_entry_signal_requires_all_four_conditions():
    stock = _ohlc([100 + i * 0.2 + (2 if i % 9 == 0 else 0) for i in range(90)])
    bench = _ohlc([200 + i * 0.05 for i in range(90)])
    frame = m.build_indicator_frame(stock, bench)
    expected = (
        (frame["zlema25"] > frame["zlema25"].shift(1))
        & (frame["zlema25"].shift(1) <= frame["zlema25"].shift(2))
        & frame["rs_above_ema9"]
        & frame["rs_ema9_rising"]
        & (frame.index >= 24)
    )
    pd.testing.assert_series_equal(frame["entry_signal"], expected, check_names=False)


def _signal_frame():
    dates = pd.bdate_range("2024-03-01", periods=6)
    return pd.DataFrame(
        {
            "date": dates,
            "close": [100.0, 102.0, 105.0, 104.0, 103.0, 106.0],
            "zlema25": [100.0, 99.0, 100.0, 101.0, 100.5, 101.0],
            "rs_ema9_rising": [True, True, True, True, True, False],
            "entry_signal": [False, False, True, False, False, False],
        }
    )


def test_simulation_exits_on_first_zlema_down_close():
    completed, opened = m.simulate_stock(
        "TEST",
        _signal_frame(),
        pd.Timestamp("2024-03-01"),
        pd.Timestamp("2024-03-31"),
    )
    assert opened.empty
    trade = completed.iloc[0]
    assert trade["entry_close"] == 105.0
    assert trade["exit_close"] == 103.0
    assert trade["exit_reason"] == "ZLEMA_DOWN"
    assert trade["holding_trading_days"] == 2


def test_open_trade_is_not_in_completed_trades():
    frame = _signal_frame().iloc[:4].copy()
    completed, opened = m.simulate_stock(
        "TEST", frame, pd.Timestamp("2024-03-01"), pd.Timestamp("2024-03-31")
    )
    assert completed.empty
    assert len(opened) == 1


def test_simulation_records_rs_only_and_combined_exit_reasons():
    rs_only = _signal_frame()
    rs_only.loc[3, "rs_ema9_rising"] = False
    completed, _ = m.simulate_stock(
        "TEST", rs_only, pd.Timestamp("2024-03-01"), pd.Timestamp("2024-03-31")
    )
    assert completed.iloc[0]["exit_reason"] == "RS_NOT_RISING"

    combined = _signal_frame()
    combined.loc[3, "zlema25"] = 99.0
    combined.loc[3, "rs_ema9_rising"] = False
    completed, _ = m.simulate_stock(
        "TEST", combined, pd.Timestamp("2024-03-01"), pd.Timestamp("2024-03-31")
    )
    assert completed.iloc[0]["exit_reason"] == "ZLEMA_AND_RS"


def test_summary_counts_wins_zeros_and_compounds():
    trades = pd.DataFrame(
        {
            "symbol": ["A", "A", "A"],
            "return_pct": [10.0, -5.0, 0.0],
            "holding_trading_days": [2, 4, 3],
        }
    )
    row = m.summarize_trades(trades, ["A"]).set_index("symbol").loc["A"]
    assert row["wins"] == 1
    assert row["losses"] == 1
    assert row["zeros"] == 1
    assert row["win_rate_pct"] == pytest.approx(100 / 3)
    assert row["compounded_return_pct"] == pytest.approx(4.5)


def _empty_result(symbols=None):
    symbols = symbols or ["TEST"]
    trades = pd.DataFrame(columns=m.TRADE_COLUMNS)
    return {
        "symbols": symbols,
        "start": pd.Timestamp("2024-01-01"),
        "end": pd.Timestamp("2024-12-31"),
        "trades": trades,
        "open_trades": pd.DataFrame(columns=m.OPEN_COLUMNS),
        "summary": m.summarize_trades(trades, symbols),
        "skipped": [],
    }


def test_build_markdown_has_disclaimer_and_open_section():
    text = m.build_markdown(_empty_result())
    assert "SEBI registered" in text
    assert "Open Trades" in text
    assert "TEST" in text
    assert "combined compounded return is a strategy-sequence diagnostic" in text.lower()


def test_write_outputs_always_writes_csv_headers(tmp_path):
    trades_path, open_path, report_path = m.write_outputs(_empty_result(), tmp_path)
    assert trades_path.name == "daily_zlema25_weekly_rs_trades.csv"
    assert open_path.name == "daily_zlema25_weekly_rs_open.csv"
    assert report_path.name == "daily_zlema25_weekly_rs_summary.md"
    assert trades_path.read_text(encoding="utf-8").startswith("symbol,entry_date")
    assert open_path.read_text(encoding="utf-8").startswith("symbol,entry_date")
    assert "SEBI registered" in report_path.read_text(encoding="utf-8")


def test_run_backtest_rejects_backwards_dates():
    with pytest.raises(ValueError, match="start date"):
        m.run_backtest(
            ["TEST"], pd.Timestamp("2024-02-01"), pd.Timestamp("2024-01-01")
        )


def test_run_backtest_reports_missing_stock(monkeypatch):
    benchmark = _ohlc([200.0 + i for i in range(80)])
    calls = []

    def fake_load(symbol, lookback=10000):
        calls.append((symbol, lookback))
        return benchmark if symbol == m.BENCHMARK else None

    monkeypatch.setattr(m, "load_ohlc", fake_load)
    result = m.run_backtest(
        ["MISSING"], pd.Timestamp("2024-01-01"), pd.Timestamp("2024-12-31")
    )
    assert result["skipped"] == [
        {"symbol": "MISSING", "reason": "OHLC data unavailable"}
    ]
    assert result["summary"]["symbol"].tolist() == ["MISSING", "COMBINED"]
    assert calls == [(m.BENCHMARK, 10000), ("MISSING", 10000)]


def test_run_backtest_requires_benchmark(monkeypatch):
    monkeypatch.setattr(m, "load_ohlc", lambda symbol, lookback=10000: None)
    with pytest.raises(ValueError, match="benchmark"):
        m.run_backtest(
            ["TEST"], pd.Timestamp("2024-01-01"), pd.Timestamp("2024-12-31")
        )


def test_run_backtest_reports_insufficient_stock(monkeypatch):
    benchmark = _ohlc([200.0 + i for i in range(80)])
    insufficient = _ohlc([100.0 + i for i in range(m.MIN_DAILY_BARS - 1)])
    monkeypatch.setattr(
        m,
        "load_ohlc",
        lambda symbol, lookback=10000: benchmark
        if symbol == m.BENCHMARK
        else insufficient,
    )
    result = m.run_backtest(
        ["SHORT"], pd.Timestamp("2024-01-01"), pd.Timestamp("2024-12-31")
    )
    assert result["skipped"] == [
        {"symbol": "SHORT", "reason": "Insufficient OHLC history"}
    ]


def test_main_returns_two_for_validation_errors(monkeypatch, capsys):
    monkeypatch.setattr(
        "sys.argv",
        [
            "backtest_daily_zlema25_weekly_rs.py",
            "test",
            "--start",
            "2024-02-01",
            "--end",
            "2024-01-01",
        ],
    )
    assert m.main() == 2
    assert "start date" in capsys.readouterr().err
