from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, DateTime, Float, Integer, Boolean

class Base(DeclarativeBase):
    pass

class OrderRow(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    external_id: Mapped[str] = mapped_column(String, unique=True, index=True)
    customer_email: Mapped[str] = mapped_column(String, index=True)
    total_amount: Mapped[float] = mapped_column(Float)
    is_vip: Mapped[bool] = mapped_column(Boolean)
    date: Mapped[str] = mapped_column(DateTime)
    arrival_date: Mapped[str] = mapped_column(DateTime)
