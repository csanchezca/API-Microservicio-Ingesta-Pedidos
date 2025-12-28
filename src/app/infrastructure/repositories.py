from sqlalchemy.orm import Session
from sqlalchemy import select, func, case
from app.domain.entities import Order
from app.domain.ports import OrdersRepository
from app.infrastructure.models import OrderRow

class SQLiteOrdersRepository(OrdersRepository):
    def __init__(self, db: Session):
        self.db = db

    def save(self, order: Order) -> None:
        row = OrderRow(
            external_id=order.external_id,
            customer_email=order.customer.email,
            total_amount=order.total_amount,
            is_vip=order.is_vip,
            date=order.date,
            arrival_date=order.arrival_date,
        )
        self.db.add(row)
        self.db.commit()

    def report(self) -> list[dict]:
        # resumen por cliente
        stmt = (
            select(
                OrderRow.customer_email.label("customer_email"),
                func.count(OrderRow.id).label("total_orders"),
                func.sum(OrderRow.total_amount).label("total_amount_spent"),
                case((func.sum(OrderRow.total_amount) > 300, True), else_=False).label("is_vip"),
                func.max(OrderRow.arrival_date).label("arrival_date"),
            )
            .group_by(OrderRow.customer_email)
        )
        rows = self.db.execute(stmt).all()
        return [
            {
                "customer_email": r.customer_email,
                "total_orders": int(r.total_orders),
                "total_amount_spent": float(r.total_amount_spent or 0),
                "is_vip": bool(r.is_vip),
                "arrival_date": r.arrival_date,
            }
            for r in rows
        ]
