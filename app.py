import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Cargar el dataset
@st.cache_data
def load_data():
    df = pd.read_csv('vehicles_us.csv')
    return df

df = load_data()

# Título de la aplicación
st.header('Análisis de Vehículos Usados en Estados Unidos')

st.write('Este dashboard permite explorar visualmente el dataset de vehículos usados.')

# Checkbox para mostrar histograma del odómetro
show_histogram = st.checkbox('Mostrar Histograma del Odómetro')

if show_histogram:
    fig_histogram = go.Figure(data=[go.Histogram(x=df['odometer'])])
    fig_histogram.update_layout(
        title='Distribución del Odómetro',
        xaxis_title='Odómetro (millas)',
        yaxis_title='Frecuencia'
    )
    st.plotly_chart(fig_histogram, use_container_width=True)

# Checkbox para mostrar gráfico de dispersión
show_scatter = st.checkbox('Mostrar Gráfico de Dispersión: Precio vs Año del Modelo')

if show_scatter:
    fig_scatter = go.Figure(data=[go.Scatter(
        x=df['model_year'],
        y=df['price'],
        mode='markers',
        marker=dict(
            size=5,
            color=df['odometer'],
            colorscale='Viridis',
            showscale=True,
            colorbar=dict(title='Odómetro')
        )
    )])
    fig_scatter.update_layout(
        title='Precio vs Año del Modelo',
        xaxis_title='Año del Modelo',
        yaxis_title='Precio (USD)'
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

# Información adicional
st.subheader('Información del Dataset')
st.write(f'Número de registros: {len(df)}')
st.write(f'Columnas: {", ".join(df.columns.tolist())}')
