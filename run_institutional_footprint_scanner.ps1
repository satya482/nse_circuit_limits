# run_institutional_footprint_scanner.ps1 — Institutional Footprint Scanner
# Triggered as a trailing step of run_fetch_delivery.ps1 (~6:15 PM), after today's
# delivery% is in SQLite. Also runnable standalone for manual/backfilled re-runs.
# Logs: logs/institutional_footprint_scanner_YYYY-MM-DD.log

$logDir  = "C:\Users\satya\nse_circuit_limits\logs"
$date    = Get-Date -Format "yyyy-MM-dd"
$logFile = "$logDir\institutional_footprint_scanner_$date.log"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null

function Log($msg) {
    $line = "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] $msg"
    $line | Tee-Object -FilePath $logFile -Append
}

Log "=== INSTITUTIONAL_FOOTPRINT_SCANNER START ==="

try {
    & C:\Python313\python.exe C:\Users\satya\nse_circuit_limits\institutional_footprint_scanner.py 2>&1 |
        ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
    Log "=== FINISHED exit=0 ==="
} catch {
    Log "=== ERROR: $_ ==="
    exit 1
}

Log "--- Git commit+push ---"
& git -C C:\Users\satya\nse_circuit_limits add footprint_scans dashboard/footprint.html 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
& git -C C:\Users\satya\nse_circuit_limits commit --no-verify -m "[scan $date] institutional_footprint: scan run" 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
& git -C C:\Users\satya\nse_circuit_limits push 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
Log "--- Done ---"

# To register the scheduled task (run once as admin):
# schtasks /create /tn "NSE_InstitutionalFootprint" /tr "powershell -NonInteractive -File C:\Users\satya\nse_circuit_limits\run_institutional_footprint_scanner.ps1" /sc WEEKLY /d MON,TUE,WED,THU,FRI /st 16:45 /f
