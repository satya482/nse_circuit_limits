$ROOT = "C:\Users\satya\nse_circuit_limits"
$logDir = "$ROOT\logs"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null
$logFile = "$logDir\cluster_discovery_$(Get-Date -Format 'yyyy-MM-dd').log"
& C:\Python313\python.exe "$ROOT\cluster_membership.py" --discover 2>&1 |
    ForEach-Object { $_ | Tee-Object -FilePath $logFile -Append }
exit $LASTEXITCODE
