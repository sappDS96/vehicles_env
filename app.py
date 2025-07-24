import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go


# Cargar el DataFrame corregido
df = pd.read_csv('vehicles_clean.csv')


st.title("Panel de visualización de datos de vehículos")

# crear una casilla de verificación
build_histogram = st.checkbox('Construir un histograma')
if build_histogram:
    # Ecribir un mensaje en la aplicación
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de vehículos.')
    # Crear el histograma usando Plotly.express
    fig = px.histogram(
        df, x='price', title='Distribución de precios de vehiculo')
    # Mostrar el histograma en la aplicación Streamlit
    st.plotly_chart(fig, use_container_width=True)
if st.checkbox('Mostrar gráfico de dispersión Precio vs Odometer'):
    # Escribir un mensaje en la aplicación
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de vehiculos.')
    # Crear el gráfico de dispersión usando Plotle.express
    fig_scatter = px.scatter(df, x='odometer', y='price', color='cylinders')
    # Mostrar el gráfico de dispersión en la aplicación Streamlit
    st.plotly_chart(fig_scatter, use_container_width=True)


# Crear un botón en la aplicación Streamlit
hist_button = st.button('Construir Histograma')
if hist_button:
    # Ecribir un mensaje en la aplicación
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de vehículos.')
    # Crear el histograma usando Plotly.graph_objects
    # Se crea una figura vacia y luego se añade el histograma
    fig = go.Figure(data=[go.Histogram(x=df['type'], nbinsx=20)])
    fig.update_layout(title_text='Distribución de tipo de vehículos',)
    # Mostrar el histograma en la aplicación Streamlit
    st.plotly_chart(fig, use_container_width=True)
# Agrego otro botón que construya un gráfico de dispersión plotly. (Nuevamente, considera utilizar las funciones st.write() y st.plotly_chart()
scatter_button = st.button('Construir Gráfico de Dispersión')
if scatter_button:
    # Ecribir un mensaje en la aplicación
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de vehículos.')
    # Crear el gráfico de dispersión usando Plotly.express
    fig_scatter = px.scatter(df, x='odometer', y='price', color='paint_color',
                             title='Gráfico de Dispersión: Odometer vs Price')
    # Mostrar el gráfico de dispersión en la aplicación Streamlit
    st.plotly_chart(fig_scatter, use_container_width=True)
