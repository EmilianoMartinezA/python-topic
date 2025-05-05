# app/core/database.py
from sqlmodel import create_engine, Session 
from app.core.config import settings

#sqlmodel es un ORM (Object Relational Mapper) que interactua con bases de datos SQL utilizando Python
# y SQLAlchemy para trabajar/modificar bases de datos SQL.

engine = create_engine(
    settings.DATABASE_URL,  # se manda la URL de la base de datos
    echo=True,  # Muestra consultas SQL en consola
)

def get_session():
    with Session(engine) as session:
        yield session #se utiliza para crear una sesión de base de datos
# y se cierra automáticamente al finalizar el bloque de código.