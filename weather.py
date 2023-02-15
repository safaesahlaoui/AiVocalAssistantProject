import requests
from apiKey import *

api_address='https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid'+key2
json_data=requests.get(api_address).json()

def temp():
    temperature=round(json_data["main"]["temp"]-273,1)
    return temperature
def des():
    description=json_data["weather"][0]["descrption"]
    return description
print(temp())
print(des())