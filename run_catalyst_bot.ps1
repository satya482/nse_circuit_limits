$logDir  = "C:\Users\satya\nse_circuit_limits\logs"
$date    = Get-Date -Format "yyyy-MM-dd"
$logFile = "$logDir\catalyst_bot_$date.log"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null

function Log($msg) {
    $line = "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] $msg"
    $line | Tee-Object -FilePath $logFile -Append
}

Log "=== CATALYST_BOT START ==="

# Ensure user-level env vars are available to child processes
if (-not $env:DISCORD_WEBHOOK_URL) {
    $env:DISCORD_WEBHOOK_URL = [System.Environment]::GetEnvironmentVariable("DISCORD_WEBHOOK_URL", "User")
}

try {
    & C:\Python313\python.exe C:\Users\satya\nse_circuit_limits\stock_catalyst_bot.py 2>&1 |
        ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
    Log "=== FINISHED exit=0 ==="
} catch {
    Log "=== ERROR: $_ ==="
    exit 1
}

Log "--- Done ---"

# To register the scheduled task (run once as admin, fires after wt_bullcross_scanner):
# schtasks /create /tn "NSE_CATALYST_BOT" /tr "powershell -NonInteractive -File C:\Users\satya\nse_circuit_limits\run_catalyst_bot.ps1" /sc WEEKLY /d MON,TUE,WED,THU,FRI /st 16:35 /f
