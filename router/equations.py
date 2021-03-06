from typing import List

from fastapi import APIRouter, Depends

from models.equation import Equation, EqInput
from repository.equations import EquationRepository
from router.depends import get_equations_repository

router = APIRouter()


@router.get("/", response_model=List[Equation])
async def read_equations(
        eq: EquationRepository = Depends(get_equations_repository),
        limit: int = 20,
        skip: int = 0):
    return await eq.get_all(limit=limit, skip=0)

@router.post("/", response_model=Equation)
async def get_solution(e: EqInput,
                       eq: EquationRepository = Depends(get_equations_repository)):
    response = await eq.solution(e)
    return response
