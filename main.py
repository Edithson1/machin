import os
import streamlit as st

# Carpeta de las imágenes de prueba
directorio_pruebas = 'https://github.com/Edithson1/machin/tree/main/test'

# Verificar si el directorio existe antes de listar archivos
if not os.path.exists(directorio_pruebas):
    st.error(f"El directorio {directorio_pruebas} no existe. Verifica la ruta.")
else:
    # Lista todos los archivos en el directorio de pruebas
    archivos = os.listdir(directorio_pruebas)
    
    # Mostrar cada imagen en Streamlit
    for archivo in archivos:
        if archivo.endswith('.jpg') or archivo.endswith('.png'):
            imagen_path = os.path.join(directorio_pruebas, archivo)
            st.image(imagen_path, caption=archivo, use_column_width=True)
