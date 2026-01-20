# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a **Claude Code Plugin Marketplace** - a curated collection of specialized plugins that transform Claude Code into a systematic autonomous development platform. The repository implements a revolutionary concept: **Living Documentation** that serves as both context for AI-driven development and self-updating architectural blueprints.

### Core Concept: Living Documentation Loop

The harness creates a closed-loop system where:

1. **Documentation serves as AI context** - Structured YAML architectural blueprints and JSON progress tracking provide precise context to Claude agents during feature implementation
2. **AI updates the documentation** - As features are implemented, the harness tools automatically update the architectural documents, progress tracking, and context artifacts
3. **Documentation evolves with the codebase** - Each development iteration refines and expands the living documentation, creating an ever-improving knowledge base for future development cycles

This creates a self-reinforcing development ecosystem where the AI's context becomes more accurate and comprehensive with each feature implementation, enabling truly autonomous long-running development workflows.

### Plugin Marketplace Architecture

The repository distributes 8 specialized Claude Code plugins that work together to implement this living documentation system:

- **Requirements & Planning**: `harness-pdr`, `harness-plan` - Transform user needs into structured architectural blueprints
- **Implementation & Coordination**: `harness-implement`, `harness-agents` - Execute parallel development with context-aware agent coordination
- **Project Lifecycle**: `harness-init`, `harness-extend`, `harness-resume` - Manage project initialization, evolutionary growth, and seamless continuation
- **Context Management**: `harness-context` - Inject filtered architectural context to prevent context pollution during parallel development

Each plugin contains both the Claude Code skill definitions and specialized Python utilities that handle context injection, progress tracking, and documentation updates - closing the loop between AI context and living documentation.

## Development Commands

### Testing
```bash
# Run harness-context skill tests
python plugins/harness-context/tests/test_harness_context.py

# Run specific skill tests (from plugin directories)
cd plugins/harness-context && python tests/test_harness_context.py
```

### Plugin Development
```bash
# Test Claude.md generation system
python plugins/harness-context/utils/claude_md_generator.py

# Test project detection
python plugins/harness-plan/utils/project_detector.py

# Test context injection system
python plugins/harness-implement/utils/context_injector.py
```

### Skills Usage (Claude Code)
```bash
# Core workflow skills - available as native Claude Code skills
/harness-pdr      # Create structured Product Requirement Documents
/harness-init     # Initialize projects from PDRs with harness infrastructure
/harness-plan     # Generate architectural plans and YAML configurations
/harness-implement # Execute parallel implementation with specialized agents
/harness-resume   # Resume interrupted work with context recovery
/harness-extend   # Extend projects with incremental PDRs
```

### Git Operations
The codebase includes 146+ pre-approved bash commands in `.claude/settings.local.json` for autonomous development workflows including git operations, npm commands, AWS Bedrock operations, and specialized harness utilities.

## High-Level Architecture

This is the **N26 Harness Ecosystem** - a sophisticated implementation of Anthropic's methodology for long-running agents using Claude Code. It transforms Claude from an ad-hoc coding assistant into a systematic autonomous development platform.

### Core Architecture Pattern

**Three-layered Context Management System:**

1. **Planning Layer (YAML Architecture)**: Structured architectural blueprints stored in `.harness/arquitectura/` containing:
   - `global/stack-decisions.yaml` - Technology choices and patterns
   - `global/coding-standards.yaml` - Development conventions
   - `global/api-contracts.yaml` - REST patterns and authentication
   - `global/database-schema.yaml` - Data modeling conventions
   - `cross-cutting/` - Error handling, logging, testing strategies

2. **Execution Layer (JSON Tracking)**: Real-time progress management via:
   - `.claude/feature_list.json` - Structured task tracking with dependencies
   - Agent assignments and parallel execution coordination
   - Implementation status with unique feature IDs

3. **Progress Layer (Human-readable)**: Continuous progress updates in:
   - `.claude/claude-progress.txt` - Human-readable session progress
   - Git commit messages following structured methodology format

### Plugin-based Marketplace Architecture

The harness is distributed as **8 Claude Code marketplace plugins**:

- **Core Workflow Plugins**: `harness-pdr`, `harness-init`, `harness-plan`, `harness-implement`
- **Management Plugins**: `harness-context`, `harness-extend`, `harness-resume`, `harness-agents`

Each plugin contains:
- `SKILL.md` files with YAML frontmatter (Claude Code native format)
- Specialized Python utilities for project detection, context injection, coordination
- Template systems for project-specific configurations

