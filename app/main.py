from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Crear la aplicación FastAPI
app = FastAPI()

# Configurar CORS
origins = [
    "http://localhost",  # Permitir desde localhost
    "http://localhost:3000",  # Si tu frontend está en puerto 3000
    "https://tu-dominio-render.com",  # Si también vas a desplegar el frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Puedes agregar más dominios aquí
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos los encabezados
)

# Definir el modelo de datos
class InputData(BaseModel):
    cuartos: int

# Rutas
@app.post("/predecir")
async def predecir(data: InputData):
    # Aquí iría tu modelo de predicción
    precio_estimado = data.cuartos * 50  # Ejemplo de predicción
    return {"precio_estimado": precio_estimado}
