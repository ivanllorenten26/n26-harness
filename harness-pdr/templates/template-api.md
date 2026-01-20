# [Nombre del API/Microservicio]

## Tipo de Proyecto
- [ ] Web App Full-Stack
- [x] API/Microservicio
- [ ] Mobile App
- [ ] Sistema de Datos

## Descripción General
[Descripción clara del propósito del API, qué servicios proporciona, quiénes son los consumidores (apps web, mobile, otros servicios), y cómo se integra en el ecosistema más amplio.]

## Características Funcionales

### Core Features
- **CF-001**: [Autenticación y autorización de usuarios/servicios]
- **CF-002**: [CRUD completo para [entidad principal]]
- **CF-003**: [Búsqueda y filtrado avanzado de datos]
- **CF-004**: [Validación completa de datos de entrada]
- **CF-005**: [Manejo robusto de errores y respuestas consistentes]
- **CF-006**: [Rate limiting y throttling por usuario/IP]
- **CF-007**: [Logging estructurado y monitoring de performance]

### Secondary Features
- **SF-001**: [Paginación cursor-based para grandes datasets]
- **SF-002**: [Versionado de API (v1, v2) con backward compatibility]
- **SF-003**: [Webhooks para notificar eventos a sistemas externos]
- **SF-004**: [Bulk operations para operaciones masivas]
- **SF-005**: [Caching inteligente con invalidación automática]
- **SF-006**: [Export de datos en múltiples formatos (JSON, CSV, XML)]

## Características Técnicas

### Arquitectura
- **Patrón**: Layered Architecture con Repository Pattern
- **Stack Tecnológico**: Node.js + Express + TypeScript + PostgreSQL + Redis
- **Base de Datos**: PostgreSQL con Prisma ORM

### APIs Externas
- **Autenticación**: [Auth0, Firebase Auth, o sistema interno]
- **Email/SMS**: [SendGrid, Twilio para notificaciones]
- **Storage**: [AWS S3, Cloudinary para archivos]
- **Cache**: [Redis para caching y sesiones]

### Requisitos No Funcionales
- **Performance**: Tiempo de respuesta < 200ms (P95), throughput 1000+ RPS
- **Seguridad**: HTTPS, rate limiting, input validation, SQL injection prevention
- **Escalabilidad**: Horizontal scaling, stateless design
- **Disponibilidad**: 99.9% uptime, graceful degradation
- **Compatibilidad**: REST API compliance, OpenAPI 3.0 documentation

## Criterios de Aceptación

### Criterios Principales
1. **API Completeness**: Todos los endpoints CF-001 a CF-007 implementados y documentados
2. **Documentation**: OpenAPI/Swagger specs completas y actualizadas
3. **Performance**: SLA de response time cumplido bajo carga
4. **Security**: Autenticación, autorización, y validación funcional
5. **Deploy**: API desplegada con monitoring y alerting activo

### Criterios Técnicos
1. **Código**: TypeScript estricto, arquitectura limpia, error handling centralizado
2. **Base de Datos**: Migraciones versionadas, indexes optimizados, queries eficientes
3. **Testing**: 90%+ coverage, unit + integration + contract tests
4. **API Design**: RESTful principles, consistent response formats, proper HTTP codes
5. **Observability**: Structured logging, metrics, distributed tracing

### Criterios de Calidad
1. **API Standards**: OpenAPI 3.0 spec, consistent naming, versioning strategy
2. **Error Handling**: RFC 7807 Problem Details, detailed error messages
3. **Performance**: Response time monitoring, database query optimization
4. **Security**: OWASP compliance, dependency vulnerability scanning

## Especificaciones de API

### Autenticación
```
- Método: JWT Bearer Token
- Header: Authorization: Bearer <token>
- Refresh: POST /auth/refresh
- Scopes: read:data, write:data, admin:all
```

### Formato de Respuesta Estándar
```json
{
  "data": <payload>,
  "meta": {
    "timestamp": "2024-01-01T00:00:00Z",
    "version": "1.0",
    "request_id": "uuid"
  },
  "pagination": {
    "cursor": "string",
    "has_more": boolean,
    "total_count": number
  }
}
```

### Formato de Error Estándar
```json
{
  "error": {
    "type": "VALIDATION_ERROR",
    "title": "Invalid input parameters",
    "detail": "The 'email' field must be a valid email address",
    "instance": "/api/v1/users",
    "invalid_params": [
      {
        "name": "email",
        "reason": "must be valid email format"
      }
    ]
  },
  "meta": {
    "timestamp": "2024-01-01T00:00:00Z",
    "request_id": "uuid"
  }
}
```

### Endpoints Principales
```
POST   /api/v1/auth/login
POST   /api/v1/auth/refresh
GET    /api/v1/[resource]
POST   /api/v1/[resource]
GET    /api/v1/[resource]/:id
PUT    /api/v1/[resource]/:id
DELETE /api/v1/[resource]/:id
```

## Notas Adicionales

### Stack Específico Recomendado
- **Runtime**: Node.js 18+ + Express + TypeScript
- **Database**: PostgreSQL + Prisma ORM
- **Validation**: Zod schemas
- **Documentation**: Swagger/OpenAPI + Redoc
- **Testing**: Jest + Supertest + MSW
- **Cache**: Redis
- **Deployment**: Docker + Railway/Render

### Consideraciones de Desarrollo
- Implementar versionado desde v1
- Rate limiting por endpoint específico
- Monitoring y alerting desde día 1
- Documentación auto-generada desde código

### Integraciones Futuras
- GraphQL layer opcional
- Streaming endpoints para real-time data
- SDK generation para múltiples lenguajes
- API Gateway integration