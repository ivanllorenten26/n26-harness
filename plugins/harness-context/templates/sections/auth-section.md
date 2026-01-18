## 🔐 Autenticación y Autorización

### Sistema de Autenticación Elegido
- **Método**: [JWT/OAuth2/Session-based/API Keys]
- **Provider**: [Auth0/Clerk/Firebase Auth/Custom]
- **Justificación**: [Por qué se eligió esta solución vs alternativas]

### Flujo de Autenticación
1. **Login**: [Descripción del proceso de login]
2. **Token Management**: [Cómo se manejan los tokens/sessions]
3. **Refresh**: [Proceso de renovación de credenciales]
4. **Logout**: [Proceso de cierre de sesión]

### Configuración de Seguridad
```{{DETECTED_LANGUAGE}}
// Configuración específica de autenticación
{{#if AUTH_CONFIG}}
{{AUTH_CONFIG}}
{{else}}
// [Ejemplo de configuración de auth para este proyecto]
{{/if}}
```

### Roles y Permisos
- **{{ROLE_1}}**: [Descripción de permisos y accesos]
- **{{ROLE_2}}**: [Descripción de permisos y accesos]
- **{{ADMIN_ROLE}}**: [Permisos administrativos]

### Endpoints Protegidos
```
{{#each PROTECTED_ENDPOINTS}}
{{method}} {{path}} - Requiere: {{required_role}}
{{/each}}
```

### Variables de Entorno Auth
```bash
# Configuración de autenticación
AUTH_SECRET={{AUTH_SECRET_EXAMPLE}}
AUTH_PROVIDER_URL={{PROVIDER_URL_EXAMPLE}}
AUTH_CLIENT_ID={{CLIENT_ID_EXAMPLE}}
```