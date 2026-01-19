from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from ..extensions import db
from ..models import FavoriteCity, SearchHistory
from ..services.weather import get_weather, get_country_flag
from ..services.wiki import get_city_info
from ..services.places import get_tourist_attractions
from ..services.currency_service import get_currency_code, get_exchange_rate
from ..services.emergency_service import get_emergency_number

main_bp = Blueprint('main', __name__)


POPULAR_CITIES = ["London", "Paris", "New York", "Tokyo"]

@main_bp.route("/", methods=["GET", "POST"])
def index():
    weather = None
    city_info = None
    attractions = None
    error_message = None
    flag_url = None
    city_name = None
    is_favorite = False
    popular_weather = []
    currency_code = None
    exchange_rate = None
    timezone_offset = 0
    emergency_number = None

    # Handle query parameter (e.g. redirect from favorites)
    if request.method == 'GET' and request.args.get('city_name'):
        city_name = request.args.get("city_name").strip()
    
    # Handle form submission
    if request.method == "POST":
        city_name = request.form.get("city_name", "").strip()

    if city_name:
        if current_user.is_authenticated:
            # Log search history
            # Avoid duplicate recent history if desired, but simplified here as per original
            search_entry = SearchHistory(user_id=current_user.id, city_name=city_name)
            db.session.add(search_entry)
            db.session.commit()

            # Check if the city is in favorites
            is_favorite = FavoriteCity.query.filter_by(
                user_id=current_user.id, city_name=city_name
            ).first() is not None

        weather = get_weather(city_name)
        
        # Use the normalized English city name from OpenWeather for subsequent calls
        # This handles cases like "Parigi" -> "Paris" or "Roma" -> "Rome"
        search_term = city_name
        flag_url = None
        
        if weather:
            if 'name' in weather:
                search_term = weather['name']
            if 'flag_url' in weather:
                flag_url = weather['flag_url']

        city_info = get_city_info(search_term)
        
        # Pass coordinates if available
        lat = weather['lat'] if weather else None
        lon = weather['lon'] if weather else None
        attractions = get_tourist_attractions(search_term, lat=lat, lon=lon)
        
        if weather:
             timezone_offset = weather.get('timezone', 0)

        # Currency Conversion & Emergency
        if weather and 'country_code' in weather:
            currency_code = get_currency_code(weather['country_code'])
            emergency_number = get_emergency_number(weather['country_code'])
            
            if currency_code != "EUR":
                exchange_rate = get_exchange_rate(currency_code)

        # Handle cases where data isn't found
        if not weather:
            error_message = f"Weather data for '{city_name}' could not be retrieved."
        if city_info == "No information available." or city_info == "Errore nella lettura dei dati.":
             city_info = f"No Wikipedia information available for '{city_name}' (tried searching for '{search_term}')."
    elif request.method == "POST":
         error_message = "Please enter a valid city name."

    # Fetch popular cities weather if strictly on home page (no search)
    if not city_name and not error_message:
        for city in POPULAR_CITIES:
            w = get_weather(city)
            if w:
                popular_weather.append(w)

    return render_template(
        "index.html",
        weather=weather,
        city_info=city_info,
        attractions=attractions,
        error_message=error_message,
        flag_url=flag_url,
        city_name=city_name,
        is_favorite=is_favorite,
        popular_weather=popular_weather,
        currency_code=currency_code,
        exchange_rate=exchange_rate,
        timezone_offset=timezone_offset,
        emergency_number=emergency_number
    )

@main_bp.route("/search_history")
@login_required
def search_history():
    history = SearchHistory.query.filter_by(user_id=current_user.id).order_by(
        SearchHistory.searched_at.desc()
    ).all()
    return render_template("search_history.html", history=history)
