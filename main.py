import os
import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model

# Carpeta de las imágenes de prueba
directorio_pruebas = 'test'


# Verificar si el directorio existe antes de listar archivos
if not os.path.exists(directorio_pruebas):
    st.error(f"El directorio {directorio_pruebas} no existe. Verifica la ruta.")
else:
    # Lista todos los archivos en el directorio de pruebas
    archivos = os.listdir(directorio_pruebas)
    
    # Lista para almacenar las rutas de las imágenes
    rutas_imagenes = []
    
    # Obtener las rutas de las imágenes y guardarlas en la lista
    for archivo in archivos:
        if archivo.endswith('.jpg') or archivo.endswith('.png'):
            imagen_path = os.path.join(directorio_pruebas, archivo)
            rutas_imagenes.append(imagen_path)

    
    # Función para cargar y preprocesar una imagen
    def cargar_y_preprocesar_imagen(ruta_imagen):
        imagen = cv2.imread(ruta_imagen)
        imagen = cv2.resize(imagen, (512, 512))
        imagen = imagen.astype('float32') / 255.0
        imagen = np.expand_dims(imagen, axis=-1)
        imagen = np.expand_dims(imagen, axis=0)
    
        return imagen

    # Cargar el modelo
    modelo = load_model('modelo_eficiente1.keras')
    st.write("Modelo cargado correctamente.")

    # Procesar y predecir para cada imagen
    if rutas_imagenes:
        for ruta_imagen in rutas_imagenes:
            imagen_procesada = cargar_y_preprocesar_imagen(ruta_imagen)
            prediccion = modelo.predict(imagen_procesada)
            st.image(ruta_imagen, caption=f"Predicción: {prediccion}")
    else:
        st.write("No se encontraron imágenes en el directorio especificado.")
