from fastapi import APIRouter
from fastapi import Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm.session import Session
from starlette.responses import JSONResponse

from src.db import crud
from src.db.database import get_db
from src.schemas.error import Error
from src.schemas.response import Response
from src.schemas.user import UserCreate
from src.services import users_service

router = APIRouter(prefix="/users", tags=["Users"], )


@router.post('/', response_model=Response)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    status_code, content = users_service.create_user(user, db)
    return JSONResponse(status_code=status_code, content=jsonable_encoder(content))


@router.get('/')
def get_all_users(db: Session = Depends(get_db)):
    return crud.get_all_users(db)


@router.get('/{id}')
def get_user_by_id(id: int, db: Session = Depends(get_db)):
    user = crud.get_user_by_id(db, id)
    if user is None:
        return JSONResponse(status_code=404, content=jsonable_encoder(Error(error="User with such id does not exist")))
    return JSONResponse(status_code=200, content=jsonable_encoder(user))
