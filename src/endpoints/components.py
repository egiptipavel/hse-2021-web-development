from fastapi import APIRouter
from fastapi import Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm.session import Session
from starlette.responses import JSONResponse

from src.models.error import Error
from src.models.response import Response
from src.sql_app import crud
from src.sql_app.database import get_db
from src.sql_app.schemas import ComponentCreate

router = APIRouter(prefix="/components", tags=["Components"], )


@router.post('/', response_model=Response)
def add_component(component: ComponentCreate, db: Session = Depends(get_db)):
    status_code, content = add(component, db)
    return JSONResponse(status_code=status_code, content=jsonable_encoder(content))


@router.get('/{id}', response_model=ComponentCreate)
def get_component(id: int, db: Session = Depends(get_db)):
    status_code, content = get(id, db)
    return JSONResponse(status_code=status_code, content=jsonable_encoder(content))


@router.delete('/{id}', response_model=Response)
def delete_component(id: int, db: Session = Depends(get_db)):
    status_code, content = delete(id, db)
    return JSONResponse(status_code=status_code, content=jsonable_encoder(content))


def check_component(component: ComponentCreate):
    if component.cost <= 0:
        return 400, Error(error="Cost must be more than 0 dollars")


def check_and_add_component(component: ComponentCreate, db: Session):
    result = check_component(component)
    if result is not None:
        return result[0], result[1]
    else:
        crud.add_component(db, component)
        return 200, Response(response="Component added successfully")


def add(component: ComponentCreate, db: Session):
    return check_and_add_component(component, db)


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
