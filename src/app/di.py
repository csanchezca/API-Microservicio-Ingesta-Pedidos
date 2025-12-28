from functools import lru_cache
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from app.infrastructure.repositories import SQLiteOrdersRepository
from app.services.orders_service import OrdersService

DATABASE_URL = "sqlite:///./orders.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},  # SQLite + threads (uvicorn reload)
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db_session() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_orders_service() -> OrdersService:
    # OJO: no Depends aquí; esto es un provider simple para routers
    # (si quieres, puedes hacerlo con Depends(get_db_session) pero no es obligatorio)
    db = SessionLocal()
    try:
        repo = SQLiteOrdersRepository(db)
        return OrdersService(repo)
    finally:
        db.close()
