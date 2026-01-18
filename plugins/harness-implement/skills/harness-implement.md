---
name: harness-implement
description: Execute parallel implementation with architectural context injection for long-running agents. Coordinates multiple specialized agents to implement features while maintaining architectural consistency through YAML context injection.
allowed-tools: Read, Write, Bash, Glob, Grep, Task, TodoWrite
context: fork
agent: general-purpose
---

# Harness Implementation with Context Injection

Execute implementation tasks using the long-running agents harness methodology with proper architectural context injection and agent coordination. This is the core implementation phase that enables parallel development while maintaining consistency.

## When to Use This Skill

I will automatically use this skill when:
- You ask to "implement the planned features"
- "Execute parallel development"
- "Build the [feature/component]"
- "Start implementation phase"
- "Continue harness implementation"

Optionally specify agent preference:
- "Implement with frontend agent"
- "Use backend agent for this feature"
- "Execute with data agent"

## Core Methodology

This skill implements the **Implementation Phase** from Anthropic's methodology:

1. **Context Injection**: Load architectural YAML and inject relevant context to specialized agents
2. **Parallel Coordination**: Execute multiple agents simultaneously on independent tasks
3. **Incremental Progress**: Each session completes discrete, testable features
4. **Clean State Management**: Always leave project in working, deployable state

## Process

### 1. Architecture Context Loading
- Read all YAML files from `.harness/arquitectura/` directory
- Load current project state from `feature_list.json`
- Analyze available tasks and dependencies
- Determine optimal parallel execution strategy

### 2. Task Selection and Agent Assignment
- Identify tasks ready for execution (dependencies satisfied)
- Group tasks by agent type for parallel execution:
  - **Frontend Agent**: UI components, user interactions, styling
  - **Backend Agent**: APIs, business logic, data processing
  - **Data Agent**: Database schemas, migrations, data models
  - **DevOps Agent**: Infrastructure, deployment, monitoring

### 3. Context Injection Per Agent

Each agent receives filtered, relevant context:

**Frontend Agent Context**:
```yaml
global_architecture:
  stack_decisions:
    frontend: # React, TypeScript, styling frameworks
  coding_standards: # Component naming, file organization
  api_contracts: # How to consume backend APIs
cross_cutting_concerns:
  error_handling: # Frontend error boundaries
  logging: # Client-side logging patterns
feature_architecture:
  components: # Specific component contracts
  styling: # Design system guidelines
```

**Backend Agent Context**:
```yaml
global_architecture:
  stack_decisions:
    backend: # Node.js, Express, database choices
    infrastructure: # Deployment and scaling
  coding_standards: # API naming, service organization
  api_contracts: # REST conventions to implement
  database_schema: # Data modeling patterns
cross_cutting_concerns:
  error_handling: # Global error middleware
  logging: # Structured server logging
feature_architecture:
  api_spec: # Specific endpoints to implement
  business_logic: # Service layer patterns
```

**Data Agent Context**:
```yaml
global_architecture:
  database_schema: # Complete data modeling guide
  stack_decisions:
    backend: # Database technology and ORM
cross_cutting_concerns:
  data_validation: # Input validation patterns
feature_architecture:
  data_models: # Specific schemas to implement
  migrations: # Database change patterns
```

### 4. Parallel Subagent Execution
- Launch specialized subagents with injected context using Task tool
- Use explicit subagent delegation:
  - "Use the harness-frontend-agent subagent to implement UI components"
  - "Use the harness-backend-agent subagent to create API endpoints"
  - "Use the harness-data-agent subagent to implement database schemas"
  - "Use the harness-devops-agent subagent to configure deployment"
- Each subagent works on independent, parallelizable tasks
- Maintain coordination through shared architectural YAML contracts

### 5. Progress Tracking and Checkpointing
- Update `feature_list.json` as tasks complete
- Maintain `claude-progress.txt` with human-readable updates
- Create git commits for each completed feature
- Ensure clean state after each implementation session

