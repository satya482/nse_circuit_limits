$logDir  = "C:\Users\satya\nse_circuit_limits\logs"
$date    = Get-Date -Format "yyyy-MM-dd"
$logFile = "$logDir\swing_scanner_$date.log"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null

function Log($msg) {
    $line = "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] $msg"
    $line | Tee-Object -FilePath $logFile -Append
}

Log "=== NSE_SwingScanner START ==="

try {
    & C:\Python313\python.exe C:\Users\satya\nse_circuit_limits\swing_scanner.py 2>&1 |
        ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
    Log "=== FINISHED exit=0 ==="
} catch {
    Log "=== ERROR: $_ ==="
    exit 1
}
