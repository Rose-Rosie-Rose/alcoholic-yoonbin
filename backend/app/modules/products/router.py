from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.modules.products.models import Product, ProductStatus
from app.modules.products.schemas import ProductCreate, ProductRead

# 담당: 조윤빈 — 요구사항: docs/planning/Product Management.md
router = APIRouter(prefix="/products", tags=["products"])


@router.get("", response_model=list[ProductRead])
def list_products(
    status: ProductStatus | None = None, db: Session = Depends(get_db)
) -> list[Product]:
    query = select(Product).order_by(Product.id)
    if status:
        query = query.where(Product.status == status)
    return list(db.scalars(query))


@router.post("", response_model=ProductRead, status_code=status.HTTP_201_CREATED)
def create_product(body: ProductCreate, db: Session = Depends(get_db)) -> Product:
    product = Product(**body.model_dump())
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


@router.get("/{product_id}", response_model=ProductRead)
def get_product(product_id: int, db: Session = Depends(get_db)) -> Product:
    product = db.get(Product, product_id)
    if product is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "상품을 찾을 수 없습니다.")
    return product


# TODO: GET /products/export — 열을 선택해서 xlsx 다운로드 (예: openpyxl)
