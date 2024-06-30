import os
import requests
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

# Filtrar solo las imágenes (asumiendo que las imágenes tienen extensiones conocidas)
image_files = [file for file in files if file['name'].lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]

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

# Función para cargar y preprocesar una imagen
def cargar_y_preprocesar_imagen(ruta_imagen):
    imagen = cv2.imread(ruta_imagen)
    imagen = cv2.resize(imagen, (512, 512))
    imagen = imagen.astype('float32') / 255.0
    imagen = np.expand_dims(imagen, axis=-1)
    imagen = np.expand_dims(imagen, axis=0)
    return imagen

# Context manager para suprimir la salida estándar
@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:
            yield
        finally:
            sys.stdout = old_stdout

