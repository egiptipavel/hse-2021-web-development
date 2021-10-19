from sqlalchemy.orm import Session

from . import models, schemas


def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(login=user.login, password=user.password)
    db.add(db_user)
    db.commit()


def get_all_users(db: Session):
    return db.query(models.User).all()


def create_order_to_user(db: Session, user_id: int):
    db_order_to_user = models.OrderToUser(user_id=user_id)
    db.add(db_order_to_user)
    db.commit()
    db.refresh(db_order_to_user)
    return db_order_to_user


def create_order(db: Session, id_order: int, component: int):
    db_order = models.Order(id=id_order, component=component)
    db.add(db_order)
    db.commit()


def get_all_orders(db: Session, user_id: int = None):
    if user_id is None:
        return db.query(models.OrderToUser).all()
    else:
        return db.query(models.OrderToUser).filter(models.OrderToUser.user_id == user_id).all()


def get_component_by_id(db: Session, component_id: int):
    return db.query(models.Component).filter(models.Component.id == component_id).first()


def add_component(db: Session, component: schemas.ComponentCreate):
    db_component = models.Component(name=component.name, type=component.type, cost=component.cost)
    db.add(db_component)
    db.commit()


def delete_component_by_id(db: Session, component_id):
    db_component = get_component_by_id(db, component_id)
    db.delete(db_component)
    db.commit()
