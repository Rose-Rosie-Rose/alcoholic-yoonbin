import { PageHeader } from '../../shared/components/PageHeader'
import { ApiState } from '../../shared/components/ApiState'
import { useApi } from '../../shared/hooks/useApi'
import { ORDER_STATUS_LABEL, type Order } from './types'

// 담당: 강경원 — 요구사항: docs/planning/Order Management.md
export function OrderListPage() {
  const { data, error, loading } = useApi<Order[]>('/orders')

  return (
    <>
      <PageHeader title="주문 관리" description="발주 요청부터 입고까지 주문 진행 상황을 관리합니다." />
      <ApiState loading={loading} error={error} empty={data?.length === 0} />
      {data && data.length > 0 && (
        <table>
          <thead>
            <tr>
              <th>주문번호</th>
              <th>상품 ID</th>
              <th>수량</th>
              <th>상태</th>
              <th>생성일</th>
            </tr>
          </thead>
          <tbody>
            {data.map((o) => (
              <tr key={o.id}>
                <td>{o.order_no}</td>
                <td>{o.product_id}</td>
                <td>{o.quantity}</td>
                <td>{ORDER_STATUS_LABEL[o.status]}</td>
                <td>{new Date(o.created_at).toLocaleDateString()}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </>
  )
}
