$ROOT = "C:\Users\satya\nse_circuit_limits"
$logDir = "$ROOT\logs"
$date = Get-Date -Format "yyyy-MM-dd"
$logFile = "$logDir\us_near_52w_high_chart_dashboard_$date.log"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null

function Log($msg) {
    "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] $msg" |
        Tee-Object -FilePath $logFile -Append
}

Log "=== US_WEEKLY_NEAR_52W_HIGH START ==="
& C:\Python313\python.exe "$ROOT\us_near_52w_high_chart_dashboard.py" 2>&1 |
    ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
$pythonExit = $LASTEXITCODE
if ($pythonExit -ne 0) {
    Log "=== ERROR: generation failed (exit $pythonExit); previous output preserved ==="
    exit $pythonExit
}

$outputs = @("dashboard/us_near_52w_high_charts.html", "us_near_52w_high_scans/us_near_52w_high_scans.md")
& git -C $ROOT add -- $outputs
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
& git -C $ROOT diff --cached --quiet -- $outputs
$diffExit = $LASTEXITCODE
if ($diffExit -eq 1) {
    & git -C $ROOT commit --no-verify --only -m "[scan $date] US weekly near-high charts" -- $outputs 2>&1 |
        ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
} elseif ($diffExit -ne 0) {
    exit $diffExit
}
. "$ROOT\git_helpers.ps1"
Push-GitWithRetry -RepoPath $ROOT -LogFile $logFile
if ($LASTEXITCODE -ne 0) { exit 1 }
Log "=== US_WEEKLY_NEAR_52W_HIGH FINISHED ==="
exit 0
