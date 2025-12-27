from typing import Protocol
from app.domain.entities import Order

class OrdersRepository(Protocol):
    def save(self, order: Order) -> None:
        ...

    def report(self) -> list[dict]:
        ...
