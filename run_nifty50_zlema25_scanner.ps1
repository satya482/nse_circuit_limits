$root = "C:\Users\satya\nse_circuit_limits"
$logDir = "$root\logs"
$date = Get-Date -Format "yyyy-MM-dd"
$logFile = "$logDir\nifty50_zlema25_scanner_$date.log"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null

function Log($message) {
    $line = "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] $message"
    $line | Tee-Object -FilePath $logFile -Append
}

Log "=== NIFTY50_ZLEMA25 START ==="

& C:\Python313\python.exe "$root\nifty50_zlema25_scanner.py" 2>&1 |
    ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
$scannerExit = $LASTEXITCODE
if ($scannerExit -ne 0) {
    Log "=== FAILED exit=$scannerExit ==="
    exit $scannerExit
}

Log "=== SCAN FINISHED exit=0 ==="
Log "--- Git commit+push ---"
& git -C $root add -- "nifty50_zlema25_scans/" "data/nifty50_constituents.csv" 2>&1 |
    ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
if ($LASTEXITCODE -ne 0) {
    Log "=== GIT ADD FAILED exit=$LASTEXITCODE ==="
    exit $LASTEXITCODE
}

& git -C $root diff --cached --quiet --
if ($LASTEXITCODE -eq 1) {
    & git -C $root commit --no-verify -m "nifty50-zlema25 scan $date" 2>&1 |
        ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
    if ($LASTEXITCODE -ne 0) {
        Log "=== GIT COMMIT FAILED exit=$LASTEXITCODE ==="
        exit $LASTEXITCODE
    }
    & git -C $root push 2>&1 |
        ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
    if ($LASTEXITCODE -ne 0) {
        Log "=== GIT PUSH FAILED exit=$LASTEXITCODE ==="
        exit $LASTEXITCODE
    }
} elseif ($LASTEXITCODE -ne 0) {
    Log "=== GIT DIFF FAILED exit=$LASTEXITCODE ==="
    exit $LASTEXITCODE
} else {
    Log "No generated changes to commit."
}

Log "--- Done ---"

# To register the scheduled task (run once as admin):
# schtasks /create /tn "NSE_NIFTY50_ZLEMA25" /tr "powershell -NonInteractive -File C:\Users\satya\nse_circuit_limits\run_nifty50_zlema25_scanner.ps1" /sc WEEKLY /d MON,TUE,WED,THU,FRI /st 16:27 /f
