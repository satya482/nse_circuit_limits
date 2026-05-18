
$source   = "C:\Users\satya\Downloads\NSE_Investor_Story"
$repo     = "C:\Users\satya\nse_circuit_limits"
$logFile  = "$repo\logs\sync_investor_stories_$(Get-Date -Format 'yyyy-MM-dd').log"
$manifest = "$repo\logs\sync_manifest.json"

function Log($msg) {
    $line = "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')  $msg"
    Write-Host $line
    Add-Content -Path $logFile -Value $line -Encoding UTF8
}

New-Item -ItemType Directory -Path "$repo\logs" -Force | Out-Null

# ── Load manifest (tracks every file ever synced) ─────────────────────────────
$syncedNames = @{}
$allEntries  = @()
if (Test-Path $manifest) {
    $raw = Get-Content $manifest -Raw -Encoding UTF8 | ConvertFrom-Json
    # ConvertFrom-Json returns PSObject (single item) or array — normalise to array
    foreach ($e in @($raw)) {
        $syncedNames[$e.file] = $true
        $allEntries += $e
    }
}

Log "=== Investor Story Sync started ==="

# ── Find HTML files ────────────────────────────────────────────────────────────
$files = Get-ChildItem -Path $source -Filter "*.html" -File -ErrorAction SilentlyContinue

if (-not $files) {
    Log "No HTML files found in $source. Exiting."
    exit 0
}

$copied     = 0
$newEntries = @()

foreach ($f in $files) {
    # Skip if already recorded in manifest
    if ($syncedNames.ContainsKey($f.Name)) {
        Log "Skip    $($f.Name)  (already synced)"
        continue
    }

    # Derive symbol: everything before the first underscore, uppercased.
    # If no underscore, use the full stem.  e.g. AEROFLEX_Q4.html -> AEROFLEX
    $stem   = [System.IO.Path]::GetFileNameWithoutExtension($f.Name)
    $symbol = ($stem -split '_')[0].ToUpper()

    $destDir = "$repo\reports\$symbol"
    $dest    = "$destDir\$($f.Name)"

    New-Item -ItemType Directory -Path $destDir -Force | Out-Null
    Copy-Item $f.FullName -Destination $dest -Force

    $entry = [PSCustomObject]@{
        file      = $f.Name
        symbol    = $symbol
        synced_at = (Get-Date -Format 'yyyy-MM-dd HH:mm:ss')
        dest      = "reports/$symbol/$($f.Name)"
    }
    $newEntries   += $entry
    $allEntries   += $entry
    $syncedNames[$f.Name] = $true

    Log "Copied  $($f.Name)  ->  reports\$symbol\"
    $copied++
}

Log "Files copied: $copied"

if ($newEntries.Count -gt 0) {
    # ── Persist manifest ──────────────────────────────────────────────────────
    $allEntries | ConvertTo-Json -Depth 3 | Set-Content $manifest -Encoding UTF8
    Log "Manifest updated: $($allEntries.Count) total entries"

    # ── Rebuild index ─────────────────────────────────────────────────────────
    Log "Rebuilding index..."
    python "$repo\scripts\generate_index.py" 2>&1 | ForEach-Object { Log $_ }

    # ── Git commit + push ─────────────────────────────────────────────────────
    Set-Location $repo
    git add reports/ logs/sync_manifest.json 2>&1 | Out-Null
    $staged = git diff --staged --name-only

    if ($staged) {
        $msg = "investor stories sync: $(Get-Date -Format 'yyyy-MM-dd HH:mm') IST ($copied new)"
        git commit -m $msg 2>&1 | Out-Null
        git push 2>&1 | Out-Null
        Log "Pushed to GitHub: $msg"
    } else {
        Log "Nothing new to commit."
    }
} else {
    Log "No new files - skipping index rebuild and git push."
}

Log "=== Done ==="
