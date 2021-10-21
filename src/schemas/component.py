from pydantic import BaseModel


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
