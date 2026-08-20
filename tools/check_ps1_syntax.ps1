# check_ps1_syntax.ps1 — parse every tracked .ps1 for syntax errors before commit.
# Catches the class of bug where a non-ASCII char (em dash, curly quote, etc.) in a
# no-BOM UTF-8 script silently corrupts PowerShell 5.1's tokenizer: the runner then
# no-ops with zero log output and the scheduled task just shows LastTaskResult=1/failed.
# Run manually: pwsh -File tools\check_ps1_syntax.ps1  (or powershell.exe on 5.1)

$root = Split-Path -Parent $PSScriptRoot
$failed = $false

Get-ChildItem -Path $root -Filter *.ps1 -Recurse -ErrorAction SilentlyContinue |
    Where-Object {
        $relative = $_.FullName.Substring($root.Length)
        $relative -notmatch '\\\.claude\\worktrees\\'
    } |
    ForEach-Object {
        $errors = $null; $tokens = $null
        [System.Management.Automation.Language.Parser]::ParseFile($_.FullName, [ref]$tokens, [ref]$errors) | Out-Null
        if ($errors.Count -gt 0) {
            $failed = $true
            Write-Host "FAIL: $($_.FullName)" -ForegroundColor Red
            $errors | ForEach-Object { Write-Host "  Line $($_.Extent.StartLineNumber): $($_.Message)" -ForegroundColor Red }
        }
    }

if ($failed) {
    Write-Host "`nOne or more .ps1 files have syntax errors. Fix before committing." -ForegroundColor Red
    exit 1
} else {
    Write-Host "All .ps1 files parse OK." -ForegroundColor Green
    exit 0
}
