$repo    = "C:\Users\satya\nse_circuit_limits"
$logFile = "$repo\logs\discord_sync_$(Get-Date -Format 'yyyy-MM-dd').log"

New-Item -ItemType Directory -Path "$repo\logs" -Force | Out-Null

function Log($msg) {
    $line = "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')  $msg"
    Write-Host $line
    Add-Content -Path $logFile -Value $line -Encoding UTF8
}

Log "=== Discord Sync started ==="
python "$repo\scripts\discord_sync.py" 2>&1 | ForEach-Object { Log $_ }
Log "=== Discord Sync done ==="
