from pydantic import BaseModel


class Component(BaseModel):
    id: int
    name: str
    type: str
    cost: float
