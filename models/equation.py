from typing import Optional

from pydantic import BaseModel


class Equation(BaseModel):
    id: Optional[int] = None
    equation: str
    a: int
    b: int
    c: int
    solution: str


class EqInput(BaseModel):
    a: int
    b: int
    c: int
