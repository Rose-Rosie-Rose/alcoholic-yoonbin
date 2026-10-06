"""모든 테이블 모델을 한곳에서 import — Alembic 이 테이블을 찾을 수 있도록.

새 모듈에 models.py 를 만들면 여기에 한 줄 추가하세요.
"""

from app.core.database import Base
from app.modules.auth.models import User
from app.modules.orders.models import Order
from app.modules.products.models import Product, Supplier
from app.modules.tasks.models import Task

__all__ = ["Base", "Order", "Product", "Supplier", "Task", "User"]
