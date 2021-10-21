from sqlalchemy.orm.session import Session

from src.db import crud
from src.schemas.component import ComponentCreate
from src.schemas.error import Error
from src.schemas.response import Response


def check_component_exist(component_id: int, db: Session):
    component = crud.get_component_by_id(db, component_id)
    return component is not None


def check_and_add_component(component: ComponentCreate, db: Session):
    status_code, content = check_component(component)
    if status_code is not None:
        return status_code, content
    crud.add_component(db, component)
    return 200, Response(response="Component added successfully")


def delete(id: int, db: Session):
    if crud.get_component_by_id(db, id) is None:
        return 400, Error(error="Component with such id does not exist")
    else:
        crud.delete_component_by_id(db, id)
        return 200, Response(response="Component has been deleted")


def get(id: int, db: Session):
    component = crud.get_component_by_id(db, id)
    if component is not None:
        return 200, component
    return 400, Error(error="No component with such id")


def check_component(component: ComponentCreate):
    if component.cost <= 0:
        return 400, Error(error="Cost must be more than 0 dollars")
    else:
        return None, None
