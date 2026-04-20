# Escenarios de Calidad ATAM - Microservicio de Descuentos

## Metodología

Los siguientes escenarios siguen el formato estándar de ATAM (Architecture Trade-off Analysis Method): Fuente → Estímulo → Artefacto → Entorno → Respuesta → Medida.

---

## Escenario 1: Disponibilidad

| Componente        | Descripción                                                           |
|-------------------|-----------------------------------------------------------------------|
| **Fuente**        | Usuarios del sistema OmniStream durante horas pico                    |
| **Estímulo**      | 10,000 peticiones concurrentes de cálculo de descuento en 5 segundos  |
| **Artefacto**     | Microservicio de Descuentos                                           |
| **Entorno**       | 3 instancias del microservicio desplegadas en contenedores            |
| **Respuesta**     | El microservicio procesa todas las solicitudes sin rechazar peticiones|
| **Medida**        | Tiempo de respuesta < 150ms (percentil 95). Tasa de éxito > 99.9%     |

**Justificación:** El negocio proyecta un aumento de tráfico de 100x durante el próximo mes. El monolito actual no puede garantizar este nivel de disponibilidad porque el MotorDescuentos comparte recursos con el resto del sistema.

---

## Escenario 2: Mantenibilidad

| Componente    | Descripción                                                                                                       |
|---------------|-------------------------------------------------------------------------------------------------------------------|
| **Fuente**    | Product Owner / Equipo de desarrollo                                                                              |
| **Estímulo**  | Cambio en reglas de negocio: descuento VIP del 20% → 25%. Adición de nueva regla "descuento por referral del 5%"  |
| **Artefacto** | Microservicio de Descuentos                                                                                       |
| **Entorno**   | Sistema en producción. Monolito legado operando con otras funcionalidades                                         |
| **Respuesta** | El cambio se implementa únicamente en el microservicio                                                            |
| **Medida**    | Tiempo de implementación < 4 horas. Cero modificaciones en el monolito. Pruebas unitarias actualizadas y en verde |

**Justificación:** La auditoría de Fase 1 identificó que el MotorDescuentos usa `getattr()` y números mágicos. Extraerlo a un microservicio aislará los cambios de reglas de descuento del resto del sistema.

---

## Escenario 3: Escalabilidad (adicional)

| Componente    | Descripción                                                                  |
|---------------|------------------------------------------------------------------------------|
| **Fuente**    | Picos estacionales de tráfico                                                |
| **Estímulo**  | Aumento del 500% en solicitudes de descuento en 10 minutos                   |
| **Artefacto** | Microservicio de Descuentos                                                  |
| **Entorno**   | Sistema con auto-escalado configurado (CPU > 70%)                            |
| **Respuesta** | El orquestador crea nuevas instancias automáticamente                        |
| **Medida**    | Nuevas instancias disponibles en < 60 segundos. Sin degradación del servicio |

**Justificación:** La escalabilidad horizontal es el principal driver para extraer el microservicio.