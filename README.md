# 🏥 VitalsFlow: Advanced Hospital Operations Dashboard

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-FF4B4B.svg)
![GitHub Actions](https://img.shields.io/badge/CI/CD-GitHub%20Actions-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

**VitalsFlow** es una solución de análisis de datos de extremo a extremo (End-to-End) diseñada para monitorizar y optimizar las operaciones hospitalarias. El proyecto transforma datos clínicos crudos en un dashboard interactivo de alto impacto, permitiendo la toma de decisiones basada en métricas de rendimiento real.

## 🚀 Vista Previa

> **Link del Dashboard en Vivo:** [VitalsFlow](https://vitalflow-jhair-zambrano.streamlit.app/)

## 🛠️ Arquitectura y Principios de Ingeniería

El software fue diseñado siguiendo una **Arquitectura Modular por Capas** y aplicando principios **SOLID** para garantizar la escalabilidad y el mantenimiento:

- **Data Layer (`src/data_manager.py`):** Encapsula la lógica de conexión a SQLite y transformaciones iniciales (Principio de Responsabilidad Única).
- **View Layer (`src/visuals.py`):** Clase especializada en la generación de gráficos de alta fidelidad con Plotly, desacoplada de la lógica de negocio.
- **Controller/Orchestrator (`app.py`):** Gestiona el flujo de la aplicación y la interactividad del usuario.

## 📊 Funcionalidades Clave

- **Filtros Dinámicos:** Segmentación global por condición médica, tipo de admisión y rango histórico de años.
- **Análisis de Tendencias (Q1):** Visualización de volumen con **Media Móvil ajustable** (suavizado de ruido) y curvas tipo *Spline*.
- **Métricas Operativas (Q3):** Análisis interactivo de tiempos de estancia promedio.
- **Visualización Financiera (Q2):** Top 10 centros médicos por volumen de facturación con gradientes de color.
- **Identidad Visual:** Soporte nativo para **Modo Oscuro/Claro** y sidebar profesional estilizado.

## ⚙️ Configuración del Proyecto

### Requisitos Previos

- Python 3.10 o superior.
- Git.

### Instalación Local

1. Clona el repositorio:

   ```bash
   git clone [https://github.com/tu-usuario/vitalsflow.git](https://github.com/tu-usuario/vitalsflow.git)
   cd vitalsflow
    ```

2. Crea y activa un entorno virtual:

```bash
python -m venv .venv
# Windows:
.\venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt

```

4. Ejecuta la aplicación:

```bash
streamlit run app.py

```

## 🔄 Fase 5: Pipeline de CI/CD

Este proyecto implementa un flujo de automatización completo:

* **CI (Continuous Integration):** A través de **GitHub Actions**, cada `push` activa un pipeline que valida el entorno, las dependencias y la integridad del código Python.
* **CD (Continuous Deployment):** Despliegue automático y sincronizado hacia **Streamlit Community Cloud** mediante webhooks, permitiendo actualizaciones en tiempo real con un solo comando (`git push`).

## 📁 Estructura del Repositorio

```text
vitalsflow/
├── .github/workflows/   # Pipeline de CI/CD (GitHub Actions)
├── .streamlit/          # Configuración visual del tema
├── data/                # Base de datos SQLite (healthcare_warehouse.db)
├── src/                 # Código fuente modular (Data & Visuals)
├── app.py               # Orquestador principal de la aplicación
└── requirements.txt     # Dependencias del proyecto

```

---

Desarrollado con ❤️ por Jhair Zambrano
