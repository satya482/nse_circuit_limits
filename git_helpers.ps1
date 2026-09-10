# git_helpers.ps1 - shared git push-with-retry for run_*.ps1 scanner scripts
#
# Root cause fixed here (2026-09-10): scheduled scanners run back-to-back and can
# each commit+push around the same time. If another script pushed to main first,
# a plain "git push" is rejected (non-fast-forward) and the current script's
# commits are stranded locally, never reaching GitHub, with no retry.
#
# Push-GitWithRetry pushes once; on rejection it pulls (merge, not rebase - safe
# for unrelated files touched by other scanners) and retries the push exactly
# once. A real conflict (rare - would mean two scripts touched the same output
# file) is left unresolved and reported as a failure for manual review, not
# auto-resolved.

function Push-GitWithRetry {
    param(
        [Parameter(Mandatory = $true)][string]$RepoPath,
        [Parameter(Mandatory = $true)][string]$LogFile
    )

    & git -C $RepoPath push 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $LogFile -Append }
    if ($LASTEXITCODE -ne 0) {
        "Push rejected - pulling (merge) and retrying once..." | Tee-Object -FilePath $LogFile -Append | Out-Null
        & git -C $RepoPath pull --no-rebase --no-edit 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $LogFile -Append }
        if ($LASTEXITCODE -eq 0) {
            & git -C $RepoPath push 2>&1 | ForEach-Object { $_ | Tee-Object -FilePath $LogFile -Append }
        } else {
            "Pull failed (likely a real merge conflict) - not retrying push. Resolve manually." | Tee-Object -FilePath $LogFile -Append | Out-Null
        }
    }
}
