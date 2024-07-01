import os
import streamlit as st
import cv2
import numpy as np
import pandas as pd
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

    # Dataframe para almacenar nombres de imágenes y predicciones
    df_resultados = pd.DataFrame(columns=['ID', 'score'])
    
    # Procesar y predecir para cada imagen
    if rutas_imagenes:
        for ruta_imagen in rutas_imagenes:
            nombre_imagen = os.path.basename(ruta_imagen)
            imagen_procesada = cargar_y_preprocesar_imagen(ruta_imagen)
            prediccion = modelo.predict(imagen_procesada)
            if prediccion[0][0] >= 0.5:
                prediccion[0][0] = 1
            else:
                prediccion[0][0] = 0
            df_resultados = df_resultados.append({'ID': nombre_imagen, 'score': prediccion[0][0]}, ignore_index=True)
        st.write("Resultados de las predicciones:")
        st.dataframe(df_resultados)
    else:
        st.write("No se encontraron imágenes en el directorio especificado.")
