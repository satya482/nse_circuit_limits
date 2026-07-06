import pandas as pd

from capital import regime_throttle as rt


def _history_csv(tmp_path, rows):
    path = tmp_path / "breadth_history.csv"
    pd.DataFrame(rows).to_csv(path, index=False)
    return str(path)


def test_classify_regime_green():
    assert rt.classify_regime(ratio_5d=1.8, pct_above_sma200=65.0, sma200_falling=False) == "GREEN"


def test_classify_regime_green_boundary():
    assert rt.classify_regime(ratio_5d=1.6, pct_above_sma200=50.0, sma200_falling=False) == "GREEN"
    assert rt.classify_regime(ratio_5d=1.6, pct_above_sma200=80.0, sma200_falling=False) == "GREEN"


def test_classify_regime_red_low_ratio():
    assert rt.classify_regime(ratio_5d=0.5, pct_above_sma200=65.0, sma200_falling=False) == "RED"


def test_classify_regime_red_sma200_falling_and_low():
    assert rt.classify_regime(ratio_5d=1.0, pct_above_sma200=15.0, sma200_falling=True) == "RED"


def test_classify_regime_neutral_sma200_low_but_not_falling():
    # below 20% but NOT falling -> not RED per spec (RED needs falling), falls to NEUTRAL
    assert rt.classify_regime(ratio_5d=1.0, pct_above_sma200=15.0, sma200_falling=False) == "NEUTRAL"


def test_classify_regime_neutral_default():
    assert rt.classify_regime(ratio_5d=1.0, pct_above_sma200=40.0, sma200_falling=False) == "NEUTRAL"


def test_sma200_falling_true_when_lower_than_lookback():
    df = pd.DataFrame({
        "date": ["2026-06-25", "2026-06-26", "2026-06-29", "2026-06-30", "2026-07-01", "2026-07-02"],
        "universe_tag": ["breadth_broad"] * 6,
        "pct_above_sma200": [70.0, 68.0, 65.0, 60.0, 55.0, 50.0],
    })
    assert rt.sma200_falling(df, "breadth_broad", "2026-07-02", lookback=5) is True


def test_sma200_falling_false_when_flat_or_rising():
    df = pd.DataFrame({
        "date": ["2026-06-25", "2026-06-26", "2026-06-29", "2026-06-30", "2026-07-01", "2026-07-02"],
        "universe_tag": ["breadth_broad"] * 6,
        "pct_above_sma200": [50.0, 52.0, 55.0, 58.0, 60.0, 62.0],
    })
    assert rt.sma200_falling(df, "breadth_broad", "2026-07-02", lookback=5) is False


def test_sma200_falling_false_when_insufficient_history():
    df = pd.DataFrame({
        "date": ["2026-07-02"],
        "universe_tag": ["breadth_broad"],
        "pct_above_sma200": [15.0],
    })
    assert rt.sma200_falling(df, "breadth_broad", "2026-07-02", lookback=5) is False


def test_regime_for_date_green(tmp_path):
    path = _history_csv(tmp_path, [
        {"date": "2026-06-25", "universe_tag": "breadth_broad", "ratio_5d": 1.7, "pct_above_sma200": 60.0},
        {"date": "2026-07-02", "universe_tag": "breadth_broad", "ratio_5d": 1.8, "pct_above_sma200": 65.0},
    ])
    result = rt.regime_for_date("2026-07-02", history_path=path)
    assert result == {"regime": "GREEN", "max_slots": 6, "time_stop_mode": "standard"}


def test_regime_for_date_red(tmp_path):
    path = _history_csv(tmp_path, [
        {"date": "2026-06-25", "universe_tag": "breadth_broad", "ratio_5d": 0.9, "pct_above_sma200": 30.0},
        {"date": "2026-07-02", "universe_tag": "breadth_broad", "ratio_5d": 0.5, "pct_above_sma200": 25.0},
    ])
    result = rt.regime_for_date("2026-07-02", history_path=path)
    assert result == {"regime": "RED", "max_slots": 0, "time_stop_mode": "halted"}


def test_regime_for_date_missing_row_defaults_neutral(tmp_path):
    path = _history_csv(tmp_path, [
        {"date": "2026-06-25", "universe_tag": "breadth_broad", "ratio_5d": 1.7, "pct_above_sma200": 60.0},
    ])
    result = rt.regime_for_date("2026-07-02", history_path=path)
    assert result == {"regime": "NEUTRAL", "max_slots": 3, "time_stop_mode": "bar3_only"}
