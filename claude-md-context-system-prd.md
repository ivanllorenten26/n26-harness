# PRD: Claude.md Project Context System
## Extensión del Harness System para Contexto de Proyecto

---

## 🎯 **Objetivo del Producto**

Extender el sistema harness actual con capacidades para generar, gestionar y utilizar archivos `claude.md` específicos por proyecto, proporcionando contexto de negocio y decisiones arquitectónicas únicas del proyecto mientras mantiene la separación con los patrones arquitectónicos reutilizables del sistema harness.

---

## 📋 **Resumen Ejecutivo**

### **Problema Actual**
- El sistema harness actual proporciona excelente contexto arquitectónico y de patrones, pero carece de contexto específico del proyecto
- Los agentes no tienen acceso a información crítica como reglas de negocio, decisiones arquitectónicas específicas, integraciones externas, y flujos de trabajo únicos del proyecto
- Falta un mecanismo estándar para documentar y acceder al contexto del proyecto de manera consistente

### **Solución Propuesta**
Implementar un sistema de archivos `claude.md` por proyecto que:
- Se genere automáticamente con templates inteligentes
- Se integre seamlessly con el sistema de context injection existente
- Proporcione contexto de negocio y proyecto específico a todos los agentes
- Mantenga separación clara entre contexto del sistema vs. contexto del proyecto

### **Beneficios Esperados**
- **Mejor comprensión del contexto**: Agentes entienden tanto patrones arquitectónicos como reglas de negocio específicas
- **Onboarding más rápido**: Nuevos desarrolladores comprenden el proyecto instantáneamente
- **Decisiones más informadas**: Implementaciones consideran restricciones y decisiones específicas del proyecto
- **Consistencia**: Estructura estándar para documentar proyectos

---

## 🚀 **Funcionalidades Requeridas**

### **F1: Generación Automática de claude.md**
#### **Descripción**
Al inicializar o detectar un proyecto, generar automáticamente un archivo `claude.md` con un template inteligente basado en la tecnología detectada.

#### **Criterios de Aceptación**
- [ ] Detectar si ya existe `claude.md` en el proyecto
- [ ] Generar template apropiado basado en tecnología detectada (TypeScript/Python/Kotlin)
- [ ] Incluir secciones relevantes según el tipo de proyecto (API, fullstack, etc.)
- [ ] Preservar `claude.md` existente y solo sugerir mejoras
- [ ] Template debe incluir todas las secciones identificadas en el análisis

#### **Casos de Uso**
```bash
# Caso 1: Proyecto nuevo sin claude.md
cd nuevo-proyecto/
/harness-init
# → Genera claude.md con template completo

# Caso 2: Proyecto existente sin claude.md
cd proyecto-existente/
/harness-context  # (funcionalidad propuesta: init)
# → Analiza proyecto y genera claude.md personalizado

# Caso 3: Proyecto con claude.md existente
cd proyecto-con-claude-md/
/harness-context  # (funcionalidad propuesta: update)
# → Sugiere mejoras al claude.md existente
```

### **F2: Context Injection Enhancement**
#### **Descripción**
Extender el sistema de context injection existente para combinar automáticamente el contexto del sistema harness con el contexto específico del proyecto desde `claude.md`.

#### **Criterios de Aceptación**
- [ ] Leer y parsear `claude.md` automáticamente
- [ ] Combinar contexto del sistema + contexto del proyecto
- [ ] Filtrar contexto relevante por tipo de agente
- [ ] Manejar gracefully proyectos sin `claude.md`
- [ ] Priorizar información del `claude.md` sobre defaults del sistema cuando hay conflicto

