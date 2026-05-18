
$source  = "C:\Users\satya\Downloads\NSE_Investor_Story"
$repo    = "C:\Users\satya\nse_circuit_limits"
$logFile = "$repo\logs\sync_investor_stories_$(Get-Date -Format 'yyyy-MM-dd').log"

function Log($msg) {
    $line = "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')  $msg"
    Write-Host $line
    Add-Content -Path $logFile -Value $line -Encoding UTF8
}

New-Item -ItemType Directory -Path "$repo\logs" -Force | Out-Null

Log "=== Investor Story Sync started ==="

# ── Find HTML files ────────────────────────────────────────────────────────────
$files = Get-ChildItem -Path $source -Filter "*.html" -File -ErrorAction SilentlyContinue

if (-not $files) {
    Log "No HTML files found in $source. Exiting."
    exit 0
}

$copied = 0
foreach ($f in $files) {
    # Expect: SYMBOL_YYYY-MM-DD.html  (e.g. AEROFLEX_2026-05-17.html)
    if ($f.Name -match '^([A-Z0-9&_]+?)_(\d{4}-\d{2}-\d{2})\.html$') {
        $symbol  = $Matches[1]
        $destDir = "$repo\reports\$symbol"
        $dest    = "$destDir\$($f.Name)"

        New-Item -ItemType Directory -Path $destDir -Force | Out-Null

        if (-not (Test-Path $dest)) {
            Copy-Item $f.FullName -Destination $dest -Force
            Log "Copied  $($f.Name)  ->  reports\$symbol\"
            $copied++
        } else {
            Log "Skip    $($f.Name)  (already exists)"
        }
    } else {
        Log "Skip    $($f.Name)  (filename doesn't match SYMBOL_YYYY-MM-DD.html)"
    }
}

Log "Files copied: $copied"

# ── Rebuild index ──────────────────────────────────────────────────────────────
Log "Rebuilding index..."
python "$repo\scripts\generate_index.py" 2>&1 | ForEach-Object { Log $_ }

# ── Git commit + push (only if something changed) ─────────────────────────────
Set-Location $repo
git add reports/ 2>&1 | Out-Null
$staged = git diff --staged --name-only

if ($staged) {
    $msg = "investor stories sync: $(Get-Date -Format 'yyyy-MM-dd HH:mm') IST ($copied new)"
    git commit -m $msg 2>&1 | Out-Null
    git push 2>&1 | Out-Null
    Log "Pushed to GitHub: $msg"
} else {
    Log "Nothing new to commit."
}

Log "=== Done ==="
