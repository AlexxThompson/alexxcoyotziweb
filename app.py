import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configuración de la página
st.set_page_config(page_title="Sneaker Shop", page_icon=":athletic_shoe:", layout="wide")

# Título y subtítulo
st.title("Sneaker Shop - Tienda de Zapatillas Deportivas")
st.subheader("Encuentra los mejores modelos de sneakers aquí")

# Sidebar para navegación
st.sidebar.title("Navegación")
st.sidebar.write("Explora nuestras categorías y novedades")

# Imagen de introducción
st.image("https://www.example.com/sneakers-shop.jpg", use_container_width=True)

st.write("""
    Bienvenido a **Sneaker Shop**, tu tienda favorita para comprar las mejores zapatillas deportivas. 
    Ofrecemos una amplia variedad de modelos y marcas que se ajustan a todos los estilos. 
    ¡Explora nuestras categorías y encuentra el par perfecto para ti!
""")

# Sección de categorías con columnas
st.header("Categorías de Sneakers")
col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://www.example.com/basketball-sneakers.jpg", caption="Zapatillas de Basketball", use_container_width=True)
    st.button("Ver Zapatillas de Basketball")

with col2:
    st.image("https://www.example.com/running-sneakers.jpg", caption="Zapatillas de Running", use_container_width=True)
    st.button("Ver Zapatillas de Running")

with col3:
    st.image("https://www.example.com/casual-sneakers.jpg", caption="Zapatillas Casual", use_container_width=True)
    st.button("Ver Zapatillas Casual")

# Datos de ejemplo (puedes usar datos reales aquí)
st.header("Ventas de Sneakers por Modelo")
data = {
    'Modelo': ['Air Jordan 1', 'Nike Air Max 90', 'Adidas Ultraboost', 'Puma RS-X', 'Reebok Classic'],
    'Ventas (Unidades)': [230, 180, 150, 100, 90]
}

df = pd.DataFrame(data)

# Mostrar la tabla de datos
st.table(df)

# Crear un gráfico de barras
st.subheader("Ventas por Modelo")
fig, ax = plt.subplots()
ax.bar(df['Modelo'], df['Ventas (Unidades)'], color=['#FF6347', '#FFD700', '#6A5ACD', '#32CD32', '#FF69B4'])
ax.set_xlabel("Modelo de Sneaker")
ax.set_ylabel("Ventas (Unidades)")
ax.set_title("Ventas de Sneakers por Modelo")

st.pyplot(fig)

# Sección de contacto
st.header("Contáctanos")
st.write("¿Tienes alguna pregunta o te gustaría hacer un pedido especial? ¡Escríbenos!")
contact_form = """
<form action="https://formsubmit.co/tu_correo@example.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="nombre" placeholder="Tu nombre" required>
    <input type="email" name="email" placeholder="Tu email" required>
    <textarea name="mensaje" placeholder="Tu mensaje aquí"></textarea>
    <button type="submit">Enviar</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)


