> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.

# Design: Tree-sitter Symbol Index

**Date:** 2026-06-26
**Status:** Approved
**Goal:** Agents query a pre-built symbol index (file:line per definition) instead of spawning investigator subagents for code location. Zero per-repo setup — global tools + Claude Code post-commit hook.

---

## Architecture

```
post-commit hook (Claude Code settings.json PostToolUse)
  → ~/.claude/tools/build_index.py
      → tree-sitter parses all .py files in cwd
      → writes .code-index/symbols.json  (gitignored, per-repo)

agent: "find X"
  → find-fix-router skill
      → Bash: python ~/.claude/tools/query_index.py X
          hit  → file:line table, done
          miss → cavecrew-investigator fallback
```

---

## Components

### `~/.claude/tools/build_index.py`

- Takes CWD as repo root (optional `--root` arg override)
- Uses `tree_sitter_languages` package (pre-built binaries, no C compiler)
- Captures: `function_definition`, `class_definition` — name + line number
- Skips: `__pycache__`, `.venv`, `node_modules`, `*.pyc`, `*.pyi`
- Writes `.code-index/symbols.json` atomically (write to temp file → rename)
- No-op guard: reads `git rev-parse HEAD` on entry, compares to `.code-index/.last_commit`; exits in ~5ms if HEAD unchanged
- Appends `.code-index/` to repo `.gitignore` on first run if not already present
- Exits silently (no error) if no `.py` files found

### `~/.claude/tools/query_index.py`

- Args: `symbol_name [--repo /abs/path]` (default repo: CWD)
- Partial match, case-insensitive: `zlema` matches `zlema`, `zlema25`, `_zlema`
- Output format: `file.py:62: function zlema` — one line per match, stdout
- Exit 1 + empty output on: index missing, index has `"error"` key, no matches

### Index schema

```json
{
  "repo": "/abs/path/to/repo",
  "built_at": "2026-06-26T16:00:00+05:30",
  "head_commit": "abc1234",
  "symbols": {
    "zlema": [
      {"file": "ema25_zl_scanner.py", "line": 62, "kind": "function"}
    ],
    "WaveTrendCalculator": [
      {"file": "wavetrend_scanner.py", "line": 15, "kind": "class"}
    ]
  }
}
```

Keys are lowercase symbol names. Values are arrays (same name, multiple files).

### Claude Code hook (`~/.claude/settings.json`)

```json
"hooks": {
  "PostToolUse": [{
    "matcher": "Bash",
    "hooks": [{
      "type": "command",
      "command": "python C:/Users/satya/.claude/tools/build_index.py"
    }]
  }]
}
```

Fires after every `Bash` tool call. The no-op guard in `build_index.py` makes non-commit calls ~5ms.

### `~/.claude/skills/find-fix-router/SKILL.md` (updated decision tree)

```
Step 0: python ~/.claude/tools/query_index.py [X]
  hit  → return file:line table, done (no subagent)
  miss → proceed to Step 1 (cavecrew-investigator)

Step 1: spawn cavecrew-investigator ...
```

---

## Error Handling

| Condition | Behavior |
|-----------|----------|
| Index missing | `query_index.py` exits 1 → fallback fires |
| HEAD unchanged since last build | `build_index.py` exits in ~5ms, no write |
| `tree_sitter_languages` not installed | `build_index.py` writes `{"error": "..."}` → query exits 1 → fallback |
| Non-Python repo | No `.py` files found → no index written → fallback |
| No matches | `query_index.py` exits 1 → fallback |

All failure modes degrade gracefully to cavecrew-investigator. No user-visible errors.

---

## Installation

1. `pip install tree-sitter tree-sitter-languages` (global Python)
2. Write `~/.claude/tools/build_index.py`
3. Write `~/.claude/tools/query_index.py`
4. Add PostToolUse hook to `~/.claude/settings.json`
5. Update `~/.claude/skills/find-fix-router/SKILL.md` decision tree
6. Run `build_index.py` once manually in each existing repo to seed the index

---

## What Does Not Change

- Scanner pipeline code
- Per-repo `.gitignore` (auto-patched by indexer on first run)
- Existing cavecrew-investigator behavior (still the fallback)
- find-fix-router override clause (user "use general-purpose" still respected)

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
