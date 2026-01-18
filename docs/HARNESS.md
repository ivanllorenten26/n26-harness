# Long-Running Agents Harness Ecosystem

A complete implementation of Anthropic's methodology for long-running agents using Claude Code, enabling autonomous development of any type of project using structured PDRs (Product Requirement Documents).

## Available Skills ✨

The following skills are automatically available in Claude Code and will activate based on your requests:

### 📝 `/harness-pdr`
**PDR Creation Assistant** - Helps create comprehensive Product Requirement Documents
- **Purpose**: Guide users through creating well-structured PDRs that lead to successful autonomous development
- **When it activates**: "Create a PDR for [project description]", "Help me write requirements", "Generate specifications"
- **What it does**:
  - Conducts an interactive interview to understand your project vision
  - Guides you through defining Core Features (CF-001, CF-002...), Secondary Features (SF-001...), and Technical Requirements
  - Generates structured acceptance criteria and quality requirements
  - Produces a complete PDR in the exact format needed by harness-init
  - Provides specialized templates for different project types (web apps, APIs, mobile, data systems)
- **Output**: Complete, structured PDR document ready for project initialization

### 🚀 `/harness-init`
**Project Initialization from PDR** - Sets up complete harness infrastructure
- **Purpose**: Initialize any project from a PDR with complete long-running agent infrastructure
- **When it activates**: "Initialize harness project from [PDR file]", "Set up project from requirements"
- **What it does**:
  - Parses the PDR and extracts all features, requirements, and specifications
  - Creates standard harness directory structure with tracking files
  - Generates comprehensive feature_list.json with unique IDs, priorities, and dependencies
  - Sets up git repository with proper .gitignore and initial commit
  - Creates progress tracking system (claude-progress.txt) for human-readable updates
  - Automatically triggers `/harness-plan` for architectural planning
- **Output**: Complete project structure ready for architectural planning

### 🏗️ `/harness-plan`
**Architectural Planning Engine** - The critical planning phase that prevents "one-shotting"
- **Purpose**: Generate comprehensive architectural plans and YAML configurations that enable parallel implementation
- **When it activates**: Automatically after harness-init, or "Plan the architecture", "Generate system design"
- **What it does**:
  - Analyzes the complete PDR to make informed architectural decisions
  - Generates comprehensive YAML architecture documents:
    - `global/stack-decisions.yaml` - Technology stack and architectural patterns
    - `global/coding-standards.yaml` - Development conventions and project structure
    - `global/api-contracts.yaml` - REST conventions, authentication, pagination
    - `global/database-schema.yaml` - Data modeling patterns and conventions
    - `cross-cutting/error-handling.yaml` - Global error management strategy
    - `cross-cutting/logging.yaml` - Structured logging approach
    - `cross-cutting/testing-strategy.yaml` - Testing pyramid and tools
  - Creates intelligent task breakdown with parallel execution groups
  - Updates feature list with architectural metadata and agent assignments
  - Generates project-specific init.sh script for development environment
- **Output**: Complete architectural blueprint enabling coordinated parallel development

### ⚡ `/harness-implement`
**Parallel Implementation Coordinator** - Orchestrates specialized subagents with context injection
- **Purpose**: Execute implementation tasks using specialized subagents while maintaining architectural consistency
- **When it activates**: "Implement the planned features", "Build the application", "Execute parallel development"
- **What it does**:
  - Loads complete architectural context from YAML files
  - Identifies tasks ready for parallel execution based on dependencies
  - Performs **context injection** - each subagent receives filtered, relevant architectural context:
    - Frontend subagent gets UI patterns, component standards, API consumption contracts
    - Backend subagent gets database schemas, API implementation contracts, business logic patterns
    - Data subagent gets database modeling standards, migration patterns, performance guidelines
    - DevOps subagent gets infrastructure patterns, deployment strategies, monitoring setup
  - Coordinates multiple specialized subagents working simultaneously on independent tasks
  - Ensures each implementation session completes discrete, testable features
  - Maintains clean state management with proper git commits and progress updates
- **Output**: Incrementally implemented features with maintained architectural consistency