### Context Injection Engine

**Agent-filtered context delivery system:**
- **Frontend agents** receive: UI patterns, component standards, API consumption contracts
- **Backend agents** receive: Database schemas, API implementation contracts, business logic patterns
- **Data agents** receive: Database modeling standards, migration patterns, performance guidelines
- **DevOps agents** receive: Infrastructure patterns, deployment strategies, monitoring setup

This prevents context pollution and enables true parallel development while maintaining architectural consistency.

### Specialized Agent Coordination

Four real Claude Code subagents with `.md` definitions:
- `plugins/harness-agents/agents/harness-frontend-agent.md` - React, TypeScript, UI/UX specialist
- `plugins/harness-agents/agents/harness-backend-agent.md` - APIs, business logic, database integration
- `plugins/harness-agents/agents/harness-data-agent.md` - Database design, migrations, data processing
- `plugins/harness-agents/agents/harness-devops-agent.md` - Infrastructure, deployment, monitoring

### Autonomous Development Pipeline

Complete workflow implementation:
1. **Requirements → PDR creation** (`harness-pdr`) - Interactive requirement gathering
2. **PDR → Project initialization** (`harness-init`) - Infrastructure setup and feature extraction
3. **Planning → Architecture generation** (`harness-plan`) - YAML blueprint creation
4. **Implementation → Parallel development** (`harness-implement`) - Context-aware agent coordination
5. **Extension → Evolutionary growth** (`harness-extend`) - Incremental feature addition
6. **Recovery → Seamless continuation** (`harness-resume`) - Context restoration after interruption

## Project Structure Generated by Harness

When initializing projects, the harness creates:

```
project/
├── .claude/
│   ├── feature_list.json        # Structured task tracking
│   ├── claude-progress.txt      # Human-readable progress
│   └── pdr.md                   # Original requirements
├── .harness/
│   └── arquitectura/            # YAML architectural blueprints
│       ├── global/              # Stack decisions, standards
│       └── cross-cutting/       # Error handling, logging, testing
├── src/                         # Generated project structure
└── [framework-specific files]   # Based on detected/planned architecture
```

## Key Architectural Innovations

### Multi-layered Context Preservation
- **YAML architectural blueprints** maintain design decisions across sessions
- **JSON progress tracking** enables exact continuation after interruption
- **Human-readable progress** provides transparency and debugging capability

### Dependency-aware Parallel Execution
- Intelligent task breakdown respecting feature dependencies
- Context injection prevents architectural drift during parallel development
- Clean state management ensures always-deployable project state

### Cross-session Learning and Pattern Recognition
- Project type detection with confidence scoring (TypeScript/Remix, Python/FastAPI, Kotlin/Spring)
- Template system with framework-specific architectural patterns
- Evolutionary extension capability without disrupting existing implementation

### Quality Assurance and Compliance
- Automated compliance scoring against established architectural patterns
- Feature-level testing integrated into implementation workflow
- Clean architecture enforcement with validation systems

## Supported Project Types

The harness includes comprehensive templates and detection for:

- **TypeScript/Remix**: Full-stack web applications with modern React patterns
- **Python/FastAPI**: High-performance APIs with async patterns and data processing
- **Kotlin/Spring Boot**: Enterprise applications with robust architectural patterns
- **Multi-language Polyglot**: Universal project detection with cross-technology coordination

## Context Injection Patterns

When working with harness-generated projects, Claude Code receives filtered architectural context:

- **Business Context**: From original PDR and project domain understanding
- **Technical Context**: From YAML architectural decisions and framework patterns
- **Implementation Context**: From current feature progress and dependency relationships
- **Quality Context**: From testing strategies and compliance requirements

This context injection system enables Claude to maintain architectural consistency while working on specific features, preventing the "context drift" problem common in long-running development sessions.

## Methodology Compliance

This implementation follows Anthropic's research on "Effective harnesses for long-running agents" including:

- **Structured Artifacts**: YAML + JSON for cross-session context preservation
- **Incremental Progress**: Complete features per session with clean state management
- **Parallel Execution**: Dependency-aware concurrent development coordination
- **Context Injection**: Agent-specific architectural context filtering
- **Quality Assurance**: Automated testing and compliance validation
- **Recovery Mechanisms**: Seamless continuation after interruption or failure

The harness transforms Claude Code from conversational assistance to systematic autonomous development, enabling true long-running agent capabilities for complex software projects.