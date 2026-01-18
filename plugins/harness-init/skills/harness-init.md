---
name: harness-init
description: Initialize a new project with the Anthropic long-running agents harness methodology. Use when starting a new project from a PDR file or setting up the harness framework for autonomous development.
allowed-tools: Read, Write, Bash, Glob, Grep, TodoWrite
context: fork
agent: general-purpose
---

# Harness Initialization

Initialize a project with the Anthropic long-running agents methodology from a Product Requirements Document (PDR). This skill sets up the complete infrastructure for autonomous long-running development following the methodology described in Anthropic's engineering blog.

## When to Use This Skill

I will automatically use this skill when you ask to:
- "Initialize a harness project from [PDR file]"
- "Set up long-running agents from PDR"
- "Create a new project with harness methodology"
- "Initialize project from requirements document"

## Process

### 1. PDR Analysis and Parsing
- Read and analyze the provided PDR file in Markdown format
- Extract key requirements, features, and technical specifications
- Identify project type (web app, API, mobile app, data system)
- Determine appropriate architecture patterns and technology stack

### 2. Project Structure Creation
- Create standard harness directory structure:
  ```
  ├── .claude/
  │   ├── pdr.md                    # Original PDR
  │   ├── feature_list.json         # Feature tracking
  │   ├── claude-progress.txt       # Human-readable progress log
  │   └── project_config.json       # Project configuration
  ├── .harness/arquitectura/                 # Architecture YAML (will be created by harness-plan)
  ├── init.sh                      # Development server script
  └── [project-specific structure]
  ```

### 3. Feature Breakdown and Tracking
- Parse PDR to extract all features (Core, Secondary, Technical)
- Create comprehensive `feature_list.json` with:
  - Unique feature IDs (CF-001, SF-001, etc.)
  - Priority levels and complexity estimates
  - Acceptance criteria for each feature
  - Agent assignments (frontend, backend, data, devops)
  - Dependency mapping for parallel execution

### 4. Harness Infrastructure Setup
- Initialize git repository with appropriate .gitignore
- Create progress tracking system (`claude-progress.txt`)
- Set up project configuration with methodology metadata
- Generate basic initialization script for development environment

### 5. Project Context Generation
- **Auto-detect project technology** using project detector
- **Generate claude.md** with project-specific context template
- **Populate project information** from PDR analysis and auto-detection
- **Create baseline documentation** for project-specific patterns and decisions

### 6. Integration with Planning Phase
- Automatically trigger `/harness-plan` skill after initialization
- Ensure seamless transition from setup to architectural planning
- Maintain context and state across skill transitions

## Key Principles from Anthropic Methodology

1. **Incremental Progress**: Each session must make measurable progress
2. **Clean State**: Always leave project in deployable/continuable state
3. **Structured Artifacts**: Use JSON and YAML for machine-readable state
4. **Context Preservation**: Maintain clear history for next sessions
5. **Testing Integration**: Build testing into every feature implementation

## Expected Outputs

After initialization:
- ✅ Project directory structure created
- ✅ Git repository initialized with initial commit
- ✅ PDR parsed and saved in `.claude/pdr.md`
- ✅ Comprehensive feature list generated in `feature_list.json`
- ✅ Progress tracking initialized in `claude-progress.txt`
- ✅ Project configuration created
- ✅ **claude.md generated** with project-specific context and business rules
- ✅ Basic `init.sh` development script created
- 🔄 **Automatically triggers `harness-plan` for architectural planning**

## Usage Examples

**Simple initialization:**
> "Initialize a harness project from my-app-requirements.md"

**With specific project type:**
> "Set up a web app harness from the PDR file app-spec.md"

**Resume from existing PDR:**
> "Create harness project structure from the requirements document"

## Next Steps After Initialization

The initialization automatically flows into the planning phase:
1. `harness-plan` will analyze the PDR in detail
2. Generate complete architectural YAML documents
3. Create task breakdown with parallel execution groups
4. Set up context injection system for agents
5. Ready for implementation with `harness-implement`

This creates a complete autonomous development pipeline following Anthropic's proven methodology for long-running agents.