from fastapi import APIRouter, Depends, HTTPException
from app.schemas.orders import OrderIn, ReportRowOut
from app.services.orders_service import OrdersService
from app.domain.entities import Customer, Item
from app.domain.errors import ValidationError
from app.di import get_orders_service

router = APIRouter(prefix="/orders", tags=["orders"])

@router.post("", status_code=201)
def create_order(payload: OrderIn, service: OrdersService = Depends(get_orders_service)):
    try:
        customer = Customer(
            email=str(payload.customer.email),
            name=payload.customer.name,
            client_id=payload.customer.client_id,
        )
        items = [Item(sku=i.sku, quantity=i.quantity, price_unit=i.price_unit) for i in payload.items]

        order = service.create_order(
            external_id=payload.external_id,
            customer=customer,
            items=items,
            date=payload.date,
        )
        return {
            "external_id": order.external_id,
            "is_vip": order.is_vip,
            "arrival_date": order.arrival_date,
            "total_amount": order.total_amount,
        }
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(e))

@router.get("/report", response_model=list[ReportRowOut])
def report(service: OrdersService = Depends(get_orders_service)):
    return service.get_report()
