# Claude Context - {{PROJECT_NAME}}

## 🎯 Contexto del Proyecto

### Dominio de Negocio
- **Qué hace**: [Aplicación web fullstack - descripción del producto/servicio]
- **Usuarios objetivo**: [Usuarios web que necesitan [funcionalidad principal]]
- **Valor único**: [Qué diferencia esta aplicación web de alternativas]

### Reglas de Negocio Críticas
- [Regla específica importante 1]
- [Regla específica importante 2]
- [Restricciones del dominio web específicas]

## 🏗️ Arquitectura de ESTE Proyecto

### Stack Tecnológico Elegido
- **Lenguaje**: TypeScript {{TYPESCRIPT_VERSION}}
- **Framework**: Remix {{REMIX_VERSION}} (elegido por: SSR, progressive enhancement, web standards)
- **Base de datos**: [PostgreSQL/SQLite/etc.] (justificación)
- **Styling**: [Tailwind CSS/styled-components/CSS modules]
- **Deploy**: [Vercel/Netlify/Fly.io] para Remix app

### Decisiones Arquitectónicas Específicas
- **Autenticación**: [Remix Auth + OAuth/JWT/Sessions]
- **Estado**: [Remix built-in + React context para client state]
- **Storage**: [Cloudinary/AWS S3 para assets]
- **Database ORM**: [Prisma/Drizzle/raw SQL]

## 🔧 Configuración Específica de Remix

### Variables de Entorno Críticas
```bash
# Remix & deployment
SESSION_SECRET=your-session-secret-here
DATABASE_URL=postgresql://user:pass@localhost:5432/dbname

# External services
{{#each EXTERNAL_SERVICES}}
{{name}}_API_KEY={{example}}
{{/each}}
```

### Rutas de Remix Principales
#### **Pages (Rutas de UI)**
- `/` - Landing page con Remix meta + SEO
- `/dashboard` - Dashboard principal (requiere auth)
- `/{{MAIN_RESOURCE}}` - Lista de {{MAIN_RESOURCE}} (loader + componente)
- `/{{MAIN_RESOURCE}}/new` - Crear {{MAIN_RESOURCE}} (action + form)
- `/{{MAIN_RESOURCE}}/$id` - Ver/editar {{MAIN_RESOURCE}} (loader + action)
- `/login` - Autenticación (action para login)
- `/logout` - Logout (action)

#### **API Routes (Resource Routes)**
- `/api/health` - Health check
- `/api/{{MAIN_RESOURCE}}` - CRUD API endpoints
- `/webhooks/[service]` - Webhooks externos (action only)

### Loaders y Actions Críticos
```typescript
// Ejemplo de loader importante
export async function loader({ params, request }: LoaderFunctionArgs) {
  // Autenticación
  const user = await authenticator.isAuthenticated(request);

  // Lógica de negocio específica
  const data = await [función específica del dominio];

  return json({ data, user });
}

// Ejemplo de action importante
export async function action({ request }: ActionFunctionArgs) {
  const formData = await request.formData();

  // Validación específica del proyecto
  const validated = [validación específica];

  // Lógica de negocio
  await [operación específica del dominio];

  return redirect('/success-path');
}
```

## 👥 Contexto del Equipo

### Responsabilidades Remix-Specific
- **Fullstack Lead**: [Nombre] - Loaders, actions, arquitectura Remix
- **Frontend**: [Nombre] - Componentes, styling, UX
- **Backend/Data**: [Nombre] - Database, external APIs, business logic
- **DevOps**: [Nombre] - Deployment, performance, monitoring

### Flujo de Trabajo Remix
1. **Feature Planning**: Definir rutas, loaders, actions necesarios
2. **Development**:
   - Crear route modules con loader/action
   - Implementar componentes UI
   - Conectar con database/APIs
3. **Testing**: Unit tests para utilities, E2E para user flows
4. **Deploy**: Commit → Auto deploy a staging → Manual a prod

## 🚨 Consideraciones Especiales de Remix

### Performance Crítica
- **Initial Page Load**: Target <2s (Remix SSR + progressive enhancement)
- **Navigation**: <200ms con Remix prefetching
- **Form Submissions**: <500ms con optimistic UI
- **Image Loading**: Lazy loading + Cloudinary optimization

### Patrones de Remix Específicos
- **Error Boundaries**: En cada route level para manejo de errores
- **Meta Functions**: SEO optimizado por página
- **Progressive Enhancement**: Funciona sin JavaScript
- **Nested Routes**: Layout compartido para secciones similares

### Remix-Specific Security
- **CSRF Protection**: Remix built-in con session
- **Content Security Policy**: Headers apropiados
- **Input Validation**: En actions antes de DB operations
- **Authentication**: [Específica del proyecto - JWT/session]

### Monitoreo de Remix App
- **Core Web Vitals**: LCP, FID, CLS tracking
- **Route Performance**: Loader execution times
- **Error Tracking**: Boundary catches + external service
- **User Analytics**: [Específico del proyecto]

## 📚 Recursos Remix del Proyecto

### Remix-Specific Docs
- **Route Structure**: [Internal documentation de la app]
- **Shared Components**: [Component library o design system]
- **Database Schema**: [Prisma schema o database docs]
- **Deployment Guide**: [Remix deployment específico]

### Remix Development Setup
```bash
# Local development
npm run dev          # Remix dev server
npm run build        # Build for production
npm run typecheck    # TypeScript validation
npm run test         # Unit tests

# Database (si usa Prisma)
npx prisma migrate dev
npx prisma studio
```

### External Services Integration
{{#each EXTERNAL_APIS}}
- **{{name}}**: [Purpose] - [Integration pattern]
{{/each}}

---

## 🎯 **Información para Claude Code - Remix Patterns**

### Convenciones de Código Remix
```typescript
// Route module structure
export async function loader({ request, params }: LoaderFunctionArgs) {
  // 1. Authentication
  // 2. Data fetching
  // 3. Return json()
}

export async function action({ request }: ActionFunctionArgs) {
  // 1. Form data parsing
  // 2. Validation
  // 3. Business logic
  // 4. Redirect or return data
}

export default function RouteComponent() {
  const data = useLoaderData<typeof loader>();
  const actionData = useActionData<typeof action>();

  // Progressive enhancement patterns
  return (
    <Form method="post">
      {/* Remix Form for progressive enhancement */}
    </Form>
  );
}

export function ErrorBoundary() {
  const error = useRouteError();
  // Error handling específico de la ruta
}
```

### Estructura de Archivos Remix
```
app/
├── routes/                    # Remix file-based routing
│   ├── _index.tsx            # Home page (/)
│   ├── dashboard.tsx         # Dashboard route
│   ├── {{MAIN_RESOURCE}}/    # Resource routes
│   │   ├── _index.tsx        # List page
│   │   ├── new.tsx          # Create page
│   │   └── $id.tsx          # Detail page
│   └── api/                  # API resource routes
├── components/               # Shared components
├── utils/                    # Utilities & business logic
├── styles/                   # Styling (Tailwind, etc.)
└── root.tsx                 # App shell
```

### Remix + Clean Architecture Integration
- **Domain Layer**: `app/domain/` - Business entities y rules
- **Application Layer**: `app/utils/` - Use cases y application logic
- **Infrastructure**: `app/lib/` - Database, external APIs
- **Presentation**: `app/routes/` + `app/components/` - Remix UI layer

---

*📅 Última actualización: {{CURRENT_DATE}}*
*🤖 Generado automáticamente por N26 Harness System para Remix*
*✨ Customizar según las necesidades específicas de la aplicación Remix*