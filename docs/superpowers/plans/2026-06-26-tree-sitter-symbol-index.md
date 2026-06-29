> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.

# Tree-sitter Symbol Index Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a global Python symbol indexer that rebuilds on every git commit via a Claude Code PostToolUse hook, letting agents query file:line instantly instead of spawning investigator subagents.

**Architecture:** Two global scripts in `~/.claude/tools/` (indexer + query), a PostToolUse hook in `~/.claude/settings.json` that triggers the indexer, and an updated find-fix-router skill that checks the index before falling back to cavecrew-investigator. All files live outside any git repo — no project-level changes.

**Tech Stack:** Python 3.13, `tree-sitter-languages` (pre-built Tree-sitter grammars), PowerShell for verification.

## Global Constraints

- All tool scripts: `C:\Users\satya\.claude\tools\` (create dir if missing)
- All test scripts: `C:\Users\satya\.claude\tools\tests\`
- Index per-repo: `<repo_root>\.code-index\symbols.json` (gitignored by indexer)
- Stamp file: `<repo_root>\.code-index\.last_commit` (7-char HEAD sha)
- JSON keys are **lowercase** symbol names; `"name"` field preserves original casing
- Path separators in index: forward slashes only (`/`), even on Windows
- IST timestamps: `datetime.timezone(datetime.timedelta(hours=5, minutes=30))`
- No git commits in this plan — all output files are outside git repos; tasks end with verification steps

---

### Task 1: build_index.py — Tree-sitter indexer

**Files:**
- Create: `C:\Users\satya\.claude\tools\build_index.py`
- Create: `C:\Users\satya\.claude\tools\tests\test_build_index.py`

**Interfaces:**
- Produces: `<repo_root>\.code-index\symbols.json` — consumed by Task 2's `query_index.py`
- Produces: `<repo_root>\.code-index\.last_commit` — no-op guard stamp

- [ ] **Step 1: Install dependency**

```powershell
pip install tree-sitter-languages
```

Expected output includes: `Successfully installed tree-sitter-languages-...`

Verify:
```powershell
python -c "from tree_sitter_languages import get_parser; print('ok')"
```
Expected: `ok`

- [ ] **Step 2: Create tools directory**

```powershell
New-Item -ItemType Directory -Force "C:\Users\satya\.claude\tools\tests" | Out-Null
```

- [ ] **Step 3: Write the failing tests**

Create `C:\Users\satya\.claude\tools\tests\test_build_index.py`:

```python
#!/usr/bin/env python3
import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from build_index import collect_py_files, parse_symbols, needs_rebuild, ensure_gitignore

def test_collect_skips_pycache():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "scanner.py").write_text("def scan(): pass")
        cache = root / "__pycache__"
        cache.mkdir()
        (cache / "cached.py").write_text("def cached(): pass")
        files = collect_py_files(root)
        names = [f.name for f in files]
        assert "scanner.py" in names
        assert "cached.py" not in names
        print("PASS: collect_py_files skips __pycache__")

def test_parse_finds_functions_and_classes():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        sample = root / "sample.py"
        sample.write_text(
            "def zlema(series, n):\n"
            "    pass\n"
            "\n"
            "class WaveTrendCalculator:\n"
            "    def compute(self):\n"
            "        pass\n"
        )
        symbols = parse_symbols([sample], root)
        if symbols is None:
            print("SKIP: tree_sitter_languages not installed")
            return
        assert "zlema" in symbols
        assert symbols["zlema"][0]["kind"] == "function"
        assert symbols["zlema"][0]["line"] == 1
        assert "wavetrendcalculator" in symbols
        assert symbols["wavetrendcalculator"][0]["kind"] == "class"
        assert symbols["wavetrendcalculator"][0]["line"] == 4
        # method is also indexed
        assert "compute" in symbols
        print("PASS: parse_symbols finds functions and classes")

def test_parse_key_is_lowercase():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "f.py").write_text("class MyClass: pass\n")
        symbols = parse_symbols([root / "f.py"], root)
        if symbols is None:
            print("SKIP")
            return
        assert "myclass" in symbols
        assert symbols["myclass"][0]["name"] == "MyClass"
        print("PASS: parse_symbols key is lowercase, name preserves casing")

def test_parse_path_uses_forward_slashes():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        sub = root / "sub"
        sub.mkdir()
        (sub / "mod.py").write_text("def fn(): pass\n")
        symbols = parse_symbols([sub / "mod.py"], root)
        if symbols is None:
            print("SKIP")
            return
        assert "\\" not in symbols["fn"][0]["file"]
        print("PASS: parse_symbols paths use forward slashes")

