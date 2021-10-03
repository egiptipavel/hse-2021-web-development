from src.endpoints.components import components, add
from src.models.component import Component


def test_add_component():
    components.clear()
    component = Component(id=1, name="name", type="type", cost=1)
    status_code, content = add(component)
    assert status_code == 200
    assert content.response == "Component added successfully"
