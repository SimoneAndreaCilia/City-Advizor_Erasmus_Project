import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev_key_for_local_testing_only'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///city_advisor.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # API Keys
    OPENWEATHER_API_KEY = os.environ.get('OPENWEATHER_API_KEY')
    GOOGLE_PLACES_API_KEY = os.environ.get('GOOGLE_PLACES_API_KEY')
    OPENTRIPMAP_API_KEY = os.environ.get('OPENTRIPMAP_API_KEY')
