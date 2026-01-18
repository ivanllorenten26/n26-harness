## 🔌 API Específica del Proyecto

### Arquitectura de API
- **Estilo**: [REST/GraphQL/tRPC/gRPC]
- **Versionado**: [v1, v2, etc. - estrategia de versionado]
- **Documentación**: [OpenAPI/Swagger/GraphQL Schema]

### Endpoints de Negocio Críticos
#### **{{MAIN_RESOURCE}} Management**
```
GET    /api/{{MAIN_RESOURCE}}           - Lista con filtros y paginación
POST   /api/{{MAIN_RESOURCE}}           - Crear nuevo {{MAIN_RESOURCE}}
GET    /api/{{MAIN_RESOURCE}}/{id}      - Obtener {{MAIN_RESOURCE}} específico
PUT    /api/{{MAIN_RESOURCE}}/{id}      - Actualizar {{MAIN_RESOURCE}} completo
PATCH  /api/{{MAIN_RESOURCE}}/{id}      - Actualización parcial
DELETE /api/{{MAIN_RESOURCE}}/{id}      - Eliminar {{MAIN_RESOURCE}}
```

#### **Endpoints de Utilidad**
```
GET    /api/health                      - Health check del API
GET    /api/version                     - Información de versión
POST   /api/{{MAIN_RESOURCE}}/search    - Búsqueda avanzada
GET    /api/{{MAIN_RESOURCE}}/stats     - Estadísticas y métricas
```

### Formatos de Request/Response
```json
// Ejemplo de request típico
{
  "{{MAIN_FIELD}}": "{{EXAMPLE_VALUE}}",
  "{{SECONDARY_FIELD}}": "{{SECONDARY_VALUE}}",
  "metadata": {
    "{{META_FIELD}}": "{{META_VALUE}}"
  }
}

// Ejemplo de response típico
{
  "data": {
    "id": "{{EXAMPLE_ID}}",
    "{{MAIN_FIELD}}": "{{EXAMPLE_VALUE}}",
    "createdAt": "2024-01-16T12:00:00Z",
    "updatedAt": "2024-01-16T12:00:00Z"
  },
  "meta": {
    "version": "1.0",
    "timestamp": "2024-01-16T12:00:00Z"
  }
}
```

### Paginación y Filtrado
- **Paginación**: [offset/cursor-based - parámetros específicos]
- **Filtros**: [Parámetros de query disponibles]
- **Ordenamiento**: [Campos por los que se puede ordenar]

### Rate Limiting
- **Límites**: [Requests per minute/hour por endpoint]
- **Headers**: [Rate limit headers devueltos]
- **Estrategia**: [Por IP/por usuario/por API key]

### Error Handling
```json
// Formato estándar de errores
{
  "error": {
    "code": "{{ERROR_CODE}}",
    "message": "{{ERROR_MESSAGE}}",
    "details": {
      "field": "{{FIELD_NAME}}",
      "reason": "{{VALIDATION_REASON}}"
    },
    "timestamp": "2024-01-16T12:00:00Z"
  }
}
```

### Webhooks (si aplica)
```
POST   /webhooks/{{SERVICE_NAME}}       - Webhook de {{SERVICE_NAME}}
POST   /webhooks/payments               - Webhook de pagos
POST   /webhooks/notifications          - Webhook de notificaciones
```