# run_breadth_monitor.ps1 — NSE Breadth Monitor (standalone, independent of run_all_scanners.ps1)
# Schedule: Mon–Fri 5:30 PM IST — runs AFTER regular scanners, manages its own data fetch
# Logs: logs/breadth_monitor_YYYY-MM-DD.log

$ROOT    = "C:\Users\satya\nse_circuit_limits"
$logDir  = "$ROOT\logs"
$date    = Get-Date -Format "yyyy-MM-dd"
$logFile = "$logDir\breadth_monitor_$date.log"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null

function Log($msg) {
    $line = "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] $msg"
    $line | Tee-Object -FilePath $logFile -Append
}

Log "=== BREADTH_MONITOR START ==="

# ── Step 1: Kite token (skip if fresh) ───────────────────────────────────────
Log "--- Kite token refresh ---"
& C:\Python313\python.exe "$ROOT\ema-compression-scanner\kite_auth.py" 2>&1 |
    ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
if ($LASTEXITCODE -ne 0) {
    Log "=== ERROR: Kite auth failed (exit $LASTEXITCODE) - aborting ==="
    exit 1
}
Log "--- Kite auth OK ---"

# ── Step 2: Fetch breadth universe OHLC (--all = includes breadth backfill) ──
Log "--- Fetching OHLC data (--all) ---"
& C:\Python313\python.exe "$ROOT\fetch_data.py" --all 2>&1 |
    ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
if ($LASTEXITCODE -ne 0) {
    Log "=== ERROR: fetch_data.py --all failed (exit $LASTEXITCODE) - aborting ==="
    exit 1
}
Log "--- Data fetch complete ---"

# ── Step 3: Run breadth monitor ───────────────────────────────────────────────
Log "--- Running breadth monitor ---"
& C:\Python313\python.exe "$ROOT\scanners\breadth_monitor.py" 2>&1 |
    ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
if ($LASTEXITCODE -ne 0) {
    Log "=== ERROR: breadth_monitor.py failed (exit $LASTEXITCODE) ==="
    exit 1
}
Log "--- Breadth monitor complete ---"

# ── Step 4: Git commit + push ─────────────────────────────────────────────────
Log "--- Git commit+push ---"
$gitResult = & git -C $ROOT status --porcelain data/breadth_history.csv dashboard/breadth.html 2>&1
if ($gitResult) {
    $csv  = Import-Csv "$ROOT\data\breadth_history.csv"
    $last = $csv | Select-Object -Last 1
    $up4  = $last.up4_count
    $dn4  = $last.down4_count
    $r5   = [math]::Round([double]$last.ratio_5d, 2)
    $msg  = "[scan $date] breadth-monitor: up4=${up4} dn4=${dn4} ratio5d=$r5"

    & git -C $ROOT add data/breadth_history.csv dashboard/breadth.html 2>&1 |
        ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
    & git -C $ROOT commit --no-verify -m $msg 2>&1 |
        ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
    & git -C $ROOT push 2>&1 |
        ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
} else {
    Log "No changes to commit."
}
Log "=== BREADTH_MONITOR DONE ==="

# ── Step 5: Bounce-RS scanner + dashboard rebuild ─────────────────────────────
# Runs here (not at 4:40 PM) because today's ratio_5d row above must exist first.
Log "--- Running Bounce-RS scanner ---"
& "$ROOT\run_bounce_rs_scanner.ps1"
if ($LASTEXITCODE -ne 0) {
    Log "=== ERROR: run_bounce_rs_scanner.ps1 failed (exit $LASTEXITCODE) ==="
}
Log "--- Rebuilding WT+Squeeze dashboard with fresh Bounce-RS data ---"
& "$ROOT\run_wt_squeeze_dashboard.ps1"
if ($LASTEXITCODE -ne 0) {
    Log "=== ERROR: run_wt_squeeze_dashboard.ps1 failed (exit $LASTEXITCODE) ==="
}
Log "=== BOUNCE_RS + DASHBOARD REBUILD DONE ==="

# To register scheduled task (run once as admin):
# schtasks /create /tn "NSE_BreadthMonitor" /tr "powershell.exe -NonInteractive -WindowStyle Hidden -ExecutionPolicy Bypass -File C:\Users\satya\nse_circuit_limits\run_breadth_monitor.ps1" /sc WEEKLY /d MON,TUE,WED,THU,FRI /st 17:30 /f
