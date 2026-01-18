# Template para Modificaciones del Sistema Harness

## Información Básica
- **Tipo de Modificación**: [Skill | Agent | Template | Utility]
- **Nombre del Componente**: [nombre-del-componente]
- **Versión Actual**: [x.x.x]
- **Fecha de Modificación**: [YYYY-MM-DD]

## Análisis Previo Requerido

### 1. Estado Actual del Componente
```yaml
componente_actual:
  ubicacion: ".claude/[skills|agents]/[nombre]"
  archivos_principales:
    - "[archivo].md"
    - "[otros-archivos]"
  dependencias_directas:
    - "[componente-1]"
    - "[componente-2]"
  dependencias_indirectas:
    - "[sistema-1]"
    - "[sistema-2]"
  herramientas_utilizadas:
    - "[tool-1]"
    - "[tool-2]"
```

### 2. Impacto de la Modificación
```yaml
impacto_analizado:
  componentes_afectados:
    directos: ["[lista-componentes-directos]"]
    indirectos: ["[lista-componentes-indirectos]"]
  documentacion_afectada:
    - "[doc-1]"
    - "[doc-2]"
  templates_afectados:
    - "[template-1]"
    - "[template-2]"
  breaking_changes: [true|false]
  compatibilidad_mantenida: [true|false]
```

## Especificación de Cambios

### Cambios Funcionales
```markdown
### [CF-001]: [Descripción del cambio principal]
- **Antes**: [Comportamiento actual]
- **Después**: [Comportamiento deseado]
- **Razón**: [Justificación del cambio]

### [CF-002]: [Segundo cambio principal]
- **Antes**: [Estado actual]
- **Después**: [Estado deseado]
- **Razón**: [Justificación]
```

### Cambios Técnicos
```yaml
cambios_tecnicos:
  herramientas_nuevas:
    - nombre: "[tool-name]"
      proposito: "[para-que-se-usa]"
      impacto: "[donde-impacta]"
  herramientas_modificadas:
    - nombre: "[existing-tool]"
      cambios: "[que-cambia]"
      razon: "[por-que-cambia]"
  herramientas_removidas:
    - nombre: "[deprecated-tool]"
      razon: "[por-que-se-elimina]"
      reemplazo: "[que-lo-reemplaza]"
```

## Plan de Implementación

### Fase 1: Preparación
```bash
# Pasos previos obligatorios
1. Backup de componentes existentes
2. Análisis de dependencias completo
3. Validación de coherencia arquitectónica actual
4. Documentación del estado baseline
```

### Fase 2: Implementación Incremental
```bash
# Secuencia de modificaciones (orden crítico)
1. [Primer cambio - más básico/foundational]
2. [Segundo cambio - dependiente del primero]
3. [Tercer cambio - construcción sobre anteriores]
4. [Validación intermedia]
5. [Cambios finales]
```

### Fase 3: Validación y Documentación
```bash
# Validación post-implementación
1. Tests de funcionalidad básica
2. Validación de integración con otros componentes
3. Verificación de coherencia del sistema completo
4. Actualización automática de documentación
5. Tests de regresión en componentes dependientes
```

## Criterios de Validación

### Funcional
- [ ] El componente modificado cumple con los nuevos requisitos
- [ ] No se ha roto funcionalidad existente
- [ ] Integración correcta con otros componentes
- [ ] Herramientas funcionan según especificación

### Arquitectónico
- [ ] Mantiene coherencia con metodología Anthropic Long-Running Agents
- [ ] Compatible con sistema de context injection
- [ ] Integrable con task coordination
- [ ] Sigue convenciones del harness ecosystem

### Documentación
- [ ] Documentación actualizada automáticamente
- [ ] Ejemplos de uso actualizados
- [ ] Referencias cruzadas corregidas
- [ ] Changelog actualizado

## Testing y Validación

### Tests Automáticos
```yaml
test_plan:
  unit_tests:
    - funcionalidad_basica
    - integracion_herramientas
    - validacion_parametros
  integration_tests:
    - context_injection_compatibility
    - task_coordination_compatibility
    - cross_component_communication
  regression_tests:
    - existing_functionality_preserved
    - dependent_components_unaffected
    - documentation_consistency
```

