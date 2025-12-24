from flask import Blueprint, request, jsonify
from ..services.weather import get_weather, get_country_flag
from ..services.wiki import get_city_info
from ..services.places import get_tourist_attractions

api_bp = Blueprint('api', __name__)

@api_bp.route("/", methods=["GET"])
def api():
    # Note: prefix is /api so this route is /api/
    city_name = request.args.get("city_name")
    if not city_name:
        return jsonify({"error": "City name is required"}), 400

    weather = get_weather(city_name)
    
    search_term = city_name
    flag_url = None
    
    if weather:
        if 'name' in weather:
            search_term = weather['name']
        if 'flag_url' in weather:
            flag_url = weather['flag_url']

    city_info = get_city_info(search_term)
    attractions = get_tourist_attractions(search_term)

    return jsonify({
        "city_name": city_name,
        "weather": weather,
        "city_info": city_info,
        "attractions": attractions,
        "flag_url": flag_url,
    })
