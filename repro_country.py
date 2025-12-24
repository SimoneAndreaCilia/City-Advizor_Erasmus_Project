
import requests
import os
from config import Config

OPENWEATHER_API_KEY = Config.OPENWEATHER_API_KEY

def check_geo(city):
    print(f"--- Checking '{city}' ---")
    
    # 1. Weather API
    url_weather = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
    res_weather = requests.get(url_weather)
    if res_weather.status_code == 200:
        data = res_weather.json()
        print(f"Weather API: Name='{data.get('name')}', SysCountry='{data.get('sys', {}).get('country')}' Coords=({data.get('coord', {}).get('lat')}, {data.get('coord', {}).get('lon')})")
    else:
        print(f"Weather API failed: {res_weather.status_code}")

    # 2. Geo API
    url_geo = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={OPENWEATHER_API_KEY}"
    res_geo = requests.get(url_geo)
    if res_geo.status_code == 200:
        data = res_geo.json()
        print(f"Geo API:")
        for i, item in enumerate(data):
            print(f"  {i+1}. Name='{item.get('name')}', Country='{item.get('country')}' Coords=({item.get('lat')}, {item.get('lon')})")
    else:
        print(f"Geo API failed: {res_geo.status_code}")

if __name__ == "__main__":
    check_geo("Italy")
    check_geo("Italia")
    check_geo("France")
    check_geo("Rome")
