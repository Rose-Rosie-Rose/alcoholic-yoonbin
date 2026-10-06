// backend/app/modules/orders/schemas.py 의 OrderRead 와 맞춘다
export type OrderStatus = 'requested' | 'ordered' | 'received' | 'cancelled'

export const ORDER_STATUS_LABEL: Record<OrderStatus, string> = {
  requested: '발주 요청',
  ordered: '발주 완료',
  received: '입고 완료',
  cancelled: '취소',
}

export type Order = {
  id: number
  order_no: string
  product_id: number
  supplier_id: number | null
  quantity: number
  status: OrderStatus
  created_at: string
}
