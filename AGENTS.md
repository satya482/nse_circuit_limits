> Warning: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.

# Agent Instructions

This file is the repo-wide handoff contract for Codex, Claude Code, and any other coding agent working in `C:\Users\satya\nse_circuit_limits`.

## First Reads

1. Read `HANDOFF.md` for the current architecture, daily workflows, known dirty worktree state, and takeover checklist.
2. Read `CLAUDE.md` for detailed scanner-specific operating notes. It is Claude-named but contains repo-critical rules that apply to all agents.
3. Check `git status --short` before editing. This repo is actively shared with Claude Code; never overwrite or revert work you did not create.

## Non-Negotiable Repo Rules

- Every generated or newly created `.md` and `.html` file must include the SEBI disclaimer string `SEBI registered`.
- Use `disclaimer.py` constants in generators:
  - Markdown: `SEBI_MD_HEADER` and `SEBI_MD_FOOTER`
  - HTML: `SEBI_HTML_BANNER` and `SEBI_HTML_FOOTER`
- Pre-commit hooks are intentionally disabled for this repo because they hang or are too slow in practice. If committing here, use `git commit --no-verify`.
- Do not commit secrets, local SQLite databases, Telegram sessions, caches, logs, or raw downloaded data.
- Prefer `ohlc_db.py` / `us_ohlc_db.py` as scanner data access layers instead of reading SQLite directly.
- Treat PowerShell runner scripts as the production operating contract; most scheduled tasks log to `logs/` and commit scanner outputs.

## Validation Defaults

- Use focused tests first: `python -m pytest tests/<target_test>.py -v`.
- For broader Python validation, use `python -m pytest`.
- Do not run live data fetchers or scanner orchestration unless the user expects network/Kite/NSE access and local credentials to be used.
- Pine scripts cannot be fully tested locally; validate syntax and behavior manually in TradingView when required by the relevant plan.

## Watchlist Symbol Additions

When asked to add symbol(s) to the manual watchlists (phrasing like "add X to new listings",
"track this IPO", "add SYM to the watchlist", or a pasted list of tickers to track), update
**both** `new_listings.txt` and `ipo_listings.txt` together — they're read by
`near_52w_high_scanner.py` / `ipo_scanner.py` with no OHLC or gate requirement, so appending
blind (no `market.db` validation) is correct, not sloppy.

1. Normalize each symbol: strip an `NSE:` prefix, uppercase, trim whitespace.
2. Per file, skip symbols already present (case-insensitive, ignoring blank lines and
   `#`-comments) — don't create a no-op diff on a file where everything's already tracked.
   Don't touch the comment header block or reorder existing lines.
3. Append new symbols one per line. Both files have historically been saved without a
   trailing newline — check for one and add it before your first new line, or you'll
   concatenate onto the last existing symbol.
4. Stage only the two watchlist files (`git add new_listings.txt ipo_listings.txt`), never
   `git add -A` — something else may be mid-edit in this repo.
5. `git commit --no-verify -m "Add SYM1, SYM2 to new_listings.txt, ipo_listings.txt"` (name
   whichever file(s) actually changed), then `git push` immediately.
6. If push fails non-fast-forward, `git pull --rebase` and push again; stop and show the user
   on a real conflict rather than resolving it silently.

Claude Code also has this as the `ipo-add` skill (`~/.claude/skills/ipo-add/SKILL.md`) — same
procedure, kept in sync with this section.

## Shared-Agent Coordination

- Before starting: capture current `git status --short`.
- During work: avoid unrelated formatting churn and generated output refreshes.
- Before handoff: update `HANDOFF.md` if architecture, workflows, or current active work changed.
- If Claude Code and Codex touch the same file concurrently, stop and inspect diffs carefully before patching.

---

*Warning: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
