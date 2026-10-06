import enum

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base, TimestampMixin, str_enum


class UserRole(enum.StrEnum):
    """사용자 권한 — Dashboard 최종의 'DB USER 별 권한 부여'에 사용"""

    ADMIN = "admin"
    MANAGER = "manager"
    STAFF = "staff"


class User(TimestampMixin, Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    name: Mapped[str] = mapped_column(String(50))
    hashed_password: Mapped[str] = mapped_column(String(255))
    role: Mapped[UserRole] = mapped_column(str_enum(UserRole), default=UserRole.STAFF)
    is_active: Mapped[bool] = mapped_column(default=True)
