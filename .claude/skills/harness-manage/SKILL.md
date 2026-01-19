# HARNESS MANAGE - Gestión de Agentes y Skills del Sistema Harness

## Descripción

Este skill proporciona capacidades completas para modificar, crear y gestionar los agentes y skills del ecosistema N26 Harness. Antes de realizar cualquier modificación, analiza profundamente la estructura existente para garantizar compatibilidad y coherencia con la metodología de Anthropic Long-Running Agents.

## Funcionalidades Principales

### 1. Análisis del Sistema Actual
- **Mapeo completo** de la estructura de skills y agentes existente
- **Análisis de dependencias** entre componentes del sistema
- **Validación de coherencia** arquitectónica antes de modificaciones
- **Documentación automática** del estado actual del sistema

### 2. Gestión de Skills
- **Crear nuevos skills** siguiendo las convenciones del harness
- **Modificar skills existentes** manteniendo compatibilidad
- **Validar funcionalidad** de skills antes de implementación
- **Actualizar documentación** automáticamente

### 3. Gestión de Agentes
- **Crear nuevos agentes** especializados con contexto filtrado
- **Modificar agentes existentes** preservando especializaciones
- **Configurar herramientas** disponibles para cada agente
- **Gestionar contexto inyectado** por tipo de agente

### 4. Automodificación y Evolución
- **Autoactualización** cuando se detectan cambios en el sistema
- **Mejora continua** basada en patrones detectados
- **Documentación automática** de cambios realizados
- **Validación post-modificación** del sistema completo

## Estructura del Sistema Analizada

### Skills Existentes (6 total)
```
.claude/skills/
├── harness-pdr/         # Creación de Product Requirement Documents
├── harness-init/        # Inicialización de proyectos desde PDRs
├── harness-plan/        # Planificación arquitectónica con YAMLs
├── harness-implement/   # Implementación paralela coordinada
├── harness-resume/      # Recuperación de contexto después de interrupciones
├── harness-extend/      # Extensión de proyectos con PDRs incrementales
└── harness-manage/      # ESTE SKILL - Gestión del ecosistema
```

### Agentes Especializados (4 total)
```
plugins/harness-agents/agents/
├── harness-frontend-agent.md    # React, TypeScript, UI/UX
├── harness-backend-agent.md     # Node.js, APIs, databases
├── harness-data-agent.md        # Database design, data processing
└── harness-devops-agent.md      # Infrastructure, deployment, monitoring
```

### Infraestructura de Soporte
```
.harness/
├── templates/           # Plantillas arquitectónicas (YAML + PDR)
│   ├── architecture/    # web-fullstack.yaml, api-microservice.yaml
│   └── pdr/            # template-web-app.md, template-api.md
└── utils/              # Python utilities
    ├── context-injector.py    # Sistema de inyección de contexto
    └── task-coordinator.py    # Coordinación de tasks paralelos
```

## Uso del Skill

### Comandos Principales

#### 1. Análizar Sistema
```bash
/harness-manage analyze
```
Analiza completamente el estado actual del sistema y genera reporte detallado.

#### 2. Crear Nuevo Skill
```bash
/harness-manage create-skill [nombre] [descripción] [funcionalidades]
```
Crea un nuevo skill siguiendo las convenciones del harness.

#### 3. Modificar Skill Existente
```bash
/harness-manage modify-skill [nombre] [cambios-solicitados]
```
Modifica un skill existente manteniendo compatibilidad.

#### 4. Crear Nuevo Agente
```bash
/harness-manage create-agent [tipo] [especialización] [herramientas]
```
Crea un nuevo agente especializado con contexto filtrado.

#### 5. Modificar Agente Existente
```bash
/harness-manage modify-agent [tipo] [modificaciones]
```
Modifica un agente existente preservando especialización.

#### 6. Validar Sistema
```bash
/harness-manage validate
```
Valida la coherencia completa del sistema después de modificaciones.

#### 8. Validar Plugins
```bash
/harness-manage validate-plugins
```
Ejecuta validaciones específicas de plugins:
- YAML frontmatter en todos los skills
- Referencias correctas en plugin.json
- Directorios commands innecesarios
- Registro correcto de skills en Claude Code

#### 7. Generar Documentación
```bash
/harness-manage document
```
Actualiza toda la documentación del sistema automáticamente.

## Metodología de Trabajo

### 1. Análisis Previo (OBLIGATORIO)
Antes de cualquier modificación, el skill debe:
- Mapear estructura actual completa
- Identificar dependencias entre componentes
- Validar coherencia arquitectónica existente
- Documentar estado baseline

