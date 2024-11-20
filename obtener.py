import streamlit as st
import os
from pathlib import Path

# Configuración general
BASE_DIR = Path("analisis_matematico")  # Carpeta base
PASSWORD = "Tt5plco5"

# Solicitar contraseña al inicio
input_password = st.text_input("Ingresa la contraseña para acceder:", type="password")

if input_password != PASSWORD:
    st.error("Contraseña incorrecta. No tienes acceso a esta página.")
    st.stop()

# Mostrar el logo
st.image("escudo_COLOR.jpg", width=150)

# Título de la aplicación
st.title("Información de Archivos y Directorios")

# Mostrar el path actual
st.header("Información del Path Actual")
current_path = os.getcwd()
st.write("El directorio de trabajo actual es:", current_path)

# Usar pathlib para obtener el path absoluto del archivo
current_file_path = Path(__file__).resolve()
st.write("El archivo ejecutado está ubicado en:", current_file_path)

# Mostrar contenido del directorio actual
st.header("Contenido del Directorio Actual")
files_and_dirs = os.listdir(current_path)
st.write(files_and_dirs)

# Selección de carpeta
st.header("Seleccionar Carpeta")
if BASE_DIR.exists() and BASE_DIR.is_dir():
    carpetas = [str(carpeta) for carpeta in BASE_DIR.iterdir() if carpeta.is_dir()]
    if carpetas:
        carpeta_seleccionada = st.selectbox("Selecciona una carpeta:", carpetas)
        st.write("Carpeta seleccionada:", carpeta_seleccionada)
    else:
        st.warning("No hay carpetas disponibles en la ruta especificada.")
else:
    st.error(f"La carpeta base '{BASE_DIR}' no existe.")
    st.stop()

# Selección de archivo dentro de la carpeta seleccionada
st.header("Seleccionar Archivo")
carpeta_path = Path(carpeta_seleccionada)
archivos = [
    archivo.name for archivo in carpeta_path.iterdir() if archivo.is_file()
]
if archivos:
    archivo_seleccionado = st.selectbox("Selecciona un archivo:", archivos)
    archivo_path = carpeta_path / archivo_seleccionado
    st.write("Archivo seleccionado:", archivo_path)
else:
    st.warning("No hay archivos disponibles en la carpeta seleccionada.")

# Descargar el archivo seleccionado
if archivo_path and archivo_path.exists():
    st.header("Descargar Archivo")
    try:
        with open(archivo_path, "rb") as file:
            st.download_button(
                label=f"Descargar {archivo_seleccionado}",
                data=file,
                file_name=archivo_seleccionado,
                mime="application/octet-stream"
            )
    except Exception as e:
        st.error(f"Error al preparar el archivo para la descarga: {str(e)}")

