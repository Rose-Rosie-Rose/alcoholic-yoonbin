// backend/app/modules/products/schemas.py 의 ProductRead 와 맞춘다
export type ProductStatus = 'on_sale' | 'upcoming' | 'sold_out' | 'discontinued'

export const PRODUCT_STATUS_LABEL: Record<ProductStatus, string> = {
  on_sale: '판매중',
  upcoming: '판매예정',
  sold_out: '품절',
  discontinued: '단종',
}

export type Product = {
  id: number
  sku: string
  name: string
  category: string | null
  status: ProductStatus
  supplier_id: number | null
  cost_price: number
  sale_price: number
  stock_quantity: number
  reorder_point: number
}