### 2. Planificación de Cambios
Para cada modificación:
- Evaluar impacto en otros componentes
- Determinar cambios necesarios en documentación
- Identificar tests de validación requeridos
- Planificar secuencia de implementación

### 3. Implementación Incremental
- Realizar cambios en orden de dependencias
- Validar cada paso antes del siguiente
- Mantener backup de versiones previas
- Documentar cambios en tiempo real

### 4. Validación Post-Implementación
Después de cada cambio:
- Ejecutar tests de funcionalidad
- Validar coherencia del sistema completo
- Verificar compatibilidad con metodología Anthropic
- Actualizar documentación si es necesario

### 5. Automodificación (Si Requerida)
Si los cambios afectan este skill:
- Analizar modificaciones necesarias al propio skill
- Implementar automodificaciones de forma segura
- Validar funcionalidad actualizada
- Documentar evolución del skill

## Convenciones y Estándares

### Para Skills
- **Archivo principal**: `SKILL.md` con estructura estándar
- **YAML Frontmatter**: OBLIGATORIO con formato exacto:
  ```yaml
  ---
  name: skill-name
  description: Clear description of functionality
  allowed-tools: Read, Write, Glob, Grep, TodoWrite, Bash, Edit
  context: fork
  agent: general-purpose
  ---
  ```
- **Documentación**: Descripción clara, uso, ejemplos
- **Integración**: Compatible con sistema de context injection
- **Herramientas**: Especificación clara de tools disponibles
- **Commands Directory**: ⚠️ NO usar `commands/` directories vacíos
- **Plugin.json**: NO referenciar `"commands": ["./commands/"]` si no hay archivos
- **Validación**: Tests de funcionalidad básica

### Para Agentes
- **Archivo principal**: `[tipo]-agent.md` con especialización clara
- **Herramientas**: Lista específica según especialización
- **Contexto**: Filtrado apropiado por tipo de agente
- **Especialización**: Foco claro en dominio específico
- **Coordinación**: Compatible con sistema de parallel execution

### Para Plugin.json (Claude Code Plugins)
- **Estructura mínima requerida**:
  ```json
  {
    "name": "plugin-name",
    "version": "3.0.0",
    "description": "Clear plugin description",
    "author": {
      "name": "Author Name",
      "email": "author@email.com"
    },
    "skills": ["./skills/plugin-name.md"]
  }
  ```
- **⚠️ NO incluir `"commands": ["./commands/"]` si directory está vacío**
- **✅ Usar `"agents": [...]` para plugins de agentes (ej: harness-agents)**
- **✅ Validar que todos los paths referenciados existen**
- **✅ Mantener naming consistente entre name y skill files**

### Para Documentación
- **Formato**: Markdown con estructura consistente
- **Actualización**: Automática cuando hay cambios
- **Ejemplos**: Casos de uso prácticos incluidos
- **Referencias**: Enlaces a documentación relacionada
- **Versionado**: Tracking de cambios y evolución

## Seguridad y Validación

### Validaciones Obligatorias de Plugins
- **YAML Frontmatter**: Todos los skills deben tener YAML frontmatter válido
- **Plugin.json Structure**: Validación de estructura y referencias correctas
- **Commands Directory**: Verificación de directorios vacíos y referencias innecesarias
- **Skills Registration**: Confirmación de que todos los skills se registran correctamente
- **Tools Configuration**: Verificación de herramientas disponibles por skill

### Validaciones Arquitectónicas Generales
- **Coherencia arquitectónica**: Mantenimiento de principios harness
- **Compatibilidad**: Con metodología Anthropic Long-Running Agents
- **Funcionalidad**: Tests básicos de operación
- **Documentación**: Actualización automática completa
- **Dependencias**: Verificación de integridad de enlaces

### Salvaguardas
- **Backup automático**: Antes de modificaciones importantes
- **Rollback**: Capacidad de revertir cambios problemáticos
- **Validación incremental**: Verificación paso a paso
- **Log de cambios**: Registro detallado de todas las modificaciones
- **Alertas**: Notificación de incompatibilidades detectadas

## Integración con Ecosistema

### Context Injection System
- **Filtrado inteligente**: Contexto apropiado por tipo de modificación
- **Preservación**: Mantenimiento de sistema de inyección existente
- **Extensión**: Capacidad de añadir nuevos tipos de contexto

