import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import sys
import os
# 📌 Agregar la carpeta "scripts" al path para que Streamlit encuentre los módulos
sys.path.append(os.path.abspath("scripts"))
from graphs import Graficos
from hall_plot import Hall_Plot

# 🎯 Título de la aplicación 
st.title("📊 Hall Plot - Análisis de Inyección")
st.subheader("App desarrollada por Jesús Pacheco")

st.write("""
El **Gráfico de Hall** es una herramienta utilizada en la ingeniería de yacimientos para evaluar el comportamiento de los pozos inyectores en sistemas de waterflooding. 
Este gráfico muestra la relación entre la presión acumulada de inyección y el volumen de agua inyectado, lo que permite detectar cambios en la resistencia al flujo. 
Un comportamiento lineal en el gráfico indica condiciones de inyección estables, mientras que desviaciones en la pendiente pueden sugerir taponamiento del pozo, daño a la formación o restricciones en el sistema de inyección.
Además, la **derivada del Gráfico de Hall** ayuda a identificar cambios en la resistencia al flujo con mayor sensibilidad, permitiendo una detección más temprana de problemas operacionales en el inyector.
""")


# 📌 Carga de archivos
st.markdown("### 📂 Cargar Archivos")
file = st.sidebar.file_uploader("🔹 Carga el CSV con datos de inyección", type=["csv"])
file_pmp = st.sidebar.file_uploader("🔹 Carga el CSV con datos de PMP y presión de yacimiento", type=["csv"])

if file and file_pmp:
    st.success("✅ Archivos cargados correctamente")

    # 📌 Cargar data
    df = pd.read_csv(file)
    estatica = pd.read_csv(file_pmp)

    # 📌 Convertir columna fecha a formato datetime
    df['FECHA'] = pd.to_datetime(df['FECHA'])

    # 📌 Lista de inyectores
    inyector_list = df['POZO'].unique().tolist()

    # 📌 Selector dinámico para inyector
    st.sidebar.header("📊 Parámetros del Inyector")
    inyector_seleccionado = st.sidebar.selectbox("🔍 Seleccione un inyector", inyector_list)

    # 📌 Filtrar el DataFrame por el inyector seleccionado
    df_filter = df[df['POZO'] == inyector_seleccionado].copy()
    df_filter['FECHA_FORMAT'] = df_filter['FECHA'].dt.strftime("%d-%m-%Y")

    # 📌 Filtrar la data estática
    estatica_filter = estatica[estatica['POZO'] == inyector_seleccionado]
    
    # 📌 Entradas de presión en la barra lateral (evita error si no hay datos en estatica_filter)
    if not estatica_filter.empty:
        py = float(estatica_filter.iloc[0, 2])
        pmp = float(estatica_filter.iloc[0, 1])
    else:
        py, pmp = 0, 0  # Valores por defecto si no hay datos

    col1, col2 = st.sidebar.columns(2)
    with col1:
        st.number_input("Presión de Yacimiento", py, disabled=True)
    with col2:
        st.number_input("PMP", pmp, disabled=True)

    # 📌 Generar gráfico principal
    st.write(f"### Gráfico para el inyector **{inyector_seleccionado}**")

    # 📌 Generar Hall Plot
    hall_df = Hall_Plot(df=df_filter, estatica=estatica_filter, py=py, pmp=pmp).data()
    graficos = Graficos(hall_df)

    # 📌 Crear y mostrar el gráfico principal
    fig = graficos.grafico_2()
    fig.update_layout(
        xaxis=dict(title="Acumulado Wi"),
        yaxis=dict(title="Variable Y"),
    )
    st.plotly_chart(fig, use_container_width=True)

    # 📌 Mostrar tabla de datos en un `st.expander`
    with st.expander("📄 Ver Datos del Inyector"):
        st.dataframe(hall_df[['POZO', 'FECHA', 'AGUA_INYECTADA', 'PIA', 'acumulado_wi', 'acumulado_delta_presion', 'derivada_']].reset_index(drop=True))

    # 📌 Botón para descargar los datos si el DataFrame no está vacío
    if not hall_df.empty:
        csv = hall_df[['POZO', 'FECHA', 'AGUA_INYECTADA', 'PIA', 'acumulado_wi', 'derivada_', 'acumulado_delta_presion']].to_csv(index=False).encode("utf-8")
        st.download_button(
            label="📥 Descargar Datos en CSV",
            data=csv,
            file_name=f"{inyector_seleccionado}_datos.csv",
            mime="text/csv"
        )
    else:
        st.warning("⚠️ No hay datos disponibles para descargar.")


  


