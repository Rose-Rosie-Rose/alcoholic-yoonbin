import { PageHeader } from '../../shared/components/PageHeader'
import { ApiState } from '../../shared/components/ApiState'
import { useApi } from '../../shared/hooks/useApi'

// backend/app/modules/dashboard/schemas.py 의 DashboardSummary 와 맞춘다
type DashboardSummary = {
  product_count: number
  low_stock_count: number
  open_order_count: number
  open_task_count: number
}

const CARDS: { key: keyof DashboardSummary; label: string }[] = [
  { key: 'product_count', label: '전체 상품' },
  { key: 'low_stock_count', label: '발주 필요 상품' },
  { key: 'open_order_count', label: '진행 중 주문' },
  { key: 'open_task_count', label: '진행 중 업무' },
]

// 요구사항: docs/planning/Dashboard 최종.md — TODO: 사용자 권한별로 보이는 카드 다르게
export function DashboardPage() {
  const { data, error, loading } = useApi<DashboardSummary>('/dashboard/summary')

  return (
    <>
      <PageHeader title="대시보드" />
      <ApiState loading={loading} error={error} empty={false} />
      {data && (
        <div className="cards">
          {CARDS.map((card) => (
            <div key={card.key} className="card">
              <div className="muted">{card.label}</div>
              <div className="card-value">{data[card.key]}</div>
            </div>
          ))}
        </div>
      )}
    </>
  )
}
