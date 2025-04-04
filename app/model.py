# app/modelo.py
import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

# Datos ficticios: cuartos vs precio
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([50, 100, 150, 200, 250])  # en miles

modelo = LinearRegression()
modelo.fit(X, y)

# Guardar el modelo
joblib.dump(modelo, "./modelo_precio_casa.pkl")
print("✅ Modelo entrenado y guardado.")
