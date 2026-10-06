from pydantic import BaseModel, ConfigDict

from app.modules.products.models import ProductStatus


class ProductBase(BaseModel):
    sku: str
    name: str
    category: str | None = None
    status: ProductStatus = ProductStatus.ON_SALE
    supplier_id: int | None = None
    cost_price: float = 0
    sale_price: float = 0
    stock_quantity: int = 0
    reorder_point: int = 0


class ProductCreate(ProductBase):
    pass


class ProductRead(ProductBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
