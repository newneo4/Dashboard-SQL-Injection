import numpy as np
import streamlit as st
from tensorflow.keras.models import load_model
import pickle

model = load_model("modelos/sql_injection_model2.h5")

with open("modelos/vectorizer.pkl", "rb") as file:
    vectorizer = pickle.load(file)

predicciones = {
    1: "Estás a salvo, no es una SQL Injection",
    0: "¡Cuidado! Estás en peligro",
}

def predict_query(query):
    query_vectorized = vectorizer.transform([query])
    
    query_array = query_vectorized.toarray()
    
    query_array = query_array.reshape(-1, 1, query_array.shape[1])
    
    predictions = model.predict(query_array)
    
    indice_maximo = int(round(predictions[0][0]))
    
    prediction_label = predicciones[indice_maximo]
    
    print(predicciones[int(round(predictions[0][0]))], predictions, indice_maximo)
    
    return prediction_label
