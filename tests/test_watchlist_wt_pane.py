import json
import math
import shutil
import subprocess

import pandas as pd
import pytest

import union_chart_dashboard as dashboard


def prices(flat=False):
    values = [100.0 if flat else 100 + 8 * math.sin(i / 5) for i in range(150)]
    return pd.DataFrame(dict(date=pd.date_range('2026-01-01', periods=150),
                             open=values, high=values, low=values, close=values,
                             volume=[1000] * 150))


def test_wt_series_matches_pine_formula_and_all_crosses():
    df = prices()
    pane = dashboard.compute_wt_pane_series(df)
    # Independent recursive implementation of Satya_All_Panel.pine defaults.
    esa = deviation = wt = None
    expected = []
    for value in df.close:
        esa = value if esa is None else esa + 2 / 11 * (value - esa)
        delta = abs(value - esa)
        deviation = delta if deviation is None else deviation + 2 / 11 * (delta - deviation)
        ci = (value - esa) / (0.015 * deviation) if deviation else 0
        wt = ci if wt is None else wt + 2 / 22 * (ci - wt)
        expected.append(wt)
    signal = [None] * 3 + [sum(expected[i-3:i+1]) / 4 for i in range(3, len(expected))]
    assert pane['wt1'] == pytest.approx(expected)
    assert pane['wt2'][:3] == [None] * 3
    assert pane['wt2'][3:] == pytest.approx(signal[3:])
    crosses = [None] * len(expected)
    for i in range(4, len(expected)):
        if expected[i] > signal[i] and expected[i-1] <= signal[i-1]:
            crosses[i] = 'wt_bull'
        elif expected[i] < signal[i] and expected[i-1] >= signal[i-1]:
            crosses[i] = 'wt_bear'
    assert pane['crosses'] == crosses
    assert {'wt_bull', 'wt_bear'} <= set(crosses)
    json.dumps(pane, allow_nan=False)


def test_flat_wt_has_no_false_crosses():
    pane = dashboard.compute_wt_pane_series(prices(flat=True))
    assert pane['wt1'] == [0] * 150
    assert pane['wt2'] == [None] * 3 + [0] * 147
    assert pane['crosses'] == [None] * 150


def test_wt_data_and_html_are_opt_in():
    df = prices()
    old, _ = dashboard.build_chart_data({'TEST': df}, {'TEST': 'NSE'})
    assert 'wt_pane' not in old[0]
    records, skipped = dashboard.build_chart_data({'TEST': df}, {'TEST': 'NSE'}, include_wt_pane=True)
    assert skipped == 0
    assert len(records[0]['wt_pane']['wt1']) == len(records[0]['bars'])
    old_html = dashboard.build_html(old, '2026-09-21')
    assert 'id="wtPaneVisible"' not in old_html
    assert 'id="wtpane-TEST"' not in old_html
    html = dashboard.build_html(records, '2026-09-21', wt_pane_enabled=True)
    assert 'id="wtPaneVisible" checked' in html
    assert html.index('id="rspane-TEST"') < html.index('id="wtpane-TEST"')
    assert 'SEBI registered' in html


