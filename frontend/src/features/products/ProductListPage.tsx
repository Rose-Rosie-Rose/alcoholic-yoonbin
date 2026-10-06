import { useState } from 'react'
import { PageHeader } from '../../shared/components/PageHeader'
import { ApiState } from '../../shared/components/ApiState'
import { useApi } from '../../shared/hooks/useApi'
import { PRODUCT_STATUS_LABEL, type Product, type ProductStatus } from './types'

// 담당: 조윤빈 — 요구사항: docs/planning/Product Management.md
// TODO: 상품 상세 보기 방식 결정 (새 페이지 / 우측 패널 / 모달)
// TODO: 엑셀(xlsx) 다운로드 + 열 선택 기능
// TODO: 판매처 목록, 판매량 표시
export function ProductListPage() {
  const [status, setStatus] = useState<ProductStatus | 'all'>('all')
  const query = status === 'all' ? '' : `?status=${status}`
  const { data, error, loading } = useApi<Product[]>(`/products${query}`)

  return (
    <>
      <PageHeader
        title="상품 관리"
        description="판매 중인 상품 전체 목록과 발주가 필요한 상품을 확인합니다."
        actions={<button disabled>엑셀 다운로드 (준비 중)</button>}
      />

      <div className="tabs">
        <button className={status === 'all' ? 'active' : ''} onClick={() => setStatus('all')}>
          전체
        </button>
        {(Object.keys(PRODUCT_STATUS_LABEL) as ProductStatus[]).map((key) => (
          <button key={key} className={status === key ? 'active' : ''} onClick={() => setStatus(key)}>
            {PRODUCT_STATUS_LABEL[key]}
          </button>
        ))}
      </div>

      <ApiState loading={loading} error={error} empty={data?.length === 0} />
      {data && data.length > 0 && (
        <table>
          <thead>
            <tr>
              <th>SKU</th>
              <th>상품명</th>
              <th>카테고리</th>
              <th>상태</th>
              <th>원가</th>
              <th>판매가</th>
              <th>재고</th>
            </tr>
          </thead>
          <tbody>
            {data.map((p) => (
              <tr key={p.id} className={p.stock_quantity <= p.reorder_point ? 'warn' : ''}>
                <td>{p.sku}</td>
                <td>{p.name}</td>
                <td>{p.category ?? '-'}</td>
                <td>{PRODUCT_STATUS_LABEL[p.status]}</td>
                <td>{p.cost_price.toLocaleString()}</td>
                <td>{p.sale_price.toLocaleString()}</td>
                <td>{p.stock_quantity}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </>
  )
}
