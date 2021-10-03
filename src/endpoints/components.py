from typing import Dict

from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse

from src.models.component import Component
from src.models.error import Error
from src.models.response import Response

router = APIRouter(prefix="/components", tags=["Components"], )

components: Dict[int, Component] = dict()


@router.post('/', response_model=Response)
def add_component(component: Component):
    status_code, content = add(component)
    return JSONResponse(status_code=status_code, content=jsonable_encoder(content))


@router.put('/', response_model=Response)
def update_component(component: Component):
    status_code, content = update(component)
    return JSONResponse(status_code=status_code, content=jsonable_encoder(content))


@router.delete('/{id}', response_model=Response)
def delete_component(id: int):
    status_code, content = delete(id)
    return JSONResponse(status_code=status_code, content=jsonable_encoder(content))


@router.get('/{id}', response_model=Component)
def get_component(id: int):
    status_code, content = get(id)
    return JSONResponse(status_code=status_code, content=jsonable_encoder(content))


def check_and_add_component(component: Component):
    if component.cost <= 0:
        return 400, Error(error="Cost must be more than 0 dollars")
    else:
        components[component.id] = component
        return 200, Response(response="Component added successfully")


def add(component: Component):
    if components.get(component.id) is not None:
        return 400, Error(error="Component with such id already exists")
    return check_and_add_component(component)


def update(component: Component):
    if components.get(component.id) is None:
        return 400, Error(error="Component with such id does not exist")
    return check_and_add_component(component)


def delete(id: int):
    if components.get(id) is None:
        return 400, Error(error="Component with such id does not exist")
    else:
        components.pop(id)
        return 200, Response(response="Component has been deleted")


def get(id: int):
    for component in components.values():
        if component.id == id:
            return 200, jsonable_encoder(component)
    return 400, Error(error="No component with such id")
