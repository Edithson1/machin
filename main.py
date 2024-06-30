import os
from keras import models
import numpy as np
import tensorflow as tf
import sys
from contextlib import contextmanager
import tqdm


# Carpeta de las imágenes de prueba
directorio_pruebas = '/kaggle/working/upch-intro-ml/test/test'

# Lista todos los archivos en el directorio de pruebas
archivos = os.listdir(directorio_pruebas)

# Mostrar cada imagen en Streamlit
for archivo in archivos:
    if archivo.endswith('.jpg') or archivo.endswith('.png'):
        imagen_path = os.path.join(directorio_pruebas, archivo)
        st.image(imagen_path, caption=archivo, use_column_width=True)
