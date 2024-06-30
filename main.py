import os
import streamlit as st

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

    
    # Imprimir las rutas de las imágenes
    if rutas_imagenes:
        st.write("Rutas de las imágenes:")
        for ruta in rutas_imagenes:
            st.write(ruta)
    else:
        st.write("No se encontraron imágenes en el directorio especificado.")
