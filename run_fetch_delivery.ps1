$logDir  = "C:\Users\satya\nse_circuit_limits\logs"
$date    = Get-Date -Format "yyyy-MM-dd"
$logFile = "$logDir\fetch_delivery_$date.log"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null

function Log($msg) {
    $line = "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] $msg"
    $line | Tee-Object -FilePath $logFile -Append
}

Log "=== FETCH_DELIVERY START ==="

try {
    & C:\Python313\python.exe C:\Users\satya\nse_circuit_limits\fetch_delivery.py 2>&1 |
        ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
    & C:\Python313\python.exe C:\Users\satya\nse_circuit_limits\backfill_delivery_markers.py 2>&1 |
        ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
    Log "=== FINISHED exit=0 ==="
} catch {
    Log "=== ERROR: $_ ==="
    exit 1
}

Log "--- Git commit+push ---"
$scanDate = Get-Date -Format "yyyy-MM-dd"
& git -C C:\Users\satya\nse_circuit_limits add wt_scans/ ema25_zl_scans/ weekly_zl_scans/ trend_scans/ rs_highline_scans/ wt_squeeze_dashboard.html dashboard.html trend_dashboard.html 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
& git -C C:\Users\satya\nse_circuit_limits commit --no-verify -m "[scan $scanDate] delivery backfill: symbol markers updated" 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
& git -C C:\Users\satya\nse_circuit_limits push 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
Log "--- Done ---"

# Runs here (not standalone) because it needs today's delivery% just fetched above.
Log "--- Running Institutional Footprint scanner ---"
& C:\Users\satya\nse_circuit_limits\run_institutional_footprint_scanner.ps1
if ($LASTEXITCODE -ne 0) {
    Log "=== ERROR: run_institutional_footprint_scanner.ps1 failed (exit $LASTEXITCODE) ==="
}
Log "=== INSTITUTIONAL_FOOTPRINT DONE ==="

# To register the scheduled task (run once as admin):
# schtasks /create /tn "NSE_FetchDelivery" /tr "powershell -NonInteractive -File C:\Users\satya\nse_circuit_limits\run_fetch_delivery.ps1" /sc WEEKLY /d MON,TUE,WED,THU,FRI /st 18:15 /f