### Tests Manuales
```bash
# Validación manual requerida
1. Ejecutar skill/agent modificado con casos de uso típicos
2. Verificar output y comportamiento esperado
3. Validar integración con flujo harness completo
4. Confirmar que documentación refleja cambios
```

## Rollback Plan

### Condiciones de Rollback
- Falla en tests de funcionalidad básica
- Rotura de compatibilidad con componentes críticos
- Inconsistencias en documentación no resolubles
- Performance degradation significativa

### Procedimiento de Rollback
```bash
1. Restaurar archivos desde backup automático
2. Revertir cambios en documentación
3. Restaurar templates afectados
4. Validar que sistema retorna a estado previo
5. Documentar causa del rollback para análisis
```

## Automodificación (Si Aplicable)

### Criterios para Automodificación
```yaml
automodificacion_requerida:
  cuando:
    - el_skill_se_modifica_a_si_mismo: true
    - cambios_afectan_funcionalidad_propia: true
    - nuevas_capacidades_requieren_actualizacion: true
  como:
    - analisis_de_impacto_propio: "obligatorio"
    - implementacion_segura: "paso_a_paso"
    - validacion_interna: "completa"
    - documentacion_actualizada: "automatica"
```

### Procedimiento de Automodificación
```bash
1. Análisis de necesidad de automodificación
2. Backup del skill actual (harness-manage)
3. Implementación incremental de cambios propios
4. Validación de funcionalidad propia actualizada
5. Tests de autovalidación
6. Actualización de esta documentación
```

## Changelog y Versionado

### Formato de Changelog
```markdown
## [Versión X.Y.Z] - YYYY-MM-DD

### Added (Funcionalidades añadidas)
- [Nueva funcionalidad 1]
- [Nueva funcionalidad 2]

### Changed (Funcionalidades modificadas)
- [Cambio en funcionalidad existente 1]
- [Cambio en funcionalidad existente 2]

### Deprecated (Funcionalidades deprecadas)
- [Funcionalidad que será removida]

### Removed (Funcionalidades eliminadas)
- [Funcionalidad eliminada 1]

### Fixed (Bugs corregidos)
- [Bug corregido 1]
- [Bug corregido 2]

### Security (Cambios de seguridad)
- [Mejora de seguridad 1]
```

### Versionado Semántico
- **MAJOR (X)**: Cambios incompatibles en API/funcionalidad
- **MINOR (Y)**: Funcionalidad nueva compatible hacia atrás
- **PATCH (Z)**: Bug fixes compatibles hacia atrás

## Comunicación de Cambios

### Documentación Afectada
```yaml
documentacion_updates:
  README_principal: "[que-seccion-cambiar]"
  HARNESS_md: "[que-documentar]"
  skill_documentacion: "[actualizacion-automatica]"
  agent_documentacion: "[cambios-necesarios]"
  templates: "[templates-afectados]"
```

### Notificaciones
- [ ] Log de cambios en sistema
- [ ] Actualización de métricas del harness
- [ ] Notification en dashboard (si aplicable)
- [ ] Documentación en commit message

## Métricas Post-Implementación

### Performance
```yaml
metricas_monitoreo:
  tiempo_ejecucion:
    baseline: "[X]ms"
    post_cambio: "[Y]ms"
    delta: "[+/-Z]%"
  memoria_utilizada:
    baseline: "[X]MB"
    post_cambio: "[Y]MB"
    delta: "[+/-Z]%"
  tokens_contexto:
    baseline: "[X] tokens"
    post_cambio: "[Y] tokens"
    delta: "[+/-Z]%"
```

### Funcionalidad
```yaml
validacion_funcional:
  casos_uso_nuevos: "[X] casos validados"
  casos_uso_existentes: "[Y] casos revalidados"
  integracion_componentes: "[Z] integraciones verificadas"
  documentacion_actualizada: "[true|false]"
```

---

**Template para Modificaciones Seguras del Ecosistema CYLON26**

*"Una modificación bien planificada es una mejora garantizada"*