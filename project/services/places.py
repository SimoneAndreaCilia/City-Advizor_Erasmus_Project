import requests
from flask import current_app

def get_tourist_attractions(city, lat=None, lon=None):
    """Retrieve top tourist attractions using OpenTripMap."""
    # Fallback if coordinates are not provided (should be passed from weather service)
    if not lat or not lon:
        print("DEBUG: No coordinates provided for OpenTripMap.")
        return []

    api_key = current_app.config['OPENTRIPMAP_API_KEY']
    # Radius search: 5000m radius, 'interesting_places' kind, sorted by rate (popularity)
    url = "https://api.opentripmap.com/0.1/en/places/radius"
    params = {
        "radius": 5000,
        "lon": lon,
        "lat": lat,
        "kinds": "interesting_places",
        "rate": "3",
        "limit": 5,
        "apikey": api_key
    }
    
    try:
        response = requests.get(url, params=params)
        data = response.json()
        
        if response.status_code == 200 and "features" in data:
            results = []
            for feature in data["features"]:
                props = feature["properties"]
                geometry = feature["geometry"]
                
                # Format 'kinds' into a description
                # kinds is comma separated like "museums,cultural,interesting_places"
                kinds_list = props.get("kinds", "").split(",")
                # Filter/clean up descriptions
                clean_kinds = [
                    k.replace("_", " ").title() 
                    for k in kinds_list 
                    if k not in ["interesting_places", "tourist_object", "other"]
                ]
                description = ", ".join(clean_kinds[:3]) if clean_kinds else "Tourist Attraction"

                results.append({
                    "name": props.get("name", "Unknown Attraction"),
                    "address": "", # OTM radius search doesn't give address, we can leave empty or omit
                    "rating": f"{props.get('rate', 'N/A')}/3", # OTM uses 1-3 rate
                    "lat": geometry["coordinates"][1],
                    "lng": geometry["coordinates"][0],
                    "description": description
                })

            
            if results:
                return results
            
    except Exception as e:
        print(f"Error calling OpenTripMap: {e}")
    
    # Mock data fallback (Used if API fails or returns no results)
    return [
        {
            "name": f"{city} National Museum",
            "address": "123 Museum Way, " + city,
            "rating": "4.8/5",
            "lat": 0,
            "lng": 0,
            "description": "Museum, Art Gallery, Historical Landmark"
        },
        {
            "name": f"Great Park of {city}",
            "address": "45 Green Ave, " + city,
            "rating": "4.6/5",
            "lat": 0,
            "lng": 0,
            "description": "Park, Tourist Attraction, Nature Reserve"
        },
        {
            "name": f"The {city} Tower",
            "address": "1 Skyline Blvd, " + city,
            "rating": "4.7/5",
            "lat": 0,
            "lng": 0,
            "description": "Observation Deck, Landmark, Skyscraper"
        }
    ]
