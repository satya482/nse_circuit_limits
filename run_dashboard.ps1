$workDir = "C:\Users\satya\.gemini\antigravity\scratch\circuit_dashboard"
$logDir  = "C:\Users\satya\nse_circuit_limits\logs"
$date    = Get-Date -Format "yyyy-MM-dd"
$logFile = "$logDir\circuit_dashboard_$date.log"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null

function Log($msg) {
    $line = "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] $msg"
    $line | Tee-Object -FilePath $logFile -Append
}

Set-Location $workDir
Log "=== CircuitDashboardDaily START ==="

try {
    & python main.py 2>&1 |
        ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
    Log "=== FINISHED exit=0 ==="
} catch {
    Log "=== ERROR: $_ ==="
    exit 1
}

Log "--- Git commit+push ---"
& git add NSE_Circuit_Limits.md index.html nse.csv 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
& git commit -m "chore: update circuit limits dashboard $date" 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
& git push 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
Log "--- Done ---"