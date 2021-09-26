from src.endpoints.orders import create
from src.endpoints.orders import orders, count_of_orders
from src.tests.integration.test_components import test_add_component


def test_create_order_successful():
    orders.clear()
    count_of_orders.pop()
    count_of_orders.append(1)
    test_add_component()
    result = create(1, [1])
    assert result.get("status_code") == 200
    assert result.get("content").get("response") == "Order created"


def test_create_order_not_successful():
    orders.clear()
    count_of_orders.pop()
    count_of_orders.append(1)
    result = create(1, [1])
    assert result.get("status_code") == 400
    assert result.get("content").get("error") == "No component with 1 id"


def test_create_order_twice():
    test_create_order_successful()
    test_add_component()
    result = create(1, [1])
    assert result.get("status_code") == 200
    assert result.get("content").get("response") == "Order created"