def test_generated_wt_chart_renders_levels_markers_and_sync():
    node = shutil.which('node')
    if not node:
        pytest.skip('Node is needed for generated JavaScript verification')
    html = dashboard.build_html([], '2026-09-21', wt_pane_enabled=True)
    body = html.split('function buildWtPane(entry) {', 1)[1].split('function applyControls()', 1)[0]
    script = '''
const assert = require('assert');
let ranges=[], levels=[], series=[], chartOptions, resizeCallback;
const paneChart = {
  addLineSeries(options) { const s={ options, setData(x){this.data=x;}, setMarkers(x){this.markers=x;}, createPriceLine(x){levels.push(x);} }; series.push(s); return s; },
  timeScale(){return {setVisibleLogicalRange(r){ranges.push(r);}};},
  subscribeCrosshairMove(fn){this.move=fn;}, setCrosshairPosition(){}, clearCrosshairPosition(){}, applyOptions(){}
};
const LightweightCharts={createChart(el, opts){chartOptions=opts;return paneChart;},LineStyle:{Dashed:2,Solid:0}};
const element={clientWidth:640,clientHeight:380};
const document={getElementById(){return element;}};
const ResizeObserver=class {constructor(fn){resizeCallback=fn;} observe(){}};
function fixedLogicalRange(){return {from:0,to:4};}
function syncWtCrosshair(){}
function alignWtPaneAxes(){}
function requestAnimationFrame(fn){fn();}
const entry={record:{symbol:'TEST',bars:[['2026-01-01'],['2026-01-02'],['2026-01-03']],wt_pane:{wt1:[null,2,-2],wt2:[null,1,-1],crosses:[null,'wt_bull','wt_bear']}},chart:{timeScale(){return {subscribeVisibleLogicalRangeChange(fn){entry.range=fn;}};}}};
''' + 'function buildWtPane(entry) {' + body + '''
buildWtPane(entry);
assert.equal(series.length,2);
assert.deepEqual(series[0].options.autoscaleInfoProvider(()=>null),{priceRange:{minValue:-60,maxValue:60}});
assert.deepEqual(series[0].options.autoscaleInfoProvider(()=>({priceRange:{minValue:-10,maxValue:20}})),{priceRange:{minValue:-60,maxValue:60}});
assert.deepEqual(series[0].options.autoscaleInfoProvider(()=>({priceRange:{minValue:-90,maxValue:100}})),{priceRange:{minValue:-90,maxValue:100}});
assert.deepEqual(series[0].data,[{time:'2026-01-01'},{time:'2026-01-02',value:2},{time:'2026-01-03',value:-2}]);
assert.deepEqual(levels.map(x=>x.price),[0,53,60,-53,-60]);
assert.deepEqual(series[1].markers.map(x=>x.color),['#00ff00','#ff0000']);
assert.deepEqual(series[1].markers.map(x=>x.shape),['arrowUp','arrowDown']);
assert.equal(chartOptions.handleScroll,false);
entry.range({from:1,to:2});
assert.deepEqual(ranges[ranges.length-1],{from:1,to:2});
resizeCallback();
'''
    result = subprocess.run([node, '-e', script], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr


def test_wt_crosshair_uses_each_panes_value_and_clears_in_gaps():
    node = shutil.which('node')
    if not node:
        pytest.skip('Node is needed for generated JavaScript verification')
    html = dashboard.build_html([], '2026-09-21', wt_pane_enabled=True)
    fn = html.split('function syncWtCrosshair(entry, wtSeries) {', 1)[1].split('function alignWtPaneAxes(entry)', 1)[0]
    script = '''
const assert=require('assert');
function chart(){return {subscribeCrosshairMove(fn){this.move=fn;},setCrosshairPosition(value,time,series){this.last={value,time,series};},clearCrosshairPosition(){this.last=null;}};}
const entry={chart:chart(),wtChart:chart(),rsChart:chart(),candleSeries:'price',rsLineSeries:'rs',record:{bars:[['2026-01-01',0,0,0,100],['2026-01-02',0,0,0,110]],wt_pane:{wt1:[null,25]},rs_pane:{rs_line:[1000,1100]}}};
''' + 'function syncWtCrosshair(entry, wtSeries) {' + fn + '''
syncWtCrosshair(entry,'wt');
entry.chart.move({time:'2026-01-02'});
assert.deepEqual(entry.wtChart.last,{value:25,time:'2026-01-02',series:'wt'});
assert.equal(entry.rsChart.last.value,1100);
entry.wtChart.move({time:'2026-01-02'});
assert.equal(entry.chart.last.value,110);
entry.rsChart.move({time:'2026-01-01'});
assert.equal(entry.wtChart.last,null);
entry.wtChart.move({});
assert.equal(entry.chart.last,null);
assert.equal(entry.rsChart.last,null);
'''
    result = subprocess.run([node, '-e', script], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr


def test_missing_benchmark_dates_preserve_shared_pane_indexes():
    node = shutil.which('node')
    if not node:
        pytest.skip('Node is needed for generated JavaScript verification')
    html = dashboard.build_html([], '2026-09-21', wt_pane_enabled=True)
    fn = html.split('function alignPaneDates(bars, points) {', 1)[1].split('function syncWtCrosshair', 1)[0]
    script = "const assert=require('assert');\nfunction alignPaneDates(bars, points) {" + fn + '''
assert.deepEqual(alignPaneDates([['d1'],['d2'],['d3']],[{time:'d2',value:10,color:'blue'}]),
  [{time:'d1'},{time:'d2',value:10,color:'blue'},{time:'d3'}]);
'''
    result = subprocess.run([node, '-e', script], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr


def test_axis_alignment_uses_widest_axis_and_avoids_update_loop():
    node = shutil.which('node')
    if not node:
        pytest.skip('Node is needed for generated JavaScript verification')
    html = dashboard.build_html([], '2026-09-21', wt_pane_enabled=True)
    fn = html.split('function alignWtPaneAxes(entry) {', 1)[1].split('function buildWtPane(entry)', 1)[0]
    script = '''
const assert=require('assert'); let calls=0;
function chart(width){return {priceScale(){return {width(){return width;},applyOptions(opts){width=opts.minimumWidth;calls++;}};}};}
const entry={chart:chart(85),rsChart:chart(68),wtChart:chart(52)};
''' + 'function alignWtPaneAxes(entry) {' + fn + '''
alignWtPaneAxes(entry);
assert.equal(entry.chart.priceScale().width(),85);
assert.equal(entry.rsChart.priceScale().width(),85);
assert.equal(entry.wtChart.priceScale().width(),85);
alignWtPaneAxes(entry); assert.equal(calls,3);
'''
    result = subprocess.run([node, '-e', script], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr


def test_wt_toggle_hides_all_panes_and_restores_without_rebuilding():
    node = shutil.which('node')
    if not node:
        pytest.skip('Node is needed for generated JavaScript verification')
    html = dashboard.build_html([], '2026-09-21', wt_pane_enabled=True)
    listener = html.split("document.getElementById('wtPaneVisible').addEventListener", 1)[1].split('</script>', 1)[0]
    script = '''
const assert=require('assert');
let callback;
const wraps=[{hidden:false},{hidden:false}];
const document={getElementById(){return {addEventListener(name,fn){callback=fn;}};},querySelectorAll(){return wraps;}};
''' + "document.getElementById('wtPaneVisible').addEventListener" + listener + '''
callback({target:{checked:false}}); assert(wraps.every(w=>w.hidden));
callback({target:{checked:true}}); assert(wraps.every(w=>!w.hidden));
'''
    result = subprocess.run([node, '-e', script], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
