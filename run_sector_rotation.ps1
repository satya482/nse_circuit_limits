$logDir  = "C:\Users\satya\nse_circuit_limits\logs"
$date    = Get-Date -Format "yyyy-MM-dd"
$logFile = "$logDir\sector_rotation_$date.log"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null

function Log($msg) {
    $line = "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] $msg"
    $line | Tee-Object -FilePath $logFile -Append
}

Log "=== SECTOR_ROTATION START ==="

try {
    & C:\Python313\python.exe C:\Users\satya\nse_circuit_limits\sector_rotation_scanner.py 2>&1 |
        ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
    Log "=== FINISHED exit=0 ==="
} catch {
    Log "=== ERROR: $_ ==="
    exit 1
}

Log "--- Git commit+push ---"
& git -C C:\Users\satya\nse_circuit_limits add sector_rotation_scans/ 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
& git -C C:\Users\satya\nse_circuit_limits commit --no-verify -m "sector-rotation scan $date" 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
& git -C C:\Users\satya\nse_circuit_limits push 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
if ($LASTEXITCODE -ne 0) {
    Log "=== ERROR: git push FAILED (exit $LASTEXITCODE) - commits NOT on GitHub, check for non-fast-forward ==="
    exit 1
}
Log "--- Done ---"

# To register the scheduled task (run once as admin):
# schtasks /create /tn "NSE_SECTOR_ROTATION" /tr "powershell -NonInteractive -File C:\Users\satya\nse_circuit_limits\run_sector_rotation.ps1" /sc WEEKLY /d MON,TUE,WED,THU,FRI /st 16:45 /f
