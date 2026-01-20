---
name: harness-plan
description: Generate comprehensive architectural planning and YAML configuration for long-running agent projects. Critical phase for creating structured architecture that enables parallel agent implementation with context injection.
allowed-tools: Read, Write, Bash, Glob, Grep, TodoWrite
context: fork
agent: general-purpose
---

# Harness Architectural Planning

**CRITICAL SKILL** - Generate comprehensive architectural plans and YAML configurations that enable parallel agent implementation with context injection. This implements the planning phase from Anthropic's long-running agents methodology.

## When to Use This Skill

I will automatically use this skill when:
- Triggered automatically after `harness-init`
- You ask for "architectural planning for harness project"
- "Generate system design and implementation plan"
- "Create YAML architecture for the project"
- "Plan parallel implementation strategy"

## Core Methodology

This skill implements the **Planning Phase** from Anthropic's methodology, solving the critical problem where agents attempt to "one-shot" entire applications. Instead, we:

1. **Analyze requirements comprehensively**
2. **Make architectural decisions upfront**
3. **Create structured contracts (YAML)**
4. **Enable parallel implementation with clear boundaries**

## Process

### 1. Deep PDR Analysis
- Read the complete PDR from `.claude/pdr.md`
- Extract and categorize ALL features:
  - Core Features (CF-001, CF-002, etc.)
  - Secondary Features (SF-001, SF-002, etc.)
  - Technical Requirements (TR-001, TR-002, etc.)
- Analyze non-functional requirements
- Identify integration points and dependencies

### 2. Architectural Decision Making
- Determine technology stack based on project type
- Choose architecture patterns (MVC, hexagonal, microservices, etc.)
- Define API contracts and data schemas
- Plan component boundaries and responsibilities
- Select development tools and frameworks

### 3. YAML Architecture Generation
Create comprehensive architecture documentation:

**Global Architecture (`.harness/arquitectura/global/`)**:
- `stack-decisions.yaml` - Technology choices and rationale
- `coding-standards.yaml` - Naming conventions, project structure
- `api-contracts.yaml` - REST conventions, authentication, pagination
- `database-schema.yaml` - Data model patterns and conventions

**Cross-Cutting Concerns (`.harness/arquitectura/cross-cutting/`)**:
- `error-handling.yaml` - Global error strategy and patterns
- `logging.yaml` - Structured logging approach
- `testing-strategy.yaml` - Testing pyramid and tools

**Feature-Specific Architecture (`.harness/arquitectura/features/`)**:
- `[feature-name]/architecture.yaml` - Feature-specific decisions
- `[feature-name]/api-spec.yaml` - API endpoints for feature
- `[feature-name]/components.yaml` - UI components and contracts

### 4. Task Breakdown and Parallel Groups
- Analyze feature dependencies and create dependency graph
- Group tasks into parallel execution phases:
  - **Setup Phase**: Infrastructure, database, tooling (parallel)
  - **Foundation Phase**: Auth, base components, routing (parallel after setup)
  - **Feature Phase**: Individual features (massively parallel)
  - **Polish Phase**: Testing, optimization, deployment (parallel)

### 5. Context Injection Strategy
- Design what architectural context each agent type needs:
  - **Frontend Agent**: UI patterns, component standards, API contracts
  - **Backend Agent**: Database schema, API contracts, business logic patterns
  - **Data Agent**: Database patterns, data processing standards
  - **DevOps Agent**: Infrastructure patterns, deployment strategies
- Create filtered context to reduce token usage per agent

### 6. Update Feature Tracking
- Transform basic `feature_list.json` into comprehensive implementation plan
- Add architectural metadata to each feature
- Assign appropriate agent types (frontend, backend, data, devops)
- Set up parallel execution groups with dependencies
- Mark architecture as complete and ready for implementation

## Key Outputs

### Architecture YAML Files
```
.harness/arquitectura/
├── global/
│   ├── stack-decisions.yaml      # Tech stack and architecture patterns
│   ├── coding-standards.yaml     # Development conventions
│   ├── api-contracts.yaml        # Global API standards
│   └── database-schema.yaml      # Data modeling standards
├── features/
│   └── [feature-name]/
│       ├── architecture.yaml     # Feature-specific architecture
│       ├── api-spec.yaml        # Feature APIs
│       └── components.yaml       # UI component contracts
└── cross-cutting/
    ├── error-handling.yaml       # Error management strategy
    ├── logging.yaml              # Logging patterns
    └── testing-strategy.yaml     # Testing approach
```

### Updated Feature List
- Complete task breakdown with 20-50+ implementation tasks
- Parallel execution groups (setup → foundation → features → polish)
- Agent assignments with clear responsibilities
- Dependencies mapped for optimal parallel execution
- Ready for context injection during implementation

### Development Infrastructure
- `init.sh` - Development server startup script specific to chosen stack
- Architecture-specific tooling configuration
- Integration with chosen development tools

## Critical Success Factors

1. **Comprehensive Analysis**: Every PDR requirement becomes trackable tasks
2. **Clear Boundaries**: Each agent knows exactly what to build and how
3. **Context Contracts**: YAML provides unambiguous architectural guidance
4. **Parallel Optimization**: Task breakdown enables maximum parallelization
5. **Implementation Ready**: Next phase can begin immediately without decisions

## Integration with Implementation

After planning completes:
- `harness-implement` can immediately begin parallel execution
- Each agent receives precisely the architectural context it needs
- No "guessing" or architectural decisions during implementation
- Clean handoff with complete context preservation

## Methodology Compliance

This skill directly implements Anthropic's core insight:
> "The key insight here was finding a way for agents to quickly understand the state of work when starting with a fresh context window, which is accomplished with structured artifacts alongside clear architectural contracts."

The YAML architecture serves as the "structured artifacts" that enable consistent progress across multiple agent sessions and context windows.