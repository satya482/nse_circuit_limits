# run_consolidation_scanner.ps1 — Consolidation Tracker (Phase 1+2)
# Run after 4:05 PM IST on trading days (after run_fetch_data.ps1).
# Logs: logs/consolidation_scanner_YYYY-MM-DD.log

$logDir  = "C:\Users\satya\nse_circuit_limits\logs"
$date    = Get-Date -Format "yyyy-MM-dd"
$logFile = "$logDir\consolidation_scanner_$date.log"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null

function Log($msg) {
    $line = "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] $msg"
    $line | Tee-Object -FilePath $logFile -Append
}

Log "=== CONSOLIDATION_SCANNER START ==="

try {
    & C:\Python313\python.exe C:\Users\satya\nse_circuit_limits\consolidation\consolidation_scanner.py 2>&1 |
        ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
    Log "=== FINISHED exit=0 ==="
} catch {
    Log "=== ERROR: $_ ==="
    exit 1
}

Log "--- Git commit+push ---"
& git -C C:\Users\satya\nse_circuit_limits add results consolidation_scans 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
& git -C C:\Users\satya\nse_circuit_limits commit --no-verify -m "[scan $date] consolidation: scan run" 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
& git -C C:\Users\satya\nse_circuit_limits push 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
Log "--- Done ---"

# To register the scheduled task (run once as admin):
# schtasks /create /tn "NSE_ConsolidationScanner" /tr "powershell -NonInteractive -File C:\Users\satya\nse_circuit_limits\run_consolidation_scanner.ps1" /sc WEEKLY /d MON,TUE,WED,THU,FRI /st 16:35 /f
