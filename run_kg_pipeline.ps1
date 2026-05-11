$workDir  = "C:\Users\satya\nse_circuit_limits"
$etlDir   = "$workDir\fundamental_context\etl"
$expDir   = "$workDir\fundamental_context\graph\exporters"
$logDir   = "$workDir\logs"
$date     = Get-Date -Format "yyyy-MM-dd"
$logFile  = "$logDir\kg_pipeline_$date.log"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null

function Log($msg) {
    $line = "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] $msg"
    $line | Tee-Object -FilePath $logFile -Append
}

Log "=== KG_Pipeline START ==="

# Step 1 — Daily ETL pipeline (RSS → score recompute → EP flag)
try {
    & C:\Python313\python.exe "$etlDir\daily_pipeline.py" --mode full 2>&1 |
        ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
    Log "--- Step 1 done (daily_pipeline) ---"
} catch {
    Log "ERROR step 1: $_"
    exit 1
}

# Step 2 — Export to JSON (graph.json, catalysts.json, ep_watchlist.json, themes.json)
try {
    & C:\Python313\python.exe "$expDir\export_to_json.py" 2>&1 |
        ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
    Log "--- Step 2 done (export_to_json) ---"
} catch {
    Log "ERROR step 2: $_"
    exit 1
}

# Step 3 — Generate macro scenario JSONs (Vikram verdicts via Haiku)
try {
    & C:\Python313\python.exe "$expDir\generate_scenarios.py" 2>&1 |
        ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
    Log "--- Step 3 done (generate_scenarios) ---"
} catch {
    Log "ERROR step 3: $_"
    exit 1
}

# Step 3b — Weekly: refresh screener.in Key Points + concall insights (Sundays only)
$dayOfWeek = (Get-Date).DayOfWeek
if ($dayOfWeek -eq 'Sunday') {
    Log "--- Step 3b: weekly screener insights refresh (Sunday) ---"
    try {
        & C:\Python313\python.exe "$workDir\fundamental_context\graph\loaders\load_screener_insights.py" --limit 100 2>&1 |
            ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
        Log "--- Step 3b done (load_screener_insights) ---"
    } catch {
        Log "WARN step 3b skipped: $_"
    }
}

# Step 4 — Re-generate main dashboard (with EP + catalyst sections)
try {
    & C:\Python313\python.exe "$workDir\dashboard_generator.py" 2>&1 |
        ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
    Log "--- Step 4 done (dashboard_generator) ---"
} catch {
    Log "ERROR step 4: $_"
}

# Step 5 — Git commit + push
Log "--- Git commit+push ---"
& git -C $workDir add `
    graph_data/ `
    graph_dashboard.html `
    dashboard.html `
    "fundamental_context/data/processed/" 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }

& git -C $workDir commit -m "kg update $date" 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
& git -C $workDir push 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
Log "=== KG_Pipeline DONE ==="

# Schedule (run once as admin):
# schtasks /create /tn "NSE_KGPipeline" /tr "powershell.exe -NonInteractive -WindowStyle Hidden -File C:\Users\satya\nse_circuit_limits\run_kg_pipeline.ps1" /sc WEEKLY /d MON,TUE,WED,THU,FRI /st 17:15 /f
