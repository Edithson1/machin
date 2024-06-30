import os
import requests
from PIL import Image
from io import BytesIO
from tensorflow.keras.models import load_model
import streamlit as st

# URL base de la API de GitHub
api_url = 'https://api.github.com/repos/Edithson1/machin/contents/test'

# Directorio local para almacenar las imágenes descargadas
local_dir = 'imagenes_descargadas'
os.makedirs(local_dir, exist_ok=True)

# Obtener la lista de archivos del repositorio
response = requests.get(api_url)

# Comprobar si la respuesta fue exitosa (código de estado 200)
if response.status_code == 200:
    files = response.json()
    
    # Mostrar la respuesta de la API en Streamlit para depuración
    st.write("Respuesta de la API de GitHub:")
    st.write(files)

    # Comprobar si la respuesta es una lista
    if isinstance(files, list):
        # Filtrar solo las imágenes (asumiendo que las imágenes tienen extensiones conocidas)
        image_files = [file for file in files if 'name' in file and file['name'].lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]
        
        # Descargar y guardar las imágenes
        for file in image_files:
            image_url = file['download_url']
            image_name = file['name']
            response = requests.get(image_url)
            img = Image.open(BytesIO(response.content))
            img.save(os.path.join(local_dir, image_name))
            
        # Cargar el modelo desde un archivo local (asegúrate de que el modelo esté en el mismo directorio)
        model_path = 'model.keras'
        if os.path.exists(model_path):
            model = load_model(model_path)
            st.success("Modelo cargado correctamente.")
        else:
            st.error(f"No se encontró el archivo del modelo en '{model_path}'.")
            
    else:
        st.error("La respuesta de la API no es una lista. Verifique la URL y los permisos del repositorio.")
else:
    st.error(f"Error al obtener archivos del repositorio. Código de estado: {response.status_code}")

# Mostrar nombres de imágenes descargadas en Streamlit dentro de expanders
if os.path.exists(local_dir):
    st.write("Imágenes descargadas:")
    for image_file in image_files:
        image_path = os.path.join(local_dir, image_file)
        with st.expander(f"Ver nombre de archivo: {image_file}"):
            st.write(f"Nombre del archivo: {image_file}")
