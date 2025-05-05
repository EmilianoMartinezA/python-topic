# app/routers/movies.py
from fastapi import APIRouter, Depends, HTTPException, status, request
from typing import List
from sqlmodel import Session
from app.core.database import get_session
from app.models.movie import MovieCreate, MovieRead, MovieUpdate
from app.models.logging import log_request
from app.crud.movie import (
    create_movie,
    get_movies,
    get_movie,
    update_movie,
    mark_movie_as_watched,
    delete_movie,
)

router = APIRouter()

@router.post("/", response_model=MovieRead, status_code=status.HTTP_201_CREATED)
@log_request
def add_movie(
    request: request,
    movie_create: MovieCreate,
    session: Session = Depends(get_session)
) -> MovieRead:
    return create_movie(session, movie_create)

@router.get("/", response_model=List[MovieRead])
@log_request
def list_movies(
    request: request,
    skip: int = 0,
    limit: int = 100,
    session: Session = Depends(get_session)
) -> List[MovieRead]:
    return get_movies(session, skip, limit)

@router.get("/{movie_id}", response_model=MovieRead)
@log_request
def read_movie(
    request: request,
    movie_id: int,
    session: Session = Depends(get_session)
) -> MovieRead:
    movie = get_movie(session, movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

@router.put("/{movie_id}", response_model=MovieRead)
@log_request
def edit_movie(
    request: request,
    movie_id: int,
    movie_update: MovieUpdate,
    session: Session = Depends(get_session)
) -> MovieRead:
    updated = update_movie(session, movie_id, movie_update)
    if not updated:
        raise HTTPException(status_code=404, detail="Movie not found or inactive")
    return updated

@router.patch("/{movie_id}/watch", response_model=MovieRead)
@log_request
def watch_movie(
    request: request,
    movie_id: int,
    session: Session = Depends(get_session)
) -> MovieRead:
    watched = mark_movie_as_watched(session, movie_id)
    if not watched:
        raise HTTPException(status_code=404, detail="Movie not found or inactive")
    return watched

@router.delete("/{movie_id}", status_code=status.HTTP_204_NO_CONTENT)
@log_request
def remove_movie(
    request: request,
    movie_id: int,
    session: Session = Depends(get_session)
):
    success = delete_movie(session, movie_id)
    if not success:
        raise HTTPException(status_code=404, detail="Movie not found or inactive")
    return None