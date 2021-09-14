from fastapi import APIRouter
from starlette.responses import JSONResponse

from schemas.schema import Animal

router = APIRouter(prefix="/animals", tags=["Animals"], responses={404: {"description": "Not found"}}, )


@router.post('/')
def add_an_animal(animal: Animal):
    if animal.weight > 0:
        return "The " + animal.type + " weighs " + str(animal.weight) + " kg"
    else:
        return JSONResponse(status_code=400, content="Weight must be more than 0 kg")


@router.get('/{name}')
def get_an_animal(name: str):
    return {"name": name}
