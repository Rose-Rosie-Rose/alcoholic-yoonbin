import enum
from decimal import Decimal

from sqlalchemy import ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base, TimestampMixin, str_enum


class ProductStatus(enum.StrEnum):
    """Product Management.md 의 카테고리 분류 (품절, 단종, 판매예정, 판매중)"""

    ON_SALE = "on_sale"
    UPCOMING = "upcoming"
    SOLD_OUT = "sold_out"
    DISCONTINUED = "discontinued"


class Supplier(TimestampMixin, Base):
    """상품을 주문(매입)하는 거래처 — '어디에서 주문하는지'"""

    __tablename__ = "suppliers"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    contact: Mapped[str | None] = mapped_column(String(100))

    products: Mapped[list["Product"]] = relationship(back_populates="supplier")


class Product(TimestampMixin, Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    sku: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    name: Mapped[str] = mapped_column(String(200))
    category: Mapped[str | None] = mapped_column(String(50))
    status: Mapped[ProductStatus] = mapped_column(
        str_enum(ProductStatus), default=ProductStatus.ON_SALE
    )
    supplier_id: Mapped[int | None] = mapped_column(ForeignKey("suppliers.id"))
    cost_price: Mapped[Decimal] = mapped_column(Numeric(12, 2), default=0)  # 원자재 값
    sale_price: Mapped[Decimal] = mapped_column(Numeric(12, 2), default=0)
    stock_quantity: Mapped[int] = mapped_column(default=0)  # 물량
    reorder_point: Mapped[int] = mapped_column(default=0)  # 재고가 이 값 이하이면 발주 필요

    supplier: Mapped[Supplier | None] = relationship(back_populates="products")

    # TODO: 판매처(쿠팡, 에이블리 등) 목록과 판매량 — SalesChannel 테이블 설계 후 추가 (docs/erd.md)
