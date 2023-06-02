"""This module contains routes and view functions for imteracting
with the fromtend
"""
from flask import request, jsonify
from app import app, db
from app.models import User, Farmer, Category, Product
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.utils import secure_filename
from app.helper import allowed_file
from config import Config
from datetime import timedelta
import os

@app.route('/status', methods=['GET'])
def status():
    """Check server connection status"""
    return jsonify({'Status': 'Ok!!'})

@app.route('/login', methods=['POST'])
def login():
    """checks if user is valid and found in the database
    then creates a jwt token for that user and returns a 
    response to the client containing the the user token"""
    form_email = request.form.get('email')
    form_password = request.form.get('password')
    user = User.query.filter_by(email=form_email).first()
    if user is None or check_password_hash(user.password_hash, form_password) != True:
        return jsonify({'message': 'Invalid email or password'}), 401
    else:
        access_token = create_access_token(identity=user.id, expires_delta=timedelta(days=7))
        return jsonify({'message': 'Login successful',
                        'token': access_token,
                        'user_id': user.id}), 200

@app.route('/register', methods=['POST'])
def register():
    """Handles registration form sent from the frontend
    and stores in the database
    """
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    form_email = request.form.get('email')
    form_password = request.form.get('password')
    form_role = request.form.get('role')
    form_phone = request.form.get('phone')
    if 'location' in request.form:
        location = request.form.get('location')
    user_exists = User.query.filter_by(email=form_email).first()
    if user_exists:
        return jsonify({'message': 'user already exists'}), 403
    hashed_password = generate_password_hash(form_password)
    if form_role == 'farmer':
        user = User(first_name=first_name,
                    last_name=last_name,
                    email=form_email,
                    password_hash=hashed_password,
                    role=form_role,
                    phone=form_phone)
        db.session.add(user)
        #necessary to generate user_id used to create farmer object
        db.session.commit()

        farmer = Farmer(location=location, user_id=user.id)
        db.session.add(farmer)
        db.session.commit()
        return jsonify({'message': 'Registration successful'}), 200
    elif form_role == 'buyer':
        user = User(first_name=first_name,
                    email=form_email,
                    last_name=last_name,
                    role=form_role,
                    password_hash=hashed_password,
                    phone=form_phone)
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
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'email': user.email,
                    'role': user.role,
                    'phone': user.phone,
                    'role': user.role,
                    'image_url': user.image_url
                })

@app.route('/updateUserInfo/<int:id>', methods=['POST'])
@jwt_required()
def update_user(id):
    current_user = get_jwt_identity()
    if current_user != id:
        return jsonify({'message': 'Unauthorized'}), 401
    user = User.query.get(id)
    if not user:
        return jsonify({'message': 'User Not Found'}), 404
    if user.role == 'farmer':
        farmer = Farmer.query.filter_by(user_id=user.id).first()
        if 'first_name' in request.form:
            user.first_name = request.form.get('first_name')
        if 'last_name' in request.form:
            user.last_name = request.form.get('last_name')
        if 'email' in request.form:
            user.email = request.form.get('email')
        if 'phone' in request.form:
            user.phone = request.form.get('phone')
        if 'location' in request.form:
            farmer.location = request.form.get('location')
        if 'image' in request.files:
            file = request.files['image']
            if file.filename == '':
                return jsonify({'error': 'no file selected'})
            if not allowed_file(file.filename):
                return jsonify({'error': 'Invalid file format'})
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['USER_IMAGE_FOLDER'], filename)
            file.save(file_path)
            user.image_url = file_path
        
        return jsonify({'message': 'user updated successfully'})
    elif user.role == 'buyer':
        if 'first_name' in request.form:
            user.first_name = request.form.get('first_name')
        if 'last_name' in request.form:
            user.last_name = request.form.get('last_name')
        if 'email' in request.form:
            user.email = request.form.get('email')
        if 'image' in request.files:
            file = request.files['image']
            if file.filename == '':
                return jsonify({'error': 'No file selected'})
            if not allowed_file(file.filename):
                return jsonify({'error': 'Invalid file format'})
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['USER_IMAGE_FOLDER'], filename)
            file.save(file_path)
            user.image_url = file_path
    
        db.session.commit()
        return jsonify({'message': 'user updated successfully'})

