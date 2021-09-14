from pydantic import BaseModel


class Animal(BaseModel):
    name: str
    type: str
    weight: float
