"""
app/core/main.py

Punto de entrada de la aplicación FastAPI.
Define la instancia principal, preparacion de la base de datos y routers de la API.
"""
from fastapi import FastAPI # Import FastAPI
from sqlmodel import SQLModel # Import SQLModel
from app.core.database import engine # Import engine from database module
from app.routers import movies # Import movies router from routers module

app = FastAPI(
    title="ToWatchList API",
    description="Servicio para gestionar una lista de películas a ver",
    version="1.0.0"
) # se crea una instancia de FastAPI

@app.on_event("startup") # se define un evento que se ejecuta al iniciar la aplicación
def on_startup():
    """
    Evento que se ejecuta al iniciar la aplicación.

    - Crea todas las tablas definidas en los modelos de SQLModel si no existen.
    """
    SQLModel.metadata.create_all(engine)
# se crea la base de datos y las tablas si no existen
app.include_router(movies.router, prefix="/movies", tags=["movies"])  
# se incluye el router de películas en la aplicación

# from app.routers import health
# app.include_router(health.router, prefix="/health", tags=["health"])
