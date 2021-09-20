from fastapi import APIRouter
from starlette.responses import JSONResponse

from models.components import Component

router = APIRouter(prefix="/components", tags=["Components"], )


@router.post('/')
def add_a_component(component: Component):
    if component.cost > 0:
        return "The " + component.type + " costs " + str(component.cost) + " dollars"
    else:
        return JSONResponse(status_code=400, content="Cost must be more than 0 dollars")


@router.get('/{name}')
def get_a_component(name: str):
    return {"name": name}
