# app/tests/test_movies.py
import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine
from app.main import app
from app.core.database import get_session
from app.models.movie import Movie, MovieCreate
from app.models.log import RequestLog

# Configurar base de datos de pruebas en memoria
test_engine = create_engine("sqlite:///:memory:", connect_args={"check_same_thread": False})

# Reemplazar dependencia de sesión para usar la base de datos de pruebas
def override_get_session():
    with Session(test_engine) as session:
        yield session

app.dependency_overrides[get_session] = override_get_session

@pytest.fixture(autouse=True)
def prepare_db():
    # Crear todas las tablas en la DB de pruebas
    SQLModel.metadata.create_all(test_engine)
    yield
    # Limpiar tablas tras cada prueba
    SQLModel.metadata.drop_all(test_engine)

client = TestClient(app)

def test_add_and_get_movie():
    # Añadir una nueva película
    payload = {"name": "The Matrix", "release_date": "1999-03-31T00:00:00", "watched": False}
    response = client.post("/movies/", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "The Matrix"
    assert data["watched"] is False
    movie_id = data["id"]

    # Recuperar la película creada
    response = client.get(f"/movies/{movie_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == movie_id
    assert data["name"] == "The Matrix"

def test_update_movie():
    # Crear película
    payload = {"name": "Inception", "release_date": "2010-07-16T00:00:00"}
    response = client.post("/movies/", json=payload)
    movie_id = response.json()["id"]

    # Actualizar nombre y marcar como vista
    update_payload = {"name": "Inception Updated", "watched": True}
    response = client.put(f"/movies/{movie_id}", json=update_payload)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Inception Updated"
    assert data["watched"] is True

def test_list_and_delete_movie():
    # Crear dos películas
    client.post("/movies/", json={"name": "A", "release_date": "2000-01-01T00:00:00"})
    client.post("/movies/", json={"name": "B", "release_date": "2001-01-01T00:00:00"})

    # Listar películas
    response = client.get("/movies/?skip=0&limit=10")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2

    # Eliminar la primera película
    movie_id = data[0]["id"]
    response = client.delete(f"/movies/{movie_id}")
    assert response.status_code == 204

    # Verificar que no aparece en la lista
    response = client.get("/movies/?skip=0&limit=10")
    data = response.json()
    assert all(m["id"] != movie_id for m in data)

def test_request_logs_created():
    # Contar logs antes
    with Session(test_engine) as session:
        initial_logs = session.query(RequestLog).count()

    # Hacer una petición GET a lista
    response = client.get("/movies/")
    assert response.status_code == 200

    # Verificar que se creó un log
    with Session(test_engine) as session:
        after_logs = session.query(RequestLog).count()
    assert after_logs == initial_logs + 1