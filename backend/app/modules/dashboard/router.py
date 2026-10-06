from fastapi import APIRouter, Depends
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.modules.dashboard.schemas import DashboardSummary
from app.modules.orders.models import Order, OrderStatus
from app.modules.products.models import Product
from app.modules.tasks.models import Task, TaskStatus

# 요구사항: docs/planning/Dashboard 최종.md — 각 모듈의 데이터를 읽기만 하는 집계 모듈
router = APIRouter(prefix="/dashboard", tags=["dashboard"])


@router.get("/summary", response_model=DashboardSummary)
def get_summary(db: Session = Depends(get_db)) -> DashboardSummary:
    def count(query) -> int:
        return db.scalar(select(func.count()).select_from(query.subquery())) or 0

    # TODO: 로그인 사용자 권한(UserRole)에 따라 보여줄 항목 제한
    return DashboardSummary(
        product_count=count(select(Product.id)),
        low_stock_count=count(
            select(Product.id).where(Product.stock_quantity <= Product.reorder_point)
        ),
        open_order_count=count(
            select(Order.id).where(Order.status.in_([OrderStatus.REQUESTED, OrderStatus.ORDERED]))
        ),
        open_task_count=count(select(Task.id).where(Task.status != TaskStatus.DONE)),
    )
