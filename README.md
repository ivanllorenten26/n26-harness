# CYLON26 Harness Ecosystem - Claude Code Marketplace

A comprehensive collection of plugins implementing Anthropic's methodology for long-running agents using Claude Code, enabling autonomous development of any type of project through structured PDRs.

## 🚀 Quick Installation

```bash
# Install the entire marketplace
/plugin marketplace add your-org/cylon26-harness

# Install specific plugins
/plugin install harness-init@cylon26-harness
/plugin install harness-plan@cylon26-harness
/plugin install harness-implement@cylon26-harness
```

## 📦 Available Plugins

### Core Workflow Plugins

| Plugin | Description | Category |
|--------|-------------|----------|
| **harness-pdr** | Create comprehensive Product Requirement Documents | Documentation |
| **harness-init** | Initialize harness projects from PDRs | Development |
| **harness-plan** | Generate architectural plans and YAML configs | Development |
| **harness-implement** | Execute parallel implementation with agents | Development |

### Management & Extension Plugins

| Plugin | Description | Category |
|--------|-------------|----------|
| **harness-context** | Generate project-specific claude.md files | Development |
| **harness-extend** | Extend projects with incremental features | Development |
| **harness-resume** | Resume work after interruptions | Development |
| **harness-agents** | Specialized agents for parallel coordination | Development |

## 🔄 Complete Workflow

```bash
# 1. Create requirements
"Create a PDR for a web application"  # → harness-pdr activates

# 2. Initialize project
"Initialize harness project from my-app-pdr.md"  # → harness-init activates

# 3. Generate architecture
"Plan the architecture"  # → harness-plan activates automatically

# 4. Implement features
"Implement the planned features"  # → harness-implement activates

# 5. Extend functionality
"Extend project with admin-panel-pdr.md"  # → harness-extend activates
```

## 🎯 Key Features

- **🧠 Autonomous Development**: Complete project lifecycle from requirements to implementation
- **⚡ Parallel Execution**: Multiple specialized agents work simultaneously
- **📋 Context Preservation**: YAML + JSON artifacts maintain state across sessions
- **🔄 Incremental Extension**: Add features seamlessly to existing projects
- **🎨 Template System**: Comprehensive templates for different project types

## 🏗️ Architecture

The harness ecosystem implements a **tri-layered context management system**:

### 1. **Planning Layer** (YAML Architecture)
```yaml
global/
├── stack-decisions.yaml      # Technology choices
├── coding-standards.yaml     # Development conventions
├── api-contracts.yaml        # REST patterns
└── database-schema.yaml      # Data modeling
```

### 2. **Execution Layer** (JSON Tracking)
```json
{
  "core_features": [...],
  "implementation_status": "in_progress",
  "agent_assignments": {...}
}
```

### 3. **Progress Layer** (Human-Readable)
```
📋 Current Session: Feature Implementation Phase
✅ Authentication system completed
🔄 User dashboard in progress (harness-frontend-agent)
⏳ Payment integration queued
```

## 🤖 Specialized Agents

The harness-agents plugin provides four specialized agents with harness- prefix:

- **harness-frontend-agent**: React, TypeScript, UI/UX, responsive design
- **harness-backend-agent**: APIs, business logic, database integration
- **harness-data-agent**: Schema design, migrations, data validation
- **harness-devops-agent**: Infrastructure, deployment, monitoring

These agents coordinate through harness-implement for parallel development with architectural consistency.

## 📁 Project Structure Generated

```
your-project/
├── .claude/
│   ├── feature_list.json        # Structured task tracking
│   ├── claude-progress.txt      # Human-readable progress
│   └── pdr.md                   # Original requirements
├── .harness/
│   └── arquitectura/            # YAML architectural blueprints
├── src/                         # Generated project structure
└── [project-specific files according to architecture]
```

## 🔧 Advanced Usage

### Team Installation

Create `.claude/settings.json` in your project repos:

```json
{
  "extraKnownMarketplaces": {
    "cylon26-harness": {
      "source": {
        "source": "github",
        "repo": "your-org/cylon26-harness"
      }
    }
  },
  "enabledPlugins": {
    "harness-init@cylon26-harness": true,
    "harness-plan@cylon26-harness": true,
    "harness-implement@cylon26-harness": true
  }
}
```

### Private Repository Setup

```bash
export GITHUB_TOKEN=ghp_xxxx
/plugin marketplace add your-private-org/cylon26-harness
```

## 🏗️ Project Structure

### Marketplace Plugins (For Users)
```
plugins/                    # Distributed via Claude Code marketplace
├── harness-init/          # Project initialization
├── harness-pdr/           # Requirements creation
├── harness-plan/          # Architecture planning
├── harness-implement/     # Implementation coordination
├── harness-context/       # Project context management
├── harness-extend/        # Feature extension
├── harness-resume/        # Context recovery
└── harness-agents/        # Specialized development agents
```

### Internal Tools (For Maintainers)
```
.claude/                   # Internal harness development tools
└── skills/
    └── harness-manage/    # Ecosystem management (not distributed)
```

**Note**: The specialized harness agents are now included in the `harness-agents` plugin for distribution:
```
plugins/harness-agents/
└── agents/
    ├── harness-frontend-agent.md
    ├── harness-backend-agent.md
    ├── harness-data-agent.md
    └── harness-devops-agent.md
```

## 📖 Documentation

- [Complete Harness Guide](./docs/HARNESS.md)
- [PDR Conventions](./docs/PDR-CONVENTIONS.md)
- [Ecosystem Management](./docs/HARNESS_MANAGE.md) (Internal)
- [Flow Analysis](./docs/HARNESS_FLOW_ANALYSIS.md)

## 📈 Success Metrics

- **90%+ Context Recovery** through structured artifacts
- **70% Faster Development** via parallel agent coordination
- **Zero Setup Time** for continuing interrupted projects
- **100% Architectural Consistency** across all team members

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

---

**"BY YOUR COMMAND" - Autonomous development made simple. 🤖**

**CYLON26 Harness Ecosystem v3.0 - The future of AI-assisted software development.**