"""
app/core/config.py

Define la configuración central de la aplicación usando Pydantic.
Carga variables de entorno desde un archivo .env para parámetros como la conexión a la base de datos.
"""
# este archivo contiene la configuración de la aplicación, incluyendo la URL de la base de datos
from pydantic import BaseSettings 

class Settings(BaseSettings):
    """
    Configuración principal de la aplicación.

    Attributes:
    DATABASE_URL (str): URL de conexión a la base de datos ("postgresql://user:pass@host/db").
    """
    DATABASE_URL: str

    class Config:
        """
        Configuración interna de Pydantic.

        - env_file: archivo de variables de entorno a leer.
        - env_file_encoding: codificación del archivo .env.
        """
        env_file = ".env"
        env_file_encoding = "utf-8" # codificación de archivo .env
settings = Settings() # instancia de la clase Settings que carga la configuración desde el archivo .env
