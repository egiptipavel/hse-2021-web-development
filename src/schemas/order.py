from pydantic import BaseModel


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
