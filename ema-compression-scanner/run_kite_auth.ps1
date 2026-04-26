$logDir  = "C:\Users\satya\nse_circuit_limits\logs"
$date    = Get-Date -Format "yyyy-MM-dd"
$logFile = "$logDir\kite_auth_$date.log"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null

function Log($msg) {
    $line = "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] $msg"
    $line | Tee-Object -FilePath $logFile -Append
}

Log "=== Kite_Auth START ==="

try {
    & C:\Python313\python.exe C:\Users\satya\nse_circuit_limits\ema-compression-scanner\kite_auth.py 2>&1 |
        ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
    Log "=== FINISHED ==="
} catch {
    Log "=== ERROR: $_ ==="
    exit 1
}