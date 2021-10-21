from fastapi.encoders import jsonable_encoder

from src.db import crud, models
from ..database_for_tests import db
from ...schemas.component import ComponentCreate
from ...schemas.error import Error
from ...schemas.response import Response
from ...schemas.user import UserCreate
from ...services import orders_service


def delete_data_from_table():
    db.query(models.Order).delete(synchronize_session='fetch')
    db.commit()
    db.query(models.User).delete(synchronize_session='fetch')
    db.commit()
    db.query(models.OrderToUser).delete(synchronize_session='fetch')
    db.commit()
    db.query(models.Component).delete(synchronize_session='fetch')
    db.commit()


def test_create_order_successful():
    delete_data_from_table()
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
    delete_data_from_table()
    component_id = crud.add_component(db, ComponentCreate(name="name", type="type", cost=1.0)).id
    status_code, content = orders_service.create_order(1, [component_id], db)
    assert status_code == 400
    assert content == jsonable_encoder(Error(error="User with such id does not exist"))
    result = db.query(models.Order).filter(models.Order.component == component_id).all()
    assert len(result) == 0
    result = db.query(models.OrderToUser).filter(models.OrderToUser.user_id == 1).all()
    assert len(result) == 0
