import streamlit as st
import pandas as pd
import plotly.express as px

# ——————————————————————————————————————————————————————————
# 1) Título y encabezado
st.title("Análisis de Anuncios de Coches (US)")
st.header("Explora Tus Datos de Vehículos de Forma Interactiva")

# ——————————————————————————————————————————————————————————
# 2) Cargo datos
df = pd.read_csv("vehicles_us.csv")

# ——————————————————————————————————————————————————————————
# 3) Widgets de filtrado en la barra lateral

# Rango de años
min_year = int(df["model_year"].min())
max_year = int(df["model_year"].max())
year_range = st.sidebar.slider(
    "Selecciona el rango de año",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year)
)

# Condición del vehículo
condiciones = df["condition"].unique().tolist()
condiciones_seleccionadas = st.sidebar.multiselect(
    "Condición del vehículo",
    options=condiciones,
    default=condiciones
)

# Rango de precio
min_price = int(df["price"].min())
max_price = int(df["price"].max())
price_range = st.sidebar.slider(
    "Selecciona rango de precio",
    min_value=min_price,
    max_value=max_price,
    value=(min_price, max_price),
    step=500
)

# ——————————————————————————————————————————————————————————
# 4) Aplico todos los filtros al DataFrame
df_filtrado = df[
    (df["model_year"].between(year_range[0], year_range[1])) &
    (df["condition"].isin(condiciones_seleccionadas)) &         # ← usa aquí condiciones_seleccionadas
    (df["price"].between(price_range[0], price_range[1]))
]

# ——————————————————————————————————————————————————————————
# 5) Métricas rápidas
st.sidebar.markdown("## Métricas rápidas")
st.sidebar.metric("Total de anuncios", len(df_filtrado))
st.sidebar.metric("Precio promedio", f"${df_filtrado['price'].mean():,.0f}")
st.sidebar.metric("Kilometraje promedio", f"{df_filtrado['odometer'].mean():,.0f} km")

# ——————————————————————————————————————————————————————————
# 6) Vista previa de datos filtrados
st.subheader("Vista previa de datos filtrados")
st.dataframe(df_filtrado.head())

# ——————————————————————————————————————————————————————————
# 7) Gráfico de dispersión por defecto
st.subheader("Precio vs. Año de Fabricación")
scatter1 = px.scatter(
    df_filtrado,
    x="model_year",
    y="price",
    color="condition",
    title=f"Precio vs. Año ({year_range[0]}–{year_range[1]})",
    hover_data=["model"]
)
st.plotly_chart(scatter1)

# ——————————————————————————————————————————————————————————
# 8) Botón: histograma de precios
if st.button("Mostrar histograma de precios"):
    st.write("### Histograma de precios dinámico")
    hist = px.histogram(
        df_filtrado,
        x="price",
        nbins=30,
        title="Distribución de precios tras filtro"
    )
    st.plotly_chart(hist)

# ——————————————————————————————————————————————————————————
# 9) Botón: scatter Precio vs. Kilometraje
if st.button("Mostrar scatter Precio vs. Kilometraje"):
    st.write("### Scatter: Precio vs. Kilometraje")
    scatter2 = px.scatter(
        df_filtrado,
        x="odometer",
        y="price",
        color="condition",
        title="Precio vs. Kilometraje",
        hover_data=["model", "model_year"]
    )
    st.plotly_chart(scatter2)
    







