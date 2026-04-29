$logDir = Join-Path $PSScriptRoot "logs"
if (-not (Test-Path $logDir)) { New-Item -ItemType Directory -Path $logDir | Out-Null }
$logFile = Join-Path $logDir ("zl_squeeze_scanner_" + (Get-Date -Format "yyyy-MM-dd") + ".log")

Set-Location $PSScriptRoot

Write-Host "Running ZL Squeeze Scanner..." -ForegroundColor Cyan
python zl_squeeze_scanner.py 2>&1 | Tee-Object -FilePath $logFile

git add zl_squeeze_scans/
git commit -m "scan: zl-squeeze $(Get-Date -Format 'yyyy-MM-dd')"
