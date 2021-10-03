from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    id: Optional[int]
    login: str
    password: str
