// 모든 API 호출이 거치는 공통 함수. 인증 토큰, 에러 처리 등은 여기서 한 번에 처리한다.
export async function apiGet<T>(path: string): Promise<T> {
  const res = await fetch(`/api${path}`)
  if (!res.ok) {
    throw new Error(`API ${res.status}: ${path}`)
  }
  return res.json() as Promise<T>
}
