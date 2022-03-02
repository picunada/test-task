from typing import Optional

from pydantic import BaseModel, Field, validator


class Color(BaseModel):
    id: Optional[int]
    number: int
    attempts: str
    color: str

class ColorInput(BaseModel):
    number: int
