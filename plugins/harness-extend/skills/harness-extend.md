---
name: harness-extend
description: Extend existing harness projects with new features from incremental PDR files. Seamlessly integrates new requirements into existing projects while maintaining architectural consistency and continuing development workflow.
allowed-tools: Read, Write, Bash, Glob, Grep, Task, TodoWrite
context: fork
agent: general-purpose
---

# Extend Harness Projects

Add new features and capabilities to existing harness projects from incremental PDR specifications. This skill enables evolutionary development by extending existing projects with new requirements while maintaining architectural consistency and development momentum.

## When to Use This Skill

I will automatically use this skill when:
- You ask to "extend the project with new requirements"
- "Add features from this new PDR file"
- "Integrate additional requirements"
- "Expand the project with [new PDR]"
- "Continue development with updated specs"

## Core Methodology

This skill implements **Evolutionary Development** within Anthropic's methodology:

1. **Incremental Requirements**: Add new features without disrupting existing work
2. **Architecture Compatibility**: Ensure new features align with existing architecture
3. **Dependency Integration**: Properly integrate new features into existing task graph
4. **Context Preservation**: Maintain all existing progress and context
5. **Seamless Continuation**: Enable immediate continuation of development

## Process

### 1. Current State Analysis
- **Load existing project context**:
  - Read current `feature_list.json` and progress state
  - Analyze existing architecture from `.harness/arquitectura/` YAML files
  - Review current implementation progress and completed features
- **Validate project health**:
  - Ensure existing project is in clean state
  - Verify no broken or incomplete features
  - Confirm architecture is consistent

### 2. New Requirements Analysis
- **Parse new/updated PDR file**:
  - Extract new core features (CF-XXX)
  - Identify new secondary features (SF-XXX)
  - Analyze new technical requirements (TR-XXX)
- **Compare with existing requirements**:
  - Identify genuinely new features vs. modifications
  - Detect conflicts with existing features
  - Find opportunities for integration or consolidation

### 3. Architecture Compatibility Assessment
- **Analyze architectural impact**:
  - Determine if new features require architecture changes
  - Identify new technology dependencies or stack changes
  - Assess impact on existing architectural decisions
- **Plan architecture evolution**:
  - Update existing YAML files where necessary
  - Create new feature-specific architecture as needed
  - Maintain backward compatibility with existing implementation

### 4. Feature Integration and Dependency Mapping
- **Merge feature lists**:
  - Add new features with appropriate IDs (continuing sequence)
  - Set priority levels considering existing feature priorities
  - Map dependencies between new and existing features
- **Update parallel execution groups**:
  - Integrate new features into appropriate execution phases
  - Identify new opportunities for parallel development
  - Ensure optimal task ordering with updated dependencies

### 5. Context and Progress Integration
- **Update progress tracking**:
  - Extend `claude-progress.txt` with extension context
  - Update `project_config.json` with new requirements
  - Maintain complete history of project evolution
- **Preserve existing progress**:
  - Keep all completed features marked as done
  - Maintain existing git history and commits
  - Ensure no regression in existing functionality

### 6. Architecture Updates
Update architectural YAML files as needed:

**Global Architecture Updates**:
- `stack-decisions.yaml` - Add new technology requirements
- `coding-standards.yaml` - Extend standards for new feature types
- `api-contracts.yaml` - Add new API patterns or contracts
- `database-schema.yaml` - Extend data model for new features

**New Feature Architecture**:
- Create `.harness/arquitectura/features/[new-feature]/` directories
- Generate feature-specific architecture YAML
- Define integration contracts with existing features

### 7. Implementation Planning
- **Update implementation roadmap**:
  - Integrate new tasks into existing parallel groups
  - Plan optimal implementation order
  - Identify quick wins vs. complex integrations
- **Agent assignment optimization**:
  - Assign new features to appropriate agents
  - Balance workload across agent types
  - Plan any new specialized agent requirements

## Extension Scenarios

### Scenario 1: Additive Features
**Situation**: New features that don't conflict with existing ones
**Action**:
- Simply add to feature list with appropriate dependencies
- Create feature-specific architecture as needed
- Continue with normal implementation flow

### Scenario 2: Feature Modifications
**Situation**: Changes to existing feature requirements
**Action**:
- Update existing feature specifications
- Assess if already implemented features need changes
- Plan refactoring tasks if necessary

### Scenario 3: Architecture Evolution
**Situation**: New features require architectural changes
**Action**:
- Plan migration strategy for existing implementation
- Update global architecture YAML files
- Create migration tasks in feature list

### Scenario 4: New Technology Requirements
**Situation**: New features need different or additional technology
**Action**:
- Extend technology stack in stack-decisions.yaml
- Plan integration with existing technology choices
- Create setup tasks for new technology

### Scenario 5: Major Scope Expansion
**Situation**: Significant new functionality that changes project scope
**Action**:
- May recommend re-running `harness-plan` for major replanning
- Ensure project structure can accommodate growth
- Plan major architecture evolution if needed

## Integration Patterns

### Feature List Merging
```json
{
  "features": [
    // Existing features (preserve IDs and state)
    {"id": "CF-001", "passes": true, "implemented_at": "..."},
    {"id": "CF-002", "passes": false, "status": "in_progress"},

    // New features (continue ID sequence)
    {"id": "CF-011", "description": "New feature from extension PDR"},
    {"id": "SF-008", "dependencies": ["CF-011", "CF-002"]}
  ],
  "extension_history": [
    {
      "extended_at": "2024-01-15T10:00:00Z",
      "pdr_file": "additional-features.md",
      "features_added": ["CF-011", "SF-008", "SF-009"]
    }
  ]
}
```

### Architecture Evolution
```yaml
# stack-decisions.yaml evolution
technology_stack:
  frontend:
    framework: "react"  # Existing
    charts: "recharts"  # New requirement
  backend:
    framework: "express"  # Existing
    queue: "redis"        # New requirement
```

### Dependency Integration
- New features can depend on existing features
- Existing in-progress features may gain new dependencies
- Parallel groups may be reorganized for optimal execution

## Validation and Quality Assurance

### Pre-Extension Checks
- ✅ **Existing project is healthy** (tests pass, no broken features)
- ✅ **Architecture is consistent** (YAML files are complete)
- ✅ **New PDR is well-formed** (follows expected format)
- ✅ **No major conflicts detected** (new vs. existing requirements)

### Post-Extension Validation
- ✅ **Feature list is consistent** (no duplicate IDs, proper dependencies)
- ✅ **Architecture is coherent** (new and existing elements work together)
- ✅ **Implementation plan is viable** (parallel groups make sense)
- ✅ **Progress tracking is maintained** (existing history preserved)

## Success Criteria

A successful extension operation:
- ✅ **Seamlessly integrates new requirements** (no disruption to existing work)
- ✅ **Maintains architectural consistency** (new features align with existing design)
- ✅ **Preserves all existing progress** (no loss of completed work)
- ✅ **Enables immediate continuation** (ready for `harness-implement`)
- ✅ **Optimizes development workflow** (efficient parallel execution plan)

## Integration with Other Skills

**Before Extension**:
- May use `harness-resume` to ensure clean starting state
- Could require completion of in-progress features

**After Extension**:
- Usually continues with `harness-implement` for new features
- May trigger `harness-plan` for major architectural changes
- Seamlessly integrates with existing development workflow

This skill enables projects to grow and evolve naturally while maintaining the structured, autonomous development approach of the harness methodology.