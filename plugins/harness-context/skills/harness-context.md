---
name: harness-context
description: Generate and manage claude.md files with project-specific context
allowed-tools: Read, Write, Glob, Grep, TodoWrite, Bash, Edit
context: fork
agent: general-purpose
---

# Harness Context - Gestión de claude.md

## Descripción

Este skill proporciona capacidades completas para generar, gestionar y utilizar archivos `claude.md` específicos por proyecto. Los archivos `claude.md` contienen contexto de negocio y decisiones arquitectónicas únicas del proyecto, complementando los patrones arquitectónicos reutilizables del sistema harness.

## Funcionalidades

### 1. Generación de claude.md
- **Auto-detección**: Genera templates basados en la tecnología detectada del proyecto
- **Templates inteligentes**: Adapta secciones según el tipo de proyecto (API, fullstack, CLI)
- **Preservación**: Mantiene archivos `claude.md` existentes y sugiere mejoras
- **Variables dinámicas**: Reemplaza automáticamente información del proyecto detectado

### 2. Validación y Mantenimiento
- **Validación de estructura**: Verifica completeness y formato del `claude.md`
- **Detección de gaps**: Identifica secciones faltantes basadas en el proyecto actual
- **Linting**: Verifica formato y consistencia
- **Sugerencias**: Propone actualizaciones cuando cambia la tecnología

### 3. Integración con Context Injection
- **Parsing automático**: Extrae información estructurada del `claude.md`
- **Filtrado por agente**: Contexto relevante según el tipo de agente
- **Fallback graceful**: Funciona sin problemas cuando `claude.md` no existe
- **Priorización**: Información del `claude.md` toma precedencia sobre defaults

## Comandos Disponibles

### `init` - Generar claude.md
Genera un archivo `claude.md` para el proyecto actual basado en auto-detección.

**Uso:**
```bash
/harness-context init
```

**Comportamiento:**
- Analiza el proyecto actual con el project detector
- Selecciona template apropiado (TypeScript/Remix, Python/FastAPI, Kotlin/Spring Boot)
- Genera `claude.md` con secciones relevantes al proyecto
- Preserva archivo existente si ya hay uno (sugiere actualización)

### `validate` - Validar claude.md
Valida la estructura y completeness del `claude.md` existente.

**Uso:**
```bash
/harness-context validate
```

**Comportamiento:**
- Verifica que existe `claude.md`
- Valida estructura de secciones principales
- Identifica campos vacíos o incompletos
- Proporciona score de completeness (0-100%)
- Sugiere secciones faltantes basadas en dependencias detectadas

### `update` - Sugerir mejoras
Analiza el proyecto actual y sugiere actualizaciones al `claude.md`.

**Uso:**
```bash
/harness-context update
```

**Comportamiento:**
- Compara `claude.md` actual con detección automática del proyecto
- Identifica inconsistencias (frameworks cambiados, nuevas dependencias)
- Sugiere nuevas secciones basadas en cambios detectados
- Propone actualización de información obsoleta

### `lint` - Verificar formato
Verifica formato y consistencia del `claude.md`.

**Uso:**
```bash
/harness-context lint
```

**Comportamiento:**
- Verifica formato markdown correcto
- Valida estructura de secciones (jerarquía H2/H3)
- Revisa consistencia en naming y formato
- Identifica enlaces rotos o formatos incorrectos

### `migrate` - Migrar versión antigua
Migra un `claude.md` de versión anterior al formato actual.

**Uso:**
```bash
/harness-context migrate
```

**Comportamiento:**
- Detecta versión del `claude.md` existente
- Aplica transformaciones necesarias al nuevo formato
- Preserva información existente
- Agrega nuevas secciones requeridas

## Herramientas Disponibles

- **Read**: Para leer el `claude.md` existente y archivos de configuración
- **Write**: Para generar nuevos archivos `claude.md`
- **Edit**: Para actualizar archivos `claude.md` existentes
- **Glob**: Para buscar archivos relacionados al proyecto
- **Grep**: Para analizar patrones en el código
- **Bash**: Para ejecutar project detector y otros utilitarios

## Templates por Tecnología

### TypeScript + Remix
- Secciones específicas de fullstack web
- Loaders/Actions de Remix
- Rutas y componentes UI
- Progressive enhancement patterns

### Python + FastAPI
- Secciones específicas de API backend
- Async/await patterns
- Pydantic models y validation
- Background tasks y webhooks

### Kotlin + Spring Boot
- Secciones específicas de servicios empresariales
- Spring annotations y dependency injection
- JPA y database patterns
- Enterprise security patterns

### Base Template
- Template genérico para cualquier tecnología
- Secciones core aplicables a todos los proyectos
- Estructura expandible según necesidades

## Integración con Skills Existentes

