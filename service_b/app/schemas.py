from pydantic import BaseModel, Field
from typing import Annotated

class Coordintas(BaseModel):
    lat: Annotated[float, Field(
        ge=-90,
        le=90
    )]
    lon: Annotated[float, Field(
        ge=-180,
        le=180
    )]
    

def is_valid_coordinates(data: dict):
    ip = next(iter(data))
    coords = data[ip]
    try:
        Coordintas.model_validate(coords)
        return True
    except (ValueError, ValueError, StopIteration):
        return False