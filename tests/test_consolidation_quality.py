import pandas as pd
from consolidation import quality


def test_quality_score_perfect_setup_scores_100():
    score = quality.quality_score(
        bb_width_percentile=0.0,
        ema_stage="STAGE_2_COMPRESSED",
        vol_percentile=0.0,
        rs_char="CHAR_4_RISING",
        cmf=0.15,
        deliv_trend_label="RISING",
    )
    assert score == 100.0


def test_quality_score_worst_setup_scores_zero():
    score = quality.quality_score(
        bb_width_percentile=20.0,
        ema_stage="STAGE_3_DIVERGING",
        vol_percentile=20.0,
        rs_char="CHAR_1_DECLINING",
        cmf=-0.05,
        deliv_trend_label="BELOW",
    )
    assert score == 0.0


def test_quality_score_unknown_deliv_trend_scores_zero_points_for_that_component():
    score = quality.quality_score(
        bb_width_percentile=0.0,
        ema_stage="STAGE_2_COMPRESSED",
        vol_percentile=0.0,
        rs_char="CHAR_4_RISING",
        cmf=0.15,
        deliv_trend_label=None,
    )
    assert score == 90.0  # 100 minus the 10-pt delivery component


def test_deliv_trend_rising_when_ma20_well_above_baseline(monkeypatch):
    import ohlc_db
    dates = pd.date_range("2026-01-01", periods=120, freq="D")
    pcts = [20.0] * 100 + [35.0] * 20  # recent 20d well above the 120d median
    df = pd.DataFrame({"date": dates, "deliv_pct": pcts})
    monkeypatch.setattr(ohlc_db, "load_delivery", lambda symbol, lookback=120, db_path=None: df)
    assert quality.deliv_trend("TEST") == "RISING"


def test_deliv_trend_none_on_insufficient_history(monkeypatch):
    import ohlc_db
    monkeypatch.setattr(ohlc_db, "load_delivery", lambda symbol, lookback=120, db_path=None: None)
    assert quality.deliv_trend("TEST") is None
