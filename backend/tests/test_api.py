def test_health(client):
    assert client.get("/api/health").json() == {"status": "ok"}


def test_product_create_and_filter(client):
    body = {"sku": "P-001", "name": "테스트 상품", "stock_quantity": 2, "reorder_point": 5}
    created = client.post("/api/products", json=body)
    assert created.status_code == 201
    assert created.json()["status"] == "on_sale"

    assert len(client.get("/api/products?status=on_sale").json()) == 1
    assert client.get("/api/products?status=sold_out").json() == []
    assert client.get("/api/products/999").status_code == 404


def test_dashboard_summary(client):
    client.post(
        "/api/products", json={"sku": "P-001", "name": "A", "stock_quantity": 1, "reorder_point": 3}
    )
    product_id = client.get("/api/products").json()[0]["id"]
    client.post("/api/orders", json={"order_no": "PO-1", "product_id": product_id, "quantity": 10})
    client.post("/api/tasks", json={"title": "재고 확인"})

    assert client.get("/api/dashboard/summary").json() == {
        "product_count": 1,
        "low_stock_count": 1,
        "open_order_count": 1,
        "open_task_count": 1,
    }


def test_login_not_implemented(client):
    res = client.post("/api/auth/login", json={"email": "a@example.com", "password": "x"})
    assert res.status_code == 501
