## 💳 Sistema de Pagos

### Proveedor de Pagos
- **Servicio**: [Stripe/PayPal/Square/Custom]
- **Justificación**: [Por qué se eligió este proveedor vs alternativas]
- **Ambiente**: [Sandbox/Test/Production configuraciones]

### Métodos de Pago Soportados
- ✅ **Tarjetas de crédito/débito**: Visa, Mastercard, American Express
- ✅ **Transferencias bancarias**: ACH, SEPA (según región)
- ✅ **Wallets digitales**: Apple Pay, Google Pay, PayPal
- ❌ **Criptomonedas**: No soportado actualmente

### Flujo de Pagos
1. **Iniciación**: [Cómo se inicia el proceso de pago]
2. **Validación**: [Verificaciones previas al cobro]
3. **Procesamiento**: [Comunicación con proveedor de pagos]
4. **Confirmación**: [Manejo de respuesta exitosa]
5. **Error Handling**: [Manejo de fallos en el pago]

### Webhooks de Pagos
```bash
# Endpoints de webhooks críticos
POST /webhooks/{{PAYMENT_PROVIDER}}     - Confirmaciones de pago
POST /webhooks/refunds                  - Procesamiento de reembolsos
POST /webhooks/disputes                 - Manejo de disputas
```

### Configuración de Pagos
```bash
# Variables de entorno para pagos
{{PAYMENT_PROVIDER}}_PUBLIC_KEY={{PUBLIC_KEY_EXAMPLE}}
{{PAYMENT_PROVIDER}}_SECRET_KEY={{SECRET_KEY_EXAMPLE}}
{{PAYMENT_PROVIDER}}_WEBHOOK_SECRET={{WEBHOOK_SECRET_EXAMPLE}}
```

### Montos y Comisiones
- **Moneda principal**: [USD/EUR/MXN/etc.]
- **Montos mínimos**: [Ej: $1.00 USD]
- **Montos máximos**: [Ej: $10,000 USD]
- **Comisiones**: [Ej: 2.9% + $0.30 por transacción]
- **Tarifas adicionales**: [Disputas, reembolsos, etc.]

### Seguridad PCI
- **Compliance**: PCI DSS Level {{PCI_LEVEL}}
- **Tokenización**: [Cómo se manejan los datos de tarjetas]
- **Encriptación**: [Protección de datos sensibles]
- **Auditorías**: [Frecuencia y proceso de auditorías]

### Reembolsos y Disputas
- **Política de reembolsos**: [Tiempo límite, condiciones]
- **Proceso automatizado**: [Reembolsos automáticos vs manuales]
- **Manejo de disputas**: [Proceso para chargebacks]
- **Documentación requerida**: [Qué evidencia se recolecta]

### Testing de Pagos
```{{DETECTED_LANGUAGE}}
// Tarjetas de prueba para testing
{{#if TESTING_CARDS}}
{{TESTING_CARDS}}
{{else}}
// [Configurar tarjetas de prueba del proveedor]
{{/if}}
```

### Métricas de Pagos
- **Tasa de éxito**: Target >95%
- **Tiempo de procesamiento**: <3 segundos
- **Disputas**: <1% del volumen total
- **Reembolsos**: Tracking automático