def test_needs_rebuild_true_when_no_stamp():
    with tempfile.TemporaryDirectory() as tmp:
        assert needs_rebuild(Path(tmp), "abc1234") is True
        print("PASS: needs_rebuild True when no stamp")

def test_needs_rebuild_false_when_same_commit():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        d = root / ".code-index"
        d.mkdir()
        (d / ".last_commit").write_text("abc1234")
        assert needs_rebuild(root, "abc1234") is False
        print("PASS: needs_rebuild False when commit unchanged")

def test_needs_rebuild_true_when_different_commit():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        d = root / ".code-index"
        d.mkdir()
        (d / ".last_commit").write_text("abc1234")
        assert needs_rebuild(root, "def5678") is True
        print("PASS: needs_rebuild True when commit changed")

def test_ensure_gitignore_adds_entry():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        ensure_gitignore(root)
        assert ".code-index/" in (root / ".gitignore").read_text()
        print("PASS: ensure_gitignore adds entry")

def test_ensure_gitignore_no_duplicate():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / ".gitignore").write_text(".code-index/\n")
        ensure_gitignore(root)
        assert (root / ".gitignore").read_text().count(".code-index/") == 1
        print("PASS: ensure_gitignore no duplicate")

if __name__ == "__main__":
    test_collect_skips_pycache()
    test_parse_finds_functions_and_classes()
    test_parse_key_is_lowercase()
    test_parse_path_uses_forward_slashes()
    test_needs_rebuild_true_when_no_stamp()
    test_needs_rebuild_false_when_same_commit()
    test_needs_rebuild_true_when_different_commit()
    test_ensure_gitignore_adds_entry()
    test_ensure_gitignore_no_duplicate()
    print("\nAll tests passed.")
```

- [ ] **Step 4: Run tests — confirm they fail**

```powershell
python "C:\Users\satya\.claude\tools\tests\test_build_index.py"
```

Expected: `ModuleNotFoundError: No module named 'build_index'`

- [ ] **Step 5: Write build_index.py**

Create `C:\Users\satya\.claude\tools\build_index.py`:

```python
#!/usr/bin/env python3
"""Tree-sitter symbol indexer. Writes .code-index/symbols.json at repo root."""
import argparse
import datetime
import json
import os
from pathlib import Path

SKIP_DIRS = {"__pycache__", ".venv", "venv", "node_modules", ".git",
             ".mypy_cache", "dist", "build", ".tox", ".eggs"}


def get_repo_root(start: str = None) -> Path:
    p = Path(start or os.getcwd()).resolve()
    while p != p.parent:
        if (p / ".git").exists():
            return p
        p = p.parent
    return Path(start or os.getcwd()).resolve()


def get_head_commit(repo_root: Path) -> str:
    try:
        head = (repo_root / ".git" / "HEAD").read_text().strip()
        if head.startswith("ref:"):
            ref_path = repo_root / ".git" / head[5:].strip()
            if ref_path.exists():
                return ref_path.read_text().strip()[:7]
        return head[:7]
    except Exception:
        return "unknown"


def needs_rebuild(repo_root: Path, head: str) -> bool:
    stamp = repo_root / ".code-index" / ".last_commit"
    if not stamp.exists():
        return True
    return stamp.read_text().strip() != head


def collect_py_files(repo_root: Path) -> list:
    files = []
    for f in repo_root.rglob("*.py"):
        if not any(part in SKIP_DIRS for part in f.parts):
            files.append(f)
    return files


def parse_symbols(py_files: list, repo_root: Path) -> dict | None:
    try:
        from tree_sitter_languages import get_parser
    except ImportError:
        return None

    parser = get_parser("python")
    symbols = {}

    for py_file in py_files:
        try:
            source = py_file.read_bytes()
            tree = parser.parse(source)
            rel = str(py_file.relative_to(repo_root)).replace("\\", "/")
            stack = [tree.root_node]
            while stack:
                node = stack.pop()
                if node.type in ("function_definition", "class_definition"):
                    for child in node.children:
                        if child.type == "identifier":
                            name = child.text.decode()
                            kind = "function" if node.type == "function_definition" else "class"
                            line = child.start_point[0] + 1
                            key = name.lower()
                            if key not in symbols:
                                symbols[key] = []
                            symbols[key].append({
                                "file": rel,
                                "line": line,
                                "kind": kind,
                                "name": name,
                            })
                            break
                stack.extend(node.children)
        except Exception:
            continue

    return symbols


