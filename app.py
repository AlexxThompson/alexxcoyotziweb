import streamlit as st
import pandas as pd

# Cargar datos
@st.cache
def cargar_datos():
    return pd.read_csv('cars_data.csv')

data = cargar_datos()

st.title("Concesionario de Coches")
st.sidebar.header("Filtros de búsqueda")

# Filtros
marca = st.sidebar.selectbox("Marca", data["Marca"].unique())
modelo = st.sidebar.selectbox("Modelo", data[data["Marca"] == marca]["Modelo"].unique())
año = st.sidebar.selectbox("Año", sorted(data["Año"].unique(), reverse=True))

# Filtrar coches según selección
filtered_data = data[(data["Marca"] == marca) & (data["Modelo"] == modelo) & (data["Año"] == año)]

if not filtered_data.empty:
    for index, row in filtered_data.iterrows():
        st.image(row["Imagen"], width=300)
        st.subheader(f'{row["Marca"]} {row["Modelo"]} ({row["Año"]})')
        st.write(f"**Precio**: ${row['Precio']}")
        st.button(f"Consultar sobre {row['Marca']} {row['Modelo']}")
else:
    st.write("No se encontraron coches con los criterios seleccionados.")

