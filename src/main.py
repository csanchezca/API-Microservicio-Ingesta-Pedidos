from fastapi import FastAPI
from app.routers.orders import router as orders_router
from app.infrastructure.db import engine
from app.infrastructure.models import Base

app = FastAPI(title="Order Ingestion Service")
Base.metadata.create_all(bind=engine)

app.include_router(orders_router)
