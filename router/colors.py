from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from models.color import Color, ColorInput
from repository.colors import ColorRepository
from router.depends import get_colors_repository

router = APIRouter()


@router.get("/", response_model=List[Color])
async def get_all(
        colors: ColorRepository = Depends(get_colors_repository),
        limit: int = 20,
        skip: int = 0):
    return await colors.get_all(limit=limit, self=0)


@router.get(f"/{id}", response_model=Color)
async def get_by_id(id: int, colors: ColorRepository = Depends(get_colors_repository)):
    response = colors.get_by_id(id)
    return response


@router.post("/", response_model=Color)
async def guess_the_color(e: ColorInput,
                          colors: ColorRepository = Depends(get_colors_repository)):
    if e.number not in range(0, 100):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Number out of range (0, 100)")

    response = await colors.guess_color(e)

    return response
