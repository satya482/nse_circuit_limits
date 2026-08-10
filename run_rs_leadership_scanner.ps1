$logDir  = "C:\Users\satya\nse_circuit_limits\logs"
$date    = Get-Date -Format "yyyy-MM-dd"
$logFile = "$logDir\rs_leadership_scanner_$date.log"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null

function Log($msg) {
    $line = "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] $msg"
    $line | Tee-Object -FilePath $logFile -Append
}

Log "=== RS_LEADERSHIP_SCANNER START ==="

try {
    & C:\Python313\python.exe C:\Users\satya\nse_circuit_limits\rs_leadership_scanner.py 2>&1 |
        ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
    Log "=== FINISHED exit=0 ==="
} catch {
    Log "=== ERROR: $_ ==="
    exit 1
}

Log "--- Git commit+push ---"
$scanDate = Get-Date -Format "yyyy-MM-dd"
& git -C C:\Users\satya\nse_circuit_limits add rs_leadership_scans/ 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
& git -C C:\Users\satya\nse_circuit_limits commit --no-verify -m "[scan $scanDate] rs-leadership: scan complete" 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
& git -C C:\Users\satya\nse_circuit_limits push 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
if ($LASTEXITCODE -ne 0) {
    Log "=== ERROR: git push FAILED (exit $LASTEXITCODE) - commits NOT on GitHub, check for non-fast-forward ==="
    exit 1
}
Log "--- Done ---"

# To register the scheduled task (run once as admin):
# schtasks /create /tn "NSE_RS_Leadership" /tr "powershell -NonInteractive -File C:\Users\satya\nse_circuit_limits\run_rs_leadership_scanner.ps1" /sc WEEKLY /d MON,TUE,WED,THU,FRI /st 16:30 /f
