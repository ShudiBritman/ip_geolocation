from fastapi import APIRouter, HTTPException
from app.services import get_coordinates_by_ip, save_ip_and_coordinates, get_all_data
from .validation import is_valid_ip

router = APIRouter()

@router.post('/ip/{ip}')
def post_ip(ip: str):
    if not is_valid_ip(ip):
        raise HTTPException(status_code=400, detail="invalid IP")
    try:
        coordinates = get_coordinates_by_ip(ip)
        data = {ip: coordinates}
        response = save_ip_and_coordinates(data)
        return response
    except HTTPException: 
        raise
    except Exception: 
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get('/ip')
def list_ips():
    try: 
        data = get_all_data()
        return data
    except HTTPException: 
        raise
    except Exception: 
        raise HTTPException(status_code=500, detail="Internal server error")



