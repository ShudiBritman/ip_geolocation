import requests 
import os
from fastapi import HTTPException


def get_coordinates_by_ip(ip: str) -> dict: 
    try:
        response = requests.get(f'http://ip-api.com/json/{ip}') 
        data = response.json()
        coordinates = {'lat': data['lat'],'lon': data['lon']}
        return coordinates
    except Exception: 
        raise HTTPException(status_code=500, detail="An error from ip-api.com")


def get_server_b_base_url():
    host = os.getenv('HOST_SERVER_B', 'localhost')
    port = int(os.getenv('PORT_SERVER_B', 8080))
    base_url = f'http://{host}:{port}/'
    return base_url


def save_ip_and_coordinates(data: dict):
    base_url = get_server_b_base_url()
    try:
        response = requests.post(url=f'{base_url}/ip', json=data)
        return response.json()
    except HTTPException:
        raise
    except Exception: 
        raise HTTPException(status_code=500, detail="An error to save data")


def get_all_data():
    base_url = get_server_b_base_url()
    try:
        response = requests.get(url=f'{base_url}/ip')
        return response.json()
    except HTTPException:
        raise
    except Exception: 
        raise HTTPException(status_code=500, detail="An error to load data")



def test_server_b():
    base_url = get_server_b_base_url()
    response = requests.get(url=base_url)
    return response.json()
