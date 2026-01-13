from fastapi import APIRouter
from services import get_coordinates_by_ip, save_ip_and_coordinates,get_all_data, test_server_b
from validation import is_valid_ip

router = APIRouter()

@router.post('/ip/{ip}')
def post_ip(ip: str):
    if not is_valid_ip(ip):
        return {"message": "The IP address you entered is invalid. Please try again with a valid address."}
    try:
        coordinates = get_coordinates_by_ip(ip)
        data = {ip: coordinates}
        response = save_ip_and_coordinates(data)
        return response
    except Exception as e: 
        return {"error": str(e)}
    

@router.get('/ip')
def get_data():
    try: 
        data = get_all_data()
        return data
    except Exception as e: 
        return {"error": str(e)}


@router.get('/')
def test():
    response = test_server_b()
    return response