### 🔄 `/harness-resume`
**Context Recovery and Continuation** - Seamlessly resumes interrupted work
- **Purpose**: Analyze current project state and continue from the last valid checkpoint
- **When it activates**: "Resume the harness project", "Continue where we left off", "Analyze current state"
- **What it does**:
  - Performs comprehensive state analysis reading all progress artifacts
  - Loads complete architectural context from YAML files
  - Runs validation tests to identify any broken or incomplete features
  - Detects half-implemented features that need completion or cleanup
  - Identifies the optimal next steps based on current progress and dependencies
  - Restores full context for seamless continuation as if never interrupted
  - Can handle various recovery scenarios: clean interruptions, mid-feature breaks, broken state, architectural drift
- **Output**: Restored project context ready for continued development

### 📈 `/harness-extend`
**Evolutionary Project Extension** - Seamlessly integrates new requirements
- **Purpose**: Add new features from incremental PDRs while maintaining existing progress and architectural consistency
- **When it activates**: "Extend the project with [new PDR]", "Add features from requirements"
- **What it does**:
  - Analyzes current project state and validates project health
  - Parses new/updated PDR files for additional requirements
  - Performs compatibility assessment between new and existing features
  - Updates architectural YAML files to accommodate new requirements
  - Merges new features into existing feature list with proper prioritization and dependencies
  - Maintains complete history of project evolution
  - Plans optimal implementation order for new features
  - Integrates new features into existing parallel execution groups
- **Output**: Extended project ready for continued development with new capabilities

## Anthropic's Methodology Implementation 🎯

This ecosystem directly implements the principles from Anthropic's "Effective harnesses for long-running agents" research:

### Phase 1: Initialization and Planning
```bash
# Claude automatically detects and uses appropriate skills
"Initialize harness project from my-app-pdr.md"
# → harness-init creates structure and extracts requirements
# → harness-plan generates complete architectural blueprint
```

**Key Innovation**: The critical **planning phase** prevents the "one-shotting" problem where agents try to build entire applications at once. Instead, we get comprehensive architectural planning upfront.

### Phase 2: Parallel Implementation
```bash
"Implement the planned features"
# → harness-implement coordinates real specialized subagents
# → Context injection with filtered architectural YAML per subagent
# → Incremental progress with automated testing
# → Explicit delegation: "Use harness-frontend-agent subagent to implement UI"
```

**Key Innovation**: **Context injection** ensures each subagent receives precisely the architectural context it needs, maintaining consistency without overwhelming any single agent with irrelevant information.

### Phase 3: Continuation and Evolution
```bash
"Continue where we left off"
# → harness-resume analyzes state and continues seamlessly

"Add these new features from updated-pdr.md"
# → harness-extend integrates without disrupting existing work
```

**Key Innovation**: **Context preservation** across multiple sessions through structured artifacts (YAML + JSON) enables true long-running development.

## Generated Project Structure 📁

```
project/
├── .claude/
│   ├── pdr.md                    # Original PDR
│   ├── feature_list.json         # Feature tracking with progress
│   ├── claude-progress.txt       # Human-readable progress log
│   ├── project_config.json       # Project configuration
│   ├── skills/                   # Harness skills (this ecosystem)
│   └── agents/                   # Specialized subagent definitions
├── .harness/arquitectura/                 # Architectural YAML documents
│   ├── global/
│   │   ├── stack-decisions.yaml  # Technology stack and patterns
│   │   ├── coding-standards.yaml # Development conventions
│   │   ├── api-contracts.yaml    # Global API standards
│   │   └── database-schema.yaml  # Data modeling standards
│   ├── features/
│   │   └── [feature-name]/       # Feature-specific architecture
│   │       ├── architecture.yaml # Feature architectural decisions
│   │       ├── api-spec.yaml     # Feature-specific APIs
│   │       └── components.yaml   # UI component contracts
│   └── cross-cutting/
│       ├── error-handling.yaml   # Global error strategy
│       ├── logging.yaml          # Logging patterns
│       └── testing-strategy.yaml # Testing approach
├── plugins/                               # Official Claude Code plugins
│   ├── harness-init/                  # Project initialization plugin
│   ├── harness-plan/                  # Architectural planning plugin
│   ├── harness-implement/             # Implementation coordination plugin
│   └── [other harness plugins...]
├── .harness/utils/                        # Python utilities for coordination
├── init.sh                      # Stack-specific development script
└── [project-specific structure according to architecture]
```

