> ⚠️ **Disclaimer:** I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.

# Reduce Token Usage Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Cut Claude Code weekly token usage by routing code-location tasks to cavecrew subagents and defaulting all subagents to Haiku instead of Sonnet.

**Architecture:** Two independent changes — (1) one-line JSON edit to user settings, (2) new global skill created via skill-creator. No scanner or pipeline code touched.

**Tech Stack:** JSON config edit; Claude Code skill (SKILL.md markdown); PowerShell for verification.

## Global Constraints

- `defaultSubagentModel` value must be exact: `claude-haiku-4-5-20251001`
- Settings file is user-level: `C:\Users\satya\.claude\settings.json` — NOT project-level
- Main thread model stays Sonnet — only subagents get Haiku
- Skill must be global (user-level), not project-scoped
- Never edit `.env` or `market.db`

---

### Task 1: Add defaultSubagentModel to user settings.json

**Files:**
- Modify: `C:\Users\satya\.claude\settings.json`

**Interfaces:**
- Produces: all spawned subagents default to `claude-haiku-4-5-20251001` unless overridden per-call

- [ ] **Step 1: Read current settings.json**

```
Read C:\Users\satya\.claude\settings.json
```

Current content (for reference):
```json
{
  "permissions": { ... },
  "enableWorkflows": true,
  "statusLine": { ... },
  "enabledPlugins": { ... },
  "extraKnownMarketplaces": { ... },
  "effortLevel": "high",
  "autoUpdatesChannel": "latest"
}
```

- [ ] **Step 2: Add defaultSubagentModel key**

Add at the top level of the JSON object (after `"effortLevel": "high"`):

```json
"defaultSubagentModel": "claude-haiku-4-5-20251001",
```

Final relevant section of the file should look like:
```json
{
  "effortLevel": "high",
  "autoUpdatesChannel": "latest",
  "defaultSubagentModel": "claude-haiku-4-5-20251001"
}
```

- [ ] **Step 3: Verify JSON is valid**

Run:
```powershell
Get-Content "C:\Users\satya\.claude\settings.json" | ConvertFrom-Json | Select-Object defaultSubagentModel
```

Expected output:
```
defaultSubagentModel
--------------------
claude-haiku-4-5-20251001
```

- [ ] **Step 4: Verify key is present and correct**

If Step 3 output shows `claude-haiku-4-5-20251001` — done. If blank or error — the JSON is malformed; re-read the file and fix the syntax (missing comma, extra brace, etc.).

---

### Task 2: Create global find-fix-router skill via skill-creator

**Files:**
- Creates (via skill-creator): global skill `find-fix-router` in user plugin directory

**Interfaces:**
- Consumes: nothing from Task 1
- Produces: a skill that auto-triggers whenever I'm about to do a "find + fix" or "locate X" task, routing to cavecrew-investigator first

- [ ] **Step 1: Invoke skill-creator skill**

Use the Skill tool to invoke `skill-creator` with the following pre-written SKILL.md content. Tell skill-creator:

> "I want to create a new global skill called `find-fix-router`. Skip evals — just create and install it. Here is the complete SKILL.md content to use:"

```markdown
---
name: find-fix-router
description: Routes "find + fix" and "locate X" tasks to the right subagent type to minimize token usage. Auto-triggers whenever the user asks to find code, locate a symbol, explore a module, or fix something across the codebase — especially before spawning any general-purpose agent for code location. Use this skill whenever you sense a code-search or find-then-edit pattern, even if the user doesn't say "find" explicitly.
---

# Find-Fix Router

Use this skill before spawning any subagent for a code-location or code-location+edit task.

## Decision Tree

```
Task: find / locate / explore / fix (anything requiring first knowing WHERE)
  │
  └─► Step 1: ALWAYS spawn cavecrew-investigator
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
        → spawn general-purpose (now Haiku via defaultSubagentModel)
           only when cavecrew-investigator output is insufficient
```

## Hard Rule

Never spawn general-purpose for pure code location ("where is X defined", "what calls Y", "which files use Z"). cavecrew-investigator handles this for a fraction of the cost with better output compression.

## Override

User says "use general-purpose" or "use Sonnet" → follow user instruction, skip this routing.
```

- [ ] **Step 2: Confirm skill-creator installs the skill globally**

When skill-creator prompts about location, confirm: **user-level (global)**, not project-scoped.

- [ ] **Step 3: Verify skill appears in available skills list**

After installation, the skill `find-fix-router` should appear in the skills list when starting a new session. Ask skill-creator to confirm the install path.

- [ ] **Step 4: Smoke test**

In a new Claude Code session, say:
> "find where ZLEMA25 is calculated and show me the formula"

Expected: cavecrew-investigator spawns first (not general-purpose). Verify in the session's agent activity that the investigator fired before any general-purpose agent.

---

## Verification Checklist

After both tasks:

- [ ] `defaultSubagentModel` key present in `C:\Users\satya\.claude\settings.json` with value `claude-haiku-4-5-20251001`
- [ ] `find-fix-router` skill available globally
- [ ] Smoke test: "find X" task routes to cavecrew-investigator, not general-purpose
- [ ] Main thread still uses Sonnet (check model indicator in status line)

---

*⚠️ Disclaimer: I am not a SEBI registered investment advisor. All content is for educational and informational purposes only and does not constitute investment advice. Please consult a SEBI registered investment advisor before making any investment decisions. Investments in securities market are subject to market risks, read all related documents carefully before investing.*
