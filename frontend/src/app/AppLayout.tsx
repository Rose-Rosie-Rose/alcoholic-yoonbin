import { NavLink, Outlet } from 'react-router'

const NAV_ITEMS = [
  { to: '/dashboard', label: '대시보드' },
  { to: '/products', label: '상품 관리' },
  { to: '/orders', label: '주문 관리' },
  { to: '/tasks', label: '업무 관리' },
]

// 로그인 후 모든 화면이 공유하는 틀 (사이드바 + 본문)
export function AppLayout() {
  return (
    <div className="layout">
      <aside className="sidebar">
        <div className="brand">ERP</div>
        <nav>
          {NAV_ITEMS.map((item) => (
            <NavLink key={item.to} to={item.to} className="nav-link">
              {item.label}
            </NavLink>
          ))}
        </nav>
      </aside>
      <main className="content">
        <Outlet />
      </main>
    </div>
  )
}
