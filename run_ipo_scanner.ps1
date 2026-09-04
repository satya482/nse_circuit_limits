$logDir  = "C:\Users\satya\nse_circuit_limits\logs"
$date    = Get-Date -Format "yyyy-MM-dd"
$logFile = "$logDir\ipo_scanner_$date.log"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null

function Log($msg) {
    $line = "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] $msg"
    $line | Tee-Object -FilePath $logFile -Append
}

Log "=== NSE_IPO_SCANNER START ==="

& C:\Python313\python.exe C:\Users\satya\nse_circuit_limits\ipo_scanner.py 2>&1 |
    ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
$pythonExit = $LASTEXITCODE
if ($pythonExit -ne 0) {
    Log "=== ERROR: scanner FAILED (exit $pythonExit) ==="
    exit $pythonExit
}
Log "=== FINISHED exit=0 ==="

Log "--- Git commit+push ---"
& git -C C:\Users\satya\nse_circuit_limits add ipo_scans/ipo_scans.md ipo_scans/ipo_scans_$date.md 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
& git -C C:\Users\satya\nse_circuit_limits commit --no-verify -m "[scan $date] ipo: scan run" 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
& git -C C:\Users\satya\nse_circuit_limits push 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
if ($LASTEXITCODE -ne 0) {
    Log "=== ERROR: git push FAILED (exit $LASTEXITCODE) - commits NOT on GitHub, check for non-fast-forward ==="
    exit 1
}
Log "--- Done ---"

# Run via run_all_scanners.ps1 (Run-Scanner "IPOScanner") -- no standalone scheduled task.
