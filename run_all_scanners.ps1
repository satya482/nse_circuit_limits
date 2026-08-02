$ROOT    = "C:\Users\satya\nse_circuit_limits"
$logDir  = "$ROOT\logs"
$date    = Get-Date -Format "yyyy-MM-dd"
$logFile = "$logDir\all_scanners_$date.log"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null

function OrcLog($msg) {
    $line = "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] [ORCH] $msg"
    $line | Tee-Object -FilePath $logFile -Append
}

if (-not $env:DISCORD_WEBHOOK_URL) {
    $env:DISCORD_WEBHOOK_URL = [System.Environment]::GetEnvironmentVariable("DISCORD_WEBHOOK_URL", "User")
}
if (-not $env:GMAIL_APP_PASSWORD) {
    $env:GMAIL_APP_PASSWORD = [System.Environment]::GetEnvironmentVariable("GMAIL_APP_PASSWORD", "User")
}

$overallStart = Get-Date
$results      = [System.Collections.Generic.List[hashtable]]::new()

function Run-Scanner($Name, $ScriptPath) {
    OrcLog "--- START $Name ---"
    $start = Get-Date
    & powershell.exe -NonInteractive -WindowStyle Hidden -ExecutionPolicy Bypass -File $ScriptPath
    $exit   = $LASTEXITCODE
    $dur    = "{0:mm}m {0:ss}s" -f ((Get-Date) - $start)
    $status = if ($exit -eq 0) { "PASS" } else { "FAIL" }
    OrcLog "--- $status $Name  exit=$exit  duration=$dur ---"
    $results.Add(@{ Name = $Name; Status = $status; Exit = $exit; Duration = $dur })
}

OrcLog "=== NSE_AllScanners START ==="

Run-Scanner "FetchData"            "$ROOT\run_fetch_data.ps1"
Run-Scanner "EMAScreener"          "$ROOT\run_ema_screener.ps1"
Run-Scanner "SwingScanner"         "$ROOT\run_swing_scanner.ps1"
Run-Scanner "MomentumScanner"      "$ROOT\run_momentum_scanner.ps1"
Run-Scanner "MomentumRSWeekly"     "$ROOT\run_momentum_rs_weekly_scanner.ps1"
Run-Scanner "EMA25_ZL"             "$ROOT\run_ema25_zl_scanner.ps1"
Run-Scanner "EMA55_Cross"          "$ROOT\run_ema55_cross_scanner.ps1"
Run-Scanner "NIFTY50_ZLEMA25"      "$ROOT\run_nifty50_zlema25_scanner.ps1"
Run-Scanner "ZL_Squeeze"           "$ROOT\run_zl_squeeze_scanner.ps1"
Run-Scanner "InsideBarScanner"     "$ROOT\run_inside_bar_scanner.ps1"
Run-Scanner "WeeklyZL"             "$ROOT\run_weekly_zl_scanner.ps1"
Run-Scanner "RS_WeeklyEMA9"        "$ROOT\run_rs_weekly_ema9_scanner.ps1"

$comp = "$ROOT\ema-compression-scanner\run_scanner.ps1"
if (Test-Path $comp) { Run-Scanner "EMA_Compression" $comp }
else { OrcLog "--- SKIP EMA_Compression (not found) ---" }

Run-Scanner "WT_BullCross"         "$ROOT\run_wt_bullcross_scanner.ps1"
Run-Scanner "RS_HighLine"          "$ROOT\run_rs_highline_scanner.ps1"
Run-Scanner "RS_Leadership"        "$ROOT\run_rs_leadership_scanner.ps1"
Run-Scanner "MinerviniTrend"       "$ROOT\run_minervini_trend_scanner.ps1"
Run-Scanner "WT_SqueezeDash"       "$ROOT\run_wt_squeeze_dashboard.ps1"
Run-Scanner "TrendScanner"         "$ROOT\run_trend_scanner.ps1"
Run-Scanner "TrendDashboard"       "$ROOT\run_trend_dashboard.ps1"

Run-Scanner "CircuitLimits"        "$ROOT\run_dashboard.ps1"
Run-Scanner "US_FetchData"         "$ROOT\run_us_fetch_data.ps1"
Run-Scanner "US_ZL_Squeeze"        "$ROOT\run_us_zl_squeeze_scanner.ps1"
Run-Scanner "Dashboard"            "$ROOT\run_dashboard_generator.ps1"
Run-Scanner "CatalystBot"          "$ROOT\run_catalyst_bot.ps1"
Run-Scanner "ScanStatusMailer"     "$ROOT\run_scan_status_mailer.ps1"

$total  = "{0:hh}h {0:mm}m {0:ss}s" -f ((Get-Date) - $overallStart)
$passed = ($results | Where-Object { $_.Status -eq "PASS" }).Count
$failed = ($results | Where-Object { $_.Status -eq "FAIL" }).Count

OrcLog "======================================================"
OrcLog "=== SUMMARY"
foreach ($r in $results) {
    $flag = if ($r.Status -eq "PASS") { "[OK]" } else { "[!!]" }
    OrcLog ("  {0,-6} {1,-28} {2}" -f $flag, $r.Name, $r.Duration)
}
OrcLog "--- TOTAL: $total  |  PASSED: $passed  FAILED: $failed"
OrcLog "======================================================"

# Fire BreadthMonitor as separate task — doesn't block, separate log
OrcLog "--- Triggering NSE_BreadthMonitor ---"
Start-ScheduledTask -TaskName "NSE_BreadthMonitor" -ErrorAction SilentlyContinue
OrcLog "--- NSE_BreadthMonitor triggered ---"

if ($failed -gt 0) { exit 1 }
exit 0

# To register the scheduled task (run once from an admin PowerShell):
# schtasks /create /tn "NSE_AllScanners" /tr "powershell.exe -NonInteractive -WindowStyle Hidden -ExecutionPolicy Bypass -File C:\Users\satya\nse_circuit_limits\run_all_scanners.ps1" /sc WEEKLY /d MON,TUE,WED,THU,FRI /st 15:35 /f
#
# To disable all individual tasks after verifying the orchestrator works:
# @("NSE_FetchData","NSE_EMAScreener","NSE_SwingScanner","NSE_MomentumScanner","NSE_MomentumRSWeeklyScanner","NSE_EMA25_ZL","NSE_ZL_SQUEEZE","NSE_CircuitLimits","US_FETCH_DATA","NSE_Dashboard","US_ZL_SQUEEZE","NSE_ScanStatusMailer") | ForEach-Object { schtasks /change /tn $_ /disable }
