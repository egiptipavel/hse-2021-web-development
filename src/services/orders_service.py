from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm.session import Session

from src.endpoints.components import check_component_exist
from src.endpoints.users import check_user_exist
from src.models.error import Error
from src.models.response import Response
from src.sql_app import crud


def create_order(user_id: int, components: List[int], db: Session):
    if check_user_exist(user_id, db) is False:
        return 400, jsonable_encoder(Error(error="User with such id does not exist"))
    for component_id in components:
        if check_component_exist(component_id, db) is False:
            return 400, jsonable_encoder(Error(error="Component with such id does not exist"))
    id_order = crud.create_order_to_user(db, user_id).id
    for component in components:
        crud.create_order(db, id_order, component)
    return 200, jsonable_encoder(Response(response="Order created"))
