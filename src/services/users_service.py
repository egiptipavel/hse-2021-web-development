from sqlalchemy.orm.session import Session

from src.db import crud
from src.schemas.user import UserCreate
from src.schemas.response import Response


def check_user_exist(id: int, db: Session):
    user = crud.get_user_by_id(db, id)
    return user is not None


def create_user(user: UserCreate, db: Session):
    crud.create_user(db, user)
    return 200, Response(response="User account created")
