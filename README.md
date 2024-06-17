# Predicción de SQL Injection

Este proyecto implementa una aplicación web utilizando Streamlit para predecir la posibilidad de SQL Injection en consultas SQL introducidas por el usuario.

## Funcionalidad

La aplicación permite a los usuarios introducir consultas SQL y obtener una predicción sobre si la consulta puede representar un riesgo de SQL Injection utilizando un modelo de aprendizaje automático cargado.

### Pasos

1. **Introducir la Consulta**: Los usuarios pueden ingresar una consulta SQL en un campo de texto proporcionado.
   
2. **Realizar la Predicción**: Al hacer clic en el botón de "Predecir", la aplicación procesa la consulta utilizando un modelo previamente entrenado y muestra la predicción en la interfaz.

### Ejemplo de Uso

```bash
# Clona el repositorio
git clone https://github.com/tu_usuario/prediccion-sql-injection.git
cd prediccion-sql-injection

# Instala las dependencias
pip install -r requirements.txt

# Ejecuta la aplicación
streamlit run app.py
```
### Archivos Incluidos

- **app.py**: Contiene la definición de la aplicación de Streamlit y la integración con el modelo de predicción.
  
- **modelos/sql_injection_model2.h5**: Archivo del modelo de TensorFlow entrenado para la detección de SQL Injection.

- **modelos/vectorizer.pkl**: Archivo pickle que contiene el vectorizador utilizado para transformar las consultas.

### DEPENDENCIAS
streamlit==1.35.0
tensorflow==2.16.2
numpy==1.26.4
scikit-learn==1.5.0

### Notas Adicionales

- Asegúrate de tener una configuración de Python adecuada y un entorno virtual activado si es necesario.
- El modelo y el vectorizador deben estar entrenados y guardados antes de ejecutar la aplicación.
- Personaliza la aplicación según tus necesidades específicas y asegúrate de revisar y ajustar las dependencias según sea necesario.
