import streamlit as st

# Título de la aplicación
st.title('Mi primera aplicación de Streamlit')

# Slider para seleccionar un número
number = st.slider('Selecciona un número', 0, 100, 50)

# Mostrar el número seleccionado
st.write('El número seleccionado es:', number)

