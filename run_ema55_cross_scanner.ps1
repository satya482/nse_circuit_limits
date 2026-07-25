$logDir  = "C:\Users\satya\nse_circuit_limits\logs"
$date    = Get-Date -Format "yyyy-MM-dd"
$logFile = "$logDir\ema55_cross_scanner_$date.log"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null

function Log($msg) {
    $line = "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] $msg"
    $line | Tee-Object -FilePath $logFile -Append
}

Log "=== NSE_EMA55_CROSS START ==="

try {
    & C:\Python313\python.exe C:\Users\satya\nse_circuit_limits\ema55_cross_scanner.py 2>&1 |
        ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
    Log "=== FINISHED exit=0 ==="
} catch {
    Log "=== ERROR: $_ ==="
    exit 1
}

Log "--- Git commit+push ---"
& git -C C:\Users\satya\nse_circuit_limits add ema55_cross_scans/ 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
& git -C C:\Users\satya\nse_circuit_limits commit --no-verify -m "ema55-cross scan $date" 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
& git -C C:\Users\satya\nse_circuit_limits push 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
Log "--- Done ---"

# To register the scheduled task (run once as admin):
# schtasks /create /tn "NSE_EMA55_Cross" /tr "powershell -NonInteractive -File C:\Users\satya\nse_circuit_limits\run_ema55_cross_scanner.ps1" /sc WEEKLY /d MON,TUE,WED,THU,FRI /st 16:28 /f
