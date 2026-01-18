# Claude Context - {{PROJECT_NAME}}

## 🎯 Contexto del Proyecto

### Dominio de Negocio
- **Qué hace**: [API backend que proporciona [servicio específico]]
- **Usuarios objetivo**: [Frontend clients, mobile apps, otros servicios]
- **Valor único**: [Qué diferencia esta API de alternativas]

### Reglas de Negocio Críticas
- [Regla específica importante 1]
- [Regla específica importante 2]
- [Restricciones del dominio API específicas]

## 🏗️ Arquitectura de ESTE Proyecto

### Stack Tecnológico Elegido
- **Lenguaje**: Python {{PYTHON_VERSION}}
- **Framework**: FastAPI {{FASTAPI_VERSION}} (elegido por: async, auto docs, type hints)
- **Base de datos**: [PostgreSQL/MongoDB/etc.] (justificación)
- **ORM**: [SQLAlchemy/Tortoise/Beanie]
- **Deploy**: [Docker + AWS/GCP/Heroku]

### Decisiones Arquitectónicas Específicas
- **Autenticación**: [JWT/OAuth2/API Keys] con FastAPI security
- **Database**: [SQLAlchemy async + PostgreSQL/etc.]
- **Cache**: [Redis para sessions/caching]
- **Background Tasks**: [Celery/FastAPI BackgroundTasks]
- **Validation**: Pydantic models para request/response

## 🔧 Configuración Específica de FastAPI

### Variables de Entorno Críticas
```bash
# FastAPI & database
DATABASE_URL=postgresql+asyncpg://user:pass@localhost:5432/dbname
REDIS_URL=redis://localhost:6379/0

# Security
JWT_SECRET_KEY=your-jwt-secret-here
JWT_ALGORITHM=HS256

# External services
{{#each EXTERNAL_SERVICES}}
{{name}}_API_KEY={{example}}
{{/each}}
```

### API Endpoints Principales
#### **Core Business Endpoints**
- `GET /` - API info y health check
- `GET /docs` - OpenAPI documentation (auto-generated)
- `POST /auth/login` - Autenticación JWT
- `GET /{{MAIN_RESOURCE}}/` - Lista {{MAIN_RESOURCE}} con paginación
- `POST /{{MAIN_RESOURCE}}/` - Crear nuevo {{MAIN_RESOURCE}}
- `GET /{{MAIN_RESOURCE}}/{id}` - Obtener {{MAIN_RESOURCE}} específico
- `PUT /{{MAIN_RESOURCE}}/{id}` - Actualizar {{MAIN_RESOURCE}}
- `DELETE /{{MAIN_RESOURCE}}/{id}` - Eliminar {{MAIN_RESOURCE}}

#### **Utility Endpoints**
- `GET /health` - Health check detallado
- `POST /webhooks/{service}` - Webhooks de servicios externos
- `GET /metrics` - Métricas de performance (si aplica)

### Modelos Pydantic Críticos
```python
# Schemas principales del dominio
class {{MainResource}}Base(BaseModel):
    # Campos base compartidos
    name: str
    description: Optional[str] = None

class {{MainResource}}Create({{MainResource}}Base):
    # Campos específicos para creación
    pass

class {{MainResource}}Response({{MainResource}}Base):
    # Campos de respuesta con metadata
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True  # Para SQLAlchemy integration
```

## 👥 Contexto del Equipo

### Responsabilidades FastAPI-Specific
- **Backend Lead**: [Nombre] - API design, async patterns, performance
- **Database**: [Nombre] - SQLAlchemy, migrations, queries optimization
- **DevOps**: [Nombre] - Docker, async deployment, monitoring
- **Frontend Integration**: [Nombre] - API contracts, documentation

### Flujo de Trabajo FastAPI
1. **API Design**: OpenAPI spec first, Pydantic schemas
2. **Development**:
   - Implementar endpoints con async/await
   - Crear Pydantic models para validation
   - Database operations con SQLAlchemy async
3. **Testing**: pytest-asyncio para async tests
4. **Deploy**: Docker build → Container registry → Deploy

## 🚨 Consideraciones Especiales de FastAPI

### Performance Crítica Async
- **Database Queries**: Target <100ms con async SQLAlchemy
- **API Response Time**: <200ms para endpoints GET
- **Concurrent Requests**: Optimizado para async handling
- **Background Tasks**: Para operaciones no-críticas

