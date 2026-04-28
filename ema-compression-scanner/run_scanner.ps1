$logDir  = "C:\Users\satya\nse_circuit_limits\logs"
$date    = Get-Date -Format "yyyy-MM-dd"
$logFile = "$logDir\ema_compression_$date.log"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null

function Log($msg) {
    $line = "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] $msg"
    $line | Tee-Object -FilePath $logFile -Append
}

Log "=== EMA_Compression START ==="

# ── Run EMA compression scanner ──────────────────────────────────────────────
try {
    & C:\Python313\python.exe C:\Users\satya\nse_circuit_limits\ema-compression-scanner\screener.py 2>&1 |
        ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }

    # Commit scan output
    git -C C:\Users\satya\nse_circuit_limits add `
        ema-compression-scanner/ema_compression_scans/ 2>&1 | Tee-Object -FilePath $logFile -Append
    git -C C:\Users\satya\nse_circuit_limits commit -m "ema-compression scan $date" 2>&1 | Tee-Object -FilePath $logFile -Append
    git -C C:\Users\satya\nse_circuit_limits push 2>&1 | Tee-Object -FilePath $logFile -Append

    Log "=== FINISHED ==="
} catch {
    Log "=== ERROR: $_ ==="
    exit 1
}

# Scheduled task (run once as admin):
# schtasks /create /tn "EMA_Compression" /tr "powershell.exe -NonInteractive -WindowStyle Hidden -File C:\Users\satya\nse_circuit_limits\ema-compression-scanner\run_scanner.ps1" /sc WEEKLY /d MON,TUE,WED,THU,FRI /st 16:35 /f