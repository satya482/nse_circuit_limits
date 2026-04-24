$logDir  = "C:\Users\satya\nse_circuit_limits\logs"
$date    = Get-Date -Format "yyyy-MM-dd"
$logFile = "$logDir\scan_status_mailer_$date.log"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null

function Log($msg) {
    $line = "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] $msg"
    $line | Tee-Object -FilePath $logFile -Append
}

Log "=== NSE_ScanStatusMailer START ==="

try {
    & C:\Python313\python.exe C:\Users\satya\nse_circuit_limits\scan_status_mailer.py 2>&1 |
        ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
    Log "=== FINISHED ==="
} catch {
    Log "=== ERROR: $_ ==="
    exit 1
}

# To register scheduled task at 7:00 PM Mon-Fri (after all scans are done):
# schtasks /create /tn "NSE_ScanStatusMailer" /tr "powershell -NonInteractive -WindowStyle Hidden -File C:\Users\satya\nse_circuit_limits\run_scan_status_mailer.ps1" /sc WEEKLY /d MON,TUE,WED,THU,FRI /st 16:40 /f