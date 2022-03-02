import sqlalchemy
from .connect import metadata

equations = sqlalchemy.Table(
    "equations",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column("equation", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("a", sqlalchemy.Integer, nullable=False),
    sqlalchemy.Column("b", sqlalchemy.Integer, nullable=False),
    sqlalchemy.Column("c", sqlalchemy.Integer, nullable=False),
    sqlalchemy.Column("solution", sqlalchemy.String, nullable=False)
)