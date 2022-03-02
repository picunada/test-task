from repository.colors import ColorRepository
from repository.equations import EquationRepository
from db.connect import database


def get_equations_repository() -> EquationRepository:
    return EquationRepository(database)


def get_colors_repository() -> ColorRepository:
    return ColorRepository(database)
