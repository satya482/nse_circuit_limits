$logDir  = "C:\Users\satya\nse_circuit_limits\logs"
$date    = Get-Date -Format "yyyy-MM-dd"
$logFile = "$logDir\wt_squeeze_dashboard_$date.log"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null

function Log($msg) {
    $line = "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] $msg"
    $line | Tee-Object -FilePath $logFile -Append
}

Log "=== WT_SQUEEZE_DASHBOARD START ==="

try {
    & C:\Python313\python.exe C:\Users\satya\nse_circuit_limits\wt_squeeze_dashboard.py 2>&1 |
        ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
    Log "=== FINISHED exit=0 ==="
} catch {
    Log "=== ERROR: $_ ==="
    exit 1
}

Log "--- Git commit+push ---"
& git -C C:\Users\satya\nse_circuit_limits add wt_squeeze_dashboard.html 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
& git -C C:\Users\satya\nse_circuit_limits commit --no-verify -m "wt-squeeze dashboard $date" 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
& git -C C:\Users\satya\nse_circuit_limits push 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
if ($LASTEXITCODE -ne 0) {
    Log "=== ERROR: git push FAILED (exit $LASTEXITCODE) - commits NOT on GitHub, check for non-fast-forward ==="
    exit 1
}
Log "--- Done ---"

# To register the scheduled task (run once as admin):
# schtasks /create /tn "NSE_WT_SQUEEZE_DASHBOARD" /tr "powershell -NonInteractive -File C:\Users\satya\nse_circuit_limits\run_wt_squeeze_dashboard.ps1" /sc WEEKLY /d MON,TUE,WED,THU,FRI /st 16:40 /f
