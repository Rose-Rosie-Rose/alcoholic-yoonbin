import { createBrowserRouter, Navigate } from 'react-router'
import { AppLayout } from './AppLayout'
import { LoginPage } from '../features/auth/LoginPage'
import { DashboardPage } from '../features/dashboard/DashboardPage'
import { ProductListPage } from '../features/products/ProductListPage'
import { OrderListPage } from '../features/orders/OrderListPage'
import { TaskListPage } from '../features/tasks/TaskListPage'

// 새 화면을 추가할 때는 features/<모듈>/ 에 페이지를 만들고 여기와 AppLayout의 NAV_ITEMS에 등록
export const router = createBrowserRouter([
  { path: '/login', element: <LoginPage /> },
  {
    path: '/',
    element: <AppLayout />,
    children: [
      { index: true, element: <Navigate to="/dashboard" replace /> },
      { path: 'dashboard', element: <DashboardPage /> },
      { path: 'products', element: <ProductListPage /> },
      { path: 'orders', element: <OrderListPage /> },
      { path: 'tasks', element: <TaskListPage /> },
    ],
  },
])
