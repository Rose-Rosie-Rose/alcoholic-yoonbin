# 기업 전사 관리 플랫폼 (ERP)

상품·주문·업무를 한곳에서 관리하는 사내 관리자 시스템입니다.

| | |
|---|---|
| 프론트엔드 | React 19 + Vite + TypeScript (`frontend/`) |
| 백엔드 | FastAPI + SQLAlchemy 2 + Alembic (`backend/`) |
| DB | SQLite(기본) / PostgreSQL(선택, `docker-compose.yml`) |
| 디자인 | [Figma 와이어프레임](https://www.figma.com/design/3lMfTE8JdR2cb7wkr8nEwe/Admin-Redesign?node-id=1-2&t=D0HdwkrkAvapqP9T-1) |

- 시스템 구조와 모듈 담당: [docs/architecture.md](docs/architecture.md)
- DB 설계 초안: [docs/erd.md](docs/erd.md)
- 브랜치·커밋·PR 규칙: [docs/conventions.md](docs/conventions.md)
- 기획 원본(Notion): [docs/planning/](docs/planning/)

## 처음 실행하기

필요한 도구: [Node.js 24](https://nodejs.org/), [uv](https://docs.astral.sh/uv/getting-started/installation/) (Python 설치와 패키지 관리를 함께 해 줍니다)

### 1. 백엔드 (터미널 1)

```bash
cd backend
cp .env.example .env          # Windows cmd: copy .env.example .env
uv sync                       # Python 3.14 + 패키지 설치 (.venv 생성)
uv run alembic upgrade head   # DB 테이블 생성 (erp.db)
uv run fastapi dev app/main.py
```

http://localhost:8000/docs 에서 API 문서를 확인할 수 있습니다.

### 2. 프론트엔드 (터미널 2)

```bash
cd frontend
npm install
npm run dev
```

http://localhost:5173 에 접속하세요. 처음에는 데이터가 없어서 목록이 비어 있습니다. API 문서(`/docs`)의 `POST /api/products`에서 상품을 하나 등록해 보세요.

## 자주 쓰는 명령

| 위치 | 명령 | 설명 |
|---|---|---|
| backend | `uv run pytest` | 테스트 |
| backend | `uv run ruff check . && uv run ruff format .` | 린트·정렬 |
| backend | `uv run alembic revision --autogenerate -m "설명"` | 모델 변경 후 마이그레이션 생성 |
| backend | `uv run alembic upgrade head` | 마이그레이션 적용 (`git pull` 후에도 실행) |
| frontend | `npm run lint` / `npm run build` | 린트 / 빌드 확인 |

## 문제 해결

- **Windows에서 `DLL load failed ... 애플리케이션 제어 정책에서 이 파일을 차단했습니다`**
  Windows 11의 스마트 앱 컨트롤이 uv가 내려받은 Python을 막은 것입니다. [python.org](https://www.python.org/downloads/)나 Python Install Manager로 Python 3.14를 설치한 뒤 다시 만드세요.
  `uv venv --clear --python <설치한 python.exe 경로>` → `uv sync`
- **다른 가상환경이 켜져 있다는 경고(`VIRTUAL_ENV ... does not match`)**: 터미널에서 `deactivate`를 실행하거나 새 터미널을 여세요.
