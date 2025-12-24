from project import create_app
from project.services.places import get_tourist_attractions

app = create_app()
with app.app_context():
    print("Testing Paris (OTM)...")
    # Paris coordinates
    results = get_tourist_attractions("Paris", lat=48.8566, lon=2.3522)
    print(f"Results: {results}")
