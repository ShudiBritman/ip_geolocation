from fastapi import APIRouter, HTTPException
from storage import get_all, add_item
from schemas import is_valid_coordinates

router = APIRouter()


@router.get("/ip")
def get_all_ip():
    result = get_all()
    return result


@router.post("/ip")
def add_new_item(data: dict):
    is_valid = is_valid_coordinates(data)
    if not is_valid:
        raise HTTPException(status_code=404, detail="Unprocessable Entity")
    else:
        return {"message": "ip added successfully"}