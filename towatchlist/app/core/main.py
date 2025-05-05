# app/main.py
from fastapi import FastAPI # Import FastAPI
from sqlmodel import SQLModel # Import SQLModel
from app.core.database import engine # Import engine from database module
from app.routers import movies # Import movies router from routers module

app = FastAPI() # se crea una instancia de FastAPI

@app.on_event("startup") # se define un evento que se ejecuta al iniciar la aplicación
def on_startup():
    SQLModel.metadata.create_all(engine)
# se crea la base de datos y las tablas si no existen
app.include_router(movies.router, prefix="/movies", tags=["movies"])  
# se incluye el router de películas en la aplicación