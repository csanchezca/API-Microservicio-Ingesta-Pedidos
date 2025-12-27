from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class Customer:
    email: str
    name: str
    client_id: str

@dataclass(frozen=True)
class Item:
    sku: str
    quantity: int
    price_unit: float

@dataclass(frozen=True)
class Order:
    external_id: str
    customer: Customer
    items: list[Item]
    date: datetime
    is_vip: bool
    arrival_date: datetime

    @property
    def total_amount(self) -> float:
        return sum(i.quantity * i.price_unit for i in self.items)
