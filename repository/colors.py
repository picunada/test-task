from typing import Optional

from core.utils import find_color
from db.colors import colors
from models.color import Color, ColorInput
from repository.base import BaseRepository


class ColorRepository(BaseRepository):
    async def get_all(self, limit: int = 20, skip: int = 0) -> Optional[Color]:
        query = colors.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query)

    async def get_by_id(self, id: int) -> Optional[Color]:
        query = colors.select().where(colors.c.id == id)
        equation = await self.database.fetch_one(query)
        if equation is None:
            return None
        return Color.parse_obj(equation)

    async def guess_color(self, c: ColorInput):
        color = Color(
            number=c.number,
            attempts="None",
            color="None"
        )

        result = find_color(c.number)

        values = {**color.dict()}
        values.pop("id", None)
        values["attempts"] = result[0]
        values["color"] = result[1]

        query = colors.insert().values(**values)

        color.attempts = result[0]
        color.color = result[1]
        color.id = await self.database.execute(query=query)

        return color
