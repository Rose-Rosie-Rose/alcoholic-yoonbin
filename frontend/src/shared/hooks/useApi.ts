import { useEffect, useState } from 'react'
import { apiGet } from '../api/client'

// GET 요청 하나를 불러와 data / error / loading 상태로 돌려준다.
export function useApi<T>(path: string) {
  const [data, setData] = useState<T | null>(null)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    let ignore = false
    apiGet<T>(path)
      .then((result) => {
        if (!ignore) setData(result)
      })
      .catch((err: Error) => {
        if (!ignore) setError(err.message)
      })
    return () => {
      ignore = true
    }
  }, [path])

  return { data, error, loading: data === null && error === null }
}
