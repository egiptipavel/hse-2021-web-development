from typing import List, Optional

from fastapi import APIRouter
from fastapi import Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm.session import Session
from starlette.responses import JSONResponse

from src.models.error import Error
from src.models.response import Response
from src.sql_app import crud
from src.sql_app.database import get_db

router = APIRouter(prefix="/orders", tags=["Orders"], )


@router.post('/', response_model=Response)
def create_order(user_id: int, components: List[int], db: Session = Depends(get_db)):
    user = crud.get_user_by_id(db, id)
    if user is None:
        return JSONResponse(status_code=400, content=jsonable_encoder(Error(error="User with such id does not exist")))
    for component_id in components:
        component = crud.get_component_by_id(db, component_id)
        if component is None:
            return JSONResponse(status_code=400,
                                content=jsonable_encoder(Error(error="Component with such id does not exist")))
    id_order = crud.create_order_to_user(db, user_id).id
    for component in components:
        crud.create_order(db, id_order, component)


@router.get('/')
def get_all_orders(user_id: Optional[int], db: Session = Depends(get_db)):
    return crud.get_all_orders(db, user_id)
