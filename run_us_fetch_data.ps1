$logDir  = "C:\Users\satya\nse_circuit_limits\logs"
$date    = Get-Date -Format "yyyy-MM-dd"
$logFile = "$logDir\us_fetch_data_$date.log"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null

function Log($msg) {
    $line = "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] $msg"
    $line | Tee-Object -FilePath $logFile -Append
}

Log "=== US_FETCH_DATA START ==="

try {
    & C:\Python313\python.exe C:\Users\satya\nse_circuit_limits\fetch_us_data.py 2>&1 |
        ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
    Log "=== FINISHED exit=0 ==="
} catch {
    Log "=== ERROR: $_ ==="
    exit 1
}

Log "--- Git commit+push (manifest) ---"
& git -C C:\Users\satya\nse_circuit_limits add us_data_manifest.csv 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
& git -C C:\Users\satya\nse_circuit_limits commit -m "us-data: manifest $date" 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
& git -C C:\Users\satya\nse_circuit_limits push 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
Log "--- Done ---"

# To register the scheduled task (run once as admin):
# schtasks /create /tn "US_FETCH_DATA" /tr "powershell -NonInteractive -File C:\Users\satya\nse_circuit_limits\run_us_fetch_data.ps1" /sc WEEKLY /d MON,TUE,WED,THU,FRI /st 16:40 /f