### harness-init
- Genera `claude.md` automáticamente durante inicialización
- Usa detección automática para seleccionar template apropiado
- Integra generación en el flujo de setup del proyecto

### harness-implement
- Lee contexto del `claude.md` para implementación
- Usa reglas de negocio y restricciones específicas del proyecto
- Aplica patrones y convenciones específicas documentadas

### harness-plan
- Considera restricciones y decisiones del `claude.md` durante planificación
- Adapta arquitectura propuesta al contexto específico del proyecto
- Valida compatibilidad con decisiones existentes

### harness-resume
- Incluye contexto del proyecto durante recuperación de estado
- Mantiene continuidad con decisiones y patrones específicos
- Preserva contexto de negocio durante interrupciones

## Arquitectura del Sistema

### Project Detection Integration
```
Project Files → Project Detector → Template Selection → claude.md Generation
                                 ↓
Context Injection ← Markdown Parser ← claude.md Content
```

### Context Flow
```
claude.md → Parser → Structured Data → Context Injector → Agent Context
                                     ↓
Template System ← Auto-Detection ← Project Analysis
```

### Template Engine
- Handlebars-style variable replacement
- Conditional sections basadas en detección automática
- Modular sections para diferentes tipos de integraciones
- Language-specific adaptations

## Casos de Uso Principales

### 1. Nuevo Proyecto
```bash
cd my-new-remix-app/
/harness-context init
# → Genera claude.md con template TypeScript/Remix
# → Incluye secciones específicas de fullstack
# → Variables reemplazadas automáticamente
```

### 2. Proyecto Existente sin claude.md
```bash
cd legacy-api/
/harness-context init
# → Analiza proyecto existente
# → Detecta FastAPI + PostgreSQL
# → Genera template Python/FastAPI personalizado
```

### 3. Mantenimiento de claude.md
```bash
cd my-project/
/harness-context validate
# → Score: 7/10 sections complete
# → Missing: Performance targets, Security requirements

/harness-context update
# → New dependency detected: Redis
# → Suggests: Add Redis caching section
```

### 4. Migración de Formato
```bash
cd old-project/
/harness-context migrate
# → Detected v1.0 format
# → Migrating to v2.0 format
# → Added: Clean Architecture patterns section
```

## Validaciones y Salvaguardas

### Validación de Templates
- Verificación de sintaxis de template
- Validación de variables requeridas
- Consistencia con detección automática

### Preservación de Datos
- Backup automático antes de modificaciones
- Preservación de contenido customizado por usuario
- Merge inteligente de actualizaciones

### Error Handling
- Fallback graceful cuando falta información
- Mensajes de error claros y actionables
- Recovery automático de estados inconsistentes

## Métricas de Éxito

### Adopción
- 90% de proyectos nuevos generan `claude.md` automáticamente
- 80% de proyectos existentes adoptan `claude.md` después de sugerencia

### Completeness
- 80% de `claude.md` tienen al menos 7/10 secciones completas
- 95% de información crítica del proyecto documentada

### Utilización
- 100% de skills principales utilizan contexto de `claude.md`
- Context injection incluye información del proyecto en 95% de casos

### Mantenimiento
- 90% de cambios en tecnología detectados y sugeridos
- <30 segundos para generar `claude.md` completo

---

## Ejemplos de Output

### Generación Exitosa
```
🔍 Analyzing current project...
   ✅ Detected: TypeScript + Remix + PostgreSQL
   📋 Selected template: typescript-remix-template.md
   🏗️  Generating claude.md with 9 sections...
   ✅ claude.md created successfully!

📋 Project context is now available for all harness agents
💡 Tip: Run /harness-context validate to check completeness
```

### Validación con Issues
```
📋 Validating claude.md structure...
   ✅ Business domain: Complete
   ✅ Tech decisions: Complete
   ⚠️  Performance targets: Missing
   ⚠️  Security requirements: Incomplete
   ✅ Team context: Complete

📊 Overall score: 7/10 sections (70% complete)
💡 Run /harness-context update to add missing sections
```

### Actualización Detectada
```
🔍 Comparing claude.md with current project...
   📦 New dependency detected: @auth0/nextjs-auth0
   🔧 Framework change detected: Remix → Next.js
   📝 3 sections need updating...

💡 Suggested updates:
   • Update framework from Remix to Next.js
   • Add Auth0 authentication section
   • Update routing patterns for Next.js

Run /harness-context update --apply to implement changes
```

---

**HARNESS-CONTEXT - Contexto Inteligente para Cada Proyecto**

*"Cada proyecto es único. El contexto debería reflejarlo."*

---

## Metadatos del Skill

- **Versión**: 1.0.0
- **Autor**: N26 Harness System
- **Dependencias**: project-detector.py, context-injector.py
- **Compatibilidad**: Todos los lenguajes soportados por el harness
- **Última actualización**: 2024-01-16