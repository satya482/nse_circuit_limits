"""Local formula checks; these do not compile or execute Pine Script."""
import math
import re
from pathlib import Path

import pytest


SOURCE = Path(__file__).resolve().parents[1] / "pine_scripts/ZLEMA25_Uptrend_Price.pine"


@pytest.mark.parametrize("previous,lagged,tick", [(100, 90, .05), (123.47, 98.12, .01), (40, 70, .05)])
def test_trigger_is_first_tradable_close_with_positive_zlema_slope(previous, lagged, tick):
    source = SOURCE.read_text(encoding="utf-8")
    boundary = re.search(r"^dailyTurnBoundary = (.+)$", source, re.M)
    assert boundary, "Missing daily turn-up boundary"
    expression = boundary[1].replace("dailyCloseZlema[1]", "previous").replace("close[12]", "lagged")
    threshold = eval(expression, {"__builtins__": {}}, dict(previous=previous, lagged=lagged))
    trigger_expression = re.search(r"^dailyTurnPrice = (.+)$", source, re.M)[1]
    trigger_expression = trigger_expression.replace("math.floor", "floor").replace("syminfo.mintick", "tick")
    trigger = eval(trigger_expression, {"__builtins__": {}}, dict(dailyTurnBoundary=threshold, floor=math.floor, tick=tick))
    alpha = 2 / 26
    def next_zlema(close):
        return alpha * (2 * close - lagged) + (1 - alpha) * previous
    assert next_zlema(threshold) == pytest.approx(previous)
    assert next_zlema(trigger) > previous
    assert next_zlema(trigger - tick) <= previous + 1e-12


def test_projection_is_daily_close_only_and_exactly_fourteen_calendar_days():
    source = SOURCE.read_text(encoding="utf-8")
    assert "dailyCloseZlema = ta.ema(2 * close - close[12], 25)" in source
    assert "timeframe.isdaily and timeframe.multiplier == 1" in source
    assert "projectionEnd = time + 14 * 24 * 60 * 60 * 1000" in source
    assert "line.delete(dailyTurnLine)" in source
    assert "label.delete(dailyTurnLabel)" in source
    assert "xloc=xloc.bar_time" in source
