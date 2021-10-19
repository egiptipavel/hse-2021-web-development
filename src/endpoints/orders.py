from typing import List, Optional

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm.session import Session
from starlette.responses import JSONResponse

from src.models.response import Response
from src.services import orders_service
from src.sql_app import crud
from src.sql_app.database import get_db

router = APIRouter(prefix="/orders", tags=["Orders"], )


@router.post('/', response_model=Response)
def create_order(user_id: int, components: List[int], db: Session = Depends(get_db)):
    status_code, content = orders_service.create_order(user_id, components, db)
    return JSONResponse(status_code=status_code, content=content)


@router.get('/')
def get_all_orders(user_id: Optional[int], db: Session = Depends(get_db)):
    return crud.get_all_orders(db, user_id)
