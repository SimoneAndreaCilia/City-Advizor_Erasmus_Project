
import os
from dotenv import load_dotenv
load_dotenv()

# Mocking Flask app config for API Key if needed, but get_weather needs current_app context.
# Instead, I'll just check the emergency service logic first.

from project.services.emergency_service import get_emergency_number

print("Testing Emergency Numbers:")
print(f"GB: {get_emergency_number('GB')}")
print(f"US: {get_emergency_number('US')}")
print(f"IT: {get_emergency_number('IT')}")
print(f"JP: {get_emergency_number('JP')}")

# Now let's try to simulate checking what OpenWeather returns for 'London'
import requests

API_KEY = os.getenv("OPENWEATHER_API_KEY")
if not API_KEY:
    print("No API Key found")
else:
    city = "London"
    geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}"
    try:
        resp = requests.get(geo_url)
        data = resp.json()
        if data:
            print(f"Geo Data for {city}: {data[0]}")
            cc = data[0]['country']
            print(f"Country Code: {cc}")
            print(f"Emergency Number for {city}: {get_emergency_number(cc)}")
        else:
            print("No geo data found")
    except Exception as e:
        print(e)
