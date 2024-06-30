import os
from keras import models
import numpy as np
import tensorflow as tf
import sys
from contextlib import contextmanager
import tqdm

# Carpeta de las imágenes de prueba
directorio_pruebas = '/kaggle/working/upch-intro-ml/test/test'

# Función para cargar y preprocesar una imagen
def cargar_y_preprocesar_imagen(ruta_imagen):
    imagen = cv2.imread(ruta_imagen)
    imagen = cv2.resize(imagen, (512, 512))a
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


# Iteramos nuestro Data Frame de ejemplo

for i, fila in tqdm.tqdm(df_samples.iterrows(), desc="Procesando imágenes", unit=" imagen"):
    ruta_imagen = fila['ID']
    img_array = cargar_y_preprocesar_imagen(ruta_imagen)

    with suppress_stdout():
        prediccion = model.predict(img_array)

    if prediccion[0][0] >= 0.5:
        resultado = 1
    else:
        resultado = 0

    nombre_archivo_con_extension = os.path.basename(ruta_imagen)
    nombre_archivo, extension = os.path.splitext(nombre_archivo_con_extension)
    df_samples.at[i, 'ID'] = nombre_archivo
    df_samples.at[i, 'score'] = resultado

