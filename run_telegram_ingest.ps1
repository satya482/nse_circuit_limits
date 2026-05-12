$workDir = "C:\Users\satya\nse_circuit_limits"
$logDir  = "$workDir\logs"
$date    = Get-Date -Format "yyyy-MM-dd"
$logFile = "$logDir\telegram_ingest_$date.log"
New-Item -ItemType Directory -Force -Path $logDir           | Out-Null
New-Item -ItemType Directory -Force -Path "$workDir\telegram_themes" | Out-Null

function Log($msg) {
    $line = "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] $msg"
    $line | Tee-Object -FilePath $logFile -Append
}

Log "=== Telegram_Ingest START ==="

# Step 1 — Fetch new messages + download attachments
try {
    & C:\Python313\python.exe "$workDir\telegram_ingest.py" 2>&1 |
        ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
    Log "--- Step 1 done (telegram_ingest) ---"
} catch {
    Log "ERROR step 1: $_"
    exit 1
}

# Step 2 — Parse files + extract themes via Claude API
try {
    & C:\Python313\python.exe "$workDir\telegram_parser.py" 2>&1 |
        ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
    Log "--- Step 2 done (telegram_parser) ---"
} catch {
    Log "ERROR step 2: $_"
    exit 1
}

# Step 3 — Regenerate dashboard HTML
try {
    & C:\Python313\python.exe "$workDir\telegram_dashboard_generator.py" 2>&1 |
        ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
    Log "--- Step 3 done (dashboard_generator) ---"
} catch {
    Log "WARN step 3 (dashboard): $_"
}

# Step 4 — Git commit + push (markdown + JSON + dashboard; raw files excluded by .gitignore)
Log "--- Git commit+push ---"
& git -C $workDir add telegram_themes/ 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
& git -C $workDir commit -m "telegram themes $date" 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
& git -C $workDir push 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
Log "=== Telegram_Ingest DONE ==="

# To register the scheduled task (run once as admin):
# schtasks /create /tn "NSE_TelegramIngest" /tr "powershell -NonInteractive -File C:\Users\satya\nse_circuit_limits\run_telegram_ingest.ps1" /sc WEEKLY /d MON,TUE,WED,THU,FRI /st 18:30 /f