#### **Ejemplo de Integración**
```python
# En context-injector.py
def get_enhanced_context(self, agent_type: str) -> Dict[str, Any]:
    # Contexto base del sistema (arquitectura, patterns)
    system_context = self._get_clean_architecture_context(agent_type)

    # Contexto específico del proyecto
    project_context = self._load_claude_md_context()

    # Combinar inteligentemente
    return self._merge_contexts(system_context, project_context, agent_type)

def _load_claude_md_context(self) -> Dict[str, Any]:
    claude_md_path = Path(self.project_path) / "claude.md"
    if claude_md_path.exists():
        return self._parse_claude_md(claude_md_path)
    return {}
```

### **F3: Template System para claude.md**
#### **Descripción**
Sistema de templates inteligentes que genere `claude.md` personalizado basado en el proyecto detectado.

#### **Criterios de Aceptación**
- [ ] Templates específicos por tecnología (TypeScript, Python, Kotlin)
- [ ] Templates específicos por tipo de proyecto (API, fullstack, CLI, etc.)
- [ ] Secciones opcionales basadas en dependencias detectadas (Stripe, Auth0, etc.)
- [ ] Variables dinámicas reemplazadas automáticamente (nombre del proyecto, framework, etc.)
- [ ] Validación de template completeness

#### **Estructura de Templates**
```yaml
# .harness/templates/claude-md/
├── base-template.md              # Template base común
├── typescript-remix-template.md  # Específico para Remix
├── python-fastapi-template.md    # Específico para FastAPI
├── kotlin-spring-template.md     # Específico para Spring Boot
└── sections/                     # Secciones modulares
    ├── auth-section.md           # Para proyectos con auth
    ├── payments-section.md       # Para e-commerce
    ├── api-section.md            # Para APIs
    └── deployment-section.md     # Para todos los proyectos
```

### **F4: Claude.md Validation y Maintenance**
#### **Descripción**
Herramientas para validar, mantener y mejorar archivos `claude.md` existentes.

#### **Criterios de Aceptación**
- [ ] Validar estructura y completeness del `claude.md`
- [ ] Detectar secciones faltantes basadas en el proyecto actual
- [ ] Sugerir actualizaciones cuando cambia la tecnología del proyecto
- [ ] Linting para formato y consistencia
- [ ] Integración con git hooks para recordatorios de actualización

#### **Comandos Propuestos (Futuras funcionalidades)**
```bash
# Propuestas de sub-comandos para /harness-context
/harness-context-validate    # Valida claude.md actual
/harness-context-update      # Sugiere mejoras
/harness-context-lint        # Linting de formato
/harness-context-migrate     # Migra de versión antigua
```

### **F5: Integration con Skills Existentes**
#### **Descripción**
Todos los skills existentes deben poder acceder y utilizar el contexto del `claude.md`.

#### **Criterios de Aceptación**
- [ ] `/harness-init` genera `claude.md` automáticamente
- [ ] `/harness-implement` usa contexto del `claude.md`
- [ ] `/harness-plan` considera restricciones del `claude.md`
- [ ] `/harness-resume` incluye contexto del proyecto
- [ ] `/harness-extend` actualiza `claude.md` si es necesario

---

## 📊 **Especificaciones Técnicas**

