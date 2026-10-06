from pydantic import BaseModel


class DashboardSummary(BaseModel):
    product_count: int
    low_stock_count: int
    open_order_count: int
    open_task_count: int