## Specialized Subagents 👥

The system coordinates real Claude Code subagents with injected architectural context:

### **harness-frontend-agent**
- **Specialization**: React, TypeScript, UI/UX, responsive design, accessibility
- **Context Injection**: Receives UI patterns, component standards, API consumption contracts, styling guidelines
- **Tools**: Browser automation (Puppeteer MCP), design systems, testing frameworks
- **Responsibilities**: Component implementation, user interactions, responsive design, client-side testing

### **harness-backend-agent**
- **Specialization**: Node.js, Express, APIs, business logic, database integration
- **Context Injection**: Receives database schemas, API implementation contracts, security patterns, performance guidelines
- **Tools**: API testing, database connections, validation frameworks
- **Responsibilities**: API endpoints, business logic, database queries, server-side validation

### **harness-data-agent**
- **Specialization**: Database design, data processing, migrations, analytics
- **Context Injection**: Receives data modeling standards, migration patterns, performance optimization guidelines
- **Tools**: Database tools, data validation, query optimization
- **Responsibilities**: Schema implementation, migrations, data integrity, performance tuning

### **harness-devops-agent**
- **Specialization**: Infrastructure, deployment, monitoring, CI/CD
- **Context Injection**: Receives infrastructure patterns, deployment strategies, monitoring configurations
- **Tools**: Docker, cloud providers, CI/CD systems, monitoring tools
- **Responsibilities**: Environment setup, deployment configuration, monitoring, scaling

**Each subagent is a real Claude Code instance with:**
- Its own conversation context and memory
- Specialized tools for its domain
- Filtered YAML context relevant only to its specialization
- Explicit delegation using Claude Code's native syntax

## Supported Project Types 🔧

### **Web Apps Full-Stack**
- **Stack**: React + TypeScript + Node.js + Express + PostgreSQL
- **Architecture**: Component-based frontend with layered backend
- **Features**: Authentication, responsive UI, real-time updates, database integration

### **APIs and Microservices**
- **Stack**: Express + TypeScript + PostgreSQL + Docker + Redis
- **Architecture**: RESTful APIs with repository pattern and caching
- **Features**: OpenAPI documentation, rate limiting, monitoring, scalability

### **Mobile Applications**
- **Stack**: React Native + TypeScript + Backend APIs
- **Architecture**: Cross-platform mobile with shared backend
- **Features**: Native components, offline capability, push notifications

### **Data Systems**
- **Stack**: Python + FastAPI + Data processing + ML frameworks
- **Architecture**: Data pipelines with analytics and machine learning
- **Features**: ETL processes, analytics dashboards, ML model deployment

## Core Principles 🎯

### 1. **Incremental Progress**
Each session completes discrete, testable features rather than attempting to build everything at once. This prevents the "one-shotting" problem identified by Anthropic.

### 2. **Clean State Management**
Always leaves the project in a deployable, continuable state. Every session ends with working code, proper commits, and updated documentation.

### 3. **Context Injection**
Architectural YAML documents maintain consistency between specialized subagents working in parallel, ensuring coherent implementation despite distributed work.

### 4. **Intelligent Parallelization**
Tasks execute in parallel while respecting dependencies, maximizing development velocity without breaking architectural integrity.

### 5. **Automated Testing Integration**
End-to-end validation is built into every feature implementation, ensuring quality and preventing regressions.

## Typical Usage Flow 🚀

### 1. **Requirements Definition**
```bash
"Create a PDR for an e-commerce platform with user authentication, product catalog, shopping cart, and payment processing"
# → harness-pdr conducts interactive interview
# → Generates comprehensive PDR with 50+ structured features
```

### 2. **Project Initialization and Planning**
```bash
"Initialize harness project from ecommerce-pdr.md"
# → harness-init creates complete project structure
# → harness-plan generates architectural blueprint with YAML configs
# → Ready for parallel implementation
```

