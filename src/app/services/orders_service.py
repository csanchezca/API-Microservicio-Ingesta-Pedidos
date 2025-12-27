from datetime import timedelta
from app.domain.entities import Order, Customer, Item
from app.domain.errors import ValidationError
from app.domain.ports import OrdersRepository

class OrdersService:
    def __init__(self, repo: OrdersRepository):
        self.repo = repo

    def create_order(self, external_id: str, customer: Customer, items: list[Item], date):
        # reglas
        for it in items:
            if it.quantity <= 0:
                raise ValidationError("quantity debe ser > 0")
            if it.price_unit < 0:
                raise ValidationError("price_unit debe ser >= 0")

        total = sum(it.quantity * it.price_unit for it in items)
        is_vip = total > 300

        arrival_date = date + timedelta(days=3 if is_vip else 5)

        order = Order(
            external_id=external_id,
            customer=customer,
            items=items,
            date=date,
            is_vip=is_vip,
            arrival_date=arrival_date,
        )

        self.repo.save(order)
        return order

    def get_report(self):
        return self.repo.report()
