import numpy as np
import streamlit as st
from tensorflow.keras.models import load_model
import pickle

# Carga el modelo
model = load_model("modelos/sql_injection_model2.h5")

# Carga el vectorizador
with open("modelos/vectorizer.pkl", "rb") as file:
    vectorizer = pickle.load(file)

predicciones = {
    0: "Estás a salvo, no es una SQL Injection",
    1: "¡Cuidado! Estás en peligro",
}

def predict_query(query):
    # Preprocesar la consulta SQL utilizando el vectorizador cargado
    query_vectorized = vectorizer.transform([query])
    
    # Convertir el vectorizado a un formato que el modelo pueda usar
    query_array = query_vectorized.toarray()
    
    # Ajustar la forma para que coincida con la entrada del modelo (None, 1, 10321)
    query_array = query_array.reshape(-1, 1, query_array.shape[1])
    
    # Realizar predicciones con el modelo cargado
    predictions = model.predict(query_array)
    
    # Obtener el índice de la clase predicha
    indice_maximo = np.argmax(predictions)
    
    # Obtener la etiqueta de predicción
    prediction_label = predicciones[indice_maximo]
    
    return prediction_label