@app.route('/product/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get(id)
    if not product:
        return jsonify({'error': 'no product found'})
    category = Category.query.get(product.category_id)
    if product:
        product_data = {
                'id': product.id,
                'name': product.name,
                'price': product.price,
                'quantity': product.quantity,
                'image_url': product.image_url,
                'category': category.name,
                'description': product.description,
                'category_id': category.id
        }
        return jsonify(product_data)
    else:
        return jsonify({'error': 'product not found'})

@app.route('/products/category', methods=['GET'])
def get_category():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    category = request.args.get('category')

    start_index = (page - 1) * per_page
    end_index = start_index + per_page

    categories = Category.query.filter_by(name=category).first()
    if not categories:
        return jsonify({'error': 'no products from this category'})
    products = Product.query.filter(Product.category_id == categories.id).all()
    total_items = len(products)
    total_pages = (total_items // per_page) + (1 if total_items % per_page > 0 else 0)
    paginated_products = products[start_index:end_index]
    response = {
            'products': [
                {
                    'id': product.id,
                    'name': product.name,
                    'price': product.price,
                    'quantity': product.quantity,
                    'image_url': product.image_url,
                    'description': product.description,
                }
                for product in paginated_products
            ],
            'page': page,
            'per_page': per_page,
            'total_items': total_items,
            'total_pages': total_pages
        }
    return jsonify(response)

@app.route('/product/<int:id>/update', methods=['PUT'])
@jwt_required()
def update_product(id):
    """enables farmers to update the details of their products"""
    current_user = get_jwt_identity()
    if current_user != id:
        return jsonify({'error': 'Unauthorized'})
    user = User.query.get(current_user)
    if not user:
        return jsonify({'error': 'user not found'})
    product = Product.query.get(id)
    if not product:
        return jsonify({'error': 'product not found'})
    if 'name' not in request.form:
        return jsonify({'error': 'product name is missing'})
    if 'price' not in request.form:
        return jsonify({'error': 'product price is missing'})
    if 'quantity' not in request.form:
        return jsonify({'error': 'product quantity is missing'})
    if 'category' not in request.form:
        return jsonify({'error': 'product category is missing'})
    if 'description' not in request.form:
        return jsonify({'error': 'product description is missing'})
    if 'image' not in request.files:
        return jsonify({'error': 'no image file provided'})
    name = request.form['name']
    price = request.form['price']
    quantity = request.form['quantity']
    category = request.form['category']
    description = request.form['description']
    file = request.files['image']

    #check that the image exists and file format is correct
    if file.filename == '':
        return jsonify({'error': 'no file selected'})
    if not allowed_file(file.filename):
        return jsonify({'error': 'Invalid file format'})
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['PRODUCT_IMAGE_FOLDER'], filename)
    if product.image_url != file_path:
        file.save(file_path)
        product.image_url = file_path
    if name != product.name:
        product.name = name
    if price != product.price:
        product.price = price
    if quantity != product.quantity:
        product.quantity = quantity
    if description != product.description:
        product.description = description

    db.session.commit()
    return jsonify({'message': 'product updated successfully'})

@app.route('/product/upload', methods=['POST'])
@jwt_required()
def add_product():
    """enables a farmer to create and list new products"""
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'user not found'})
    #Check if all required fields are present in the request
    if 'name' not in request.form:
        return jsonify({'error': 'Product name is missing'})
    if 'price' not in request.form:
        return jsonify({'error': 'Product price is missing'})
    if 'quantity' not in request.form:
        return jsonify({'error': 'Product quantity is missing'})
    if 'category' not in request.form:
        return jsonify({'error': 'product category is missing'})
    if 'description' not in request.form:
        return jsonify({'error': 'product description is missing'})
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'})

    #Retrieve the values from the request
    name = request.form['name']
    price = int(request.form['price'])
    quantity = int(request.form['quantity'])
    category = request.form['category']
    description = request.form['description']
    file = request.files['image']

    #query Category table to get id from it
    p_category = Category.query.filter_by(name=category).first()
    if not p_category:
        p_category = Category(name=category)
        db.session.add(p_category)
        db.session.commit()
    #Check if the file exists and is of the allowed type
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    if not allowed_file(file.filename):
        return jsonify({'error': 'Invalid file format'})

    #Securely save the file to the upload directory
    filename = secure_filename(file.filename)
    print(filename)
    file_path = os.path.join(app.config['PRODUCT_IMAGE_FOLDER'], filename)
    file.save(file_path)

    #Store the product details and image url in the database
    product = Product(name=name, price=price, quantity=quantity,
                      image_url=filename, farmer_id=user.id,
                      category_id=p_category.id,
                      description=description)
    db.session.add(product)
    db.session.commit()

    return jsonify({'message': 'Product uploaded successfully',
                    'product_name': product.name,
                    'category': p_category.name,
                    'price': product.price
                })
@app.route('/product/<int:id>/delete', methods=['DELETE'])
@jwt_required()
def delete_product(id):
    current_user = get_jwt_identity()
    if current_user != id:
        return jsonify({'error': 'Unauthorized'})
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'product deleted successfully'})

@app.route('/user/products', methods=['GET'])
@jwt_required()
def user_products():
    current_user = get_jwt_identity()
    user = User.query.get(current_user)
    if not user:
        return jsonify({'error': 'user not found'})
    farmer = Farmer.query.filter_by(user_id=user.id)
    if not farmer:
        return jsonify({'error': 'Unauthorized'})
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    start_index = (page - 1) * per_page
    end_index = start_index + per_page

    products = Product.query.filter_by(farmer_id=user.id).all()
    total_items = len(products)
    total_pages = (total_items // per_page) + (1 if total_items % per_page > 0 else 0)
    paginated_products = products[start_index:end_index]
    response = {
            'products': [
                {
                    'id': product.id,
                    'name': product.name,
                    'price': product.price,
                    'quantity': product.quantity,
                    'image_url': product.image_url,
                    'description': product.description,
                }
                for product in paginated_products
            ],
            'page': page,
            'per_page': per_page,
            'total_items': total_items,
            'total_pages': total_pages
        }
    return jsonify(response)