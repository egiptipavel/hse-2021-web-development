from sqlalchemy import Column, Integer, String, Float

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    login = Column(String, unique=True, index=True)
    password = Column(String)


class OrderToUser(Base):
    __tablename__ = "order_to_user"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, unique=False, index=True)
    component = Column(Integer)


class Component(Base):
    __tablename__ = "components"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    type = Column(String)
    cost = Column(Float)
