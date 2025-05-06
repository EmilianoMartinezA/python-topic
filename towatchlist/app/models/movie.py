# app/models/movie.py
from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional

class MovieBase(SQLModel):
    """
    Datos básicos de una película.

    Atributos:
        name (str): Título de la película.
        release_date (datetime): Fecha de estreno.
        watched (bool): Indicador si ya fue vista.
    """
    name: str
    release_date: datetime
    watched: bool = False

class Movie(MovieBase, table=True):
    """
    Modelo completo de película para la base de datos.

    Incluye metadatos y estado para manejo de borrado lógico.
    """
    id: Optional[int]   = Field(default=None, primary_key=True,
                                 description="Clave primaria de la película")
    created_at: datetime = Field(default_factory=datetime.utcnow,
                                  description="Fecha de creación del registro")
    updated_at: datetime = Field(default_factory=datetime.utcnow,
                                  description="Fecha de última actualización")
    status: str          = Field(default="active",
                                 description="Estado: 'active' o 'deleted'")

class MovieCreate(MovieBase):
    # Creación de una nueva película.
    pass

class MovieRead(MovieBase):
    """
    Esquema para leer datos de una película existente.

    Atributos adicionales:
        id (int): Identificador de la película.
        created_at (datetime): Fecha de creación.
        updated_at (datetime): Fecha de última actualización.
        status (str): Estado actual ('active' o 'deleted').
    """
    id: int
    created_at: datetime 
    updated_at: datetime 
    status: str

class MovieUpdate(SQLModel):
    """
    Esquema para actualizar datos de una película.

    Todos los campos son opcionales y solo los enviados se modifican.
    son opcionales porque no todos los campos son requeridos para actualizar una película.
    """
    name: Optional[str] = None
    release_date: Optional[datetime] = None
    watched: Optional[bool] = None