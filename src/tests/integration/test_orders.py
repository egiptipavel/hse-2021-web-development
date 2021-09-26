from fastapi.testclient import TestClient

from src.endpoints.orders import orders, count_of_orders
from main import app
from src.tests.integration.test_components import test_add_component

client = TestClient(app)


def test_create_order_successful():
    orders.clear()
    count_of_orders.pop()
    count_of_orders.append(1)
    test_add_component()
    response = client.post("/orders/?id_user=1", json=[1])
    assert response.status_code == 200
    assert response.json() == {"response": "Order created"}


def test_create_order_not_successful():
    orders.clear()
    count_of_orders.pop()
    count_of_orders.append(1)
    response = client.post("/orders/?id_user=1", json=[1])
    assert response.status_code == 400
    assert response.json() == {"error": "No component with 1 id"}


def test_create_order_twice():
    test_create_order_successful()
    test_add_component()
    response = client.post("/orders/?id_user=1", json=[1])
    assert response.status_code == 200
    assert response.json() == {"response": "Order created"}
