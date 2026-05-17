# Análisis de Vehículos Usados - Sprint 7

Este proyecto es una aplicación web interactiva para el análisis de datos de vehículos usados en Estados Unidos, desarrollada como parte del curso TripleTen (Sprint 7).

## Descripción del Proyecto

La aplicación permite explorar visualmente un dataset de vehículos usados mediante gráficos interactivos. Los usuarios pueden activar diferentes visualizaciones para analizar patrones y relaciones en los datos.

## Funcionalidades

La aplicación web incluye:

- **Histograma del Odómetro**: Visualiza la distribución de millas recorridas por los vehículos
- **Gráfico de Dispersión**: Muestra la relación entre el precio y el año del modelo, con codificación de color según el odómetro
- **Información del Dataset**: Muestra el número de registros y las columnas disponibles

## Visualizaciones Incluidas

1. **Histograma de Odómetro**: Distribución de frecuencias de las millas recorridas
2. **Gráfico de Dispersión (Precio vs Año)**: Relación entre el precio del vehículo y su año de fabricación

## Cómo Ejecutar Localmente

1. Asegúrate de tener Python instalado en tu sistema
2. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecuta la aplicación:
   ```bash
   streamlit run app.py
   ```
4. La aplicación se abrirá automáticamente en tu navegador (usualmente en http://localhost:8501)

## Estructura del Proyecto

```
.
├── README.md
├── app.py
├── vehicles_us.csv
├── requirements.txt
└── notebooks/
    └── EDA.ipynb
```

## Dependencias

- pandas
- plotly
- streamlit

## Dataset

El dataset utilizado contiene información sobre vehículos usados en Estados Unidos, incluyendo características como precio, año del modelo, odómetro, entre otros.

Fuente: [TripleTen Practicum Content](https://practicum-content.s3.us-west-1.amazonaws.com/new-markets/Data_sprint_4_Refactored/vehicles_us.csv)
