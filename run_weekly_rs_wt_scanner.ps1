$ROOT = $PSScriptRoot
$date = Get-Date -Format "yyyy-MM-dd"
$logDir = Join-Path $ROOT "logs"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null
$logFile = Join-Path $logDir "weekly_rs_wt_scanner_$date.log"

function Log($msg) {
    "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] $msg" | Tee-Object -FilePath $logFile -Append
}

Log "=== Weekly_RS_WT START ==="
& C:\Python313\python.exe "$ROOT\weekly_rs_wt_scanner.py" 2>&1 |
    ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
if ($LASTEXITCODE -ne 0) {
    Log "ERROR: scanner failed; outputs will not be committed"
    exit 1
}

$outputs = @("weekly_rs_wt_scans/weekly_rs_wt_scans.md", "dashboard/weekly_rs_wt.html")
& git -C $ROOT add -- $outputs
if ($LASTEXITCODE -ne 0) { exit 1 }
& git -C $ROOT diff --cached --quiet -- $outputs
$diffExit = $LASTEXITCODE
if ($diffExit -eq 1) {
    & git -C $ROOT commit --no-verify --only -m "weekly-rs-wt: $date" -- $outputs 2>&1 |
        ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
    if ($LASTEXITCODE -ne 0) { exit 1 }
} elseif ($diffExit -ne 0) { exit 1 }

. "$ROOT\git_helpers.ps1"
Push-GitWithRetry -RepoPath $ROOT -LogFile $logFile
if ($LASTEXITCODE -ne 0) {
    Log "ERROR: git push failed"
    exit 1
}
Log "=== Weekly_RS_WT FINISHED exit=0 ==="
exit 0
