from .equations import equations
from .colors import colors
from .connect import metadata, engine

metadata.create_all(bind=engine)
