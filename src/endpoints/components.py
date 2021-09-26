from typing import Dict

from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse

from src.models.component import Component
from src.models.response import Response

router = APIRouter(prefix="/components", tags=["Components"], )

components: Dict[int, Component] = dict()


@router.post('/', response_model=Response)
def add_component(component: Component):
    result = add(component)
    return JSONResponse(status_code=result.get("status_code"), content=result.get("content"))


@router.put('/', response_model=Response)
def update_component(component: Component):
    result = update(component)
    return JSONResponse(status_code=result.get("status_code"), content=result.get("content"))


@router.delete('/{id}', response_model=Response)
def delete_component(id: int):
    result = delete(id)
    return JSONResponse(status_code=result.get("status_code"), content=result.get("content"))


@router.get('/{id}', response_model=Component)
def get_component(id: int):
    result = get(id)
    return JSONResponse(status_code=result.get("status_code"), content=result.get("content"))


def check_and_add_component(component: Component):
    if component.cost <= 0:
        return {'status_code': 400, 'content': {"error": "Cost must be more than 0 dollars"}}
    else:
        components[component.id] = component
        return {'status_code': 200,
                'content': {"response": "Component added successfully"}}


def add(component: Component):
    if components.get(component.id) is not None:
        return {'status_code': 400, 'content': {"error": "Component with such id already exists"}}
    return check_and_add_component(component)


def update(component: Component):
    if components.get(component.id) is None:
        return {'status_code': 400, 'content': {"error": "Component with such id does not exist"}}
    return check_and_add_component(component)


def delete(id: int):
    if components.get(id) is None:
        return {'status_code': 400, 'content': {"error": "Component with such id does not exist"}}
    else:
        components.pop(id)
        return {'status_code': 200, 'content': {"response": "Component has been deleted"}}


def get(id: int):
    for component in components.values():
        if component.id == id:
            return {'status_code': 200, 'content': jsonable_encoder(component)}
    return {'status_code': 400, 'content': {"error": "No component with such id"}}
