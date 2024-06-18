import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from model import predict_query

class App:
    def __init__(self):
        self.titulo = "Predicción de SQL Injection"
        self.default_section = 'Probar modelo'

    def run(self):
        st.set_page_config(page_title=self.titulo, layout="wide")
        st.title(self.titulo)

        st.sidebar.title('Menú')
        if st.sidebar.button('Introducción', key='Introducción'):
            self.default_section = 'Introducción'
        if st.sidebar.button('Estadísticas', key='Estadísticas'):
            self.default_section = 'Estadísticas'
        if st.sidebar.button('Sugerencias', key='Sugerencias'):
            self.default_section = 'Sugerencias'
        if st.sidebar.button('Probar modelo', key='Probar modelo'):
            self.default_section = 'Probar modelo'

        # Mostrar la sección por defecto
        if self.default_section == 'Introducción':
            self.show_introduction()
        elif self.default_section == 'Estadísticas':
            self.show_statistics()
        elif self.default_section == 'Sugerencias':
            self.show_tips()
        elif self.default_section == 'Probar modelo':
            self.show_model()

    def show_introduction(self):
        st.title("Introducción")
        st.write("""
        Bienvenido a la aplicación de Predicción de SQL Injection. Esta herramienta fue desarrollada con el objetivo de ayudar a detectar posibles vulnerabilidades de inyección SQL en consultas de bases de datos. La inyección SQL es una de las vulnerabilidades más comunes y peligrosas que puede afectar a aplicaciones web y sistemas que utilizan bases de datos para almacenar y gestionar datos sensibles.

¿Qué es la inyección SQL?
La inyección SQL ocurre cuando los datos proporcionados por un usuario malintencionado son manipulados de tal manera que alteran el comportamiento esperado de la consulta SQL. Esto puede llevar a que se ejecuten comandos no autorizados en la base de datos, revelando información confidencial o incluso permitiendo un control total sobre el sistema.

Importancia de la prevención
Detectar y prevenir ataques de inyección SQL es crucial para garantizar la seguridad de los datos y la integridad del sistema. Las consecuencias de una explotación exitosa de esta vulnerabilidad pueden ser devastadoras, desde la pérdida de datos hasta el compromiso completo del sistema y la exposición de información privada.

Funcionamiento de la aplicación
En esta aplicación, puedes introducir consultas SQL en el campo correspondiente y utilizar un modelo predictivo para evaluar si la consulta proporcionada podría ser vulnerable a un ataque de inyección SQL. La herramienta te proporcionará una predicción sobre la seguridad de la consulta, ayudándote a identificar posibles riesgos antes de que sean explotados por un atacante.

Esperamos que esta herramienta te sea útil para mejorar la seguridad de tus aplicaciones y sistemas. Asegúrate de entender los principios básicos de seguridad en bases de datos y practicar buenas prácticas de programación para minimizar las vulnerabilidades.
        """)

    def show_statistics(self):
        st.title("Estadísticas")
        
        st.subheader("Sobre SQL Injection")
        
        st.write("""
            Los ataques de inyección SQL representan una de las amenazas más prevalentes y persistentes que enfrentan los sistemas de software públicos. De hecho, se estima que el 42% de los ataques dirigidos a sistemas públicos son atribuibles a ataques de inyección SQL. Esta forma de ataque explota vulnerabilidades de seguridad al insertar declaraciones SQL maliciosas a través de campos de entrada, con el objetivo de ejecutar comandos no autorizados en bases de datos SQL.

La gravedad de estos ataques radica en su capacidad para comprometer la integridad de los datos y la seguridad del sistema en su conjunto. Una vez que un atacante logra explotar con éxito una vulnerabilidad de inyección SQL, puede acceder, modificar o eliminar datos confidenciales, comprometiendo así la confidencialidad y disponibilidad de la información almacenada.

Recientemente, Check Point ha observado un aumento significativo en los intentos de ataques de inyección SQL a través de sus servicios de seguridad gestionada. Mediante el análisis del tráfico que activó protecciones ajustadas contra inyecciones SQL en su blade de software IPS, se pueden identificar tendencias actuales y patrones emergentes en estos intentos de ataques.

Para mitigar eficazmente estas amenazas, es fundamental implementar consultas parametrizadas en las aplicaciones, una práctica recomendada que fortalece la seguridad al prevenir la ejecución de código SQL no autorizado a través de campos de entrada. Al adoptar medidas preventivas proactivas como estas, las organizaciones pueden reducir significativamente la exposición a uno de los vectores de ataque más comunes y peligrosos a nivel mundial.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.image("assets/5.png", use_column_width=True)

        # Mostrar la segunda imagen en la segunda columna
        with col2:
            st.image("assets/6.png", use_column_width=True)


        
        st.subheader("Sobre el modelo")
        
        st.write("""
        En esta sección se presentan estadísticas relevantes sobre ataques de inyección SQL y tipos de vulnerabilidades más comunes.
        
        El modelo fue entrenado con dos datasets con distintas cantidades de datos, siendo ademas evaluado sobre otros modelos que recibieron un entrenamiento apropiado para sus caracteristicas siendo este el mas sobresaliente respecto a los demas.
        """)
        
        st.image('assets/4.png', width=700)
        
        st.subheader("Referencias")

        
        st.write("""
            - [www.statista.com](https://www.statista.com/statistics/806081/worldwide-application-vulnerability-taxonomy/#:~:text=SQL%20Injection%20is%20the%20main,site%20scripting%20(stored)%20attacks.)
            - [www.phppot.com](https://phppot.com/php/prevent-sql-injection-php/)
            - [Otras fuentes](https://blog.checkpoint.com/latest-sql-injection-trends/)
            
        """)

    def show_tips(self):
        st.title("Sugerencias")
        st.write("""
        ### Sugerencias para prevenir la inyección SQL

        #### Utilizar consultas parametrizadas
        Utiliza consultas parametrizadas en lugar de concatenar directamente los valores de entrada del usuario en las consultas SQL. Esto ayuda a prevenir que los datos ingresados por el usuario sean interpretados como parte del código SQL ejecutable.

        ```python
        query = "SELECT * FROM usuarios WHERE nombre = %s AND edad = %s"
        cursor.execute(query, (nombre_usuario, edad_usuario))
        ```

        #### Validación de entrada
        Realiza una validación exhaustiva de los datos de entrada antes de ejecutar cualquier consulta SQL. Esto incluye asegurarse de que los tipos de datos ingresados sean los esperados y que no contengan caracteres especiales que puedan ser interpretados como comandos SQL.

        ```python
        if not isinstance(nombre_usuario, str):
            raise ValueError("El nombre de usuario debe ser una cadena de texto.")
        ```

        #### Limitar privilegios de la base de datos
        Asegúrate de que las cuentas de usuario utilizadas por tu aplicación tengan solo los privilegios necesarios para realizar las operaciones requeridas. Evita utilizar cuentas con privilegios administrativos cuando no sean estrictamente necesarios.

        #### Actualización y parcheo regular
        Mantén actualizados los sistemas operativos, servidores de bases de datos y marcos de aplicación para asegurar que las vulnerabilidades conocidas estén parcheadas y reducir el riesgo de explotación.

        #### Auditoría y monitoreo continuo
        Implementa auditorías y monitoreo continuo de las consultas SQL ejecutadas por la aplicación para detectar patrones inusuales o intentos de inyección SQL en tiempo real.
        """)

    def show_model(self):
        st.title("Probar modelo")
        st.subheader("Pasos")
        st.markdown("""
        1. Introducir la query en formato de texto en el entry.
        2. Observar la predicción dada por el modelo.
        """)

        query = st.text_input("Introduce tu query aquí:", "SELECT * FROM usuarios")

        if st.button('Predecir'):
            prediction = predict_query(query)
            st.write(f"Predicción: {prediction}")

if __name__ == "__main__":
    app = App()
    app.run()
