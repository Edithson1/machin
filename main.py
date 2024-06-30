import streamlit as st
import os
from PIL import Image

# Configurar directorio de almacenamiento
DIRECTORIO_ALMACENAMIENTO = 'imagenes_subidas'

# Crear el directorio si no existe
if not os.path.exists(DIRECTORIO_ALMACENAMIENTO):
    os.makedirs(DIRECTORIO_ALMACENAMIENTO)

# Layout de Streamlit
col1, col2 = st.columns([2, 1])

col1.markdown("# Bienvenidos a mi app!")
col1.markdown("Aquí va algo de información.")

# Cargar archivos
archivos_subidos = col2.file_uploader("Carga aquí tus archivos", accept_multiple_files=True)

if archivos_subidos:
    for archivo in archivos_subidos:
        try:
            # Leer imagen
            img = Image.open(archivo)
            
            # Mostrar imagen
            col1.image(img, caption=archivo.name)
            
            # Guardar imagen
            ruta_archivo = os.path.join(DIRECTORIO_ALMACENAMIENTO, archivo.name)
            
            # Verificar si el archivo ya existe y cambiar el nombre si es necesario
            base, extension = os.path.splitext(ruta_archivo)
            counter = 1
            while os.path.exists(ruta_archivo):
                ruta_archivo = f"{base}_{counter}{extension}"
                counter += 1

            img.save(ruta_archivo)
        except Exception as e:
            st.error(f"Ocurrió un error al procesar el archivo {archivo.name}: {e}")
            
    st.success("Archivos subidos y almacenados con éxito.")
