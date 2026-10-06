from datetime import date

from pydantic import BaseModel, ConfigDict

from app.modules.tasks.models import TaskStatus


class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    assignee_id: int | None = None
    due_date: date | None = None


class TaskRead(TaskCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
    status: TaskStatus
