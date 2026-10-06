from fastapi import APIRouter, Depends, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.modules.tasks.models import Task
from app.modules.tasks.schemas import TaskCreate, TaskRead

# 담당: 미정 — 요구사항: docs/planning/Task Management.md
router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("", response_model=list[TaskRead])
def list_tasks(db: Session = Depends(get_db)) -> list[Task]:
    return list(db.scalars(select(Task).order_by(Task.id)))


@router.post("", response_model=TaskRead, status_code=status.HTTP_201_CREATED)
def create_task(body: TaskCreate, db: Session = Depends(get_db)) -> Task:
    task = Task(**body.model_dump())
    db.add(task)
    db.commit()
    db.refresh(task)
    return task
