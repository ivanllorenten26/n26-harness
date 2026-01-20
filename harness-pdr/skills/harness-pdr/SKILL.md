---
name: harness-pdr
description: Help create comprehensive Product Requirement Documents (PDRs) in the correct format for the harness methodology. Use when you need to create or refine PDR specifications for new projects.
allowed-tools: Read, Write, Glob, Grep, TodoWrite
context: fork
agent: general-purpose
---

# PDR Creation Assistant

Help create comprehensive Product Requirement Documents (PDRs) in the structured Markdown format required by the harness methodology. This skill guides you through creating well-defined specifications that lead to successful autonomous development.

## When to Use This Skill

I will automatically use this skill when you ask to:
- "Create a PDR for [project description]"
- "Help me write a product requirements document"
- "Generate PDR specifications for my project"
- "Create requirements document for [app/system description]"
- "I need help structuring my project requirements"

## PDR Creation Process

### 1. Project Understanding
- Interview you about your project vision and goals
- Identify the type of application (web app, API, mobile, data system)
- Understand your target audience and use cases
- Clarify technical preferences and constraints

### 2. Structured Requirements Gathering
Guide you through defining:

**Core Features** (CF-001, CF-002, etc.):
- Essential functionality that defines the product
- Must-have features for MVP
- User-facing capabilities that deliver primary value

**Secondary Features** (SF-001, SF-002, etc.):
- Nice-to-have enhancements
- Advanced functionality for future iterations
- Features that improve user experience but aren't critical

**Technical Requirements** (TR-001, TR-002, etc.):
- Architecture preferences and patterns
- Technology stack preferences
- Performance, security, and scalability requirements
- Integration needs and external dependencies

### 3. Acceptance Criteria Definition
Help you define clear, measurable criteria:
- **Functional criteria**: What the system must do
- **Technical criteria**: How it should be built
- **Quality criteria**: Standards it must meet
- **Business criteria**: Success metrics and goals

### 4. PDR Generation
Create a complete, structured PDR document with:
- Proper project type selection
- Detailed feature breakdown with IDs
- Technical specifications and architecture preferences
- Clear acceptance criteria
- Non-functional requirements (performance, security, etc.)

## PDR Template Structure

The skill will generate a PDR following this proven structure:

```markdown
# [Project Name]

## Tipo de Proyecto
- [ ] Web App Full-Stack
- [ ] API/Microservicio
- [ ] Mobile App
- [ ] Sistema de Datos

## Descripción General
[Clear project description and purpose]

## Características Funcionales

### Core Features
- **CF-001**: [Essential feature description]
- **CF-002**: [Essential feature description]
...

### Secondary Features
- **SF-001**: [Enhancement feature description]
- **SF-002**: [Enhancement feature description]
...

## Características Técnicas

### Arquitectura
- **Patrón**: [Architectural pattern preference]
- **Stack Tecnológico**: [Technology preferences]
- **Base de Datos**: [Database requirements]

### Requisitos No Funcionales
- **Performance**: [Performance requirements]
- **Seguridad**: [Security requirements]
- **Escalabilidad**: [Scalability requirements]

## Criterios de Aceptación
[Specific, measurable success criteria]
```

## Guided Interview Process

I'll ask targeted questions to help you define:

### Project Basics
- What problem does this solve?
- Who are the primary users?
- What's the core value proposition?
- What type of application is this?

### Feature Prioritization
- What must users be able to do? (Core features)
- What would be nice to have? (Secondary features)
- What are the technical constraints? (Technical requirements)

### Quality Requirements
- How many users should it support?
- What are the performance expectations?
- Are there security or compliance requirements?
- How should it be deployed and maintained?

### Success Criteria
- How will you know the project is successful?
- What are the key metrics or outcomes?
- What constitutes a "complete" implementation?

## Output Quality

The generated PDR will be:
- ✅ **Well-structured** with proper feature IDs and categorization
- ✅ **Comprehensive** covering functional, technical, and quality requirements
- ✅ **Actionable** with clear, implementable feature descriptions
- ✅ **Measurable** with specific acceptance criteria
- ✅ **Harness-ready** formatted for seamless use with harness-init

## Integration with Harness Workflow

After PDR creation:
1. **Save as .md file** in your project directory
2. **Ready for harness-init** - Use immediately with the harness system
3. **Evolutionary updates** - Can be extended later with harness-extend
4. **Template reuse** - Generated PDR becomes template for similar projects

## PDR Best Practices

I'll ensure your PDR follows these principles:
- **Specific features** - Clear, implementable requirements
- **Proper categorization** - Core vs. secondary vs. technical
- **Realistic scope** - Achievable within reasonable timeframes
- **Clear acceptance criteria** - Measurable success conditions
- **Architecture alignment** - Technology choices that support requirements
- **Extensibility** - Structure that allows future growth

## Example Use Cases

**Web Application PDR**:
- E-commerce platform, social network, dashboard, SaaS application

**API/Microservice PDR**:
- REST API, GraphQL service, data processing service, integration layer

**Mobile Application PDR**:
- iOS/Android app, React Native app, cross-platform solution

**Data System PDR**:
- Analytics platform, ETL pipeline, machine learning system, data warehouse

This skill transforms vague project ideas into precise, implementable specifications that enable successful autonomous development with the harness methodology.