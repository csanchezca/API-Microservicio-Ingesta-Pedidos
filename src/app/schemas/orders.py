from datetime import datetime
from pydantic import BaseModel, EmailStr, Field, conint, confloat

class CustomerIn(BaseModel):
    email: EmailStr
    name: str = Field(min_length=1)
    client_id: str = Field(min_length=1)

class ItemIn(BaseModel):
    sku: str = Field(min_length=1)
    quantity: conint(gt=0)  # >0
    price_unit: confloat(ge=0)  # >=0

class OrderIn(BaseModel):
    external_id: str = Field(min_length=1)
    customer: CustomerIn
    items: list[ItemIn]
    date: datetime

class ReportRowOut(BaseModel):
    customer_email: EmailStr
    total_orders: int
    total_amount_spent: float
    is_vip: bool
    arrival_date: datetime
