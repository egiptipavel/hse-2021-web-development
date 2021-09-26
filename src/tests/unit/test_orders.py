from src.endpoints.components import components
from src.endpoints.orders import add_order
from src.endpoints.orders import check_availability_components
from src.endpoints.orders import orders, count_of_orders
from src.models.order import Order
from src.tests.unit.test_components import test_check_and_add_component_successful


def test_check_availability_components_simple():
    components.clear()
    assert check_availability_components([]) is None


def test_check_availability_components_successful():
    components.clear()
    test_check_and_add_component_successful()
    assert check_availability_components([1]) is None
    assert components.get(1) is None


def test_check_availability_components_not_successful():
    components.clear()
    test_check_and_add_component_successful()
    assert check_availability_components([2]) == "No component with 2 id"
    assert components.get(1) is not None


def test_add_order():
    components.clear()
    orders.clear()
    count_of_orders.pop()
    count_of_orders.append(1)
    assert add_order(1, components=[0]) == "Order created"
    assert orders.get(1) == [Order(id=1, components=[0])]
