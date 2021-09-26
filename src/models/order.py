from typing import List

from pydantic.main import BaseModel


class Order(BaseModel):
    id: int
    components: List[int]
