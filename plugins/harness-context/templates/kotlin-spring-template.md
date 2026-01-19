# Claude Context - {{PROJECT_NAME}}

## 🎯 Contexto del Proyecto

### Dominio de Negocio
- **Qué hace**: [Servicio backend empresarial que proporciona [funcionalidad específica]]
- **Usuarios objetivo**: [Aplicaciones cliente, microservicios, sistemas empresariales]
- **Valor único**: [Qué diferencia este servicio de alternativas]

### Reglas de Negocio Críticas
- [Regla específica importante 1]
- [Regla específica importante 2]
- [Restricciones del dominio empresarial específicas]

## 🏗️ Arquitectura de ESTE Proyecto

### Stack Tecnológico Elegido
- **Lenguaje**: Kotlin {{KOTLIN_VERSION}}
- **Framework**: Spring Boot {{SPRING_BOOT_VERSION}} (elegido por: enterprise features, ecosistema)
- **Base de datos**: [PostgreSQL/MySQL/Oracle] (justificación empresarial)
- **ORM**: Spring Data JPA con Hibernate
- **Build**: Gradle con Kotlin DSL
- **Deploy**: [Docker + Kubernetes/OpenShift]

### Decisiones Arquitectónicas Específicas
- **Autenticación**: [Spring Security + JWT/OAuth2/LDAP]
- **Database**: [JPA + connection pooling con HikariCP]
- **Cache**: [Spring Cache + Redis/Hazelcast]
- **Message Queue**: [Spring Boot + RabbitMQ/Apache Kafka]
- **Validation**: Bean Validation (JSR-303) con Spring

## 🔧 Configuración Específica de Spring Boot

### Variables de Entorno Críticas
```bash
# Spring Boot & database
SPRING_DATASOURCE_URL=jdbc:postgresql://localhost:5432/dbname
SPRING_DATASOURCE_USERNAME=dbuser
SPRING_DATASOURCE_PASSWORD=dbpass

# Spring profiles
SPRING_PROFILES_ACTIVE=development

# Security
JWT_SECRET=your-jwt-secret-here
JWT_EXPIRATION=86400000

# External services
{{#each EXTERNAL_SERVICES}}
{{name}}_API_KEY={{example}}
{{/each}}
```

### REST Endpoints Principales
#### **Core Business Endpoints**
- `GET /` - Service info y health check
- `GET /actuator/health` - Spring Boot health endpoint
- `POST /api/auth/login` - Autenticación con Spring Security
- `GET /api/{{MAIN_RESOURCE}}` - Lista {{MAIN_RESOURCE}} con paginación
- `POST /api/{{MAIN_RESOURCE}}` - Crear nuevo {{MAIN_RESOURCE}}
- `GET /api/{{MAIN_RESOURCE}}/{id}` - Obtener {{MAIN_RESOURCE}} específico
- `PUT /api/{{MAIN_RESOURCE}}/{id}` - Actualizar {{MAIN_RESOURCE}}
- `DELETE /api/{{MAIN_RESOURCE}}/{id}` - Eliminar {{MAIN_RESOURCE}}

#### **Enterprise Endpoints**
- `GET /actuator/metrics` - Métricas de Spring Boot Actuator
- `GET /actuator/prometheus` - Métricas para Prometheus
- `POST /api/bulk/{{MAIN_RESOURCE}}` - Operaciones en lote
- `GET /api/{{MAIN_RESOURCE}}/search` - Búsqueda avanzada

### Spring Boot Data Classes Críticas
```kotlin
// JPA Entity
@Entity
@Table(name = "{{main_resource}}")
data class {{MainResource}}(
    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    val id: UUID? = null,

    @Column(nullable = false)
    val name: String,

    @Column
    val description: String? = null,

    @CreatedDate
    @Column(name = "created_at", nullable = false, updatable = false)
    val createdAt: LocalDateTime = LocalDateTime.now(),

    @LastModifiedDate
    @Column(name = "updated_at", nullable = false)
    val updatedAt: LocalDateTime = LocalDateTime.now()
)

// DTO classes
data class {{MainResource}}CreateRequest(
    @field:NotBlank(message = "Name is required")
    val name: String,

    @field:Size(max = 500, message = "Description too long")
    val description: String?
)

data class {{MainResource}}Response(
    val id: UUID,
    val name: String,
    val description: String?,
    val createdAt: LocalDateTime,
    val updatedAt: LocalDateTime
) {
    companion object {
        fun from(entity: {{MainResource}}): {{MainResource}}Response {
            return {{MainResource}}Response(
                id = entity.id!!,
                name = entity.name,
                description = entity.description,
                createdAt = entity.createdAt,
                updatedAt = entity.updatedAt
            )
        }
    }
}
```

