#DI (inyección de dependencias)

from fastapi import Depends
from sqlalchemy.orm import Session

from app.infrastructure.db import get_session
from app.infrastructure.repositories import SQLiteOrdersRepository
from app.services.orders_service import OrdersService

def get_orders_service(db: Session = Depends(get_session)) -> OrdersService:
    repo = SQLiteOrdersRepository(db)
    return OrdersService(repo)
