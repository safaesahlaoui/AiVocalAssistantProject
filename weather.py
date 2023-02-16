import requests
from apiKey import *

api_address='http://api.openweathermap.org/data/2.5/weather?q=Kenitra,MA&APPID='+key2
json_data=requests.get(api_address).json()
# i made an xsl file contain name of all known cities with their codes from openweatherapi
def temp():
     temperature=round(json_data["main"]["temp"]-273,1)
     return temperature
def des():
     description=json_data["weather"][0]["description"]
     return description

#print(temp())
#print(des())
