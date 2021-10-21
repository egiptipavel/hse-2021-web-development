from fastapi import APIRouter
from fastapi import Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm.session import Session
from starlette.responses import JSONResponse

from src.db.database import get_db
from src.schemas.component import ComponentCreate
from src.services import components_service

router = APIRouter(prefix="/components", tags=["Components"], )


@router.post('/')
def add_component(component: ComponentCreate, db: Session = Depends(get_db)):
    status_code, content = components_service.check_and_add_component(component, db)
    return JSONResponse(status_code=status_code, content=jsonable_encoder(content))


@router.get('/{id}')
def get_component(id: int, db: Session = Depends(get_db)):
    status_code, content = components_service.get(id, db)
    return JSONResponse(status_code=status_code, content=jsonable_encoder(content))


@router.delete('/{id}')
def delete_component(id: int, db: Session = Depends(get_db)):
    status_code, content = components_service.delete(id, db)
    return JSONResponse(status_code=status_code, content=jsonable_encoder(content))
