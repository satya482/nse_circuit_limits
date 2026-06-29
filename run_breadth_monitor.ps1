# run_breadth_monitor.ps1 — NSE Breadth Monitor runner
# Schedule: 4:50 PM Mon–Fri (same slot as previous breadth scanner)
# Logs: logs/breadth_monitor_YYYY-MM-DD.log

$logDir  = "C:\Users\satya\nse_circuit_limits\logs"
$date    = Get-Date -Format "yyyy-MM-dd"
$logFile = "$logDir\breadth_monitor_$date.log"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null

function Log($msg) {
    $line = "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] $msg"
    $line | Tee-Object -FilePath $logFile -Append
}

Log "=== BREADTH_MONITOR START ==="

try {
    & C:\Python313\python.exe C:\Users\satya\nse_circuit_limits\scanners\breadth_monitor.py 2>&1 |
        ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
    Log "=== FINISHED exit=0 ==="
} catch {
    Log "=== ERROR: $_ ==="
    exit 1
}

Log "--- Git commit+push ---"
$gitResult = & git -C C:\Users\satya\nse_circuit_limits status --porcelain data/breadth_history.csv dashboard/breadth.html 2>&1
if ($gitResult) {
    # Extract stats for commit message from latest CSV row
    $csv = Import-Csv "C:\Users\satya\nse_circuit_limits\data\breadth_history.csv"
    $last = $csv | Select-Object -Last 1
    $up4   = $last.up4_count
    $dn4   = $last.down4_count
    $r5    = [math]::Round([double]$last.ratio_5d, 2)
    $msg   = "[scan $date] breadth-monitor: up4=${up4} dn4=${dn4} ratio5d=$r5"

    & git -C C:\Users\satya\nse_circuit_limits add data/breadth_history.csv dashboard/breadth.html 2>&1 |
        ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
    & git -C C:\Users\satya\nse_circuit_limits commit -m $msg 2>&1 |
        ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
    & git -C C:\Users\satya\nse_circuit_limits push 2>&1 |
        ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
} else {
    Log "No changes to commit."
}
Log "--- Done ---"

# To register scheduled task (run once as admin):
# schtasks /create /tn "NSE_BreadthScanner" /tr "powershell -NonInteractive -File C:\Users\satya\nse_circuit_limits\run_breadth_monitor.ps1" /sc WEEKLY /d MON,TUE,WED,THU,FRI /st 16:50 /f
