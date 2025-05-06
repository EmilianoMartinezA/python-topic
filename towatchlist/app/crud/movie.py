"""
app/crud/movie.py

Módulo de operaciones CRUD (Create, Read, Update, Delete) para el modelo Movie.
Incluye funciones para crear, leer, actualizar, marcar como visto y eliminar.
"""
from typing import List, Optional
from sqlmodel import select
from datetime import datetime
from sqlmodel import Session
from app.models.movie import Movie, MovieCreate, MovieRead, MovieUpdate


def create_movie(session: Session, movie_create: MovieCreate) -> MovieRead:
    """
    Crea una nueva película en la base de datos.

    Parameters:
        session (Session): Sesión de SQLModel para operar sobre la base de datos.
        movie_create (MovieCreate): Esquema con los datos necesarios para crear la película.

    Returns:
        MovieRead: Esquema de lectura de la película recién creada.
    """
    movie = Movie.from_orm(movie_create)
    session.add(movie)
    session.commit()
    session.refresh(movie)
    return MovieRead.from_orm(movie)


def get_movies(session: Session, skip: int = 0, limit: int = 100) -> List[MovieRead]:
    """
    Recupera una lista de películas activas de la base de datos.

    Parameters:
        session (Session): Sesión de SQLModel.
        skip (int): Número de registros a omitir (paginación).
        limit (int): Máximo número de registros a devolver.

    Returns:
        List[MovieRead]: Lista de películas activas en formato de lectura.
    """
    statement = select(Movie).where(Movie.status == "active").offset(skip).limit(limit)
    results = session.exec(statement).all()
    return [MovieRead.from_orm(m) for m in results]


def get_movie(session: Session, movie_id: int) -> Optional[MovieRead]:
    """
    Obtiene una película activa por su identificador.

    Parameters:
        session (Session): Sesión de SQLModel.
        movie_id (int): Identificador único de la película.

    Returns:
        MovieRead | None: Esquema de lectura si existe y está activa; de lo contrario, None.
    """
    movie = session.get(Movie, movie_id)
    if movie and movie.status == "active":
        return MovieRead.from_orm(movie)
    return None


def update_movie(session: Session, movie_id: int, movie_update: MovieUpdate) -> Optional[MovieRead]:
    """
    Actualiza los campos de una película activa.

    Parameters:
        session (Session): Sesión de SQLModel.
        movie_id (int): Identificador de la película a actualizar.
        movie_update (MovieUpdate): Esquema con los campos a modificar.

    Returns:
        MovieRead | None: Esquema de lectura de la película actualizada si existía y estaba activa; de lo contrario, None.
    """
    movie = session.get(Movie, movie_id)
    if not movie or movie.status != "active":
        return None
    movie_data = movie_update.dict(exclude_unset=True)
    for key, value in movie_data.items():
        setattr(movie, key, value)
    movie.updated_at = datetime.utcnow()
    session.add(movie)
    session.commit()
    session.refresh(movie)
    return MovieRead.from_orm(movie)


def mark_movie_as_watched(session: Session, movie_id: int) -> Optional[MovieRead]:
    """
    Marca una película activa como vista (watched=True).

    Parameters:
        session (Session): Sesión de SQLModel.
        movie_id (int): Identificador de la película.

    Returns:
        MovieRead | None: Esquema de lectura actualizado si la película existía y estaba activa; de lo contrario, None.
    """
    movie = session.get(Movie, movie_id)
    if not movie or movie.status != "active":
        return None
    movie.watched = True
    movie.updated_at = datetime.utcnow()
    session.add(movie)
    session.commit()
    session.refresh(movie)
    return MovieRead.from_orm(movie)


def delete_movie(session: Session, movie_id: int) -> bool:
    """
    Realiza un borrado lógico de una película, cambiando su estado a "deleted".

    Parameters:
        session (Session): Sesión de SQLModel.
        movie_id (int): Identificador de la película a eliminar.

    Returns:
        bool: True si la película existía y se marcó como eliminada; False en caso contrario.
    """
    movie = session.get(Movie, movie_id)
    if not movie or movie.status != "active":
        return False
    movie.status = "deleted"
    movie.updated_at = datetime.utcnow()
    session.add(movie)
    session.commit()
    return True