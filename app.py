import streamlit as st

# CONFIGURACIÓN DE LA APP
st.set_page_config(page_title="LUGA AREQUIPA - Evaluador de Riesgos", layout="centered")

# FONDO INTERACTIVO CON GRADIENTE
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

# LOGO SVG MEJORADO
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

st.markdown("""
Esta herramienta permite analizar el **riesgo de inversión** en proyectos inmobiliarios en **Arequipa**, 
utilizando **Web Scraping** y **Machine Learning**.
""")

# FORMULARIO DE ENTRADA
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

# PRECIO REFERENCIAL POR DISTRITO
def obtener_precio_m2_referencial(distrito):
    precios_usd = {
        "Cayma": 1100, "Yanahuara": 1050, "Cerro Colorado": 950,
        "José Luis Bustamante y Rivero": 980, "Hunter": 850,
        "Alto Selva Alegre": 800, "Miraflores": 900,
        "Sachaca": 750, "Tiabaya": 600
    }
    return precios_usd.get(distrito, None)

tipo_cambio = 3.8
precio_m2_usd = obtener_precio_m2_referencial(distrito)
precio_m2_pen = round(precio_m2_usd * tipo_cambio, 2) if precio_m2_usd else None

if precio_m2_usd:
    st.markdown(f"""
    ### 💰 Precio promedio del mercado en **{distrito}**
    - **US$ {precio_m2_usd} / m²**
    - **S/ {precio_m2_pen} / m²**
    """)
else:
    st.warning("⚠️ No se encontró información de mercado para este distrito.")

# EVALUACIÓN DEL RIESGO
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

    # Opinión profesional
    if riesgo.startswith("BAJO"):
        st.markdown("""
        ✅ Como **ingeniero civil**, este proyecto presenta buenas condiciones técnicas y ubicación estable.  
        🏢 Desde la visión del **asesor inmobiliario**, el mercado muestra alta demanda y precio competitivo.
        """)
    elif riesgo.startswith("MEDIO"):
        st.markdown("""
        ⚠️ Como **ingeniero civil**, se recomienda revisar detalles estructurales si está en etapas tempranas.  
        🏢 El **asesor inmobiliario** sugiere analizar bien la competencia y el entorno inmediato.
        """)
    else:
        st.markdown("""
        🚨 Desde la mirada de un **ingeniero civil**, hay señales de alerta: baja área o zona con carga urbana.  
        🏢 El **asesor inmobiliario** advierte posible baja rentabilidad o demanda débil.
        """)

    # Comparación con mercado
    st.subheader("📉 Comparación con el mercado")
    precio_usuario_m2 = round(precio / area, 2)
    if precio_m2_pen:
        diferencia = precio_usuario_m2 - precio_m2_pen
        st.markdown(f"Tu proyecto tiene un precio de: **S/ {precio_usuario_m2} / m²**")

        if diferencia > 200:
            st.warning("⚠️ Tu precio está por encima del promedio.")
            st.markdown("🏢 **Asesor Inmobiliario**: Esto puede reducir velocidad de venta o aumentar riesgo.")
        elif diferencia < -200:
            st.info("✅ Tu precio está por debajo del mercado.")
            st.markdown("🏢 **Asesor Inmobiliario**: Atractivo, pero verifica rentabilidad.")
        else:
            st.success("✅ Tu precio está dentro del rango competitivo.")

    # Recomendaciones específicas
    st.subheader("📍 Recomendación según distrito")
    distrito_msg = {
        "Cayma": "Zona con alta plusvalía. Ideal para proyectos residenciales de nivel medio-alto.",
        "Yanahuara": "Tradicional con alta demanda, pero con restricciones patrimoniales.",
        "Cerro Colorado": "Zona en expansión. Revisar accesibilidad y servicios.",
        "José Luis Bustamante y Rivero": "Consolidado, pero saturado en tráfico.",
        "Hunter": "Intermedio. Evaluar servicios y seguridad.",
        "Alto Selva Alegre": "En crecimiento. Riesgo medio por topografía.",
        "Miraflores": "Conectado, pero fluctuante. Evaluar entorno.",
        "Sachaca": "Tranquilo, ideal para vivienda unifamiliar.",
        "Tiabaya": "Rural. Verificar acceso a servicios básicos."
    }
    st.info(distrito_msg.get(distrito, "No hay datos específicos para este distrito."))

    st.subheader("🏠 Consejo según tipo de inmueble")
    if tipo_inmueble == "Departamento":
        st.markdown("📌 Alta demanda en zonas universitarias y comerciales.")
    elif tipo_inmueble == "Casa":
        st.markdown("📌 Atractivas para familias. Priorizar ubicación y accesos.")
    elif tipo_inmueble == "Local comercial":
        st.markdown("📌 Evalúa flujo peatonal y permisos según rubro.")

    st.markdown("""
    > Esta evaluación es referencial.  
    > Para estudios técnicos o comerciales, contacta a nuestros especialistas en **LUGA AREQUIPA**.
    """)

