import pandas as pd

from sector_sync import add_sector_scores, load_sector_map


def test_load_sector_map_returns_empty_when_csv_missing():
    assert load_sector_map("does_not_exist.csv") == {}


def test_add_sector_scores_returns_unchanged_when_rows_empty():
    result = add_sector_scores(pd.DataFrame())

    assert result.empty


def test_add_sector_scores_scores_full_participation_sector_100():
    rows = pd.DataFrame(
        [
            {"symbol": "AAA", "close_gt_ema20": True, "rs_trend": "UP", "ics": 80},
            {"symbol": "BBB", "close_gt_ema20": True, "rs_trend": "UP", "ics": 90},
        ]
    )
    sector_map = {"AAA": "Banking", "BBB": "Banking"}

    result = add_sector_scores(rows, sector_map)

    assert (result["sector"] == "Banking").all()
    assert (result["sector_score"] == 100.0).all()


def test_add_sector_scores_unmapped_symbol_falls_back_to_unknown_sector():
    rows = pd.DataFrame(
        [{"symbol": "ZZZ", "close_gt_ema20": False, "rs_trend": "FLAT", "ics": 20}]
    )

    result = add_sector_scores(rows, sector_map={})

    assert result.iloc[0]["sector"] == "UNKNOWN"
    assert result.iloc[0]["sector_score"] == 0.0


def test_add_sector_scores_partial_participation_averages_across_three_factors():
    rows = pd.DataFrame(
        [
            {"symbol": "AAA", "close_gt_ema20": True, "rs_trend": "UP", "ics": 80},
            {"symbol": "BBB", "close_gt_ema20": False, "rs_trend": "FLAT", "ics": 20},
        ]
    )
    sector_map = {"AAA": "IT", "BBB": "IT"}

    result = add_sector_scores(rows, sector_map)

    # 1 of 2 above EMA20, 1 of 2 RS up, 1 of 2 ICS>=70 -> (0.5+0.5+0.5)/3*100 = 50.0
    assert (result["sector_score"] == 50.0).all()
