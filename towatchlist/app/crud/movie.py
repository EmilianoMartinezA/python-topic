# app/crud/movie.py
from typing import List, Optional
from sqlmodel import select
from datetime import datetime
from sqlmodel import Session
from app.models.movie import Movie, MovieCreate, MovieRead, MovieUpdate


def create_movie(session: Session, movie_create: MovieCreate) -> MovieRead:
    movie = Movie.from_orm(movie_create)
    session.add(movie)
    session.commit()
    session.refresh(movie)
    return MovieRead.from_orm(movie)


def get_movies(session: Session, skip: int = 0, limit: int = 100) -> List[MovieRead]:
    statement = select(Movie).where(Movie.status == "active").offset(skip).limit(limit)
    results = session.exec(statement).all()
    return [MovieRead.from_orm(m) for m in results]


def get_movie(session: Session, movie_id: int) -> Optional[MovieRead]:
    movie = session.get(Movie, movie_id)
    if movie and movie.status == "active":
        return MovieRead.from_orm(movie)
    return None


def update_movie(session: Session, movie_id: int, movie_update: MovieUpdate) -> Optional[MovieRead]:
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
    movie = session.get(Movie, movie_id)
    if not movie or movie.status != "active":
        return False
    movie.status = "deleted"
    movie.updated_at = datetime.utcnow()
    session.add(movie)
    session.commit()
    return True