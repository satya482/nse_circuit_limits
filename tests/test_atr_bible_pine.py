from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OVERLAY = ROOT / "pine_scripts" / "ATR_Bible_Overlay.pine"
PANEL = ROOT / "pine_scripts" / "ATR_Bible_Panel.pine"


def _source(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_overlay_has_all_seven_alerts_and_hidden_values():
    source = _source(OVERLAY)

    assert source.count("alertcondition(") == 7
    for signal in (
        "SQUEEZE_EXTREME",
        "SQUEEZE_3STAR",
        "EXPANSION_START",
        "EXIT_WARN",
        "DISTRIBUTION",
        "OVEREXTENDED",
        "CIRCUIT_SUSPECT",
    ):
        assert signal in source
    for title in ("CR", "ATR10", "StopLvl", "Shares"):
        assert f'"{title}"' in source
    assert source.count("display=display.none") == 4


def test_overlay_clears_dashboard_when_hidden():
    source = _source(OVERLAY)

    assert "if barstate.islast and not showDashboard" in source
    assert source.count("table.clear(dash, 0, 0, 1, 12)") == 2


def test_overlay_suppresses_trade_math_when_atr_is_unreliable():
    source = _source(OVERLAY)

    assert "tradeMathValid = not circuitSuspect" in source
    assert "if (showStops or showTargets) and tradeMathValid" in source
    assert 'tradeMathValid ? str.tostring(shares)' in source


def test_panel_contains_the_required_volatility_views():
    source = _source(PANEL)

    assert source.startswith("//@version=6")
    assert source.count("indicator(") == 1
    assert 'overlay          = false' in source
    assert 'fill(atr10Plot, atr50Plot' in source
    assert 'plot(cr, "Compression Ratio"' in source
    assert source.count("hline(") == 6
    assert 'plot(atrDelta, "ATR Delta", style=plot.style_histogram' in source
    assert "var label verdictLabel = na" in source


def test_overlay_and_panel_share_atr_and_cr_defaults():
    overlay = _source(OVERLAY)
    panel = _source(PANEL)

    shared_lines = (
        'atrFast = input.int(10, "ATR Fast Period"',
        'atrSlow = input.int(50, "ATR Slow Period"',
        'crExtreme  = input.float(0.50, "Extreme Squeeze Level"',
        'crBuild    = input.float(0.70, "Squeeze Building Level"',
        'crExpand   = input.float(1.00, "Expansion Start Level"',
        'crExtended = input.float(1.50, "Expanded Level"',
        'crDanger   = input.float(2.00, "Overextended / Danger Level"',
        "atr10 = ta.atr(atrFast)",
        "atr50 = ta.atr(atrSlow)",
        "cr = atr50 > 0 ? atr10 / atr50 : na",
    )
    for line in shared_lines:
        assert line in overlay
        assert line in panel