### **Template Base para claude.md**
```markdown
# Claude Context - {{PROJECT_NAME}}

## 🎯 Contexto del Proyecto

### Dominio de Negocio
- **Qué hace**: [Descripción breve del producto/servicio]
- **Usuarios objetivo**: [Quiénes son los usuarios principales]
- **Valor único**: [Qué diferencia este proyecto]

### Reglas de Negocio Críticas
- [Regla específica importante 1]
- [Regla específica importante 2]
- [Restricciones o limitaciones del dominio]

## 🏗️ Arquitectura de ESTE Proyecto

### Stack Tecnológico Elegido
- **Lenguaje**: {{DETECTED_LANGUAGE}}
- **Framework**: {{DETECTED_FRAMEWORK}}
- **Base de datos**: [Especificar DB y por qué]
- **Deploy**: [Plataforma de deployment]

### Decisiones Arquitectónicas Específicas
- **Autenticación**: [Sistema elegido y justificación]
- **Estado/Cache**: [Solución elegida]
- **Storage**: [Para archivos/imágenes si aplica]
- **Comunicación externa**: [APIs, webhooks, etc.]

## 🔧 Configuración Específica

### Variables de Entorno Críticas
```bash
# Solo las más importantes para desarrollo
CRITICAL_API_KEY=xxx
WEBHOOK_SECRET=xxx
```

### Endpoints/Rutas Críticas
{{#if API_PROJECT}}
- `GET /api/health` - Health check
- `POST /api/{{MAIN_RESOURCE}}` - Crear recurso principal
- `GET /api/{{MAIN_RESOURCE}}/:id` - Obtener recurso
{{/if}}

{{#if FULLSTACK_PROJECT}}
### Rutas de Páginas Principales
- `/dashboard` - Panel principal
- `/{{MAIN_RESOURCE}}` - Gestión del recurso principal
- `/settings` - Configuración
{{/if}}

## 👥 Contexto del Equipo

### Responsabilidades
- **Lead**: [Nombre del tech lead]
- **Backend**: [Responsable de APIs/servicios]
- **Frontend**: [Responsable de UI/UX]
- **DevOps**: [Responsable de infrastructure]

### Flujo de Trabajo
1. [Paso 1 del workflow]
2. [Paso 2 del workflow]
3. [Paso 3 del workflow]

## 🚨 Consideraciones Especiales

### Performance Crítica
- [Endpoint o función crítica]: <Xms target
- [Recurso intensivo]: [Estrategia de optimización]

### Seguridad Específica
- [Consideración de seguridad 1]
- [Consideración de seguridad 2]
- [Compliance requirements si aplica]

### Monitoreo y Alertas
- [Métrica crítica 1]: [Umbral de alerta]
- [Métrica crítica 2]: [Umbral de alerta]

## 📚 Recursos del Proyecto

### Documentación Externa
- [Diseño/Mockups]: [URL]
- [API Documentation]: [URL]
- [Business Requirements]: [URL]

### Contactos Clave
- **Product Owner**: [Nombre] ([email])
- **Tech Lead**: [Nombre] ([email])
- **QA Lead**: [Nombre] ([email])

---

*Última actualización: {{CURRENT_DATE}}*
*Generado automáticamente por CYLON26 Harness System*
```

### **Modificaciones al Context Injector**
```python
# En .harness/utils/context-injector.py

def _load_claude_md_context(self) -> Dict[str, Any]:
    """Load project-specific context from claude.md"""
    claude_md_path = self.project_path / "claude.md"

    if not claude_md_path.exists():
        return {"project_context": None}

    try:
        content = claude_md_path.read_text()
        parsed = self._parse_claude_md_content(content)
        return {
            "project_context": {
                "business_domain": parsed.get("business_domain"),
                "business_rules": parsed.get("business_rules"),
                "tech_decisions": parsed.get("tech_decisions"),
                "critical_endpoints": parsed.get("endpoints"),
                "team_context": parsed.get("team"),
                "performance_targets": parsed.get("performance"),
                "security_requirements": parsed.get("security"),
                "monitoring_requirements": parsed.get("monitoring"),
                "external_integrations": parsed.get("integrations")
            }
        }
    except Exception as e:
        print(f"⚠️  Warning: Could not parse claude.md: {e}")
        return {"project_context": None}

def _parse_claude_md_content(self, content: str) -> Dict[str, Any]:
    """Parse claude.md markdown content and extract structured data"""
    # Implementar parser que extraiga información de las secciones
    # usando regex o markdown parser
    pass
```

### **Nuevo Skill: harness-context**
```markdown
# .claude/skills/harness-context/

## Funcionalidades
- `init` - Generar claude.md para proyecto actual
- `validate` - Validar claude.md existente
- `update` - Sugerir mejoras al claude.md
- `migrate` - Migrar claude.md de versión anterior
- `lint` - Verificar formato y completeness
```