### 3. **Parallel Implementation**
```bash
"Implement the planned features"
# → harness-implement coordinates 4 specialized subagents
# → Frontend-agent builds UI components
# → Backend-agent creates APIs and business logic
# → Data-agent implements database schemas
# → DevOps-agent sets up deployment and monitoring
```

### 4. **Continuation and Evolution**
```bash
"Continue implementation"
# → harness-resume analyzes current state and continues

"Add admin panel features from admin-pdr.md"
# → harness-extend integrates new functionality seamlessly
```

## PDR Templates and Examples 📝

### Available Templates
- `plugins/harness-pdr/templates/example-web-app.md` - Complete Claude.ai clone example
- `plugins/harness-pdr/templates/template-web-app.md` - Web application template
- `plugins/harness-pdr/templates/template-api.md` - API/microservice template
- `plugins/harness-pdr/templates/pdr-template.md` - Generic base template

### PDR Conventions
See `PDR-CONVENTIONS.md` for complete guidelines on:
- Where to store PDRs (personal vs project directories)
- Naming conventions for PDRs and extensions
- Version management and evolutionary development
- Integration with the harness workflow

## Testing the Ecosystem ✅

### Quick Test
```bash
# Use the included example PDR
"Initialize harness project from plugins/harness-pdr/templates/example-web-app.md"

# Claude will automatically:
# 1. Execute harness-init (structure + feature breakdown)
# 2. Follow with harness-plan (complete architectural planning)
# 3. Be ready for harness-implement (parallel development)
```

### Complete Workflow Test
```bash
# 1. Create custom requirements
"Create a PDR for a task management application with real-time collaboration"

# 2. Initialize and plan
"Initialize harness project from the generated PDR"

# 3. Implement features
"Implement the planned features"

# 4. Continue development
"Continue implementing remaining features"

# 5. Extend functionality
"Add mobile app support to the project"
```

## Architecture Innovation 🔬

This ecosystem implements several groundbreaking architectural innovations that solve the core challenges identified in Anthropic's research on long-running agents. Each innovation addresses specific limitations that prevent AI agents from effectively working on complex, multi-session projects.

### **Innovation 1: Structured Artifact System for Context Preservation**

**The Challenge**: Context window limitations mean agents lose all previous work context when starting new sessions. Traditional approaches fail because they rely on conversation memory, which is ephemeral and limited in scope.

**Our Solution - Multi-Layered Context Architecture**:

1. **YAML Architectural Layer**: Comprehensive architectural context preserved in structured documents
   ```yaml
   # Example: .harness/arquitectura/global/stack-decisions.yaml
   project_type: "web-fullstack"
   technology_stack:
     frontend:
       framework: "react"
       language: "typescript"
       state_management: "zustand"
     backend:
       framework: "express"
       database: "postgresql"
   architecture_patterns:
     frontend: "component-based"
     backend: "layered-architecture"
   ```

2. **JSON Progress Layer**: Machine-readable progress tracking with complete state
   ```json
   // Example: .claude/feature_list.json
   {
     "features": [
       {
         "id": "CF-001",
         "status": "completed",
         "implemented_at": "2024-01-15T10:00:00Z",
         "agent_assigned": "frontend",
         "dependencies_satisfied": true,
         "test_results": "passing"
       }
     ]
   }
   ```

3. **Human-Readable Layer**: Natural language progress logs for context recovery
   ```
   // Example: .claude/claude-progress.txt
   2024-01-15 10:00 - Frontend-agent completed user authentication UI
   - React login/register components implemented
   - Form validation with Zod schemas
   - Responsive design for mobile/desktop
   - Integration tests passing
   ```

**Technical Innovation**: This tri-layered approach ensures context preservation works at multiple levels - architectural (YAML), programmatic (JSON), and human-comprehensible (text), creating redundant context recovery mechanisms.

### **Innovation 2: Architectural Planning Phase to Prevent "One-Shotting"**

**The Challenge**: AI agents naturally try to implement entire applications in a single session, leading to incomplete implementations, context exhaustion, and inconsistent architecture.

**Our Solution - Mandatory Planning Phase with Decision Crystallization**:

The `/harness-plan` skill implements a sophisticated planning engine that:

