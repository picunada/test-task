import sqlalchemy
from .connect import metadata

colors = sqlalchemy.Table(
    "colors",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column("number", sqlalchemy.Integer, nullable=False),
    sqlalchemy.Column("attempts", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("color", sqlalchemy.String, nullable=False)
)
