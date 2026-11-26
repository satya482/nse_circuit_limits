from pathlib import Path

import pytest
import shutil
import subprocess

import cluster_dashboard as cluster


def report(count=31):
    return '# Sector Rotation — 2026-11-25\n\n## ZL Breadth per Group\n\n' + '\n'.join(
        f'| Sector {i} | 2/4 | ↑ 50% | 3d | +2.0% | ⚡ A, B | A, B |'
        for i in range(count)
    )


def test_full_table_and_source_date():
    page = cluster.build_html(report())
    assert page.count('<tr data-group>') == 31
    assert '31 groups ≥40% rising' in page
    assert 'Sector 30' in page
    assert '2026-11-25' in page
    assert '⚡ A, B' in page
    assert 'SEBI registered' in page


def test_sorting_buttons_and_numeric_order():
    page = cluster.build_html(report(2))
    assert page.count('data-sort-column=') == 10
    assert 'aria-sort="none"' in page
    assert 'Click a column heading to sort' in page
    node = shutil.which('node')
    assert node, 'Node is required to validate dashboard sorting'
    script = page.split('<script>')[1].split('</script>')[0]
    check = '''
const assert = require('node:assert/strict');
assert.equal(clusterSortValue('↑ 80%', 2), 80);
assert.equal(clusterSortValue('-10.5%', 4), -10.5);
assert.equal(clusterSortValue('12/20', 1), 12);
assert.equal(clusterSortValue('3d', 3), 3);
assert.equal(clusterSortValue('—', 3), null);
assert.equal(clusterSortValue('12/20', 7), 12);
assert.equal(clusterSortValue('66.7%', 8), 66.7);
assert.equal(clusterSortValue('3', 9), 3);
function row(values) { return { cells: values.map(textContent => ({textContent})) }; }
const rows = [row(['Nine','9/12','↑ 9%','9d','+9%','—','Z','9/100','9%','9']),
              row(['Eighty','80/100','▲ 80%','80d','+80%','⚡ A','A','80/100','80%','80']),
              row(['Missing','—','—','—','—','—','—','—','—','—'])];
const buttons = [];
const headers = Array.from({length:10},()=>({setAttribute(k,v){this[k]=v;}}));
const tbody = { rows, append(...sorted){ this.rows = sorted; } };
const table = {tBodies:[tbody], tHead:{rows:[{cells:headers}]}, dataset:{},
               querySelectorAll(){return buttons;}};
sortClusterTable(table, 2);
assert.deepEqual(tbody.rows.map(r=>r.cells[0].textContent), ['Nine','Eighty','Missing']);
sortClusterTable(table, 2);
assert.deepEqual(tbody.rows.map(r=>r.cells[0].textContent), ['Eighty','Nine','Missing']);
assert.equal(headers[2]['aria-sort'],'descending');
sortClusterTable(table, 4);
assert.equal(headers[2]['aria-sort'],'none');
sortClusterTable(table, 8);
assert.deepEqual(tbody.rows.map(r=>r.cells[0].textContent), ['Nine','Eighty','Missing']);
sortClusterTable(table, 8);
assert.deepEqual(tbody.rows.map(r=>r.cells[0].textContent), ['Eighty','Nine','Missing']);
'''
    result = subprocess.run([node, '-e', 'global.document={querySelectorAll:()=>[]};\n' + script + check], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr


def test_weekly_rs_report_fields_and_legacy_fallback():
    content = report(1).replace('| A, B |', '| A, B | 2/3 | 66.7% | 1 |')
    page = cluster.build_html(content)
    assert '<td>2/3</td><td>66.7%</td><td>1</td>' in page
    legacy = cluster.build_html(report(1))
    assert '<td>—</td><td>—</td><td>—</td>' in legacy


def test_empty_and_escaped_content():
    assert 'No groups with ≥40% ZL rising' in cluster.build_html(report(0))
    page = cluster.build_html(report(1).replace('Sector 0', '<script>bad</script>'))
    assert '<script>bad</script>' not in page
    assert '&lt;script&gt;bad&lt;/script&gt;' in page


def test_missing_or_invalid_source_preserves_output(tmp_path):
    source = tmp_path / 'source.md'
    output = tmp_path / 'cluster.html'
    output.write_text('previous')
    with pytest.raises(FileNotFoundError):
        cluster.generate(source, output)
    source.write_text('invalid')
    with pytest.raises(ValueError):
        cluster.generate(source, output)
    assert output.read_text() == 'previous'


def test_pipeline_refreshes_source_then_page_before_dashboard():
    root = Path(__file__).resolve().parents[1]
    pipeline = (root / 'run_all_scanners.ps1').read_text()
    runner = (root / 'run_sector_rotation.ps1').read_text()
    assert pipeline.index('Run-Scanner "SectorRotation"') < pipeline.index('Run-Scanner "Dashboard"')
    assert runner.index('sector_rotation_scanner.py') < runner.index('cluster_dashboard.py') < runner.index('--- Git commit+push ---')
    assert 'add sector_rotation_scans/ cluster.html' in runner


def test_pending_members_and_maintenance_changes_are_visible():
    coverage = {'eligible': 10, 'ready': 7, 'discovered_at': '2026-11-26',
                'groups_updated': '2026-11-23', 'pending': [
                    {'symbol': 'NEWIPO', 'name': '<New>', 'reason': 'Awaiting weekly group assignment'}],
                'changes': {'added': ['NEWIPO'], 'removed': ['OLD'],
                            'moved': [{'symbol': 'SHIFT', 'from': 'A', 'to': 'B'}]}}
    page = cluster.build_html(report(1), coverage)
    assert 'NEWIPO' in page and 'Awaiting weekly group assignment' in page
    assert '&lt;New&gt;' in page
    assert '10 eligible' in page and '7 ready' in page
    assert 'OLD' in page and 'SHIFT' in page


def test_daily_discovery_is_before_price_fetch_and_maintenance_before_scan():
    root = Path(__file__).resolve().parents[1]
    pipeline = (root / 'run_all_scanners.ps1').read_text()
    runner = (root / 'run_sector_rotation.ps1').read_text()
    assert pipeline.index('Run-Scanner "ClusterDiscovery"') < pipeline.index('Run-Scanner "FetchData"')
    assert runner.index('cluster_membership.py') < runner.index('sector_rotation_scanner.py')