### Async Patterns Específicos
```python
# Async database operations
async def get_user(db: AsyncSession, user_id: UUID) -> User:
    result = await db.execute(select(User).where(User.id == user_id))
    return result.scalar_one_or_none()

# Dependency injection
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session

# Background tasks
@app.post("/send-email/")
async def send_email(background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email_task, email)
    return {"message": "Email sent in background"}
```

### FastAPI Security Patterns
- **JWT Authentication**: FastAPI OAuth2PasswordBearer
- **Rate Limiting**: slowapi para rate limiting
- **CORS**: FastAPI CORS middleware
- **Input Validation**: Pydantic automatic validation
- **SQL Injection**: SQLAlchemy ORM protection

### Monitoreo FastAPI Específico
- **Response Times**: Por endpoint con middleware
- **Error Tracking**: Exception handlers con logging
- **Database Performance**: SQLAlchemy query analysis
- **Memory Usage**: Async operations monitoring

## 📚 Recursos FastAPI del Proyecto

### FastAPI-Specific Docs
- **API Documentation**: `/docs` (auto-generated Swagger)
- **Database Schema**: [SQLAlchemy models documentation]
- **Async Patterns**: [Project-specific async practices]
- **Deployment Guide**: [Docker + async deployment]

### Development Setup
```bash
# Local development
pip install -r requirements.txt
uvicorn main:app --reload          # Development server
pytest                            # Run tests
alembic upgrade head              # Database migrations
python -m pytest --cov           # Coverage report

# Docker
docker build -t {{PROJECT_NAME}} .
docker run -p 8000:8000 {{PROJECT_NAME}}
```

### External Services Integration
{{#each EXTERNAL_APIS}}
- **{{name}}**: [Purpose] - [Async integration pattern]
{{/each}}

## 🔄 Async Database Operations

### SQLAlchemy Async Patterns
```python
# Session management
async_session = async_sessionmaker(
    async_engine, class_=AsyncSession, expire_on_commit=False
)

# Repository pattern
class {{MainResource}}Repository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, obj_in: {{MainResource}}Create) -> {{MainResource}}:
        db_obj = {{MainResource}}(**obj_in.dict())
        self.db.add(db_obj)
        await self.db.commit()
        await self.db.refresh(db_obj)
        return db_obj

    async def get_multi(self, skip: int = 0, limit: int = 100):
        result = await self.db.execute(
            select({{MainResource}}).offset(skip).limit(limit)
        )
        return result.scalars().all()
```

---

## 🎯 **Información para Claude Code - FastAPI Patterns**

### Convenciones de Código FastAPI
```python
# Router structure
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()

@router.get("/", response_model=List[{{MainResource}}Response])
async def read_{{main_resource}}s(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Async business logic
    items = await {{main_resource}}_service.get_multi(db, skip=skip, limit=limit)
    return items

@router.post("/", response_model={{MainResource}}Response)
async def create_{{main_resource}}(
    {{main_resource}}: {{MainResource}}Create,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Async creation logic
    return await {{main_resource}}_service.create(db, obj_in={{main_resource}})
```

### Estructura de Archivos FastAPI
```
app/
├── main.py                   # FastAPI app instance
├── core/                     # Core configuration
│   ├── config.py            # Settings
│   ├── security.py          # JWT, OAuth2
│   └── database.py          # Async database setup
├── api/                      # API routes
│   ├── api_v1/              # API version 1
│   │   ├── endpoints/       # Route handlers
│   │   └── deps.py         # Dependencies
├── models/                   # SQLAlchemy models
├── schemas/                  # Pydantic schemas
├── services/                 # Business logic
└── tests/                    # Async tests
```

### FastAPI + Clean Architecture Integration
- **Domain Layer**: `app/models/` + `app/schemas/` - Entities y value objects
- **Application Layer**: `app/services/` - Use cases con async/await
- **Infrastructure**: `app/core/`, `app/db/` - Database, external APIs
- **Presentation**: `app/api/` - FastAPI routers y endpoints

---

*📅 Última actualización: {{CURRENT_DATE}}*
*🤖 Generado automáticamente por CYLON26 Harness System para FastAPI*
*✨ Customizar según las necesidades específicas de la API FastAPI*