### Task Coordination
- **Dependencias**: Manejo apropiado de orden de ejecución
- **Parallel Execution**: Compatibilidad con coordinación paralela
- **Status Tracking**: Integración con sistema de progreso

### Metodología Anthropic
- **Structured Artifacts**: Mantenimiento de system YAML/JSON
- **Planning Prevention**: Forzado de análisis previo
- **Context Preservation**: Conservación de continuidad
- **Incremental Progress**: Desarrollo paso a paso

## Checklist de Validación de Plugins

### ✅ Antes de Crear/Modificar Cualquier Plugin

**1. YAML Frontmatter (CRÍTICO)**
- [ ] Skill file tiene `---` al inicio y final
- [ ] Contiene `name:` (coincide con plugin name)
- [ ] Contiene `description:` (descripción clara)
- [ ] Contiene `allowed-tools:` (herramientas específicas)
- [ ] Contiene `context: fork`
- [ ] Contiene `agent: general-purpose`

**2. Plugin.json Structure**
- [ ] Archivo `.claude-plugin/plugin.json` existe
- [ ] Contiene campos obligatorios: name, version, description, author
- [ ] Path `skills: ["./skills/..."]` apunta a archivo existente
- [ ] ⚠️ NO contiene `"commands": ["./commands/"]` si directory vacío
- [ ] Naming consistente entre plugin name y skill file

**3. Directory Structure**
- [ ] Commands directory: eliminar si está vacío O no referenciar en plugin.json
- [ ] Skills directory: contiene skill files con YAML frontmatter
- [ ] Templates directory: templates específicos del plugin (opcional)
- [ ] Utils directory: utilidades Python (opcional)

**4. Post-Creation Testing**
- [ ] Plugin se registra correctamente en Claude Code
- [ ] Skill está disponible con `/plugin-name`
- [ ] No hay errores de "commands path not found"
- [ ] Herramientas permitidas funcionan correctamente

### 🔥 Errores Comunes a Evitar
- **Skills sin YAML frontmatter** → Claude Code no registra el skill
- **Commands directories vacíos referenciados** → Error "commands path not found"
- **Naming inconsistente** → Confusión en registro de skills
- **Paths inexistentes en plugin.json** → Errores de carga
- **Tools no permitidos** → Fallos de ejecución de skill

## Ejemplos de Uso

### Crear Skill de Testing
```bash
/harness-manage create-skill testing-harness "Automated testing for harness projects" "unit-testing integration-testing e2e-testing coverage-reporting"
```

### Modificar Frontend Agent
```bash
/harness-manage modify-agent frontend "Add support for Vue.js and Svelte frameworks alongside React"
```

### Análisis Completo
```bash
/harness-manage analyze
# Genera reporte completo del estado del sistema
```

### Validación Post-Cambios
```bash
/harness-manage validate
# Verifica coherencia después de modificaciones
```

## Auto-Evolución

Este skill está diseñado para evolucionar automáticamente:

1. **Detección de cambios**: Monitorea modificaciones en el sistema
2. **Análisis de impacto**: Evalúa si necesita automodificación
3. **Implementación segura**: Realiza cambios en sí mismo si es necesario
4. **Validación interna**: Verifica su propia funcionalidad post-cambio
5. **Documentación actualizada**: Mantiene su documentación al día

## Roadmap de Funcionalidades

### v1.0 (Actual)
- [x] Análisis completo del sistema existente
- [x] Creación y modificación básica de skills
- [x] Creación y modificación básica de agentes
- [x] Validación de coherencia arquitectónica
- [x] Documentación automática

### v1.1 (Próximo)
- [ ] Templates automáticos para nuevos skills/agentes
- [ ] Testing automático de modificaciones
- [ ] Metrics de performance de skills
- [ ] Rollback automático en caso de errores

### v1.2 (Futuro)
- [ ] IA assistant para sugerir mejoras
- [ ] Marketplace de skills/agentes comunitarios
- [ ] Versionado avanzado con branching
- [ ] Integration con CI/CD del harness

---

**HARNESS MANAGE - Evolución Inteligente del Ecosistema N26**

*"Un sistema que se conoce a sí mismo puede evolucionar hacia la perfección"*

---

## Metadatos del Skill

- **Versión**: 1.0.0
- **Autor**: N26 Harness Ecosystem
- **Compatibilidad**: Anthropic Long-Running Agents Methodology
- **Dependencias**: context-injector.py, task-coordinator.py
- **Última actualización**: 2024-01-16
- **Estado**: Activo y evolucionando
