from fastapi import APIRouter, Depends, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.modules.orders.models import Order
from app.modules.orders.schemas import OrderCreate, OrderRead

# 담당: 강경원 — 요구사항: docs/planning/Order Management.md
router = APIRouter(prefix="/orders", tags=["orders"])


@router.get("", response_model=list[OrderRead])
def list_orders(db: Session = Depends(get_db)) -> list[Order]:
    return list(db.scalars(select(Order).order_by(Order.id.desc())))


@router.post("", response_model=OrderRead, status_code=status.HTTP_201_CREATED)
def create_order(body: OrderCreate, db: Session = Depends(get_db)) -> Order:
    order = Order(**body.model_dump())
    db.add(order)
    db.commit()
    db.refresh(order)
    return order


# TODO: PATCH /orders/{id}/status — 상태 변경, RECEIVED 시 상품 재고 증가
