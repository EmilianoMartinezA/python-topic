"""
app/models/log.py and app/models/movie.py

Estos archivos definen los esquemas de datos (modelos) que utilizas para interactuar con la base de datos:

- **log.py**: Modelo para almacenar cada petición que llega a tu API.
- **movie.py**: Modelos para representar películas en diferentes etapas (creación, lectura y actualización).
"""
from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional

class RequestLog(SQLModel, table=True):
    """
    Representa una entrada de registro (log) de solicitud HTTP.

    Atributos:
        id (Optional[int]): Identificador único (clave primaria).
        method (str): Método HTTP usado (GET, POST, etc.).
        path (str): Ruta solicitada (/movies, /health, ...).
        timestamp (datetime): Fecha y hora en que se registró la petición.
    """
    id: Optional[int] = Field(default=None, primary_key=True) # prymary key
    # esto es un campo opcional que se generará automáticamente por la base de datos
    method: str 
    path: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)