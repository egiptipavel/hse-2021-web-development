from src.endpoints.components import check_and_add_component, add, get, delete
from src.endpoints.components import components as dictionary
from src.models.component import Component


def test_check_and_add_component_not_successful():
    dictionary.clear()
    component = Component(**{"id": 1, "name": "name", "type": "type", "cost": -1})
    status_code, content = check_and_add_component(component)
    assert status_code == 400
    assert content.error == "Cost must be more than 0 dollars"


def test_check_and_add_component_successful():
    dictionary.clear()
    component = Component(**{"id": 1, "name": "name", "type": "type", "cost": 1})
    status_code, content = check_and_add_component(component)
    assert status_code == 200
    assert content.response == "Component added successfully"


def test_add_successful():
    dictionary.clear()
    component = Component(**{"id": 1, "name": "name", "type": "type", "cost": 1})
    status_code, content = add(component)
    assert status_code == 200
    assert content.response == "Component added successfully"


def test_add_not_successful():
    dictionary.clear()
    component = Component(**{"id": 1, "name": "name", "type": "type", "cost": 0})
    status_code, content = add(component)
    assert status_code == 400
    assert content.error == "Cost must be more than 0 dollars"


def test_add_twice():
    dictionary.clear()
    component = Component(**{"id": 0, "name": "name", "type": "type", "cost": 1})
    status_code, content = add(component)
    assert status_code == 200
    assert content.response == "Component added successfully"
    status_code, content = add(component)
    assert status_code == 400
    assert content.error == "Component with such id already exists"


def test_update():
    dictionary.clear()
    component = Component(**{"id": 0, "name": "name", "type": "type", "cost": 0})
    status_code, content = add(component)
    assert status_code == 400
    assert content.error == "Cost must be more than 0 dollars"


def test_delete_successful():
    dictionary.clear()
    component = Component(**{"id": 1, "name": "name", "type": "type", "cost": 1})
    add(component)
    status_code, content = delete(1)
    assert status_code == 200
    assert content.response == "Component has been deleted"


def test_delete_not_successful():
    dictionary.clear()
    status_code, content = delete(1)
    assert status_code == 400
    assert content.error == "Component with such id does not exist"


def test_get_component_successful():
    dictionary.clear()
    component = Component(**{"id": 1, "name": "name", "type": "type", "cost": 1})
    add(component)
    status_code, content = get(1)
    assert status_code == 200
    assert content == component


def test_get_component_not_successful():
    dictionary.clear()
    status_code, content = get(1)
    assert status_code == 400
    assert content.error == "No component with such id"
