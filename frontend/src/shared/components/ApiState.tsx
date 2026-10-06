type Props = {
  loading: boolean
  error: string | null
  empty: boolean
  emptyText?: string
}

// 목록 화면에서 공통으로 쓰는 로딩 / 에러 / 빈 목록 표시
export function ApiState({ loading, error, empty, emptyText = '데이터가 없습니다.' }: Props) {
  if (loading) return <p className="muted">불러오는 중...</p>
  if (error) return <p className="error">불러오지 못했습니다: {error}</p>
  if (empty) return <p className="muted">{emptyText}</p>
  return null
}
