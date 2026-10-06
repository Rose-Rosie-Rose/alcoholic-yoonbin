import { useNavigate } from 'react-router'

// 요구사항: docs/planning/Login 및 Dashboard 공통.md
// TODO: POST /api/auth/login 연동, 토큰 저장, 로그인하지 않은 사용자 접근 차단
export function LoginPage() {
  const navigate = useNavigate()

  return (
    <div className="login">
      <form
        className="login-box"
        onSubmit={(e) => {
          e.preventDefault()
          navigate('/dashboard')
        }}
      >
        <h1>ERP 로그인</h1>
        <input name="email" type="email" placeholder="이메일" />
        <input name="password" type="password" placeholder="비밀번호" />
        <button type="submit">로그인</button>
      </form>
    </div>
  )
}
