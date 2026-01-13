import requests 
import os
 


def get_coordinates_by_ip(ip: str) -> dict: 
    response = requests.get(f'http://ip-api.com/json/#{ip}') 
    data = response.json()
    coordinates = {'lat': data['lat'],'lon': data['lon']}
    return coordinates


def save_ip_and_coordinates(data: dict):
    host = os.getenv('HOST_SERVER_B', 'localhost')
    port = int(os.getenv('PORT_SERVER_B', '8080'))
    response = requests.post(url=f'http://{host}:{port}', json=data)


def test_server_b():
    host = os.getenv('HOST', 'localhost')
    port = int(os.getenv('PORT', '8080'))
    response = requests.get(url=f'http://{host}:{port}')
    return response.json()

print(get_coordinates_by_ip('213.151.56.89'))