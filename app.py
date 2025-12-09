import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Leer los datos del archivo CSV
df = pd.read_csv('vehicles_us.csv')

# Encabezado
st.header("Ánalisis de datos de anuncion de venta de autos")

# Escribir un mensaje en la aplicación
st.write('Selecciona una opción para visualizar el gráfico correspondiente.')

# Checkboxes para seleccionar los gráficos a mostrar
hist_check = st.checkbox('Construir histograma')
disp_check = st.checkbox('Construir gráfico de dispersión')

# Lógica a ejecutar cuando se hace clic en el check de histograma
if hist_check:
    
    # Crear un histograma utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de histograma
    fig = go.Figure(data=[go.Histogram(x=df['odometer'])])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Distribución del Odómetro')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    st.plotly_chart(fig, use_container_width=True)

if disp_check:
    # Crear un scatter plot utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de scatter
    fig_2 = go.Figure(data=[go.Scatter(x=df['odometer'], y=df['price'], mode='markers')])


    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig_2.update_layout(title_text='Distribución del Odómetro')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    st.plotly_chart(fig_2, use_container_width=True)