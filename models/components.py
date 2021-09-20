from pydantic import BaseModel


class Component(BaseModel):
    name: str
    type: str
    cost: float
