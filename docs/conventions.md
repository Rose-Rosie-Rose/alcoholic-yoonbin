# 협업 규칙

## 브랜치

```
main            항상 실행되는 상태. 직접 push 하지 않고 PR 로만 합친다
└─ feat/<모듈>-<내용>    예: feat/products-status-filter
└─ fix/<모듈>-<내용>     예: fix/orders-quantity-validation
└─ docs/<내용>           예: docs/erd-sales-channel
```

1. `main`을 최신으로 받기: `git switch main && git pull`
2. 브랜치 만들기: `git switch -c feat/products-excel-export`
3. 작업하고 커밋 → `git push -u origin feat/products-excel-export`
4. GitHub에서 PR 생성 → 상대방이 리뷰 → CI 통과 확인 → **Squash and merge**
5. 합친 브랜치는 삭제

## 커밋 메시지

```
<타입>(<모듈>): <무엇을 했는지>

feat(products): 상품 목록 상태 필터 추가
fix(orders): 수량 0 이하 입력 막기
docs(erd): 판매처 테이블 초안 추가
chore: ruff 설정 변경
```

| 타입 | 의미 |
|---|---|
| `feat` | 새 기능 |
| `fix` | 버그 수정 |
| `refactor` | 동작은 같고 코드 구조만 변경 |
| `docs` | 문서 |
| `test` | 테스트 |
| `chore` | 설정, 의존성 등 |

## 충돌을 줄이는 규칙

- **자기 모듈 폴더 안에서 작업**합니다. 상품 담당은 `modules/products`와 `features/products`, 주문 담당은 `modules/orders`와 `features/orders`.
- 공통 파일(`main.py`, `app/models.py`, `router.tsx`, `AppLayout.tsx`, `shared/`, `index.css`)은 **한 줄 추가 정도로만** 고치고, 크게 바꿀 때는 미리 말합니다.
- **DB 마이그레이션 파일이 동시에 생기면 충돌**합니다. 모델을 바꾸는 PR은 되도록 빨리 합치고, 다른 사람은 합쳐진 뒤 `git pull` → `uv run alembic upgrade head`를 실행합니다.
  - 두 사람의 마이그레이션이 겹쳐 "multiple heads" 오류가 나면 `uv run alembic merge heads -m "merge"`로 합칩니다.
- API 응답 형식을 바꾸면 `frontend/src/features/<모듈>/types.ts`도 같은 PR에서 고칩니다.

## 코드 스타일

- 백엔드: `uv run ruff check .` + `uv run ruff format .` (VS Code에서는 저장할 때 자동 정렬)
- 프론트: `npm run lint`
- 화면에 보이는 문구와 주석은 한국어, 변수·함수·파일 이름은 영어
- 비밀번호나 API 키는 `.env`에만 둡니다. `.env`는 git에 올라가지 않습니다.
