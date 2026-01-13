from fastapi import APIRouter, HTTPException
from . import storage
from . import schemas

router = APIRouter()


@router.get("/ip")
def get_all_ip():
    result = storage.get_all()
    return result


@router.post("/ip")
def add_new_item(data: dict):
    is_valid = schemas.is_valid_coordinates(data)
    if not is_valid:
        raise HTTPException(status_code=404, detail="Unprocessable Entity")
    else:
        result = storage.add_item(data)
        return {"message": "ip added successfully", "coordinate": result}