# run_institutional_footprint_scanner.ps1 — Institutional Footprint Scanner
# Triggered as a trailing step of run_fetch_delivery.ps1 (~6:15 PM), after today's
# delivery% is in SQLite. Also runnable standalone for manual/backfilled re-runs.
# Logs: logs/institutional_footprint_scanner_YYYY-MM-DD.log

$ROOT    = "C:\Users\satya\nse_circuit_limits"
$logDir  = "$ROOT\logs"
$date    = Get-Date -Format "yyyy-MM-dd"
$logFile = "$logDir\institutional_footprint_scanner_$date.log"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null

if (-not $env:DISCORD_WEBHOOK_URL) {
    $env:DISCORD_WEBHOOK_URL = [System.Environment]::GetEnvironmentVariable("DISCORD_WEBHOOK_URL", "User")
}

function Log($msg) {
    $line = "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] $msg"
    $line | Tee-Object -FilePath $logFile -Append
}

Log "=== INSTITUTIONAL_FOOTPRINT_SCANNER START ==="

& C:\Python313\python.exe C:\Users\satya\nse_circuit_limits\institutional_footprint_scanner.py 2>&1 |
    ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
$scanExitCode = $LASTEXITCODE
if ($scanExitCode -ne 0) {
    Log "=== ERROR: institutional_footprint_scanner.py failed (exit $scanExitCode) ==="
} else {
    Log "=== FINISHED exit=0 ==="
}

$csvPath = "$ROOT\footprint_scans\footprint_$date.csv"
if ($scanExitCode -eq 0 -and (Test-Path "$ROOT\dashboard\footprint.html") -and (Test-Path $csvPath)) {
    $rows    = Import-Csv $csvPath
    $total   = $rows.Count
    $elite   = ($rows | Where-Object { $_.rating -eq "ELITE" }).Count
    $strong  = ($rows | Where-Object { $_.rating -eq "STRONG" }).Count
    $build   = ($rows | Where-Object { $_.rating -eq "BUILDING" }).Count

    & C:\Python313\python.exe "$ROOT\discord_alert.py" "Institutional Footprint Scanner" "footprint.html dashboard generated successfully - $date" `
        --field "Scanned=$total" --field "Elite=$elite" --field "Strong=$strong" --field "Building=$build" `
        --url "https://satya482.github.io/nse_circuit_limits/dashboard/footprint.html" 2>&1 |
        ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
}

Log "--- Git commit+push ---"
& git -C C:\Users\satya\nse_circuit_limits add footprint_scans dashboard/footprint.html 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
& git -C C:\Users\satya\nse_circuit_limits commit --no-verify -m "[scan $date] institutional_footprint: scan run" 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
& git -C C:\Users\satya\nse_circuit_limits push 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
Log "--- Done ---"

exit $scanExitCode

# To register the scheduled task (run once as admin):
# schtasks /create /tn "NSE_InstitutionalFootprint" /tr "powershell -NonInteractive -File C:\Users\satya\nse_circuit_limits\run_institutional_footprint_scanner.ps1" /sc WEEKLY /d MON,TUE,WED,THU,FRI /st 16:45 /f