1. **Comprehensive Requirement Analysis**:
   - Parses PDRs to extract every feature, requirement, and constraint
   - Categorizes features by complexity, priority, and interdependencies
   - Identifies architectural decision points that must be resolved upfront

2. **Technology Stack Decision Matrix**:
   ```yaml
   # Decision rationale captured for each choice
   technology_stack:
     frontend:
       framework: "react"
       rationale: "Component-based architecture matches PDR UI requirements"
       alternatives_considered: ["vue", "angular"]
       decision_factors: ["team expertise", "ecosystem maturity", "performance"]
   ```

3. **Dependency Graph Construction**:
   - Maps feature dependencies to create optimal implementation order
   - Identifies parallelizable work streams
   - Prevents circular dependencies and implementation deadlocks

4. **Contract Definition**:
   - API contracts specify exact interface requirements
   - Database schemas define data relationships upfront
   - Component contracts establish UI boundaries

**Technical Innovation**: By forcing architectural decisions before implementation, we prevent the "implementation drift" that occurs when agents make ad-hoc decisions during coding.

### **Innovation 3: Context Injection with Filtered Relevance**

**The Challenge**: Different specialized agents need different contextual information. Providing all context to all agents leads to cognitive overload and irrelevant information processing.

**Our Solution - Intelligent Context Filtering System**:

```python
# Pseudo-code for context injection mechanism
def inject_context_for_agent(agent_type: str, task_id: str):
    global_arch = load_yaml(".harness/arquitectura/global/")

    if agent_type == "frontend":
        return {
            "ui_patterns": global_arch["coding_standards"]["project_structure"]["frontend"],
            "api_contracts": global_arch["api_contracts"],  # For consumption
            "styling_guidelines": global_arch["design_system"],
            "testing_strategy": global_arch["testing"]["frontend_specific"]
        }
    elif agent_type == "backend":
        return {
            "api_implementation": global_arch["api_contracts"],  # For implementation
            "database_schema": global_arch["database_schema"],
            "business_logic_patterns": global_arch["architecture_patterns"]["backend"],
            "security_requirements": global_arch["security"]["backend_specific"]
        }
```

**Advanced Context Filtering**:
- **Role-Based Context**: Each subagent receives only contextually relevant information
- **Task-Specific Augmentation**: Additional context based on specific feature being implemented
- **Dependency Context**: Related feature contexts when implementing interdependent features
- **Anti-Pattern Prevention**: Explicit guidance on what NOT to do based on architectural decisions

### **Innovation 4: Intelligent State Recovery and Continuation**

**The Challenge**: When work is interrupted, agents struggle to understand what was completed, what was in progress, and what the optimal next step should be.

**Our Solution - Multi-Vector State Analysis**:

1. **Git History Analysis**:
   ```bash
   # Advanced git analysis for context recovery
   git log --oneline --graph --decorate -20  # Recent work patterns
   git diff HEAD~1..HEAD --stat               # Last changes scope
   git status --porcelain                     # Current working state
   ```

2. **Feature Completion Validation**:
   - Cross-references feature_list.json claims with actual implementation
   - Runs automated tests to verify claimed completions
   - Identifies features marked "complete" but actually broken

3. **Architectural Drift Detection**:
   ```python
   # Pseudo-code for drift detection
   def detect_architectural_drift():
       expected_structure = load_yaml(".harness/arquitectura/global/coding-standards.yaml")
       actual_structure = analyze_codebase_structure()

       deviations = compare_structures(expected_structure, actual_structure)
       return prioritize_corrections(deviations)
   ```

4. **Intelligent Next-Step Recommendation**:
   - Analyzes dependency graph to find unblocked tasks
   - Considers implementation complexity and agent availability
   - Prioritizes bug fixes over new features when issues are detected

### **Innovation 5: Parallel Execution Coordination with Dependency Management**

**The Challenge**: Multiple agents working simultaneously can create conflicts, duplicate work, or implement incompatible solutions.

**Our Solution - Dependency-Aware Parallel Coordination**:

1. **Task Dependency Graph**:
   ```json
   {
     "parallel_groups": [
       {
         "name": "foundation",
         "can_execute_parallel": true,
         "tasks": ["setup-database", "setup-auth", "setup-ui-base"],
         "coordination_contracts": {
           "shared_interfaces": ["User", "AuthContext"],
           "communication_protocols": ["REST API", "JWT tokens"]
         }
       }
     ]
   }
   ```

