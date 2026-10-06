import enum

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base, TimestampMixin, str_enum


class OrderStatus(enum.StrEnum):
    REQUESTED = "requested"  # 발주 요청 (상품 관리에서 '주문 필요'로 넘어온 상태)
    ORDERED = "ordered"  # 거래처에 발주 완료
    RECEIVED = "received"  # 입고 완료 → 상품 재고 증가
    CANCELLED = "cancelled"


class Order(TimestampMixin, Base):
    """발주(매입 주문). 고객 판매 주문까지 다룰지는 Order Management 기획에서 확정"""

    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    order_no: Mapped[str] = mapped_column(String(30), unique=True, index=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    supplier_id: Mapped[int | None] = mapped_column(ForeignKey("suppliers.id"))
    quantity: Mapped[int]
    status: Mapped[OrderStatus] = mapped_column(
        str_enum(OrderStatus), default=OrderStatus.REQUESTED
    )
    requested_by_id: Mapped[int | None] = mapped_column(ForeignKey("users.id"))
