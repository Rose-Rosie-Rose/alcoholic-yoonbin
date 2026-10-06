import enum
from collections.abc import Generator
from datetime import datetime

from sqlalchemy import DateTime, Enum, create_engine, func
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, sessionmaker

from app.core.config import settings

# SQLite 는 여러 스레드에서 같은 연결을 쓰려면 이 옵션이 필요하다
connect_args = {"check_same_thread": False} if settings.database_url.startswith("sqlite") else {}
engine = create_engine(settings.database_url, connect_args=connect_args)
SessionLocal = sessionmaker(bind=engine, autoflush=False)


class Base(DeclarativeBase):
    """모든 테이블 모델의 부모 클래스"""


class TimestampMixin:
    """생성·수정 시각 컬럼을 공통으로 붙인다"""

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )


def str_enum(enum_cls: type[enum.StrEnum]) -> Enum:
    """StrEnum 을 VARCHAR 컬럼으로 저장 (DB 에는 'on_sale' 처럼 값이 저장됨)"""
    return Enum(
        enum_cls,
        values_callable=lambda members: [m.value for m in members],
        native_enum=False,
        length=20,
    )


def get_db() -> Generator[Session]:
    """라우터에서 Depends(get_db) 로 받아 쓰는 DB 세션"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