### 6. Testing and Validation
- Execute automated tests after each feature implementation
- Run integration tests to validate agent coordination
- Use browser automation (Puppeteer MCP) for end-to-end testing
- Validate against acceptance criteria from original PDR

## Subagent Specializations

### Frontend Subagent (`harness-frontend-agent`)
**Specialized for**: React, TypeScript, UI/UX, responsive design
**Tools**: Browser automation (Puppeteer MCP), design systems
**Delegation syntax**: "Use the harness-frontend-agent subagent to [task]"
**Responsibilities**:
- Component implementation following design system
- User interaction flows and state management
- Responsive design and accessibility
- Client-side testing and validation

### Backend Subagent (`harness-backend-agent`)
**Specialized for**: Node.js, Express, APIs, business logic
**Tools**: API testing, database connections
**Delegation syntax**: "Use the harness-backend-agent subagent to [task]"
**Responsibilities**:
- API endpoint implementation
- Business logic and service layers
- Database integration and queries
- Server-side validation and security

### Data Subagent (`harness-data-agent`)
**Specialized for**: Database design, data processing, migrations
**Tools**: Database tools, data validation
**Delegation syntax**: "Use the harness-data-agent subagent to [task]"
**Responsibilities**:
- Database schema implementation
- Data migration scripts
- Data validation and integrity
- Performance optimization

### DevOps Subagent (`harness-devops-agent`)
**Specialized for**: Infrastructure, deployment, monitoring
**Tools**: Docker, cloud providers, CI/CD
**Delegation syntax**: "Use the harness-devops-agent subagent to [task]"
**Responsibilities**:
- Development environment setup
- Deployment configuration
- Monitoring and logging setup
- Performance and scalability

## Coordination Patterns

### Parallel Execution Groups
Tasks are organized in dependency-aware groups:

1. **Setup Phase** (parallel subagent execution):
   - Use harness-devops-agent subagent for project structure and dependencies
   - Use harness-data-agent subagent for database setup and initial migrations
   - Use harness-devops-agent subagent for development tooling configuration

2. **Foundation Phase** (parallel after setup):
   - Use harness-backend-agent subagent for authentication system
   - Use harness-frontend-agent subagent for base UI components and design system
   - Use harness-frontend-agent subagent for core routing and navigation

3. **Feature Phase** (massively parallel after foundation):
   - Individual features implemented by appropriate specialized subagents
   - Features can be built simultaneously if no dependencies exist

4. **Polish Phase** (parallel after features):
   - Use harness-devops-agent subagent for end-to-end testing
   - Use harness-frontend-agent and harness-backend-agent subagents for performance optimization
   - Use harness-devops-agent subagent for deployment preparation

### Inter-Agent Communication
- Shared architectural YAML provides contracts
- Feature boundaries prevent conflicts
- Git serves as coordination mechanism
- Testing validates integration points

## Session Management

### Starting a Session
1. Load current project state
2. Identify next available tasks
3. Determine optimal agent assignments
4. Inject appropriate context per agent
5. Execute parallel implementation

### During Implementation
- Monitor progress through git commits
- Update feature tracking in real-time
- Handle any integration issues
- Maintain architectural consistency

### Ending a Session
- Ensure all active tasks reach clean completion
- Update progress logs and feature tracking
- Create descriptive git commits
- Validate system still works end-to-end
- Leave clear state for next session

## Success Criteria

Each implementation session must:
- ✅ Complete at least one full feature
- ✅ Maintain working application state
- ✅ Pass all existing tests
- ✅ Follow architectural guidelines
- ✅ Update tracking and progress logs
- ✅ Create clean git history

## Integration with Other Skills

**From `harness-plan`**: Receives complete architecture and task breakdown
**To `harness-resume`**: Provides clean state for recovery if interrupted
**With `harness-extend`**: Can incorporate new features mid-development

This creates a seamless flow where planning enables implementation, and implementation maintains the structured approach needed for long-running autonomous development.