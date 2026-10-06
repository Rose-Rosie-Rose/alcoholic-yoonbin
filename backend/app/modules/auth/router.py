from fastapi import APIRouter, HTTPException, status

from app.modules.auth.schemas import LoginRequest, TokenResponse

# 요구사항: docs/planning/Login 및 Dashboard 공통.md
router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", response_model=TokenResponse)
def login(body: LoginRequest) -> TokenResponse:
    # TODO: 비밀번호 해시 검증 + JWT 발급 (예: pwdlib, pyjwt)
    raise HTTPException(status.HTTP_501_NOT_IMPLEMENTED, "로그인은 아직 구현되지 않았습니다.")
