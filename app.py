import streamlit as st

# CONFIGURACIÓN GENERAL
st.set_page_config(page_title="LUGA AREQUIPA - Evaluador de Riesgos", layout="centered")

# FONDO DINÁMICO
st.markdown("""
<style>
body {
    background: linear-gradient(-45deg, #1e3c72, #2a5298, #0d324d, #7f5a83);
    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
}
@keyframes gradientBG {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
header, .stApp {
    background-color: transparent;
}
</style>
""", unsafe_allow_html=True)

# LOGO SVG
svg_logo = """
<svg width="220" height="220" viewBox="0 0 220 220" xmlns="http://www.w3.org/2000/svg">
  <style>
    .title { font: bold 20px sans-serif; fill: #ffffff; }
    .subtitle { font: bold 16px sans-serif; fill: #a0d2eb; }
  </style>
  <rect width="100%" height="100%" fill="none"/>
  <g transform="translate(40, 40)">
    <path d="M0 0 L0 120 L30 120 L30 30 L60 30 L60 0 Z" fill="#003366"/>
    <path d="M80 120 L110 60 L140 120 Z" fill="#005B9A"/>
    <rect x="107" y="85" width="6" height="6" fill="#ffffff"/>
    <rect x="114" y="85" width="6" height="6" fill="#ffffff"/>
    <rect x="107" y="92" width="6" height="6" fill="#ffffff"/>
    <rect x="114" y="92" width="6" height="6" fill="#ffffff"/>
  </g>
  <text x="50" y="180" class="title">LUGA AREQUIPA</text>
  <text x="90" y="200" class="subtitle">RISK</text>
</svg>
"""
st.markdown(f'<div style="text-align:center;">{svg_logo}</div>', unsafe_allow_html=True)

# TÍTULO PRINCIPAL
st.title("LUGA AREQUIPA")
st.subheader("Evaluador Inteligente de Riesgos Inmobiliarios")

# FORMULARIO DE DATOS
st.header("🔍 Ingrese los datos del proyecto")
tipo_inmueble = st.selectbox("Tipo de inmueble", ["Departamento", "Casa", "Local comercial"])
distrito = st.selectbox("Distrito de Arequipa", [
    "Cayma", "Yanahuara", "Cerro Colorado", "José Luis Bustamante y Rivero",
    "Hunter", "Alto Selva Alegre", "Miraflores", "Sachaca", "Tiabaya"
])
area = st.number_input("Área construida (m²)", min_value=30, max_value=1000, value=100)

# CALCULAR PRECIO AUTOMÁTICO SEGÚN DISTRITO Y ÁREA
def mostrar_precio_distrital(distrito, area):
    precios_usd = {
        "Cayma": 1100, "Yanahuara": 1050, "Cerro Colorado": 950,
        "José Luis Bustamante y Rivero": 980, "Hunter": 850,
        "Alto Selva Alegre": 800, "Miraflores": 900,
        "Sachaca": 750, "Tiabaya": 600
    }
    tipo_cambio = 3.8
    if distrito in precios_usd:
        usd = precios_usd[distrito]
        pen = round(usd * tipo_cambio, 2)
        total_pen = round(pen * area, 2)
        st.markdown(f"""
        ### 💰 Precio promedio del mercado en **{distrito}**
        - **US$ {usd} / m²**
        - **S/ {pen} / m²**
        - **S/ {total_pen} (Total estimado del proyecto)**
        """)
        return pen, total_pen
    else:
        st.warning("⚠️ No se encontró información de mercado para este distrito.")
        return None, None

precio_m2_pen, precio_total = mostrar_precio_distrital(distrito, area)

etapa = st.selectbox("Etapa del proyecto", ["Diseño", "Preventa", "Construcción", "Entrega"])
experiencia = st.radio("¿El inversionista tiene experiencia previa?", ["Sí", "No"])

# BOTÓN PARA EVALUAR
if st.button("Evaluar Riesgo"):
    puntaje = 0
    if precio_total and precio_total > 800000:
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

    # Opinión profesional
    if riesgo.startswith("BAJO"):
        st.markdown("✅ Buenas condiciones técnicas y alta demanda según expertos.")
    elif riesgo.startswith("MEDIO"):
        st.markdown("⚠️ Revisar condiciones y entorno con más detalle.")
    else:
        st.markdown("🚨 Zona o condiciones técnicas pueden generar riesgo de inversión.")

    st.markdown("> Esta evaluación es referencial. Contacta a **LUGA AREQUIPA** para un análisis completo.")

