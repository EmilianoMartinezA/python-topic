# app/core/config.py 
# este archivo contiene la configuración de la aplicación, incluyendo la URL de la base de datos
from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8" # codificación de archivo .env
settings = Settings() # instancia de la clase Settings que carga la configuración desde el archivo .env
