from fastapi import APIRouter
from services import get_coordinates_by_ip, save_ip_and_coordinates, test_server_b

router = APIRouter()

@router.post('/ip/{ip}')
def post_ip(ip: str):
    try:
        coordinates = get_coordinates_by_ip(ip)
        data = {ip: coordinates}
        response = save_ip_and_coordinates(data)
        return response
    except Exception as e: 
        return {"message": str(e)}


@router.get('/')
def test():
    response = test_server_b()
    return response
