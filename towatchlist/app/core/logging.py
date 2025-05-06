# app/core/logging.py
from functools import wraps # preserva el contexto de la función decorada
from fastapi import Request 
from sqlmodel import Session # SQLModel para una sesion de base de datos con el engine
from sqlalchemy.exc import SQLAlchemyError # captura cualquier error de SQLAlchemy
from app.core.database import engine # Motor de base de datos
from app.models.log import RequestLog # Modelo de registro de solicitudes


def log_request(func): # -> un endpoint de FastAPI llamado func
    @wraps(func)
    async def wrapper(request: Request, *args, **kwargs): # -> función con el wrapper 
        # el endpoint se ejecuta y se registra la solicitud
        # Se registra el método y la ruta de la solicitud
        # el objeto request es de tipo Request de FastAPI
        try:
            with Session(engine) as session:
                log = RequestLog(method=request.method, path=request.url.path)
                session.add(log)
                session.commit()
            # se crea un contexto de sesión para registrar la solicitud y al salir 
            # del with se cierra la sesión automáticamente
        except SQLAlchemyError:
            pass  # No bloquear la ejecución si falla el log
        return await func(request, *args, **kwargs) # se llama a la función original con los argumentos originales
    return wrapper # se devuelve el wrapper que contiene la función original