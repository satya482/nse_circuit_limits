import json

from tests.test_union_chart_dashboard import _run_generated_js_function
from union_chart_dashboard import build_html


def calculate(highs, lows=None):
    lows = lows if lows is not None else [1] * len(highs)
    bars = [[str(i), 0, h, lows[i], 0, 0] for i, h in enumerate(highs)]
    return _run_generated_js_function(
        build_html([], '2026-09-30'),
        'function darvasLineData(bars) {',
        'function rebuildDarvas(entry)',
        f'darvasLineData({json.dumps(bars)})',
    )


def test_confirmation_three_bars_after_high_and_frozen_bottom():
    result = calculate([5, 4, 4, 4, 4, 10, 9, 8, 7, 6],
                       [3, 3, 3, 3, 3, 4, 5, 2, 4, 0])
    assert result['top'][:8] == [{'time': str(i)} for i in range(8)]
    assert result['top'][8:] == [{'time': '8', 'value': 10}, {'time': '9', 'value': 10}]
    assert result['bottom'][8:] == [{'time': '8', 'value': 2}, {'time': '9', 'value': 2}]


def test_equal_high_prevents_confirmation_and_new_high_restarts_clock():
    assert all('value' not in p for p in calculate([5, 4, 4, 4, 4, 10, 10, 8, 7, 6])['top'])
    result = calculate([5, 4, 4, 4, 4, 10, 11, 9, 8, 7])
    assert 'value' not in result['top'][8]
    assert result['top'][9]['value'] == 11


def test_empty_flat_and_short_data():
    assert calculate([]) == {'top': [], 'bottom': []}
    assert all('value' not in p for p in calculate([5] * 10)['top'])
    assert all('value' not in p for p in calculate([5, 6, 7])['top'])


def test_control_enabled_only_for_requested_dashboard():
    html = build_html([], '2026-09-30', darvas_enabled=True)
    assert 'id="darvasVisible" checked' in html
    assert 'darvasVisible: true' in html
    default = build_html([], '2026-09-30')
    assert 'id="darvasVisible"' not in default
    assert 'darvasVisible: false' in default



def test_toggle_removes_and_restores_both_lines_without_duplicates():
    html = build_html([], '2026-09-30', darvas_enabled=True)
    result = _run_generated_js_function(
        html, 'function darvasLineData(bars) {', 'function applyVolumeState(entry)',
        """(() => {
          globalThis.uiState = {darvasVisible: true};
          const live = new Set();
          const entry = {darvasSeries: [], record: {bars: []}, chart: {
            addLineSeries(options) { const s = {options, setData(data) {this.data = data;}}; live.add(s); return s; },
            removeSeries(s) { live.delete(s); }
          }};
          rebuildDarvas(entry);
          const colors = entry.darvasSeries.map(s => s.options.color);
          const counts = [live.size];
          uiState.darvasVisible = false; rebuildDarvas(entry); counts.push(live.size);
          uiState.darvasVisible = true; rebuildDarvas(entry); counts.push(live.size);
          rebuildDarvas(entry); counts.push(live.size);
          return {counts, colors};
        })()""",
    )
    assert result == {'counts': [2, 0, 2, 2], 'colors': ['#008000', '#ff0000']}
    assert "rebuildDarvas(entry);" in html.split('function buildChart(symbol)', 1)[1]
    assert "darvasControl.addEventListener('change'" in html
