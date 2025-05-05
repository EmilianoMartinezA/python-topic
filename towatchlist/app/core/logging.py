# app/core/logging.py
from functools import wraps
from fastapi import Request
from sqlmodel import Session
from sqlalchemy.exc import SQLAlchemyError
from app.core.database import engine
from app.models.log import RequestLog


def log_request(func):
    @wraps(func)
    async def wrapper(request: Request, *args, **kwargs):
        try:
            with Session(engine) as session:
                log = RequestLog(method=request.method, path=request.url.path)
                session.add(log)
                session.commit()
        except SQLAlchemyError:
            pass  # No bloquear la ejecución si falla el log
        return await func(request, *args, **kwargs)
    return wrapper