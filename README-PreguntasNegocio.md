# 📉 Informe de Análisis de Negocio: VitalsFlow

Este documento detalla los hallazgos obtenidos tras el procesamiento y visualización del dataset de operaciones hospitalarias. El objetivo es responder a las 5 preguntas críticas de negocio planteadas en el reto.

## 🔍 Metodología

Para responder a estas interrogantes, se utilizó una arquitectura **ETL** (Extract, Transform, Load) sobre una base de datos **SQLite**, procesando la información mediante **SQL** y **Pandas** para asegurar la integridad de las métricas.

---

## 💡 Respuestas a las Preguntas de Negocio

### Q1: ¿Cuál es el volumen de admisiones y existe estacionalidad?

- **Hallazgo:** El volumen de pacientes se mantiene constante en un rango de ~800-900 admisiones mensuales.
- **Conclusión:** No se observan picos estacionales significativos (como épocas de gripe o festividades).
- **Nota Técnica:** El uso de una **Media Móvil** permitió confirmar que la tendencia es plana, lo cual es característico de los datasets generados algorítmicamente.

### Q2: ¿Cuáles son los 10 hospitales con mayor facturación?

- **Hallazgo:** Hospitales como *Johnson Plc* y *Smith Ltd* lideran la generación de ingresos, superando el millón de dólares en facturación acumulada.
- **Conclusión:** La distribución del ingreso está muy fragmentada entre múltiples sedes, lo que sugiere una red hospitalaria extensa.

### Q3: ¿Cuál es el tiempo promedio de estancia según el tipo de admisión?

- **Hallazgo:** La estancia promedio es notablemente uniforme (~15.5 días) independientemente de si la admisión es *Urgente*, *Electiva* o de *Emergencia*.
- **Conclusión:** Operativamente, el hospital no parece diferenciar el tiempo de cama basado en la gravedad inicial del ingreso, un punto clave para la optimización de recursos.

### Q4: ¿Cuál es la incidencia de resultados clínicos "Anormales"?

- **Hallazgo:** Existe una proporción significativa de resultados marcados como "Abnormal".
- **Conclusión:** Este KPI es crítico para la seguridad del paciente. El dashboard resalta estos casos para facilitar auditorías clínicas inmediatas.

### Q5 (Libre): ¿Existe correlación entre la condición médica y el costo?

- **Análisis:** Se utilizó un diagrama de caja (Boxplot) para comparar los costos de enfermedades como Cáncer, Diabetes y Asma.
- **Hallazgo Crítico:** La facturación es casi idéntica para todas las enfermedades.
- **Conclusión de Ingeniería:** Este análisis permitió validar que el dataset es sintético, ya que en un entorno real, condiciones de alta complejidad (Cáncer) tendrían costos significativamente superiores a condiciones crónicas controlables (Hipertensión).

---

## 🛠️ Herramientas de Análisis

- **Motor de Consultas:** SQLite 3
- **Procesamiento:** Python / Pandas
- **Visualización:** Plotly Dynamic Charts
