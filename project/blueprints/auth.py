from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from ..extensions import db
from ..models import User, FavoriteCity, SavedItinerary

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        # Validation
        if not username or not email or not password:
            flash('Please fill in all fields', 'error')
            return redirect(url_for('auth.register'))

        if password != confirm_password:
            flash('Passwords do not match', 'error')
            return redirect(url_for('auth.register'))

        # Check if user already exists
        existing_user = User.query.filter(
            (User.username == username) | (User.email == email)
        ).first()
        
        if existing_user:
            flash('Username or email already exists', 'error')
            return redirect(url_for('auth.register'))

        # Create new user
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('main.index'))
        else:
            flash('Invalid username or password', 'error')
            return redirect(url_for('auth.login'))

    return render_template('login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('main.index'))

@auth_bp.route('/favorites', methods=['POST'])
@login_required
def add_favorite():
    city_name = request.form.get('city_name')
    country_code = request.form.get('country_code')

    # Check if city is already in favorites
    existing_favorite = FavoriteCity.query.filter_by(
        user_id=current_user.id, 
        city_name=city_name
    ).first()

    if not existing_favorite:
        favorite = FavoriteCity(
            user_id=current_user.id, 
            city_name=city_name, 
            country_code=country_code
        )
        db.session.add(favorite)
        db.session.commit()
        flash(f'{city_name} added to favorites!', 'success')
    else:
        flash(f'{city_name} is already in your favorites.', 'info')

    return redirect(url_for('main.index', city_name=city_name))

@auth_bp.route('/favorites', methods=['GET'])
@login_required
def view_favorites():
    favorites = FavoriteCity.query.filter_by(user_id=current_user.id).all()
    saved_itineraries = SavedItinerary.query.filter_by(user_id=current_user.id).order_by(SavedItinerary.timestamp.desc()).all()
    return render_template('favorites.html', favorites=favorites, saved_itineraries=saved_itineraries)
