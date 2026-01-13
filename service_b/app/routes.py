from fastapi import APIRouter
from storage import get_all, add_item


router = APIRouter()


@router.get("/ip")
def get_all_ip():
    result = get_all()
    return result