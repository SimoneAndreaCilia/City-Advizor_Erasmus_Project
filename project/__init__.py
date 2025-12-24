from flask import Flask
from config import Config
from .extensions import db, login_manager

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)

    # --- AGGIUNTA IMPORTANTE PER IL LOGIN ---
    # Importiamo il modello User (assumendo che sia nel file models.py)
    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        # Dice a Flask come trovare l'utente tramite il suo ID
        return User.query.get(int(user_id))
    # ----------------------------------------

    # Register blueprints (to be created)
    from .blueprints.auth import auth_bp
    from .blueprints.main import main_bp
    from .blueprints.api import api_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp, url_prefix='/api')

    # Database creation
    with app.app_context():
        db.create_all()

    return app