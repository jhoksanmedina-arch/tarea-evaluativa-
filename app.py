import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Mi primera app en Streamlit", page_icon="💡", layout="wide")

with st.sidebar:
    st.image("logo_uss.jpg", use_container_width=True)
    st.header("Barra lateral")
    st.write("Este es el segundo espacio de la interfaz: la barra lateral.")

    nombre = st.text_input("Escribe tu nombre en la barra lateral:")
    if st.button("Saludar", key="boton_sidebar"):
        if nombre:
            st.success(f"¡Hola, {nombre}!")
        else:
            st.warning("Primero escribe tu nombre.")


col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("logo_uss.jpg", use_container_width=True)

st.title("Reconociendo la interfaz de Streamlit")

st.write(
    "Esta aplicación permite reconocer dos espacios de una interfaz de Streamlit: "
    "el área principal y la barra lateral. En ambos podemos mostrar información "
    "e incorporar componentes interactivos, como botones y campos de texto."
)

st.subheader("Flujo básico: entrada → proceso → salida")

mensaje = st.text_input("Escribe un mensaje:")

# Proceso y salida
if st.button("Mostrar mensaje", key="boton_principal"):
    if mensaje:
        st.write(f"Escribiste: **{mensaje}**")
    else:
        st.warning("No escribiste nada todavía.")
