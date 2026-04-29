$logDir  = "C:\Users\satya\nse_circuit_limits\logs"
$date    = Get-Date -Format "yyyy-MM-dd"
$logFile = "$logDir\fetch_data_$date.log"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null

function Log($msg) {
    $line = "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] $msg"
    $line | Tee-Object -FilePath $logFile -Append
}

Log "=== FETCH_DATA START ==="

# ── Step 1: Refresh Kite access token ────────────────────────────────────────
Log "--- Kite token refresh ---"
& C:\Python313\python.exe C:\Users\satya\nse_circuit_limits\ema-compression-scanner\kite_auth.py 2>&1 |
    ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }

if ($LASTEXITCODE -ne 0) {
    Log "=== ERROR: Kite auth failed (exit $LASTEXITCODE) - aborting ==="
    exit 1
}
Log "--- Kite auth OK ---"

# ── Step 2: Fetch all OHLC data into SQLite ───────────────────────────────────
Log "--- Fetching OHLC data ---"
try {
    & C:\Python313\python.exe C:\Users\satya\nse_circuit_limits\fetch_data.py 2>&1 |
        ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }

    if ($LASTEXITCODE -ne 0) {
        Log "=== ERROR: fetch_data.py failed (exit $LASTEXITCODE) ==="
        exit 1
    }
} catch {
    Log "=== ERROR: $_ ==="
    exit 1
}
Log "--- Data fetch complete ---"

# ── Step 3: Commit data_manifest.csv to git ───────────────────────────────────
Log "--- Git commit manifest ---"
& git -C C:\Users\satya\nse_circuit_limits add .ohlc_data/data_manifest.csv 2>&1 |
    ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
& git -C C:\Users\satya\nse_circuit_limits commit -m "data: manifest $date" 2>&1 |
    ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
& git -C C:\Users\satya\nse_circuit_limits push 2>&1 |
    ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }

Log "=== FETCH_DATA DONE ==="

# Scheduled task (run once as admin — runs before all scanners at 4:05 PM):
# schtasks /create /tn "NSE_FetchData" /tr "powershell.exe -NonInteractive -WindowStyle Hidden -File C:\Users\satya\nse_circuit_limits\run_fetch_data.ps1" /sc WEEKLY /d MON,TUE,WED,THU,FRI /st 16:05 /f