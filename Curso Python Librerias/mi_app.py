
import streamlit as st
import pandas as pd
# Título de la aplicación
st.title("Ejemplo Básico de Streamlit")
# Crear un DataFrame de ejemplo
data = {
    "Nombre": ["Ana", "Luis", "Sofia"],
    "Edad": [22, 29, 24],
    "Ciudad": ["Madrid", "Barcelona", "Valencia"]
}
df = pd.DataFrame(data)
# Mostrar el DataFrame en la aplicación
st.write("DataFrame de ejemplo:")
st.dataframe(df)
# Agregar un slider para filtrar por edad
edad_min = st.slider("Edad mínima", 18, 60, 20)
df_filtrado = df[df["Edad"] >= edad_min]
st.write(f"DataFrame filtrado por edad mínima de {edad_min}:")
st.dataframe(df_filtrado)
# Agregar un botón para mostrar un mensaje
if st.button("Mostrar mensaje"):
    st.write("¡Hola! Has presionado el botón.")

