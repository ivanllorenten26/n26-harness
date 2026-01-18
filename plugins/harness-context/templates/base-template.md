# Claude Context - {{PROJECT_NAME}}

## 🎯 Contexto del Proyecto

### Dominio de Negocio
- **Qué hace**: [Descripción breve del producto/servicio que desarrolla este proyecto]
- **Usuarios objetivo**: [Quiénes son los usuarios principales y cómo interactúan con el sistema]
- **Valor único**: [Qué diferencia este proyecto de alternativas existentes]

### Reglas de Negocio Críticas
- [Regla específica importante 1 - ej: "Los usuarios solo pueden cancelar reservas hasta 24h antes"]
- [Regla específica importante 2 - ej: "Las comisiones se calculan sobre el precio final incluyendo impuestos"]
- [Restricciones o limitaciones del dominio - ej: "Solo operamos en horario 9-18h zona local"]

## 🏗️ Arquitectura de ESTE Proyecto

### Stack Tecnológico Elegido
- **Lenguaje**: {{DETECTED_LANGUAGE}} (versión: {{LANGUAGE_VERSION}})
- **Framework**: {{DETECTED_FRAMEWORK}} (¿por qué se eligió vs alternativas?)
- **Base de datos**: [Especificar DB principal y justificación - ej: "PostgreSQL por transacciones ACID"]
- **Deploy**: [Plataforma de deployment - ej: "Vercel para frontend, Railway para backend"]

### Decisiones Arquitectónicas Específicas
- **Autenticación**: [Sistema elegido y justificación - ej: "Clerk por simplicidad vs Auth0"]
- **Estado/Cache**: [Solución elegida - ej: "Redis para sesiones, React Query para client state"]
- **Storage**: [Para archivos/imágenes si aplica - ej: "Cloudinary para optimización automática"]
- **Comunicación externa**: [APIs, webhooks, etc. - ej: "REST APIs, webhooks de Stripe"]

## 🔧 Configuración Específica

### Variables de Entorno Críticas
```bash
# Solo las más importantes para desarrollo local
{{#each CRITICAL_ENV_VARS}}
{{name}}={{example_value}}
{{/each}}
```

### Endpoints/Rutas Críticas
{{#if IS_API_PROJECT}}
#### **API Endpoints Principales**
- `GET /api/health` - Health check del sistema
- `POST /api/{{MAIN_RESOURCE}}` - Crear {{MAIN_RESOURCE}} principal
- `GET /api/{{MAIN_RESOURCE}}/:id` - Obtener {{MAIN_RESOURCE}} específico
- `PUT /api/{{MAIN_RESOURCE}}/:id` - Actualizar {{MAIN_RESOURCE}}
- `DELETE /api/{{MAIN_RESOURCE}}/:id` - Eliminar {{MAIN_RESOURCE}}
{{/if}}

{{#if IS_FULLSTACK_PROJECT}}
#### **Rutas de Páginas Principales**
- `/` - Landing page / Home
- `/dashboard` - Panel principal de usuario
- `/{{MAIN_RESOURCE}}` - Gestión del recurso principal
- `/{{MAIN_RESOURCE}}/new` - Crear nuevo recurso
- `/{{MAIN_RESOURCE}}/:id` - Ver/editar recurso específico
- `/settings` - Configuración de usuario/sistema
{{/if}}

## 👥 Contexto del Equipo

### Responsabilidades
- **Tech Lead**: [Nombre del tech lead - decisiones arquitectónicas]
- **Backend**: [Responsable de APIs/servicios - lógica de negocio]
- **Frontend**: [Responsable de UI/UX - experiencia de usuario]
- **DevOps**: [Responsable de infrastructure - deployments y monitoreo]

### Flujo de Trabajo del Equipo
1. **Planning**: [Cómo se planifican las funcionalidades - ej: "Sprint planning bi-semanal"]
2. **Development**: [Proceso de desarrollo - ej: "Feature branches from main"]
3. **Review**: [Proceso de code review - ej: "2 approvals mínimo"]
4. **Testing**: [Estrategia de testing - ej: "Unit tests + E2E en staging"]
5. **Deploy**: [Proceso de deployment - ej: "Auto deploy a staging, manual a prod"]

## 🚨 Consideraciones Especiales

### Performance Crítica
- **[Endpoint/función crítica 1]**: Target <Xms - [estrategia para lograrlo]
- **[Recurso intensivo]**: [Estrategia de optimización - ej: "Paginación + lazy loading"]
- **[Operación costosa]**: [Caching strategy - ej: "Cache de 1h para consultas complejas"]

### Seguridad Específica
- **[Consideración de seguridad 1]**: [ej: "Rate limiting 100 req/min por IP"]
- **[Consideración de seguridad 2]**: [ej: "Sanitización estricta en user inputs"]
- **[Compliance requirements]**: [ej: "GDPR compliance para usuarios EU"]

### Monitoreo y Alertas
- **[Métrica crítica 1]**: [Umbral de alerta - ej: "Response time >500ms"]
- **[Métrica crítica 2]**: [Umbral de alerta - ej: "Error rate >1%"]
- **[Sistema de notificaciones]**: [ej: "Slack #alerts para errores críticos"]

## 📚 Recursos del Proyecto

### Documentación Externa
- **[Diseño/Mockups]**: [URL a Figma, Adobe XD, etc.]
- **[API Documentation]**: [URL a OpenAPI, Postman, etc.]
- **[Business Requirements]**: [URL a documento de requisitos]
- **[Database Schema]**: [URL a diagrama ER o documentación de schema]

### Contactos Clave
- **Product Owner**: [Nombre] ([email]) - Decisiones de producto
- **Tech Lead**: [Nombre] ([email]) - Decisiones técnicas
- **QA Lead**: [Nombre] ([email]) - Estrategia de testing
- **DevOps**: [Nombre] ([email]) - Infrastructure y deployment

### Enlaces Útiles
- **Repository**: [URL del repositorio principal]
- **Staging Environment**: [URL del ambiente de staging]
- **Production Environment**: [URL del ambiente de producción]
- **CI/CD Pipeline**: [URL del pipeline - GitHub Actions, etc.]

---

## 🎯 **Información para Claude Code**

### Patrones de Código Específicos del Proyecto
```{{DETECTED_LANGUAGE}}
// Ejemplo de patrón específico de este proyecto
{{#if CUSTOM_PATTERNS}}
{{CUSTOM_PATTERNS}}
{{/if}}
```

### Convenciones de Naming Específicas
- **Variables**: {{VARIABLE_CONVENTION}} (ej: camelCase, snake_case)
- **Funciones**: {{FUNCTION_CONVENTION}} (ej: camelCase, PascalCase)
- **Archivos**: {{FILE_CONVENTION}} (ej: kebab-case, PascalCase)
- **Base de datos**: {{DB_CONVENTION}} (ej: snake_case para tablas)

### Estructura de Archivos Importante
```
{{PROJECT_STRUCTURE}}
```

---

*📅 Última actualización: {{CURRENT_DATE}}*
*🤖 Generado automáticamente por CYLON26 Harness System*
*✨ Personalizar este archivo según las necesidades específicas del proyecto*