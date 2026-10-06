from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from app.modules.orders.models import OrderStatus


class OrderCreate(BaseModel):
    order_no: str
    product_id: int
    supplier_id: int | None = None
    quantity: int = Field(gt=0)


class OrderRead(OrderCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
    status: OrderStatus
    created_at: datetime
