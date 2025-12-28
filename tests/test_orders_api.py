from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_order_vip_true():
    payload = {
        "external_id": "AMZ-999",
        "customer": {"email": "client@test.com", "name": "Juan Perez", "client_id": "123"},
        "items": [
            {"sku": "ABC-1", "quantity": 2, "price_unit": 150.0},
            {"sku": "ABC-2", "quantity": 1, "price_unit": 10.0},
        ],
        "date": "2025-10-20T14:30:00",
    }
    r = client.post("/orders", json=payload)
    assert r.status_code == 201, r.text
    data = r.json()
    assert data["is_vip"] is True
    assert data["arrival_date"].startswith("2025-10-23")  # +3 días

def test_create_order_invalid_quantity():
    payload = {
        "external_id": "BAD-1",
        "customer": {"email": "client@test.com", "name": "Juan Perez", "client_id": "123"},
        "items": [{"sku": "ABC-1", "quantity": 0, "price_unit": 150.0}],
        "date": "2025-10-20T14:30:00",
    }
    r = client.post("/orders", json=payload)
    assert r.status_code in (400, 422), r.text

def test_report_has_customer():
    # crea 2 orders
    for i in range(2):
        payload = {
            "external_id": f"RPT-{i}",
            "customer": {"email": "report@test.com", "name": "Tester", "client_id": "999"},
            "items": [{"sku": "SKU", "quantity": 1, "price_unit": 50.0}],
            "date": "2025-10-20T14:30:00",
        }
        r = client.post("/orders", json=payload)
        assert r.status_code == 201, r.text

    r = client.get("/orders/report")
    assert r.status_code == 200, r.text
    rows = r.json()
    assert any(x["customer_email"] == "report@test.com" for x in rows)
