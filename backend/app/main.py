from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.modules.auth.router import router as auth_router
from app.modules.dashboard.router import router as dashboard_router
from app.modules.orders.router import router as orders_router
from app.modules.products.router import router as products_router
from app.modules.tasks.router import router as tasks_router

app = FastAPI(title="ERP API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 모든 API 는 /api 아래에 둔다 (프론트 vite proxy 설정과 맞춤)
api = APIRouter(prefix="/api")


@api.get("/health", tags=["system"])
def health() -> dict[str, str]:
    return {"status": "ok"}


for module_router in (auth_router, products_router, orders_router, tasks_router, dashboard_router):
    api.include_router(module_router)

app.include_router(api)