## 👥 Contexto del Equipo

### Responsabilidades Spring Boot-Specific
- **Backend Lead**: [Nombre] - Spring architecture, enterprise patterns
- **Database**: [Nombre] - JPA, database design, performance tuning
- **Security**: [Nombre] - Spring Security, enterprise authentication
- **DevOps**: [Nombre] - Kubernetes, Spring Boot deployment, monitoring

### Flujo de Trabajo Spring Boot
1. **Service Design**: Spring Boot structure, REST API design
2. **Development**:
   - Implementar controllers con Spring MVC
   - Crear entities con JPA annotations
   - Services con Spring dependency injection
3. **Testing**: Spring Boot Test, TestContainers para integration
4. **Deploy**: Docker build → Kubernetes → Enterprise deployment

## 🚨 Consideraciones Especiales de Spring Boot

### Performance Crítica Enterprise
- **Database Queries**: JPA optimization, query tuning
- **API Response Time**: <300ms para endpoints GET
- **Connection Pooling**: HikariCP tuning para enterprise load
- **Cache Strategy**: Spring Cache con Redis para data frequently accessed

### Spring Boot Patterns Específicos
```kotlin
// Service layer
@Service
@Transactional
class {{MainResource}}Service(
    private val {{mainResource}}Repository: {{MainResource}}Repository
) {
    suspend fun create(request: {{MainResource}}CreateRequest): {{MainResource}}Response {
        val entity = {{MainResource}}(
            name = request.name,
            description = request.description
        )

        val saved = {{mainResource}}Repository.save(entity)
        return {{MainResource}}Response.from(saved)
    }

    suspend fun findAll(pageable: Pageable): Page<{{MainResource}}Response> {
        return {{mainResource}}Repository.findAll(pageable)
            .map { {{MainResource}}Response.from(it) }
    }
}

// Repository layer
@Repository
interface {{MainResource}}Repository : JpaRepository<{{MainResource}}, UUID> {
    @Query("SELECT r FROM {{MainResource}} r WHERE r.name LIKE %:name%")
    suspend fun findByNameContaining(name: String): List<{{MainResource}}>
}
```

### Spring Security Patterns
- **JWT Authentication**: Spring Security JWT filter
- **Method Security**: @PreAuthorize, @Secured annotations
- **CORS Configuration**: Spring Boot CORS setup
- **Input Validation**: Bean Validation + Spring validation
- **SQL Injection**: JPA/Hibernate automatic protection

### Enterprise Monitoring
- **Spring Boot Actuator**: Health checks, metrics
- **Prometheus Integration**: Custom metrics exposure
- **Log Aggregation**: Logback + ELK stack
- **Performance Monitoring**: APM integration (New Relic, etc.)

## 📚 Recursos Spring Boot del Proyecto

### Spring Boot-Specific Docs
- **API Documentation**: [SpringDoc OpenAPI integration]
- **Database Schema**: [JPA entities documentation]
- **Enterprise Patterns**: [Project-specific Spring patterns]
- **Deployment Guide**: [Kubernetes + Spring Boot deployment]

### Development Setup
```bash
# Local development
./gradlew bootRun                 # Start Spring Boot app
./gradlew test                    # Run tests
./gradlew build                   # Build jar
./gradlew bootJar                 # Build executable jar

# Docker
docker build -t {{PROJECT_NAME}} .
docker run -p 8080:8080 {{PROJECT_NAME}}

# Database migrations (si usa Flyway/Liquibase)
./gradlew flywayMigrate
```

