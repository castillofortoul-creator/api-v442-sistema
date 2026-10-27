from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="API Framework V44.2",
    description="Sistema de predicción de condiciones de ciclogénesis",
    version="1.0"
)

# Orígenes explícitos para asegurar la compatibilidad con tu dominio de GitHub Pages
origins = [
    "https://github.io",
    "http://localhost",
    "http://127.0.0.1"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"status": "online", "message": "API de Framework V44.2 activa y respondiendo"}

@app.get("/v442")
def calcular_balance(vance: str, presion_central_minima: float, vientos_sostenidos: float):
    r_source = round((vientos_sostenidos * 0.12), 2)
    balance = round((1013 - presion_central_minima) - r_source, 2)
    
    if balance > 15:
        resultado = "ALTA PROBABILIDAD DE INTENSIFICACIÓN: Las condiciones dinámicas favorecen el desarrollo rápido."
    elif balance >= 0:
        resultado = "CONDICIÓN ESTABLE: El sistema mantiene su estructura actual sin cambios bruscos inmediatos."
    else:
        resultado = "TENDENCIA A DISIPACIÓN / DEBILITAMIENTO: La presión interna y la fricción están limitando el sistema."
        
    return {
        "ciclón": vance,
        "r_source": r_source,
        "balance": balance,
        "resultado": resultado
    }
