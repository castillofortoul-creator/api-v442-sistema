from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(
    title="API Framework v44.2",
    description="Sistema de Prediccion de Vorticidad para Ciclones - Komchen",
    version="1.0"
)

# ESTO INDISPENSABLE: Permite que tu pagina web se conecte sin bloqueos
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class DatosCiclon(BaseModel):
    nombre: str
    presion_hpa: float
    vientos_kmh: float

@app.get("/")
def inicio():
    return {"mensaje": "API v44.2 Activa. Desarrollado en Komchen, Yucatan. Ve a /docs para probar."}

@app.post("/predecir")
def calcular_balance(datos: DatosCiclon):
    if datos.vientos_kmh < 85:
        r_source = 1.55  
    elif datos.presion_hpa > 990:
        r_source = 2.18  
    else:
        r_source = 4.15  
        
    arrastre_eje = -0.20  
    balance = -1.0 + arrastre_eje + r_source
    blow_up = r_source >= 2.20 and balance > 0
    
    return {
        "ciclon": datos.nombre,
        "metricas": {
            "r_source": round(r_source, 2),
            "balance_neto": round(balance, 2)
        },
        "diagnostico": {
            "resultado": "ALERTA: Blow-up / Landfall Detectado" if blow_up else "Regularidad: Zero Landfall / Disipacion",
            "detalles": "El sistema presenta inyeccion critica." if blow_up else "Inyeccion insuficiente. El sistema ira a aguas abiertas."
        },
        "contacto": "Grupo de Dinamica Atmosferica Avanzada, Komchen, Yucatan."
    }
