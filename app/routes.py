"""This module contains routes and view functions for imteracting
with the fromtend
"""
from flask import request, jsonify
from app import app, db
from app.models import User, Farmer
from werkzeug.security import generate_password_hash, check_password_hash


@app.route('/status', methods=['GET'])
def status():
    """Check server connection status"""
    return jsonify({'Status': 'Ok!!'})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    form_email = data.get('email')
    form_password = data.get('password')
    user = User.query.filter_by(email=form_email).first()
    if user is None or check_password_hash(user.password_hash, form_password) != True:
        return jsonify({'message': 'Invalid email or password'}), 401
    else:
        session['email'] = user.email
        return jsonify({'message': 'Login successful', 'session': session}), 200

@app.route('/register', methods=['POST'])
def register():
    """Handles registration form sent from the frontend
    and stores in the database
    """
    data = request.get_json()
    form_name = data.get('name')
    form_email = data.get('email')
    form_password = data.get('password')
    form_role = data.get('role')
    user_exists = User.query.filter_by(email=form_email).first()
    if user_exists:
        return jsonify({'message': 'user already exists'}), 403
    if form_role == 'farmer':
        form_location = data.get('location')
        form_phone = data.get('phone')
        user = User(name=form_name, email=form_email,
                    password_harsh=user.set_password(form_password))
        db.session.add(user)
        db.session.commit()
        farmer = Farmer(name=form_name,location=form_location,
                        phone=form_phone, user_id=user.id)
        db.session.add(farmer)
        db.session.commit()
        return jsonify({'message': 'Registration successful'}), 200
    elif form_role == 'buyer':
        hashed_password = generate_password_hash(form_password)
        user = User(name=form_name,
                    emiail=form_email,
                    role=form_role,
                    password_hash=hashed_password)
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'Registration successful'}), 200

@app.route('/user/<int:id>', methods=['GET'])
def user_info(id):
    user = User.query.filter_by(id=id).first()
    return jsonify({'id': user.id,
                    'name': user.name,
                    'email': user.email})