---

## 🎯 **Criterios de Éxito**

### **Métricas de Éxito**
1. **Adopción**: 90% de proyectos nuevos generan `claude.md` automáticamente
2. **Completeness**: 80% de `claude.md` tienen al menos 7/10 secciones completas
3. **Utilización**: Todos los skills principales usan contexto de `claude.md`
4. **Satisfacción**: Feedback positivo en experiencia de desarrollo

### **Casos de Prueba Críticos**
1. **Proyecto TypeScript/Remix nuevo**: Debe generar template completo con secciones de fullstack
2. **API Python/FastAPI**: Debe generar template con secciones de API y performance
3. **Proyecto existente grande**: Debe analizar y sugerir contexto relevante sin sobrescribir
4. **Proyecto sin claude.md**: Todos los skills deben funcionar normalmente con defaults

---

## 🚧 **Plan de Implementación**

### **Fase 1: Foundation (1 semana)**
- [ ] Crear templates base para `claude.md`
- [ ] Implementar parser básico de markdown
- [ ] Extender context-injector con soporte para `claude.md`
- [ ] Testing básico del sistema

### **Fase 2: Skills Integration (1 semana)**
- [ ] Crear skill `harness-context` con comandos básicos
- [ ] Integrar generación automática en `/harness-init`
- [ ] Modificar `/harness-implement` para usar contexto del proyecto
- [ ] Testing de integración

### **Fase 3: Enhancement (1 semana)**
- [ ] Templates específicos por tecnología
- [ ] Validación y linting de `claude.md`
- [ ] Mejoras en el parser (extraer datos estructurados)
- [ ] Documentación completa

### **Fase 4: Polish (1 semana)**
- [ ] Manejo avanzado de errores
- [ ] Performance optimizations
- [ ] Testing exhaustivo
- [ ] Preparación para producción

---

## 📋 **Definición de "Terminado"**

### **Funcionalidad Core Completa**
- [ ] Sistema genera `claude.md` automáticamente en proyectos nuevos
- [ ] Context injection incluye información del `claude.md`
- [ ] Todos los skills principales funcionan con y sin `claude.md`
- [ ] Templates disponibles para las 3 tecnologías principales

### **Calidad Asegurada**
- [ ] Tests unitarios cubren >80% del código nuevo
- [ ] Tests de integración para todos los workflows principales
- [ ] Documentación técnica completa
- [ ] Performance no degrada más de 100ms en context injection

### **Experiencia de Usuario**
- [ ] Proceso de setup <30 segundos para proyecto nuevo
- [ ] Mensajes de error claros y actionables
- [ ] Fallbacks graceful cuando `claude.md` falta o está mal formado
- [ ] Integración transparente con workflow existente

---

## 🤔 **Decisiones Pendientes**

### **Técnicas**
1. **Parser Strategy**: ¿Usar regex, markdown parser library, o AI parsing?
2. **Template Engine**: ¿Handlebars, Jinja2, o string replacement simple?
3. **Validation**: ¿JSON Schema para estructura o reglas custom?

### **UX/Product**
1. **Auto-update**: ¿Cuándo debe el sistema sugerir actualizaciones al `claude.md`?
2. **Migration**: ¿Cómo manejar proyectos con documentación existente en otros formatos?
3. **Team Sharing**: ¿Integrar con git hooks para recordatorios de actualización?

---

## 🎉 **Entregables Finales**

1. **Código**
   - Skill `harness-context` completo
   - Context injector enhanced
   - Templates para todas las tecnologías

2. **Documentación**
   - Guía de usuario para `claude.md`
   - Documentación técnica para developers
   - Examples y best practices

3. **Testing**
   - Test suite completa
   - Integration tests con proyectos reales
   - Performance benchmarks

---

*Este PRD está listo para ser procesado por `/harness-manage` para implementar el sistema de contexto de proyecto con archivos `claude.md`.*