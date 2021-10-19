from fastapi import APIRouter
from fastapi import Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm.session import Session
from starlette.responses import JSONResponse

from src.models.error import Error
from src.models.response import Response
from src.sql_app import crud
from src.sql_app.database import get_db
from src.sql_app.schemas import UserCreate

router = APIRouter(prefix="/users", tags=["Users"], )


@router.post('/', response_model=Response)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    crud.create_user(db, user)


@router.get('/')
def get_all_users(db: Session = Depends(get_db)):
    return crud.get_all_users(db)


@router.get('/{id}')
def get_user_by_id(id: int, db: Session = Depends(get_db)):
    user = crud.get_user_by_id(db, id)
    if user is None:
        return JSONResponse(status_code=404, content=jsonable_encoder(Error(error="User with such id does not exist")))
    return JSONResponse(status_code=200, content=jsonable_encoder(user))


def check_user_exist(id: int, db: Session):
    user = crud.get_user_by_id(db, id)
    return user is not None
