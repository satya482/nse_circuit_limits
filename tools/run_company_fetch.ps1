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
    if ($LASTEXITCODE -ne 0) { throw "Trendlyne map failed (exit $LASTEXITCODE)" }
} catch {
    Log "WARNING: trendlyne map refresh failed: $_ (continuing with existing map)"
}

# Step 2: Discover the current eligible cluster universe
Log "--- Step 2: Discover cluster universe ---"
try {
    & C:\Python313\python.exe C:\Users\satya\nse_circuit_limits\cluster_membership.py --discover 2>&1 |
        ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
    if ($LASTEXITCODE -ne 0) { throw "Cluster discovery failed (exit $LASTEXITCODE)" }
    Log "=== cluster discovery FINISHED ==="
} catch {
    Log "=== ERROR in company_fetcher: $_ ==="
    exit 1
}

# Step 3: Perform due weekly membership and monthly description maintenance
Log "--- Step 3: Cluster maintenance ---"
try {
    & C:\Python313\python.exe C:\Users\satya\nse_circuit_limits\cluster_membership.py 2>&1 |
        ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
    if ($LASTEXITCODE -ne 0) { throw "Cluster maintenance failed (exit $LASTEXITCODE)" }
    Log "=== cluster maintenance FINISHED ==="
} catch {
    Log "=== ERROR in peer_group_builder: $_ ==="
    exit 1
}

# Step 3b: Generate stock labels
Log "--- Step 3b: Generate stock labels ---"
try {
    & C:\Python313\python.exe C:\Users\satya\nse_circuit_limits\tools\generate_stock_labels.py 2>&1 |
        ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
    if ($LASTEXITCODE -ne 0) { throw "Stock label generation failed (exit $LASTEXITCODE)" }
    Log "=== generate_stock_labels FINISHED ==="
} catch {
    Log "WARNING: label generation failed: $_ (continuing)"
}

# Step 4: Commit peer_groups.json and universe snapshot
Log "--- Step 4: Git commit+push ---"
& git -C C:\Users\satya\nse_circuit_limits add tools/trendlyne_id_map.json tools/sector_rotation_universe.json peer_groups.json tools/stock_labels.json data/cluster_membership_state.json 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
& git -C C:\Users\satya\nse_circuit_limits commit --no-verify -m "monthly peer group rebuild $date" 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
. "C:\Users\satya\nse_circuit_limits\git_helpers.ps1"
Push-GitWithRetry -RepoPath "C:\Users\satya\nse_circuit_limits" -LogFile $logFile
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
Log "--- Done ---"

# To register the scheduled task (run once as admin, 1st of each month at 10 AM):
# schtasks /create /tn "NSE_COMPANY_FETCH" /tr "powershell -NonInteractive -File C:\Users\satya\nse_circuit_limits\tools\run_company_fetch.ps1" /sc MONTHLY /d 1 /st 10:00 /f
