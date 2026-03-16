import streamlit as st
from src.data_manager import DatabaseManager
from src.visuals import Visualizer

st.set_page_config(page_title="VitalsFlow | Operaciones", page_icon="🧑‍💻", layout="wide")

@st.cache_data
def load_data():
    db = DatabaseManager()
    return db.get_all_records()

try:
    df_raw = load_data()
except Exception as e:
    st.error(str(e))
    st.stop()

st.sidebar.markdown("""
    <div style='display: flex; align-items: center; margin-bottom: 10px;'>
        <h2 style='margin: 0; padding: 0;'> VitalsFlow</h2>
    </div>
""", unsafe_allow_html=True)
st.sidebar.caption("Panel de Control Operativo")
st.sidebar.divider()

st.sidebar.markdown("### 🎨 Apariencia")
tema = st.sidebar.radio("Tema", ["🌙 Modo Oscuro", "☀️ Modo Claro"], label_visibility="collapsed")
plot_theme = "plotly_dark" if tema == "🌙 Modo Oscuro" else "plotly_white"
viz = Visualizer(theme=plot_theme)

st.sidebar.divider()

st.sidebar.markdown("### 🎛️ Parámetros de Análisis")

min_year = int(df_raw['Date of Admission'].dt.year.min())
max_year = int(df_raw['Date of Admission'].dt.year.max())

rango_anios = st.sidebar.slider(
    "📅 Rango Histórico",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year)
)

condiciones = st.sidebar.multiselect("🩺 Condición Médica", df_raw['Medical Condition'].unique(), default=df_raw['Medical Condition'].unique())
admisiones = st.sidebar.multiselect("🏥 Tipo de Admisión", df_raw['Admission Type'].unique(), default=df_raw['Admission Type'].unique())

st.sidebar.divider()
st.sidebar.markdown("""
    <div style='font-size: 13px; color: gray;'>
        <p>🟢 <b>Sistema En Línea</b><br>
        <i>Motor de datos activo y sincronizado.</i></p>
    </div>
""", unsafe_allow_html=True)

df_filtered = df_raw[
    (df_raw['Date of Admission'].dt.year >= rango_anios[0]) & 
    (df_raw['Date of Admission'].dt.year <= rango_anios[1]) & 
    (df_raw['Medical Condition'].isin(condiciones)) & 
    (df_raw['Admission Type'].isin(admisiones))
]

st.title("VitalsFlow: Dashboard de Operaciones Clínicas")
st.markdown("Monitor interactivo para la toma de decisiones basada en datos.")

k1, k2, k3, k4 = st.columns(4)
k1.metric(label="Total Pacientes", value=f"{len(df_filtered):,}")
k2.metric(label="Ingresos Totales", value=f"${df_filtered['Billing Amount'].sum():,.0f}")
k3.metric(label="Estancia Promedio", value=f"{df_filtered['Days Hospitalized'].mean():.1f} Días")
k4.metric(label="Doctores Activos", value=f"{df_filtered['Doctor'].nunique()}")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Q1: Tendencia de Volumen Mensual")
    ventana_meses = st.slider("Suavizado de Tendencia (Media Móvil):", min_value=1, max_value=12, value=3, step=1)
    st.plotly_chart(viz.plot_q1_trends(df_filtered, window=ventana_meses), use_container_width=True)
    with st.expander("💡 Ver Análisis de Estacionalidad"):
        st.write(f"La línea gris representa la media móvil de **{ventana_meses} meses**. Al ajustar el deslizador, agrupamos la historia para identificar la 'Señal' sobre el 'Ruido'. Debido a la naturaleza sintética de los datos, la tendencia se mantiene sorprendentemente plana.")

with col2:
    st.subheader("Q3: Estancia Promedio de Pacientes")
    agrupacion = st.radio("Analizar por:", ["Tipo de Admisión", "Condición Médica"], horizontal=True)
    columna_q3 = 'Admission Type' if agrupacion == "Tipo de Admisión" else 'Medical Condition'
    
    st.plotly_chart(viz.plot_q3_avg_stay(df_filtered, group_col=columna_q3), use_container_width=True)
    with st.expander("💡 Ver Análisis de Estancia"):
        st.write("Muestra el promedio de días que un paciente pasa hospitalizado. Permitir agrupar por condición o tipo de ingreso ayuda a prever la ocupación de camas a futuro.")

col3, col4 = st.columns(2)

with col3:
    st.subheader("Q2: Top 10 Hospitales por Ingresos")
    st.plotly_chart(viz.plot_q2_top_hospitals(df_filtered), use_container_width=True)
    with st.expander("💡 Ver Análisis Financiero y Hallazgo de Datos"):
        st.write("Identifica los centros médicos con mayor facturación. **Nota Analítica:** La repetición de apellidos genéricos (ej. 'Smith', 'Johnson') reafirma el uso de librerías de generación de datos (*Faker*). A nivel matemático los cálculos son exactos, pero representan entidades ficticias.")

with col4:
    st.subheader("Q4: Resultados de Pruebas Clínicas")
    st.plotly_chart(viz.plot_q4_test_results(df_filtered), use_container_width=True)
    with st.expander("💡 Ver Análisis de Incidencias"):
        st.write("El segmento 'Abnormal' (Anormal) está destacado para alertar sobre la tasa de diagnósticos críticos o pruebas fallidas que requieren atención inmediata.")

st.subheader("Q5 (Libre): Dispersión de Costos por Condición Médica")
st.plotly_chart(viz.plot_q5_cost_distribution(df_filtered), use_container_width=True)
with st.expander("💡 Ver Análisis de Costos y Hallazgo Crítico"):
    st.write("El diagrama de caja está ordenado de mayor a menor costo mediano. **Nota Analítica:** Al analizar la dispersión de facturación, descubrimos que la distribución es casi idéntica para todas las enfermedades. Esto comprueba de forma visual la naturaleza sintética del dataset.")

st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: gray; padding: 10px;'>
        <p>👨‍💻 Desarrollado por <b>Tu Nombre Aquí</b> | Proyecto de Análisis de Datos de Extremo a Extremo</p>
        <p>🔗 <a href='https://github.com/tu-usuario' target='_blank'>GitHub</a> | 
        💼 <a href='https://linkedin.com/in/tu-usuario' target='_blank'>LinkedIn</a></p>
    </div>
""", unsafe_allow_html=True)
