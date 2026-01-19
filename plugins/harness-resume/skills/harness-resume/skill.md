---
name: harness-resume
description: Resume work after interruption in long-running agent projects. Analyzes current state, detects incomplete work or bugs, and continues from the appropriate checkpoint with full context recovery.
allowed-tools: Read, Write, Bash, Glob, Grep, Task, TodoWrite
context: fork
agent: general-purpose
---

# Resume Harness Work

Resume interrupted work in long-running agent projects by restoring context, analyzing current state, and continuing from the last valid checkpoint. This skill implements Anthropic's methodology for context recovery across multiple sessions.

## When to Use This Skill

I will automatically use this skill when:
- You ask to "resume the harness project"
- "Continue where we left off"
- "Pick up the interrupted work"
- "Analyze current project state and continue"
- Returning to a project after interruption
- Recovering from failed implementation sessions

## Core Methodology

This skill addresses the critical challenge of long-running agents: **maintaining progress across multiple context windows**. It implements Anthropic's approach to context recovery:

1. **State Analysis**: Comprehensive analysis of current project state
2. **Context Recovery**: Restore full architectural and progress context
3. **Issue Detection**: Identify incomplete work, bugs, or broken state
4. **Continuation Strategy**: Determine optimal next steps
5. **Seamless Restart**: Continue as if never interrupted

## Process

### 1. Project State Assessment
- **Read progress artifacts**:
  - `.claude/claude-progress.txt` - Human-readable progress log
  - `.claude/feature_list.json` - Structured feature tracking
  - `.claude/project_config.json` - Project configuration
- **Analyze git history**:
  - Recent commits to understand last work done
  - Identify any uncommitted changes
  - Check for work-in-progress branches

### 2. Architecture Context Recovery
- **Load complete architectural context**:
  - Read all YAML files from `.harness/arquitectura/` directory
  - Verify architectural consistency
  - Identify any missing or corrupted architecture files
- **Validate project structure**:
  - Ensure all expected directories and files exist
  - Check for any structural inconsistencies

### 3. Current State Validation
- **Run basic functionality tests**:
  - Execute `init.sh` to start development environment
  - Verify application starts without errors
  - Run any existing test suites
- **Identify broken or incomplete work**:
  - Check for features marked as complete but actually broken
  - Find half-implemented features without proper cleanup
  - Detect any architectural drift from planned design

### 4. Work Prioritization
- **Analyze available tasks**:
  - Identify tasks marked as in-progress but potentially abandoned
  - Find tasks ready for implementation (dependencies satisfied)
  - Prioritize bug fixes vs. new feature development
- **Determine continuation strategy**:
  - Fix broken state before continuing new work
  - Resume interrupted tasks with proper context
  - Plan next implementation phase

### 5. Context Injection and Continuation
- **Restore full context** for next implementation phase
- **Clean up any inconsistent state** before proceeding
- **Continue with appropriate skill**: Usually `harness-implement`

## Specific Recovery Scenarios

### Scenario 1: Clean Interruption
**Situation**: Work stopped cleanly with all features properly completed
**Action**:
- Validate current state is working
- Identify next priority tasks from feature list
- Continue with `harness-implement`

### Scenario 2: Mid-Feature Interruption
**Situation**: Feature implementation was interrupted halfway
**Action**:
- Assess current feature state
- Determine if work should be reverted or completed
- Clean up any inconsistent code before continuing
- Resume feature implementation with full context

### Scenario 3: Broken State
**Situation**: Current state has bugs or non-working functionality
**Action**:
- Identify root cause of breakage
- Use git history to find last working state
- Fix issues before continuing new development
- Update progress logs to reflect corrections

### Scenario 4: Architecture Drift
**Situation**: Implementation diverged from planned architecture
**Action**:
- Compare current implementation with architecture YAML
- Identify inconsistencies and deviations
- Refactor to align with planned architecture
- Update architecture if changes are justified

### Scenario 5: Missing Context
**Situation**: Critical files or context are missing
**Action**:
- Regenerate missing architectural context
- Recreate progress tracking if corrupted
- Restore from git history if possible
- Re-run `harness-plan` if architecture is completely lost

## Recovery Checklist

Before continuing work, ensure:
- ✅ **Development environment starts cleanly** (`init.sh` works)
- ✅ **All existing tests pass** (no regressions)
- ✅ **Architecture YAML is complete** (all expected files present)
- ✅ **Feature tracking is accurate** (reflects actual implementation state)
- ✅ **Git history is clean** (no uncommitted debugging code)
- ✅ **Progress logs are updated** (clear picture of what was accomplished)

## Context Recovery Patterns

### Progress Log Analysis
```
# claude-progress.txt patterns to analyze:
- Last completed features
- In-progress work descriptions
- Known issues or blockers
- Next planned steps
```

### Feature State Validation
```json
// feature_list.json analysis:
{
  "features": [
    {
      "id": "CF-001",
      "passes": true,      // Verify this is actually true
      "implemented_at": "...", // Check recent timestamp
      "status": "completed"    // Validate against actual code
    }
  ]
}
```

### Git History Investigation
```bash
# Commands used internally:
git log --oneline -10    # Recent work summary
git status              # Current working tree
git diff HEAD~1         # Last changes made
git branch              # Check for work branches
```

## Integration with Other Skills

**Before Resume**:
- May need to run basic project validation
- Could require architecture regeneration

**After Resume**:
- Usually continues with `harness-implement`
- May trigger `harness-plan` if major issues found
- Could use `harness-extend` if new requirements discovered

**Error Handling**:
- If recovery fails, may recommend starting fresh
- Can suggest reverting to last known good state
- May recommend manual intervention for complex issues

## Success Criteria

A successful resume operation:
- ✅ **Accurately assesses current state** (no false assumptions)
- ✅ **Identifies real issues** (bugs, incomplete work, drift)
- ✅ **Restores complete context** (architecture, progress, goals)
- ✅ **Enables seamless continuation** (as if never interrupted)
- ✅ **Maintains methodology compliance** (structured approach)

This skill ensures that the long-running agent methodology works across multiple sessions, maintaining the consistency and progress tracking that makes autonomous development possible.