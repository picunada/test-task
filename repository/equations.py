from typing import List, Optional

from db.equations import equations
from models.equation import Equation, EqInput
from repository.base import BaseRepository
from math import sqrt


class EquationRepository(BaseRepository):
    async def get_all(self, limit: int = 20, skip: int = 0) -> List[Equation]:
        query = equations.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query)

    async def get_by_id(self, id: int) -> Optional[Equation]:
        query = equations.select().where(equations.c.id == id)
        equation = await self.database.fetch_one(query)
        if equation is None:
            return None
        return Equation.parse_obj(equation)

    async def solution(self, e: EqInput):
        eq = Equation(
            equation="a * x ** 2 + b * x + c = 0",
            a=e.a,
            b=e.b,
            c=e.c,
            solution="0"
        )

        values = {**eq.dict()}
        values.pop("id", None)
        if values["b"] ** 2 - (4 * values["a"] * values["b"]) < 0:
            solution = "There is no solution"
            values["solution"] = solution
            eq.solution = solution
        elif values["b"] ** 2 - (4 * values["a"] * values["b"]) == 0:
            solution = -(values["b"] / 2 * values["a"])
            values["solution"] = f"solution: {solution}"
            eq.solution = f"solution: {solution}"
        else:
            solution_one = (-(values["b"]) + sqrt(values["b"] - 4 * values["a"] * values["c"])) / 2 * values["a"]
            solution_two = (-(values["b"]) - sqrt(values["b"] - 4 * values["a"] * values["c"])) / 2 * values["a"]
            values["solution"] = f"solution one: {solution_one} \n solution two: {solution_two}"
            eq.solution = f"solution one: {solution_one} \n solution two: {solution_two}"

        query = equations.insert().values(**values)
        eq.id = await self.database.execute(query)
        return eq


