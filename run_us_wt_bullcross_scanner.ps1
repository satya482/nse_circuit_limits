$logDir  = "C:\Users\satya\nse_circuit_limits\logs"
$date    = Get-Date -Format "yyyy-MM-dd"
$logFile = "$logDir\us_wt_bullcross_scanner_$date.log"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null

function Log($msg) {
    $line = "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] $msg"
    $line | Tee-Object -FilePath $logFile -Append
}

Log "=== US_WT_BULLCROSS START ==="

try {
    & C:\Python313\python.exe C:\Users\satya\nse_circuit_limits\us_wt_bullcross_scanner.py 2>&1 |
        ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
    Log "=== FINISHED exit=0 ==="
} catch {
    Log "=== ERROR: $_ ==="
    exit 1
}

Log "--- Git commit+push ---"
& git -C C:\Users\satya\nse_circuit_limits add us_wt_scans/ 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
& git -C C:\Users\satya\nse_circuit_limits commit --no-verify -m "us-wt-bullcross scan $date" 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
& git -C C:\Users\satya\nse_circuit_limits push 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
Log "--- Done ---"

# To register the scheduled task (run once as admin), after US_FETCH_DATA (4:40PM) and
# US_ZL_SQUEEZE (4:50PM):
# schtasks /create /tn "US_WT_BULLCROSS" /tr "powershell -NonInteractive -File C:\Users\satya\nse_circuit_limits\run_us_wt_bullcross_scanner.ps1" /sc WEEKLY /d MON,TUE,WED,THU,FRI /st 17:00 /f