def ensure_gitignore(repo_root: Path) -> None:
    entry = ".code-index/"
    gi = repo_root / ".gitignore"
    if gi.exists():
        if entry in gi.read_text():
            return
        with gi.open("a") as f:
            f.write(f"\n{entry}\n")
    else:
        gi.write_text(f"{entry}\n")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=None)
    args = ap.parse_args()

    repo_root = Path(args.root).resolve() if args.root else get_repo_root()
    head = get_head_commit(repo_root)

    if not needs_rebuild(repo_root, head):
        return

    py_files = collect_py_files(repo_root)
    if not py_files:
        return

    index_dir = repo_root / ".code-index"
    index_dir.mkdir(exist_ok=True)
    ensure_gitignore(repo_root)

    symbols = parse_symbols(py_files, repo_root)

    tz_ist = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
    now = datetime.datetime.now(tz_ist).isoformat()

    if symbols is None:
        data = {"error": "tree_sitter_languages not installed",
                "repo": str(repo_root), "built_at": now}
    else:
        data = {
            "repo": str(repo_root),
            "built_at": now,
            "head_commit": head,
            "symbols": symbols,
        }

    tmp = index_dir / "symbols.json.tmp"
    tmp.write_text(json.dumps(data, indent=2))
    os.replace(str(tmp), str(index_dir / "symbols.json"))
    (index_dir / ".last_commit").write_text(head)


if __name__ == "__main__":
    main()
```

- [ ] **Step 6: Run tests — confirm they pass**

```powershell
python "C:\Users\satya\.claude\tools\tests\test_build_index.py"
```

Expected:
```
PASS: collect_py_files skips __pycache__
PASS: parse_symbols finds functions and classes
PASS: parse_symbols key is lowercase, name preserves casing
PASS: parse_symbols paths use forward slashes
PASS: needs_rebuild True when no stamp
PASS: needs_rebuild False when commit unchanged
PASS: needs_rebuild True when commit changed
PASS: ensure_gitignore adds entry
PASS: ensure_gitignore no duplicate

All tests passed.
```

- [ ] **Step 7: Smoke test against this repo**

```powershell
python "C:\Users\satya\.claude\tools\build_index.py" --root "C:\Users\satya\nse_circuit_limits"
Get-Content "C:\Users\satya\nse_circuit_limits\.code-index\symbols.json" | python -c "import json,sys; d=json.load(sys.stdin); print(f'symbols: {len(d[\"symbols\"])}, head: {d[\"head_commit\"]}')"
```

Expected: `symbols: <N>, head: <7-char sha>` where N > 50.

---

### Task 2: query_index.py — query interface

**Files:**
- Create: `C:\Users\satya\.claude\tools\query_index.py`
- Create: `C:\Users\satya\.claude\tools\tests\test_query_index.py`

**Interfaces:**
- Consumes: `<repo_root>\.code-index\symbols.json` written by Task 1
- Produces: stdout lines `file.py:N: kind name`, exit 0 on match, exit 1 on miss/error

- [ ] **Step 1: Write the failing tests**

Create `C:\Users\satya\.claude\tools\tests\test_query_index.py`:

```python
#!/usr/bin/env python3
import json
import subprocess
import sys
import tempfile
from pathlib import Path

QUERY = Path(__file__).parent.parent / "query_index.py"


def make_index(root: Path, symbols: dict) -> None:
    d = root / ".code-index"
    d.mkdir(exist_ok=True)
    data = {
        "repo": str(root),
        "built_at": "2026-06-26T16:00:00+05:30",
        "head_commit": "abc1234",
        "symbols": symbols,
    }
    (d / "symbols.json").write_text(json.dumps(data))


def run(symbol: str, repo: str) -> tuple:
    r = subprocess.run(
        [sys.executable, str(QUERY), symbol, "--repo", repo],
        capture_output=True, text=True,
    )
    return r.returncode, r.stdout.strip()


def test_exact_match():
    with tempfile.TemporaryDirectory() as tmp:
        make_index(Path(tmp), {
            "zlema": [{"file": "scanner.py", "line": 62, "kind": "function", "name": "zlema"}]
        })
        rc, out = run("zlema", tmp)
        assert rc == 0, f"rc={rc}"
        assert "scanner.py:62: function zlema" in out
        print("PASS: exact match")


