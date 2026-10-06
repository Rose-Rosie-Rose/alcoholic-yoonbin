import { PageHeader } from '../../shared/components/PageHeader'
import { ApiState } from '../../shared/components/ApiState'
import { useApi } from '../../shared/hooks/useApi'
import { TASK_STATUS_LABEL, type Task } from './types'

// 담당: 미정 — 요구사항: docs/planning/Task Management.md
export function TaskListPage() {
  const { data, error, loading } = useApi<Task[]>('/tasks')

  return (
    <>
      <PageHeader title="업무 관리" description="팀 업무와 담당자, 마감일을 관리합니다." />
      <ApiState loading={loading} error={error} empty={data?.length === 0} />
      {data && data.length > 0 && (
        <table>
          <thead>
            <tr>
              <th>업무</th>
              <th>상태</th>
              <th>담당자 ID</th>
              <th>마감일</th>
            </tr>
          </thead>
          <tbody>
            {data.map((t) => (
              <tr key={t.id}>
                <td>{t.title}</td>
                <td>{TASK_STATUS_LABEL[t.status]}</td>
                <td>{t.assignee_id ?? '-'}</td>
                <td>{t.due_date ?? '-'}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </>
  )
}
