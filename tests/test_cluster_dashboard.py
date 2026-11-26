from pathlib import Path

import pytest

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
