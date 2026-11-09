import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Mi primera app en Streamlit", page_icon="💡", layout="wide")

# ---------- BARRA LATERAL ----------
with st.sidebar:
    st.image("logo_uss.jpg", use_container_width=True)
    st.header("Barra lateral")
    st.write("Este es el segundo espacio de la interfaz: la barra lateral.")

    nombre = st.text_input("Escribe tu nombre en la barra lateral:")

    # Salida automática (sin botón)
    if nombre:
        st.write(f"Tu nombre es: **{nombre}**")

    # Botón (igual que antes)
    if st.button("Saludar", key="boton_sidebar"):
        if nombre:
            st.success(f"¡Hola, {nombre}!")
        else:
            st.warning("Primero escribe tu nombre.")

# ---------- ÁREA PRINCIPAL ----------
# Logo centrado
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("logo_uss.jpg", use_container_width=True)

# Mensaje de bienvenida
st.title("¡Hola! Bienvenido a mi primera app 👋")
st.write("Escribe lo que quieras en el cuadro de abajo y yo te lo muestro en pantalla.")

# Entrada
mensaje = st.text_input("Escribe un mensaje:")

# Salida automática (sin botón)
if mensaje:
    st.write(f"Escribiste: **{mensaje}**")

# Botón (igual que antes)
if st.button("Mostrar mensaje", key="boton_principal"):
    if mensaje:
        st.success(f"Mensaje confirmado: {mensaje}")
    else:
        st.warning("No escribiste nada todavía.")
