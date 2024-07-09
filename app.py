
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

# Título de la aplicación
st.title('Análisis Exploratorio de Datos Interactivo')

# Cargar datos de ejemplo
@st.cache_data
def load_data():
    url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'
    return pd.read_csv(url)

data = load_data()

# Mostrar el dataframe completo
st.header('Datos Completo')
st.dataframe(data)

# Selección dinámica en la barra lateral
st.sidebar.header('Opciones de filtrado')
columnas = data.columns.tolist()

# Filtro dinámico: selección de columna y valor
columna_filtro = st.sidebar.selectbox('Selecciona la columna para filtrar', columnas)
unique_values = data[columna_filtro].unique()
valor_filtrado = st.sidebar.selectbox('Selecciona un valor para filtrar', unique_values)

# Filtrar los datos en función de la selección
data_filtrada = data[data[columna_filtro] == valor_filtrado]

# Mostrar el dataframe filtrado
st.header('Datos Filtrados')
st.dataframe(data_filtrada)

# Gráfico de ejemplo usando matplotlib
st.header('Gráfico de Histograma')
columna_hist = st.sidebar.selectbox('Selecciona la columna para el histograma', columnas)
fig, ax = plt.subplots()
ax.hist(data_filtrada[columna_hist], bins=20)
st.pyplot(fig)

# Gráfico de ejemplo usando plotly
st.header('Gráfico de Dispersión con Plotly')
columna_x = st.sidebar.selectbox('Selecciona la columna para el eje X', columnas)
columna_y = st.sidebar.selectbox('Selecciona la columna para el eje Y', columnas)
fig = px.scatter(data_filtrada, x=columna_x, y=columna_y, color=columna_filtro)
st.plotly_chart(fig)

# Tabla dinámica
st.header('Tabla Dinámica')
pivot_table = pd.pivot_table(data_filtrada, values=columna_y, index=[columna_filtro], aggfunc=np.mean)
st.dataframe(pivot_table)

# Ejecutar la aplicación con el siguiente comando en la terminal:
# streamlit run app.py
