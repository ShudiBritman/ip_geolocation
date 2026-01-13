from fastapi import APIRouter
from services import get_coordinates_by_ip, save_ip_and_coordinates, test_server_b

router = APIRouter()

@router.post('/ip/{ip}')
def post_ip(ip: str):
    coordinates = get_coordinates_by_ip(ip)
    data = {ip: coordinates}
    save_ip_and_coordinates(data)


@router.get('/')
def test():
    response = test_server_b()
    return response
