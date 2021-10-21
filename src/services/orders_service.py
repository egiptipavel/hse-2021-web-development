from typing import List

from sqlalchemy.orm.session import Session

from src.db import crud
from src.schemas.error import Error
from src.schemas.response import Response
from src.services.components_service import check_component_exist
from src.services.users_service import check_user_exist


def create_order(user_id: int, components: List[int], db: Session):
    if check_user_exist(user_id, db) is False:
        return 400, Error(error="User with such id does not exist")
    for component_id in components:
        if check_component_exist(component_id, db) is False:
            return 400, Error(error="Component with such id does not exist")
    id_order = crud.create_order_to_user(db, user_id).id
    for component in components:
        crud.create_order(db, id_order, component)
    return 200, Response(response="Order created")
