import os
import requests
from PIL import Image
from io import BytesIO
import numpy as np
import cv2
from tensorflow.keras.models import load_model
import pandas as pd
import streamlit as st

# URL base de la API de GitHub
api_url = 'https://api.github.com/repos/Edithson1/machin/contents/test'

# Directorio local para almacenar las imágenes descargadas
local_dir = 'imagenes_descargadas'
os.makedirs(local_dir, exist_ok=True)

try:
    # Obtener la lista de archivos del repositorio
    response = requests.get(api_url)
    response.raise_for_status()  # Lanza una excepción para errores HTTP
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

    # Preparar estructura para almacenar resultados
    resultados = []

    # Procesar cada imagen descargada
    for filename in os.listdir(local_dir):
        ruta_imagen = os.path.join(local_dir, filename)
        
        # Preprocesamiento de la imagen si es necesario (ajústalo según tus necesidades)
        imagen = cv2.imread(ruta_imagen)
        imagen = cv2.resize(imagen, (512, 512))
        imagen = imagen.astype('float32') / 255.0
        imagen = np.expand_dims(imagen, axis=0)
        
        # Realizar la predicción con el modelo cargado
        prediccion = model.predict(imagen)
        
        # Ejemplo de cómo interpretar la predicción (ajústalo según tu modelo)
        if prediccion[0][0] >= 0.5:
            resultado = 1
        else:
            resultado = 0
        
        # Guardar resultados
        resultados.append({
            'imagen': filename,
            'prediccion': resultado
        })

    # Mostrar los resultados en Streamlit
    st.write("Resultados de las predicciones:")
    df_resultados = pd.DataFrame(resultados)
    st.dataframe(df_resultados)

except requests.exceptions.RequestException as e:
    st.error(f"Error al realizar la solicitud a la API de GitHub: {str(e)}")
except Exception as e:
    st.error(f"Error inesperado: {str(e)}")

