# app/main.py
from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib

app = FastAPI()

# Modelo de entrada
class DatosEntrada(BaseModel):
    cuartos: int

# Cargar modelo
modelo = joblib.load("app/modelo_precio_casa.pkl")

@app.get("/")
def inicio():
    return {"mensaje": "API para predecir el precio de una casa"}

@app.post("/predecir")
def predecir(data: DatosEntrada):
    entrada = np.array([[data.cuartos]])
    prediccion = modelo.predict(entrada)[0]
    return {"precio_estimado": round(prediccion, 2)}