2. **Contract-Based Coordination**:
   - Shared interfaces defined in YAML prevent integration conflicts
   - API contracts ensure frontend/backend compatibility
   - Database schemas prevent data model conflicts

3. **Real-Time Conflict Detection**:
   - Git hooks detect when multiple agents modify related files
   - Automated testing runs continuously to catch integration issues
   - YAML validation ensures architectural compliance

4. **Dynamic Load Balancing**:
   - Monitors agent progress and reassigns tasks if needed
   - Identifies bottlenecks in dependency chains
   - Optimizes parallel execution based on actual completion rates

### **Innovation 6: Evolutionary Architecture with Version Management**

**The Challenge**: Projects need to evolve over time, but maintaining architectural consistency while adding new features is complex.

**Our Solution - Versioned Architectural Evolution**:

1. **Architectural Versioning**:
   ```yaml
   # .harness/arquitectura/global/stack-decisions.yaml
   version: "1.2"
   evolution_history:
     - version: "1.0"
       date: "2024-01-15"
       changes: ["Initial architecture"]
     - version: "1.1"
       date: "2024-01-20"
       changes: ["Added Redis caching layer"]
     - version: "1.2"
       date: "2024-01-25"
       changes: ["Introduced microservices for user management"]
   ```

2. **Backward Compatibility Management**:
   - Automatic detection of breaking changes
   - Migration strategy generation for architectural changes
   - Deprecation warnings for outdated patterns

3. **Extension Impact Analysis**:
   - Analyzes how new features affect existing architecture
   - Suggests architectural refactoring when needed
   - Maintains feature compatibility matrices

### **Innovation 7: Quality Assurance Through Architectural Compliance**

**The Challenge**: Ensuring code quality and architectural consistency across multiple agents and sessions.

**Our Solution - Continuous Architectural Validation**:

1. **Automated Compliance Checking**:
   ```python
   def validate_architectural_compliance():
       # Check naming conventions
       validate_naming_conventions(load_yaml("coding-standards.yaml"))

       # Validate API contract compliance
       validate_api_contracts(load_yaml("api-contracts.yaml"))

       # Check database schema compliance
       validate_database_schema(load_yaml("database-schema.yaml"))

       # Verify testing strategy adherence
       validate_testing_coverage(load_yaml("testing-strategy.yaml"))
   ```

2. **Pattern Enforcement**:
   - Linting rules generated from YAML architectural decisions
   - Automated code review based on coding standards
   - Integration test generation from API contracts

3. **Quality Metrics Tracking**:
   - Tracks architectural compliance over time
   - Measures agent adherence to established patterns
   - Provides feedback for architectural decision refinement

### **Innovation 8: Cross-Session Learning and Pattern Recognition**

**The Challenge**: Each session starts fresh without learning from previous implementation patterns or common issues.

**Our Solution - Pattern Database with Learning Integration**:

1. **Implementation Pattern Recognition**:
   - Tracks successful implementation patterns across sessions
   - Identifies common failure modes and their solutions
   - Builds a knowledge base of project-specific solutions

2. **Error Pattern Prevention**:
   - Records common mistakes and their architectural causes
   - Proactively warns about known problematic approaches
   - Suggests proven alternatives based on project history

3. **Optimization Recommendations**:
   - Identifies performance improvements that worked in similar contexts
   - Suggests architectural optimizations based on usage patterns
   - Recommends technology upgrades or pattern migrations

**Technical Achievement**: This ecosystem represents the first complete implementation of Anthropic's theoretical framework for long-running agents, providing a production-ready system that enables truly autonomous development across multiple sessions while maintaining architectural integrity and development velocity.

---

**🤖 Powered by Claude Code + Anthropic Long-Running Agents Methodology**

This ecosystem transforms Claude Code from making ad-hoc changes to systematic architectural development, enabling real autonomous development following proven software engineering best practices.

**Version**: v1.0 - Production Ready
**Based on**: "Effective harnesses for long-running agents" by Anthropic
**Implementation**: Complete autonomous development pipeline for Claude Code