### External Services Integration
{{#each EXTERNAL_APIS}}
- **{{name}}**: [Purpose] - [Spring Boot integration pattern]
{{/each}}

## 🔄 Spring Data JPA Operations

### Repository Patterns
```kotlin
// Custom repository methods
@Repository
interface {{MainResource}}Repository : JpaRepository<{{MainResource}}, UUID>,
    {{MainResource}}RepositoryCustom {

    // Query methods
    fun findByNameIgnoreCase(name: String): Optional<{{MainResource}}>

    // Custom queries
    @Query("""
        SELECT r FROM {{MainResource}} r
        WHERE r.createdAt BETWEEN :startDate AND :endDate
        ORDER BY r.createdAt DESC
    """)
    fun findByDateRange(startDate: LocalDateTime, endDate: LocalDateTime): List<{{MainResource}}>

    // Native queries cuando sea necesario
    @Query(value = "SELECT * FROM {{main_resource}} WHERE complex_condition", nativeQuery = true)
    fun complexNativeQuery(): List<{{MainResource}}>
}

// Transaction management
@Service
@Transactional
class {{MainResource}}TransactionService(
    private val {{mainResource}}Repository: {{MainResource}}Repository
) {
    @Transactional(rollbackFor = [Exception::class])
    suspend fun complexBusinessOperation(request: ComplexRequest): ComplexResponse {
        // Multiple database operations in single transaction
        // Automatic rollback on exception
    }
}
```

---

## 🎯 **Información para Claude Code - Spring Boot Patterns**

### Convenciones de Código Spring Boot
```kotlin
// Controller structure
@RestController
@RequestMapping("/api/{{main-resource}}")
@Validated
class {{MainResource}}Controller(
    private val {{mainResource}}Service: {{MainResource}}Service
) {

    @GetMapping
    suspend fun getAll(
        @RequestParam(defaultValue = "0") page: Int,
        @RequestParam(defaultValue = "10") size: Int
    ): ResponseEntity<Page<{{MainResource}}Response>> {
        val pageable = PageRequest.of(page, size)
        val result = {{mainResource}}Service.findAll(pageable)
        return ResponseEntity.ok(result)
    }

    @PostMapping
    suspend fun create(
        @Valid @RequestBody request: {{MainResource}}CreateRequest
    ): ResponseEntity<{{MainResource}}Response> {
        val created = {{mainResource}}Service.create(request)
        return ResponseEntity.status(HttpStatus.CREATED).body(created)
    }

    @ExceptionHandler(ValidationException::class)
    fun handleValidation(ex: ValidationException): ResponseEntity<ErrorResponse> {
        return ResponseEntity.badRequest().body(ErrorResponse(ex.message))
    }
}
```

### Estructura de Archivos Spring Boot
```
src/main/kotlin/
├── {{package}}/
│   ├── Application.kt           # Main Spring Boot application
│   ├── config/                  # Spring configuration
│   │   ├── DatabaseConfig.kt    # JPA, datasource config
│   │   ├── SecurityConfig.kt    # Spring Security config
│   │   └── WebConfig.kt        # MVC, CORS config
│   ├── controller/              # REST controllers
│   ├── service/                 # Business logic services
│   ├── repository/              # JPA repositories
│   ├── entity/                  # JPA entities
│   ├── dto/                     # Data transfer objects
│   └── exception/               # Custom exceptions
src/main/resources/
├── application.yml              # Spring Boot configuration
├── application-dev.yml          # Development profile
├── application-prod.yml         # Production profile
└── db/migration/               # Database migrations (Flyway)
```

### Spring Boot + Clean Architecture Integration
- **Domain Layer**: `entity/`, `dto/` - JPA entities y value objects
- **Application Layer**: `service/` - Use cases con Spring annotations
- **Infrastructure**: `repository/`, `config/` - JPA repos, external services
- **Presentation**: `controller/` - REST controllers con Spring MVC

---

*📅 Última actualización: {{CURRENT_DATE}}*
*🤖 Generado automáticamente por N26 Harness System para Spring Boot*
*✨ Customizar según las necesidades específicas del servicio Spring Boot*