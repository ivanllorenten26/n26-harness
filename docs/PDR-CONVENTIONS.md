# Convenciones para PDRs en el Ecosistema Harness

## Ubicaciones Estándar

### 1. **PDRs del Ecosistema** (Templates y ejemplos)
```
cylon26/
├── plugins/harness-pdr/
│   └── templates/
│       ├── example-web-app.md        # Ejemplo completo
│       ├── template-web-app.md       # Template para web apps
│       ├── template-api.md           # Template para APIs
│       ├── template-mobile.md        # Template para mobile
│       └── template-data.md          # Template para sistemas de datos
```

### 2. **PDRs de Proyectos Específicos**
```
mi-proyecto/
├── .claude/
│   ├── pdr.md                        # PDR original (copiado aquí por harness-init)
│   └── pdr-extensions/               # PDRs incrementales
│       ├── v2-auth-system.md         # Extensión: sistema de auth
│       ├── v3-admin-panel.md         # Extensión: panel admin
│       └── v4-analytics.md           # Extensión: analytics
```

### 3. **PDRs de Trabajo** (Antes de inicializar proyecto)
```
~/pdrs/                               # Tu directorio personal de PDRs
├── draft/                           # Borradores en desarrollo
│   ├── e-commerce-app.md
│   └── task-manager.md
├── ready/                           # Listos para harness-init
│   └── claude-clone-v1.md
└── archive/                         # PDRs de proyectos completados
    └── old-projects/
```

## Workflow Recomendado

### Paso 1: Creación de PDR
```bash
# En tu directorio de trabajo
"Crear PDR para una aplicación de e-commerce"
# → harness-pdr genera ~/pdrs/draft/e-commerce-app.md
```

### Paso 2: Inicialización de Proyecto
```bash
# Cuando el PDR esté listo
"Inicializar harness project desde ~/pdrs/ready/e-commerce-app.md"
# → harness-init copia PDR a nuevo-proyecto/.claude/pdr.md
# → harness-plan genera arquitectura completa
```

### Paso 3: Extensiones Futuras
```bash
# Para agregar nuevas funcionalidades
"Extender proyecto con ~/pdrs/extensions/admin-panel.md"
# → harness-extend integra nueva funcionalidad
# → Copia extension a .claude/pdr-extensions/
```

## Convenciones de Naming

### PDRs Principales
- `[project-name]-v[version].md` - ej: `claude-clone-v1.md`
- `[domain]-[app-type].md` - ej: `ecommerce-web-app.md`
- `[company]-[product].md` - ej: `n26-dashboard.md`

### PDRs de Extensión
- `[version]-[feature-area].md` - ej: `v2-auth-system.md`
- `extension-[feature].md` - ej: `extension-admin-panel.md`
- `[date]-[feature].md` - ej: `2024-01-analytics.md`

### Templates
- `template-[project-type].md` - ej: `template-web-app.md`
- `[industry]-template.md` - ej: `fintech-template.md`

## Gestión de Versiones

### PDR Principal
- **v1**: Funcionalidad core inicial
- **v2**: Primera extensión mayor
- **v3**: Segunda extensión mayor

### PDRs Incrementales
```
.claude/
├── pdr.md                    # PDR original v1
└── pdr-extensions/
    ├── v2-features.md        # Extensión v2
    ├── v3-features.md        # Extensión v3
    └── hotfix-security.md    # Hotfixes específicos
```

## Integration con Skills

### `/harness-pdr`
- Crea PDRs en `~/pdrs/draft/` por defecto
- Sugiere mover a `~/pdrs/ready/` cuando esté completo
- Puede usar templates existentes como base

### `/harness-init`
- Lee PDR desde cualquier ubicación
- Copia PDR a `.claude/pdr.md` del proyecto
- Preserva referencia al PDR original

### `/harness-extend`
- Acepta PDRs de extensión desde cualquier ubicación
- Copia a `.claude/pdr-extensions/[name].md`
- Integra con feature list existente

## Recomendación Final

**Usa este workflow:**

1. **PDRs de trabajo**: `~/pdrs/` (tu directorio personal)
2. **PDRs de proyecto**: `.claude/pdr.md` (copiado automáticamente)
3. **Templates**: `cylon26/plugins/harness-pdr/templates/` (este ecosistema)

Esto te permite:
- ✅ Gestionar PDRs independientemente de proyectos
- ✅ Versionado claro y extensiones organizadas
- ✅ Reutilización de templates y ejemplos
- ✅ Workflow limpio con los skills del harness