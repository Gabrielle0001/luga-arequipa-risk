import streamlit as st

st.set_page_config(page_title="LUGA AREQUIPA - Evaluador de Riesgos", layout="centered")
st.image("https://i.imgur.com/qSx0YO0.png", width=200)
st.title("LUGA AREQUIPA")
st.subheader("Evaluador Inteligente de Riesgos Inmobiliarios")

st.markdown("""
Esta herramienta permite analizar el **riesgo de inversión** en proyectos inmobiliarios en **Arequipa**, 
utilizando **Web Scraping** y **Machine Learning**.
""")

st.header("🔍 Ingrese los datos del proyecto")
tipo_inmueble = st.selectbox("Tipo de inmueble", ["Departamento", "Casa", "Local comercial"])
distrito = st.selectbox("Distrito de Arequipa", [
    "Cayma", "Yanahuara", "Cerro Colorado", "José Luis Bustamante y Rivero",
    "Hunter", "Alto Selva Alegre", "Miraflores", "Sachaca", "Tiabaya"
])
area = st.number_input("Área construida (m²)", min_value=30, max_value=1000, value=100)
precio = st.number_input("Precio del proyecto (S/)", min_value=50000, max_value=2000000, value=300000)
etapa = st.selectbox("Etapa del proyecto", ["Diseño", "Preventa", "Construcción", "Entrega"])
experiencia = st.radio("¿El inversionista tiene experiencia previa?", ["Sí", "No"])

if st.button("Evaluar Riesgo"):
    puntaje = 0
    if precio > 800000:
        puntaje += 1
    if area < 80:
        puntaje += 1
    if distrito in ["Cerro Colorado", "Hunter", "Alto Selva Alegre"]:
        puntaje += 1
    if etapa in ["Diseño", "Preventa"]:
        puntaje += 1
    if experiencia == "No":
        puntaje += 1

    if puntaje <= 1:
        riesgo = "BAJO 🟢"
    elif puntaje <= 3:
        riesgo = "MEDIO 🟡"
    else:
        riesgo = "ALTO 🔴"

    st.header("📊 Resultado de Evaluación")
    st.success(f"El **riesgo estimado** del proyecto es: **{riesgo}**")
    st.markdown("""
    > Esta es una evaluación referencial basada en patrones del mercado inmobiliario de Arequipa.  
    > Para un estudio técnico más profundo, comunícate con nuestro equipo en **LUGA AREQUIPA**.
    """)
