> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.

# Design: Reduce Claude Code Token Usage

**Date:** 2026-06-26
**Status:** Approved
**Problem:** 100% of weekly usage from subagent-heavy sessions; 32% from general-purpose subagents spawned for code-location tasks that don't require Sonnet-level reasoning.

---

## Root Cause

"Find X and fix it" tasks spawn `general-purpose` agents (Sonnet) for the locate phase. These agents return full-context output injected back into the main thread. Two inefficiencies:

1. Sonnet used where Haiku suffices (locate tasks, simple edits)
2. General-purpose agent output is verbose — large context injection per call

---

## Changes

### 1. Default subagent model: Haiku

Add to `.claude/settings.json`:

```json
"defaultSubagentModel": "claude-haiku-4-5-20251001"
```

- All spawned subagents use Haiku unless explicitly overridden
- Main thread stays Sonnet (full capability unchanged)
- Per-agent model override still available for complex multi-file workflows

### 2. Global routing skill: `cavecrew:find-fix-router`

A global user skill that auto-triggers before any "find/locate/explore + fix" task.

**Decision tree:**

```
find/locate/explore task detected
  → always start: cavecrew-investigator (compressed caveman output, ~60% smaller)
  → result scope?
      1-2 files, bounded edit  → cavecrew-builder (surgical, 1-2 file max)
      3+ files, clear list     → inline tools (Grep/Read/Edit in main thread, no subagent)
      ambiguous / open-ended   → general-purpose (now Haiku via Change 1)
  → never: general-purpose for pure code location
```

**Location:** `~/.claude/plugins/local/` (global, all projects)
**Creation:** via `skill-creator` skill

---

## Expected Impact

| Driver | Before | After |
|--------|--------|-------|
| General-purpose locate tasks | Sonnet subagent | Haiku cavecrew-investigator |
| General-purpose fix tasks (1-2 files) | Sonnet subagent | Haiku cavecrew-builder |
| General-purpose (ambiguous scope) | Sonnet | Haiku (same agent, cheaper model) |
| Main thread reasoning | Sonnet | Sonnet (unchanged) |

Estimated reduction: 50-70% of the 32% general-purpose driver → ~15-20% total weekly savings.

---

## What Does Not Change

- Scanner pipeline code (no modifications)
- Skill invocation patterns for brainstorming/writing-plans
- Cavecrew-builder hard limit of 1-2 files (by design)
- Manual override: user can always say "use general-purpose" or "use Sonnet"

---

## Implementation Steps

1. Run `update-config` skill → add `defaultSubagentModel` to `.claude/settings.json`
2. Run `skill-creator` skill → create `cavecrew:find-fix-router` global skill
3. Test: run one "find + fix" task, verify cavecrew-investigator fires first

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
