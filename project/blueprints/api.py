from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from ..extensions import db
from ..models import SavedItinerary
from ..services.weather import get_weather, get_country_flag
from ..services.wiki import get_city_info
from ..services.places import get_tourist_attractions
from ..services.ai_service import generate_itinerary_content

api_bp = Blueprint('api', __name__)

@api_bp.route("/save-itinerary", methods=["POST"])
@login_required
def save_itinerary():
    data = request.json
    city = data.get('city')
    content = data.get('content')

    if not city or not content:
        return jsonify({"error": "Missing city or content"}), 400

    # Optional: Check if already saved recently to prevent duplicates?
    # For now, just save it.

    saved = SavedItinerary(
        user_id=current_user.id,
        city=city,
        content=content
    )
    
    try:
        db.session.add(saved)
        db.session.commit()
        return jsonify({"message": "Itinerary saved successfully!", "id": saved.id})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


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

@api_bp.route("/generate-itinerary", methods=["POST"])
def generate_itinerary():
    data = request.json
    city = data.get('city')
    weather = data.get('weather') 
    temp = data.get('temp')

    if not city or not weather:
        return jsonify({"error": "Missing city or weather data"}), 400

    itinerary = generate_itinerary_content(city, weather, temp)
    return jsonify({'itinerary': itinerary})
