import requests
from flask import current_app


# Common country names (English/Italian) mapped to capitals
# This helps avoid ambiguity (e.g. "Italy" -> "Italy, Texas")
COUNTRY_CAPITALS = {
    "italy": "Rome",
    "italia": "Rome",
    "france": "Paris",
    "francia": "Paris",
    "germany": "Berlin",
    "germania": "Berlin",
    "spain": "Madrid",
    "spagna": "Madrid",
    "united kingdom": "London",
    "uk": "London",
    "inghilterra": "London",
    "england": "London",
    "usa": "Washington",
    "stati uniti": "Washington",
    "japan": "Tokyo",
    "giappone": "Tokyo",
    "china": "Beijing",
    "cina": "Beijing",
    "russia": "Moscow",
    "brazil": "Brasilia",
    "brasile": "Brasilia"
}

def get_weather(city):
    """Retrieve detailed weather information using explicit Geocoding."""
    api_key = current_app.config['OPENWEATHER_API_KEY']
    
    # Check for country redirect
    clean_city = city.lower().strip()
    if clean_city in COUNTRY_CAPITALS:
        city = COUNTRY_CAPITALS[clean_city]
    
    # 1. Geocoding Step to get precise location
    # limit=1 usually returns the most relevant result (e.g. Rome, IT over Rome, US)
    geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={api_key}"
    try:
        geo_response = requests.get(geo_url)
        geo_data = geo_response.json()
        
        if not geo_data:
            return None
            
        # Take the best match
        location = geo_data[0]
        lat = location['lat']
        lon = location['lon']
        country_code = location['country']
        name = location['name']
        
        # 2. Weather Step using coordinates
        weather_url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
        response = requests.get(weather_url)
        
        if response.status_code == 200:
            data = response.json()
            return {
                "temperature": round(data["main"]["temp"], 1),
                "feels_like": round(data["main"]["feels_like"], 1),
                "conditions": data["weather"][0]["description"].capitalize(),
                "humidity": data["main"]["humidity"],
                "wind_speed": round(data["wind"]["speed"], 1),
                "pressure": data["main"]["pressure"],
                "icon": f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}@2x.png",
                "country_code": country_code,
                "flag_url": f"https://flagcdn.com/w320/{country_code.lower()}.png",
                "name": name,
                "lat": lat,
                "lon": lon,
                "timezone": data.get("timezone", 0)
            }
    except Exception as e:
        print(f"Error in get_weather: {e}")
        pass
        
    return None

# Deprecated/Unused helper (kept for safety or removed if safe)
def get_country_flag(city):
    # This is now integrated into get_weather
    return None
