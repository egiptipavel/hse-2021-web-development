from typing import Dict, List

from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse

from src.endpoints.components import components as dictionary_of_components
from src.models.error import Error
from src.models.order import Order
from src.models.response import Response

router = APIRouter(prefix="/orders", tags=["Orders"], )

orders: Dict[int, List[Order]] = dict()

count_of_orders: List[int] = [1]


def check_availability_components(components_id: List[int]):
    for id in components_id:
        next_component = dictionary_of_components.get(id)
        if next_component is None:
            return "No component with " + str(id) + " id"
        else:
            dictionary_of_components.pop(id)


def add_order(id_user: int, components: List[int]):
    order = Order(id=count_of_orders[0], components=components)
    count_of_orders[0] += 1
    if orders.get(id_user) is not None:
        orders[id_user].append(order)
    else:
        orders[id_user] = [order]
    return "Order created"


def create(id_user: int, components: List[int]):
    result = check_availability_components(components)
    if result.__class__ == str:
        return 400, Error(error=result)
    result = add_order(id_user, components=components)
    return 200, Response(response=result)


@router.post('/', response_model=Response)
def create_order(id_user: int, components: List[int]):
    status_code, content = create(id_user, components)
    return JSONResponse(status_code=status_code, content=jsonable_encoder(content))
