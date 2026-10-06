# Product OutSourcing — Chrome 확장 (옵션)

우선순위: 옵션 (`docs/planning/Product OutSourcing.md`)

외부 판매·소싱 사이트의 상품 정보를 ERP 상품 관리로 가져오는 크롬 확장 자리입니다.
본 기능(1~5순위)이 끝난 뒤 시작합니다.

시작할 때 정할 것:

- 어떤 사이트에서 어떤 정보를 가져올지
- 가져온 데이터를 `POST /api/products` 로 바로 등록할지, 검토 후 등록할지
- 빌드 도구 (Manifest V3 + Vite 등)