def test_partial_match():
    with tempfile.TemporaryDirectory() as tmp:
        make_index(Path(tmp), {
            "zlema":   [{"file": "a.py", "line": 10, "kind": "function", "name": "zlema"}],
            "zlema25": [{"file": "b.py", "line": 20, "kind": "function", "name": "zlema25"}],
            "_zlema":  [{"file": "c.py", "line": 30, "kind": "function", "name": "_zlema"}],
        })
        rc, out = run("zlema", tmp)
        assert rc == 0
        assert "a.py:10" in out
        assert "b.py:20" in out
        assert "c.py:30" in out
        print("PASS: partial match")


def test_case_insensitive():
    with tempfile.TemporaryDirectory() as tmp:
        make_index(Path(tmp), {
            "wavetrendcalculator": [
                {"file": "wt.py", "line": 15, "kind": "class", "name": "WaveTrendCalculator"}
            ]
        })
        rc, out = run("WaveTrend", tmp)
        assert rc == 0
        assert "wt.py:15: class WaveTrendCalculator" in out
        print("PASS: case-insensitive match")


def test_no_match_exits_1():
    with tempfile.TemporaryDirectory() as tmp:
        make_index(Path(tmp), {
            "compute": [{"file": "a.py", "line": 5, "kind": "function", "name": "compute"}]
        })
        rc, out = run("nonexistent_xyz_symbol", tmp)
        assert rc == 1
        assert out == ""
        print("PASS: no match → exit 1, empty output")


def test_missing_index_exits_1():
    with tempfile.TemporaryDirectory() as tmp:
        rc, _ = run("anything", tmp)
        assert rc == 1
        print("PASS: missing index → exit 1")


def test_error_index_exits_1():
    with tempfile.TemporaryDirectory() as tmp:
        d = Path(tmp) / ".code-index"
        d.mkdir()
        (d / "symbols.json").write_text(json.dumps({"error": "tree_sitter_languages not installed"}))
        rc, _ = run("anything", tmp)
        assert rc == 1
        print("PASS: error index → exit 1")


def test_output_sorted():
    with tempfile.TemporaryDirectory() as tmp:
        make_index(Path(tmp), {
            "fn": [
                {"file": "z.py", "line": 1, "kind": "function", "name": "fn"},
                {"file": "a.py", "line": 1, "kind": "function", "name": "fn"},
            ]
        })
        rc, out = run("fn", tmp)
        lines = out.splitlines()
        assert lines == sorted(lines)
        print("PASS: output is sorted")


if __name__ == "__main__":
    test_exact_match()
    test_partial_match()
    test_case_insensitive()
    test_no_match_exits_1()
    test_missing_index_exits_1()
    test_error_index_exits_1()
    test_output_sorted()
    print("\nAll tests passed.")
```

- [ ] **Step 2: Run tests — confirm they fail**

```powershell
python "C:\Users\satya\.claude\tools\tests\test_query_index.py"
```

Expected: error about missing `query_index.py` or `FileNotFoundError`.

- [ ] **Step 3: Write query_index.py**

Create `C:\Users\satya\.claude\tools\query_index.py`:

```python
#!/usr/bin/env python3
"""Query the Tree-sitter symbol index. Exit 0 + stdout on match, exit 1 on miss."""
import argparse
import json
import os
import sys
from pathlib import Path


def get_repo_root(start: str = None) -> Path:
    p = Path(start or os.getcwd()).resolve()
    while p != p.parent:
        if (p / ".git").exists():
            return p
        p = p.parent
    return Path(start or os.getcwd()).resolve()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("symbol")
    ap.add_argument("--repo", default=None)
    args = ap.parse_args()

    repo_root = Path(args.repo).resolve() if args.repo else get_repo_root()
    index_path = repo_root / ".code-index" / "symbols.json"

    if not index_path.exists():
        sys.exit(1)

    try:
        data = json.loads(index_path.read_text())
    except Exception:
        sys.exit(1)

    if "error" in data:
        sys.exit(1)

    query = args.symbol.lower()
    symbols = data.get("symbols", {})

    matches = []
    for key, entries in symbols.items():
        if query in key:
            for entry in entries:
                matches.append(
                    f"{entry['file']}:{entry['line']}: {entry['kind']} {entry['name']}"
                )

    if not matches:
        sys.exit(1)

    print("\n".join(sorted(matches)))


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Run tests — confirm they pass**

```powershell
python "C:\Users\satya\.claude\tools\tests\test_query_index.py"
```

Expected:
```
PASS: exact match
PASS: partial match
PASS: case-insensitive match
PASS: no match → exit 1, empty output
PASS: missing index → exit 1
PASS: error index → exit 1
PASS: output is sorted

All tests passed.
```

