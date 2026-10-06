import react from '@vitejs/plugin-react'
import { defineConfig } from 'vite'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
    // 개발 중 /api 요청은 FastAPI(8000)로 전달 → 프론트 코드는 항상 상대 경로 /api 사용
    proxy: {
      '/api': 'http://localhost:8000',
    },
  },
})
