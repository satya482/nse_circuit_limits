$logDir  = "C:\Users\satya\nse_circuit_limits\logs"
$date    = Get-Date -Format "yyyy-MM-dd"
$logFile = "$logDir\company_fetch_$date.log"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null

function Log($msg) {
    $line = "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] $msg"
    $line | Tee-Object -FilePath $logFile -Append
}

Log "=== COMPANY_FETCH START (monthly) ==="

# Step 1: Refresh trendlyne ID map
Log "--- Step 1: Refresh trendlyne ID map ---"
try {
    & C:\Python313\python.exe C:\Users\satya\nse_circuit_limits\tools\build_trendlyne_map.py 2>&1 |
        ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
} catch {
    Log "WARNING: trendlyne map refresh failed: $_ (continuing with existing map)"
}

# Step 2: Fetch company descriptions (skips stocks with fresh cache)
Log "--- Step 2: Fetch company descriptions ---"
try {
    & C:\Python313\python.exe C:\Users\satya\nse_circuit_limits\tools\company_fetcher.py 2>&1 |
        ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
    Log "=== company_fetcher FINISHED ==="
} catch {
    Log "=== ERROR in company_fetcher: $_ ==="
    exit 1
}

# Step 3: Rebuild peer groups
Log "--- Step 3: Rebuild peer groups ---"
try {
    & C:\Python313\python.exe C:\Users\satya\nse_circuit_limits\tools\peer_group_builder.py 2>&1 |
        ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
    Log "=== peer_group_builder FINISHED ==="
} catch {
    Log "=== ERROR in peer_group_builder: $_ ==="
    exit 1
}

# Step 4: Commit peer_groups.json and universe snapshot
Log "--- Step 4: Git commit+push ---"
& git -C C:\Users\satya\nse_circuit_limits add tools/trendlyne_id_map.json tools/sector_rotation_universe.json peer_groups.json tools/peer_group_overrides.json 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
& git -C C:\Users\satya\nse_circuit_limits commit -m "monthly peer group rebuild $date" 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
& git -C C:\Users\satya\nse_circuit_limits push 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
Log "--- Done ---"

# To register the scheduled task (run once as admin, 1st of each month at 10 AM):
# schtasks /create /tn "NSE_COMPANY_FETCH" /tr "powershell -NonInteractive -File C:\Users\satya\nse_circuit_limits\tools\run_company_fetch.ps1" /sc MONTHLY /d 1 /st 10:00 /f
