from fastapi import APIRouter
from services import get_coordinates_by_ip, save_ip_and_coordinates, test_server_b

router = APIRouter()

@router.post('/ip/{ip}')
def post_ip(ip: str):
    data = get_coordinates_by_ip(ip)
    save_ip_and_coordinates(data)


@router.get('/')
def test():
    return test_server_b
