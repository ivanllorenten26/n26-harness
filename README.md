# Ivan Llorente Claude Code plugins marketplace

A sophisticated implementation of Anthropic's methodology for long-running agents using Claude Code, transforming Claude from an ad-hoc coding assistant into a systematic autonomous development platform.

## Overview

The Harness is a **marketplace-ready distribution of 8 Claude Code plugins** that enable autonomous software development from requirements to deployment. It implements a three-layered context management system that maintains architectural consistency across complex, long-running development projects.

## Core Skills

Install and use these Claude Code skills with the `/` command:

- **`/harness-pdr`** - Create structured Product Requirement Documents
- **`/harness-init`** - Initialize projects from PDRs with infrastructure setup
- **`/harness-plan`** - Generate YAML architectural blueprints
- **`/harness-implement`** - Execute parallel development with specialized agents
- **`/harness-resume`** - Resume interrupted work with context recovery
- **`/harness-extend`** - Add incremental features to existing projects

## Key Features

### 🤖 **Autonomous Development Pipeline**

Complete workflow from requirements gathering to deployment with specialized AI agents

### 🏗️ **Three-layered Context Management**

- **Planning Layer**: YAML architectural blueprints
- **Execution Layer**: JSON progress tracking
- **Progress Layer**: Human-readable session updates

### ⚡ **Parallel Development Coordination**

Context-aware specialized agents work simultaneously on different aspects:

- Frontend (React, TypeScript, UI/UX)
- Backend (APIs, business logic, databases)
- Data (migrations, processing, analytics)
- DevOps (infrastructure, deployment, monitoring)

### 🎯 **Project Type Detection**

Automatic detection and template generation for:

- **TypeScript/Remix** - Full-stack web applications
- **Python/FastAPI** - High-performance APIs
- **Kotlin/Spring Boot** - Enterprise applications
- **Multi-language Polyglot** - Universal coordination

## Quick Start

1. **Install Claude Code plugins** from the marketplace
2. **Create requirements**: `/harness-pdr` - Interactive requirement gathering
3. **Initialize project**: `/harness-init` - Set up infrastructure and architecture
4. **Generate plan**: `/harness-plan` - Create YAML architectural blueprints
5. **Implement features**: `/harness-implement` - Parallel development execution

## Architecture

```
project/
├── .claude/
│   ├── feature_list.json        # Structured task tracking
│   ├── claude-progress.txt      # Human-readable progress
│   └── pdr.md                   # Original requirements
├── .harness/
│   └── arquitectura/            # YAML architectural blueprints
└── src/                         # Generated project structure
```

## Development Commands

```bash
# Run tests
python plugins/harness-context/tests/test_harness_context.py

# Test utilities
python plugins/harness-context/utils/claude_md_generator.py
python plugins/harness-plan/utils/project_detector.py
```

## Key Benefits

- **Cross-session Continuity** - Resume complex projects exactly where you left off
- **Architectural Consistency** - YAML blueprints prevent technical debt
- **Quality Assurance** - Integrated testing and compliance validation
- **Context Injection** - Agent-specific filtered context prevents pollution
- **Enterprise Ready** - Clean architecture patterns and professional workflows

## Documentation

- [`HARNESS.md`](docs/HARNESS.md) - Complete system documentation
- [`CLAUDE.md`](CLAUDE.md) - Claude Code integration guide
- [`PDR-CONVENTIONS.md`](docs/PDR-CONVENTIONS.md) - Requirements documentation standards

---

**Built for Claude Code** | **Following Anthropic's Long-running Agent Methodology** | **Marketplace Ready**
