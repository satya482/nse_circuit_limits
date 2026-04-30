$workDir = "C:\Users\satya\nse_circuit_limits"
$logDir  = "$workDir\logs"
$date    = Get-Date -Format "yyyy-MM-dd"
$logFile = "$logDir\circuit_dashboard_$date.log"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null

function Log($msg) {
    $line = "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] $msg"
    $line | Tee-Object -FilePath $logFile -Append
}

Log "=== NSE_CircuitLimits START ==="

try {
    & C:\Python313\python.exe "$workDir\main.py" 2>&1 |
        ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
    Log "=== FINISHED exit=0 ==="
} catch {
    Log "=== ERROR: $_ ==="
    exit 1
}

Log "--- Git commit+push ---"
& git -C $workDir add NSE_Circuit_Limits.md index.html nse.csv 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
& git -C $workDir commit -m "dashboard $date" 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
& git -C $workDir push 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
Log "--- Done ---"

# Scheduled task (run once as admin):
# schtasks /create /tn "NSE_CircuitLimits" /tr "powershell.exe -NonInteractive -WindowStyle Hidden -File C:\Users\satya\nse_circuit_limits\run_dashboard.ps1" /sc WEEKLY /d MON,TUE,WED,THU,FRI /st 17:05 /f
