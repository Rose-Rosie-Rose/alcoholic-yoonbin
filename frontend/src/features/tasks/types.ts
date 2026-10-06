// backend/app/modules/tasks/schemas.py 의 TaskRead 와 맞춘다
export type TaskStatus = 'todo' | 'in_progress' | 'done'

export const TASK_STATUS_LABEL: Record<TaskStatus, string> = {
  todo: '할 일',
  in_progress: '진행 중',
  done: '완료',
}

export type Task = {
  id: number
  title: string
  status: TaskStatus
  assignee_id: number | null
  due_date: string | null
}
