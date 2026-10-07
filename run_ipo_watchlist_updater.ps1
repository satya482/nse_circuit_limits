$ROOT = "C:\Users\satya\nse_circuit_limits"
$date = Get-Date -Format "yyyy-MM-dd"
$logDir = "$ROOT\logs"
$logFile = "$logDir\ipo_watchlist_updater_$date.log"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null

& C:\Python313\python.exe "$ROOT\ipo_watchlist_updater.py" 2>&1 |
    ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
if ($LASTEXITCODE -ne 0) { exit 1 }

& git -C $ROOT diff --quiet -- new_listings.txt ipo_listings.txt
if ($LASTEXITCODE -eq 0) { exit 0 }
if ($LASTEXITCODE -ne 1) { exit 1 }

& git -C $ROOT add -- new_listings.txt ipo_listings.txt
if ($LASTEXITCODE -ne 0) { exit 1 }
& git -C $ROOT commit --no-verify --only -m "[watchlist $date] add NSE EQ IPOs" -- new_listings.txt ipo_listings.txt 2>&1 |
    ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
if ($LASTEXITCODE -ne 0) { exit 1 }

& git -C $ROOT push 2>&1 |
    ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
if ($LASTEXITCODE -ne 0) {
    & git -C $ROOT pull --rebase 2>&1 |
        ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
    if ($LASTEXITCODE -ne 0) { exit 1 }
    & git -C $ROOT push 2>&1 |
        ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
}
exit $LASTEXITCODE
