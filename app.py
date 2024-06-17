import streamlit as st
from model import predict_query

class App:
    def __init__(self):
        self.titulo = "Predicción de SQL Injection"
        

    def run(self):
        st.set_page_config(page_title=self.titulo, layout="wide")
        st.title(self.titulo)

        st.title("Bienvenido")
        st.subheader("Pasos")
        st.markdown("""
        1. Introducir la query en formato de texto en el entry.
        2. Observar la predicción dada por el modelo.
        """)
        
        # Input de texto para la consulta SQL
        query = st.text_input("Introduce tu query aquí:", "SELECT * FROM usuarios")
        
        if st.button('Predecir'):
            # Realizar predicción
            prediction = predict_query(query)
            st.write(f"Predicción: {prediction}")

# Ejecutar la aplicación
if __name__ == "__main__":
    app = App()
    app.run()
