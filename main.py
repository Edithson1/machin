import streamlit as st

col1, col2 = st.columns([2,1])

col1.markdown(" # Bienvenidos a mi app! ")
col1.markdown(" Aquí va algo de información. ")

datos = col2.file_uploader(" Carga aquí tu archivo de datos.csv ")


st.title('Mi primera aplicación de Streamlit')

number = st.slider('Selecciona un número', 0, 100, 50)

st.write('El número seleccionado es:', number)

