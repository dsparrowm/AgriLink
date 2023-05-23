"""This module contains routes and view functions for imteracting
with the fromtend
"""
from flask import request, jsonify
from app import app, db
from app.models import User, Farmer
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity


@app.route('/status', methods=['GET'])
def status():
    """Check server connection status"""
    return jsonify({'Status': 'Ok!!'})

@app.route('/login', methods=['POST'])
def login():
    """checks if user is valid and found in the database
    then creates a jwt token for that user and returns a 
    response to the client containing the the user token"""
    data = request.get_json()
    form_email = data.get('email')
    form_password = data.get('password')
    user = User.query.filter_by(email=form_email).first()
    if user is None or check_password_hash(user.password_hash, form_password) != True:
        return jsonify({'message': 'Invalid email or password'}), 401
    else:
        access_token = create_access_token(identity=user.id)
        return jsonify({'message': 'Login successful',
                        'token': access_token,
                        'user_id': user.id}), 200

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
        #necessary to generate user_id used to create farmer object
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

@app.route('/user', methods=['GET'])
@jwt_required()
def user_info():
    """validates jwt token received from the client
    and returns the user info to the client"""
    current_user = get_jwt_identity()
    user = User.query.get(current_user)
    return jsonify({'id': user.id,
                    'name': user.name,
                    'email': user.email,
                    'role': user.role})

@app.route('/updateUserInfo/<int:id>', methods=['PUT'])
@jwt_required()
def update_user(id):
    current_user = get_jwt_identity()
    if current_user != id:
        return jsonify({'message': 'Unauthorized'}), 401
    data = request.get_json()
    user = User.query.get(id)
    if not user:
        return jsonify({'message': 'User Not Found'}), 404
    if user.role == 'farmer':
        farmer = Farmer.query.filter_by(user_id=user.id).first()
        if 'name' in data:
            user.name = data.get('name')
            farmer.name = data.get('name')
        if 'email' in data:
            user.email = data.get('email')
        if 'phone' in data:
            farmer.phone = data.get('phone')
        db.session.commit()
        return jsonify({'message': 'user updated successfully',
                        'user': user
                        })
    elif user.role == 'buyer':
        if 'name' in data:
            user.name = data.get('name')
        if 'email' in data:
            user.email = data.get('email')
        db.session.commit()
        return jsonify({'message': 'user updated successfully',
                        'user': user
                        })
