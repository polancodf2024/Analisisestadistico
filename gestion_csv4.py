import streamlit as st
import os
from pathlib import Path
import pandas as pd

# Configuración del archivo CSV
CSV_FILE = "registro_analisis.csv"

# Solicitar contraseña al inicio
PASSWORD = "Tt5plco5"
input_password = st.text_input("Ingresa la contraseña para acceder:", type="password")

# Verificar la contraseña
if input_password != PASSWORD:
    st.error("Contraseña incorrecta. No tienes acceso a esta página.")
    st.stop()

# Mostrar el logo del escudo
st.image("escudo_COLOR.jpg", width=150)

# Título de la aplicación
st.title("Gestión de Archivo: registro_analisis.csv")

# Opción para subir el archivo registro_analisis.csv
st.header("Subir el archivo registro_analisis.csv")
uploaded_csv = st.file_uploader("Selecciona el archivo para subir y reemplazar el existente", type=["csv"])

if uploaded_csv is not None:
    try:
        # Guardar el archivo subido temporalmente
        temp_file = "temp_analisis.csv"
        with open(temp_file, "wb") as f:
            f.write(uploaded_csv.getbuffer())

        # Reemplazar el archivo existente usando el comando de Linux cp
        os.system(f"cp {temp_file} {CSV_FILE}")
        st.success("Archivo registro_analisis.csv subido y reemplazado exitosamente.")

        # Mostrar una vista previa del archivo subido
        df = pd.read_csv(CSV_FILE)
        st.dataframe(df)

        # Eliminar el archivo temporal
        os.remove(temp_file)

    except Exception as e:
        st.error("Error al subir el archivo. Por favor, intenta nuevamente.")
        st.error(str(e))

# Opción para descargar el archivo registro_analisis.csv
st.header("Descargar el archivo registro_analisis.csv")

if Path(CSV_FILE).exists():
    try:
        with open(CSV_FILE, "rb") as file:
            st.download_button(
                label="Descargar registro_analisis.csv",
                data=file,
                file_name="registro_analisis.csv",
                mime="text/csv"
            )
        st.success("Archivo listo para descargar.")
    except Exception as e:
        st.error("Error al descargar el archivo.")
        st.error(str(e))
else:
    st.warning("El archivo registro_analisis.csv no existe.")

