from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient

from src.endpoints.components import components
from main import app
from src.models.component import Component
from src.models.response import Response

client = TestClient(app)


def test_add_component():
    components.clear()
    component = Component(id=1, name="name", type="type", cost=1)
    body_of_response = Response(response="Component added successfully")
    response = client.post("/components/", json=jsonable_encoder(component))
    assert response.status_code == 200
    assert response.json() == body_of_response
