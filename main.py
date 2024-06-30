import os
import cv2
import numpy as np
import pandas as pd
import tensorflow as tf
from keras.models import load_model
from contextlib import contextmanager
import tqdm

# Definir directorio de imágenes de prueba
directorio_pruebas = '/kaggle/working/upch-intro-ml/test/test'

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

# Iterar sobre el DataFrame de ejemplo (asumiendo que df_samples está definido previamente)
for i, fila in tqdm.tqdm(df_samples.iterrows(), desc="Procesando imágenes", unit="imagen"):
    ruta_imagen = fila['ID']
    img_array = cargar_y_preprocesar_imagen(ruta_imagen)

    with suppress_stdout():
        prediccion = model.predict(img_array)

    if prediccion[0][0] >= 0.5:
        resultado = 1
    else:
        resultado = 0

    # Actualizar el DataFrame con el resultado
    nombre_archivo_con_extension = os.path.basename(ruta_imagen)
    nombre_archivo, extension = os.path.splitext(nombre_archivo_con_extension)
    df_samples.at[i, 'ID'] = nombre_archivo
    df_samples.at[i, 'score'] = resultado

# Guardar el DataFrame actualizado si es necesario
# df_samples.to_csv('resultados.csv', index=False)

