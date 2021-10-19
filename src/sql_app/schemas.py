from pydantic import BaseModel


class UserBase(BaseModel):
    login: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class OrderBase(BaseModel):
    pass


class OrderCreate(OrderBase):
    component: int


class Order(OrderBase):
    id: int

    class Config:
        orm_mode = True


class OrderToUserBase(BaseModel):
    pass


class OrderToUserCreate(OrderToUserBase):
    user_id: int


class OrderToUser(OrderToUserBase):
    id: int

    class Config:
        orm_mode = True


class ComponentBase(BaseModel):
    pass


class ComponentCreate(ComponentBase):
    name: str
    type: str
    cost: float


class Component(ComponentBase):
    id: int

    class Config:
        orm_mode = True
