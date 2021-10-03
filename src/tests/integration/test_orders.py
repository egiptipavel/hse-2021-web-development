from src.endpoints.orders import create
from src.endpoints.orders import orders, count_of_orders
from src.tests.integration.test_components import test_add_component


def test_create_order_successful():
    orders.clear()
    count_of_orders.pop()
    count_of_orders.append(1)
    test_add_component()
    status_code, content = create(1, [1])
    assert status_code == 200
    assert content.response == "Order created"


def test_create_order_not_successful():
    orders.clear()
    count_of_orders.pop()
    count_of_orders.append(1)
    status_code, content = create(1, [1])
    assert status_code == 400
    assert content.error == "No component with 1 id"


def test_create_order_twice():
    test_create_order_successful()
    test_add_component()
    status_code, content = create(1, [1])
    assert status_code == 200
    assert content.response == "Order created"
