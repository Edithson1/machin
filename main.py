import os
import requests
import gdown
from PIL import Image
from io import BytesIO
from tensorflow.keras.models import load_model
import pandas as pd
import numpy as np
import cv2
from contextlib import contextmanager
import tqdm
import streamlit as st


# URL base de la API de GitHub
api_url = 'https://api.github.com/repos/Edithson1/machin/contents/test'

# Directorio local para almacenar las imágenes descargadas
local_dir = 'imagenes_descargadas'
os.makedirs(local_dir, exist_ok=True)

# Obtener la lista de archivos del repositorio
response = requests.get(api_url)
files = response.json()

# Mostrar la respuesta de la API en Streamlit para depuración
st.write("Respuesta de la API de GitHub:")
st.write(files)

# Comprobar si la respuesta es una lista
if isinstance(files, list):
    # Filtrar solo las imágenes (asumiendo que las imágenes tienen extensiones conocidas)
    image_files = [file for file in files if 'name' in file and file['name'].lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]
else:
    st.error("La respuesta de la API no es una lista. Verifique la URL y los permisos del repositorio.")

# Descargar y guardar las imágenes
for file in image_files:
    image_url = file['download_url']
    image_name = file['name']
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    img.save(os.path.join(local_dir, image_name))

# Cargar el modelo desde Google Drive (debe estar descargado previamente como se mostró antes)
model = load_model('model.keras')

# Carpeta de las imágenes de prueba
directorio_pruebas = local_dir