- [ ] **Step 5: Smoke test against this repo**

```powershell
python "C:\Users\satya\.claude\tools\query_index.py" zlema --repo "C:\Users\satya\nse_circuit_limits"
```

Expected: multiple lines like `ema25_zl_scanner.py:62: function zlema`

---

### Task 3: Wire up — hook + skill update + seed

**Files:**
- Modify: `C:\Users\satya\.claude\settings.json`
- Modify: `C:\Users\satya\.claude\skills\find-fix-router\SKILL.md`

**Interfaces:**
- Consumes: `C:\Users\satya\.claude\tools\build_index.py` (Task 1)
- Consumes: `C:\Users\satya\.claude\tools\query_index.py` (Task 2)
- Produces: live hook + updated skill — system is fully operational

- [ ] **Step 1: Read current settings.json**

Read `C:\Users\satya\.claude\settings.json`. Current hooks section is absent — the PostToolUse key does not exist yet.

- [ ] **Step 2: Add PostToolUse hook to settings.json**

Add a `"hooks"` key at the top level. The complete hooks block to add:

```json
"hooks": {
  "PostToolUse": [
    {
      "matcher": "Bash",
      "hooks": [
        {
          "type": "command",
          "command": "python C:/Users/satya/.claude/tools/build_index.py"
        }
      ]
    }
  ]
}
```

The command uses forward slashes — required for Claude Code hook execution on Windows.

- [ ] **Step 3: Verify hook is valid JSON**

```powershell
Get-Content "C:\Users\satya\.claude\settings.json" | ConvertFrom-Json | Select-Object -ExpandProperty hooks | ConvertTo-Json -Depth 5
```

Expected: the PostToolUse array printed without error.

- [ ] **Step 4: Update find-fix-router skill — add Step 0**

Read `C:\Users\satya\.claude\skills\find-fix-router\SKILL.md`.

Replace the Decision Tree section with:

```markdown
## Decision Tree

```
Task: find / locate / explore / fix (anything requiring first knowing WHERE)
  │
  └─► Step 0: python C:/Users/satya/.claude/tools/query_index.py [X]
              exit 0 + lines → return result, DONE (no subagent)
              exit 1 (miss/no index) → continue to Step 1
  │
  └─► Step 1: spawn cavecrew-investigator
              prompt: "Find [X] — return file:line table only"
              → compressed caveman output (~60% smaller context injection)
  │
  └─► Step 2: Assess result scope

      1–2 files, edit is bounded
        → spawn cavecrew-builder
           prompt: "Edit [file:line] to [change]"
           hard limit: 1-2 files only

      3+ files, list is clear
        → use inline tools (Grep/Read/Edit in main thread)
           no subagent spawn — avoids context injection overhead

      Ambiguous / open-ended / cross-module reasoning
        → spawn general-purpose
           only when cavecrew-investigator output is insufficient
```
```

- [ ] **Step 5: Verify skill file updated**

```powershell
Select-String -Path "C:\Users\satya\.claude\skills\find-fix-router\SKILL.md" -Pattern "query_index"
```

Expected: one match on the Step 0 line.

- [ ] **Step 6: Seed index in all existing repos**

Run the indexer in each repo that has Python files:

```powershell
python "C:\Users\satya\.claude\tools\build_index.py" --root "C:\Users\satya\nse_circuit_limits"
python "C:\Users\satya\.claude\tools\build_index.py" --root "C:\Users\satya\dhan-mcp-server"
```

Verify both created their index:
```powershell
Test-Path "C:\Users\satya\nse_circuit_limits\.code-index\symbols.json"
Test-Path "C:\Users\satya\dhan-mcp-server\.code-index\symbols.json"
```

Expected: `True` for each.

- [ ] **Step 7: End-to-end test**

```powershell
python "C:\Users\satya\.claude\tools\query_index.py" zlema --repo "C:\Users\satya\nse_circuit_limits"
```

Expected: lines like:
```
ema25_zl_scanner.py:62: function zlema
momentum_scanner.py:68: function zlema
weekly_zl_scanner.py:54: function zlema
```

Then verify no-op guard works (run twice, second should be instant):
```powershell
Measure-Command { python "C:\Users\satya\.claude\tools\build_index.py" --root "C:\Users\satya\nse_circuit_limits" }
```

Expected: `TotalMilliseconds` < 50 (HEAD unchanged, no rebuild).

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
