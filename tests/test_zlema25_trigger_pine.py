"""Local checks, not Pine compilation or TradingView runtime tests."""
from pathlib import Path
import math
import re
import pytest

SOURCE = Path(__file__).resolve().parents[1] / "pine_scripts/ZLEMA25_Uptrend_Price.pine"


def test_upcoming_trigger_uses_last_confirmed_state():
    source = SOURCE.read_text(encoding="utf-8")
    assert "baseZlema = barstate.isconfirmed ? dailyCloseZlema : dailyCloseZlema[1]" in source
    assert "basePriorZlema = barstate.isconfirmed ? dailyCloseZlema[1] : dailyCloseZlema[2]" in source
    assert "laggedClose = barstate.isconfirmed ? close[11] : close[12]" in source
    assert "waitingForFirstUp = baseZlema <= basePriorZlema" in source
    assert "and waitingForFirstUp and not na(dailyTurnPrice)" in source
    assert "startPrice" not in source


@pytest.mark.parametrize("baseZlema,laggedClose,tick", [(100,90,.05),(123.47,98.12,.01),(40,70,.05)])
def test_price_is_first_tick_that_would_make_zlema_rise(baseZlema, laggedClose, tick):
    source = SOURCE.read_text(encoding="utf-8")
    boundary_expr = re.search(r"^dailyTurnBoundary = (.+)$", source, re.M)[1]
    boundary = eval(boundary_expr, {"__builtins__": {}}, dict(baseZlema=baseZlema, laggedClose=laggedClose))
    price_expr = re.search(r"^dailyTurnPrice = (.+)$", source, re.M)[1]
    price_expr = price_expr.replace("math.floor", "floor").replace("syminfo.mintick", "tick")
    price = eval(price_expr, {"__builtins__": {}}, dict(dailyTurnBoundary=boundary, floor=math.floor, tick=tick))
    alpha = 2/26
    def slope(candidate):
        return alpha * (2*candidate - laggedClose) + (1-alpha)*baseZlema - baseZlema
    assert slope(boundary) == pytest.approx(0, abs=1e-12)
    assert slope(price) > 0
    assert slope(price-tick) <= 1e-12


def test_projection_and_cleanup():
    source = SOURCE.read_text(encoding="utf-8")
    assert "timeframe.isdaily and timeframe.multiplier == 1" in source
    assert "projectionEnd = time + 14 * 24 * 60 * 60 * 1000" in source
    assert "line.delete(dailyTurnLine)" in source
    assert "label.delete(dailyTurnLabel)" in source
    assert "xloc=xloc.bar_time" in source
