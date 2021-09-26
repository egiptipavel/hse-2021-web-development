from src.endpoints.components import components, add
from src.models.component import Component


def test_add_component():
    components.clear()
    component = Component(id=1, name="name", type="type", cost=1)
    result = add(component)
    assert result.get("status_code") == 200
    assert result.get("content").get("response") == "Component added successfully"
