import streamlit as st

col1, col2 = st.columns([2,1])

col1.markdown(" # Bienvenidos a mi app! ")
col1.markdown(" Aquí va algo de información. ")

datos = col2.file_uploader(" Carga aquí tu archivo de datos.csv ")

foto = col2.camera_input(" Tomar foto ")
col2.success(" Tu foto se cargo correctamente! ")

# streamlit run app.py
# Título de la aplicación
st.title('Mi primera aplicación de Streamlit')

# Slider para seleccionar un número
number = st.slider('Selecciona un número', 0, 100, 50)

# Mostrar el número seleccionado
st.write('El número seleccionado es:', number)

