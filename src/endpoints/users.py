from typing import Dict

from fastapi import APIRouter
from starlette.responses import JSONResponse

from src.models.response import Response
from src.models.user import User

router = APIRouter(prefix="/users", tags=["Users"], )

users: Dict[str, User] = dict()


def create(user: User):
    if users.get(user.login) is None:
        users[user.login] = user
        return {'status_code': 200, 'content': {"response": "Account created"}}
    else:
        return {'status_code': 400, 'content': {"error": "User with such login already exists"}}


@router.post('/', response_model=Response)
def create_user(user: User):
    user.id = len(users)
    result = create(user)
    return JSONResponse(status_code=result.get("status_code"), content=result.get("content"))
