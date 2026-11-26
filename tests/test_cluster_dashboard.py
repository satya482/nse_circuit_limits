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
