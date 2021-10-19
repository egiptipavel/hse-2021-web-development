from pydantic.main import BaseModel


class Order(BaseModel):
    id: int
    component: int
