import streamlit as st

# CONFIGURACIÓN DE LA APP
st.set_page_config(page_title="LUGA AREQUIPA - Evaluador de Riesgos", layout="centered")

# LOGO SVG (insertado como HTML)
svg_logo = """
<svg width="300" height="300" viewBox="0 0 300 300" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="#f5f5f5"/>
  <g transform="translate(40, 60)">
    <polygon points="0,0 0,160 30,160 30,30 60,30 60,0" fill="#003366"/>
    <polygon points="70,0 70,160 100,160 100,60 130,60 130,0" fill="#005B9A"/>
    <rect x="85" y="90" width="10" height="20" fill="#f5f5f5"/>
  </g>
  <g transform="translate(160, 100)" font-family="Arial, sans-serif">
    <text x="0" y="0" font-size="24" fill="#003366" font-weight="bold">LUGA</text>
    <text x="0" y="30" font-size="24" fill="#003366" font-weight="bold">AREQUIPA</text>
    <text x="0" y="60" font-size="20" fill="#5aa5d6">RISK</text>
  </g>
</svg>
"""
st.markdown(svg_logo, unsafe_allow_html=True)

# TÍTULO
st.title("LUGA AREQUIPA")
st.subheader("Evaluador Inteligente de Riesgos Inmobiliarios")

# INTRODUCCIÓN
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

    # RESULTADO PRINCIPAL
    st.header("📊 Resultado de Evaluación")
    st.success(f"El **riesgo estimado** del proyecto es: **{riesgo}**")

    # MENSAJE SEGÚN RIESGO
    if riesgo.startswith("BAJO"):
        st.markdown("""
        ✅ Como **ingeniero civil**, este proyecto presenta buenas condiciones técnicas y ubicación estable.  
        🏢 Desde la visión del **asesor inmobiliario**, el mercado muestra alta demanda en esta zona y el precio es competitivo.
        """)
    elif riesgo.startswith("MEDIO"):
        st.markdown("""
        ⚠️ Como **ingeniero civil**, se recomienda revisar detalles estructurales o el estado de avance si está en etapas tempranas.  
        🏢 El **asesor inmobiliario** sugiere analizar bien la oferta en la zona: hay competencia y variación de precios.
        """)
    else:
        st.markdown("""
        🚨 Desde la mirada de un **ingeniero civil**, hay señales de alerta: baja área construida o zona con alta carga urbana.  
        🏢 El **asesor inmobiliario** advierte posible baja rentabilidad o demanda débil. Evaluar cambios antes de invertir.
        """)

    # RECOMENDACIONES POR DISTRITO
    st.subheader("📍 Recomendación según distrito")
    distrito_msg = {
        "Cayma": "Zona con alta plusvalía y buena infraestructura. Ideal para proyectos residenciales de nivel medio-alto.",
        "Yanahuara": "Ubicación tradicional con alta demanda, pero con restricciones urbanas en zonas patrimoniales.",
        "Cerro Colorado": "Zona en expansión, revisar accesibilidad, servicios básicos y sobreoferta en preventa.",
        "José Luis Bustamante y Rivero": "Área comercial y residencial consolidada. Verificar densificación y saturación vial.",
        "Hunter": "Zona intermedia. Requiere evaluar servicios urbanos y seguridad.",
        "Alto Selva Alegre": "Área en crecimiento mixto. Riesgo medio-alto por acceso irregular y topografía complicada.",
        "Miraflores": "Buena conexión vial pero con fluctuaciones de demanda. Evaluar entorno inmediato.",
        "Sachaca": "Zona tranquila y de crecimiento lento. Ideal para vivienda unifamiliar o proyectos ecológicos.",
        "Tiabaya": "Rural y dispersa. Verificar normativas de uso de suelo y acceso a redes de agua/luz."
    }
    st.info(distrito_msg.get(distrito, "Información no disponible para este distrito."))

    # RECOMENDACIONES SEGÚN TIPO DE INMUEBLE
    st.subheader("🏠 Consejo según tipo de inmueble")
    if tipo_inmueble == "Departamento":
        st.markdown("📌 Los departamentos en Arequipa tienen alta demanda en zonas con universidades, centros de trabajo y comercio.")
    elif tipo_inmueble == "Casa":
        st.markdown("📌 Las casas son atractivas para familias, pero deben tener buena ubicación y acceso a transporte público.")
    elif tipo_inmueble == "Local comercial":
        st.markdown("📌 Evalúa flujo peatonal y vehicular, así como permisos municipales según giro de negocio.")

    # NOTA FINAL
    st.markdown("""
    > Esta evaluación es una orientación inicial.  
    > Para un análisis técnico o comercial más profundo, contacta a los especialistas de **LUGA AREQUIPA**.
    """)
