from fastapi.encoders import jsonable_encoder
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from ...models.error import Error
from ...models.response import Response
from ...services import orders_service
from ...sql_app import crud
from ...sql_app import models
from ...sql_app.database import Base
from ...sql_app.schemas import UserCreate, ComponentCreate

SQLALCHEMY_DATABASE_URL = "postgresql://hse:password@localhost:5433/test_db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

db: Session = TestingSessionLocal()


def delete_from_table(table):
    db.query(table).delete(synchronize_session='fetch')
    db.commit()


def test_create_order_successful():
    delete_from_table(models.User)
    delete_from_table(models.Component)
    delete_from_table(models.Order)
    delete_from_table(models.OrderToUser)
    user_id = crud.create_user(db, UserCreate(password="password", **{"login": "login"})).id
    component_id = crud.add_component(db, ComponentCreate(name="name", type="type", cost=1.0)).id
    status_code, content = orders_service.create_order(user_id, [component_id], db)
    assert status_code == 200
    assert content == jsonable_encoder(Response(response="Order created"))
    result = db.query(models.Order).filter(models.Order.component == component_id).all()
    assert len(result) == 1
    order_id = result[0].id
    result = db.query(models.OrderToUser).filter(models.OrderToUser.user_id == user_id).all()
    assert len(result) == 1
    assert result[0].id == order_id


def test_create_order_not_successful():
    delete_from_table(models.User)
    delete_from_table(models.Component)
    delete_from_table(models.Order)
    delete_from_table(models.OrderToUser)
    component_id = crud.add_component(db, ComponentCreate(name="name", type="type", cost=1.0)).id
    status_code, content = orders_service.create_order(1, [component_id], db)
    assert status_code == 400
    assert content == jsonable_encoder(Error(error="User with such id does not exist"))
    result = db.query(models.Order).filter(models.Order.component == component_id).all()
    assert len(result) == 0
    result = db.query(models.OrderToUser).filter(models.OrderToUser.user_id == 1).all()
    assert len(result) == 0
