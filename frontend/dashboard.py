import streamlit as st
import pandas as pd
import requests

# Configuración de la página
st.set_page_config(page_title="Dashboard IGM", layout="wide")

st.title("Dashboard IGM: Ingresos, Gastos y Metas")

# --- BARRA LATERAL: FORMULARIO ---
with st.sidebar:
    st.header("Registrar Nueva Meta")
    
    usuario_id = st.number_input("ID de Usuario:", min_value=1, step=1)
    nombre_meta = st.text_input("Nombre de la meta:")
    costo_total = st.number_input("Costo Total ($):", min_value=0.0, format="%.2f")
    
    if st.button("Guardar Meta"):
        # Más adelante aquí pondre el requests.post() para enviar los datos a FastAPI
        st.info(f"Meta '{nombre_meta}' lista para enviarse al backend.")

# --- ÁREA PRINCIPAL ---
st.header("Tus Metas Actuales")

if st.button("🔄 Actualizar Datos"):
    try:
        # 1. Le pedimos los datos al backend (FastAPI)
        respuesta = requests.get("http://127.0.0.1:8000/metas/")
        
        if respuesta.status_code == 200:
            datos_json = respuesta.json()
            
            # 2. Pandas hace su magia: convierte el JSON en un DataFrame
            # Como por ahora el backend solo devuelve un {"status": "..."}, se mete en una lista
            df = pd.DataFrame([datos_json])
            
            # 3. Se muestra la tabla en Streamlit
            st.success("¡Conexión exitosa con FastAPI!")
            st.dataframe(df, use_container_width=True)
            
        else:
            st.error(f"Error en el servidor: Código {respuesta.status_code}")
            
    except requests.exceptions.ConnectionError:
        st.error("No se pudo conectar. ¿Está encendido el servidor de FastAPI en la otra terminal?")
else:
    st.info("Aquí aparecerá la tabla y las gráficas de Pandas en cuanto actualices los datos.")