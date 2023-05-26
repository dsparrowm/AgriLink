"""This module contains routes and view functions for imteracting
with the fromtend
"""
from flask import request, jsonify
from app import app, db
from app.models import User, Farmer, Category
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.utils import secure_filename
from app.helper import allowed_file


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
        hashed_password = generate_password_hash(form_password)
        user = User(name=form_name, email=form_email,
                    password_harsh=hashed_password)
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
                    email=form_email,
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
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'email': user.email,
                    'role': user.role,
                    'phone': user.phone,
                    'image_url': user.image_url
                })

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
        if 'first_name' in data:
            user.first_name = data.get('first_name')
            farmer.first_name = data.get('first_name')
        if 'last_name' in data:
            user.last_name = data.get('last_name')
            farmer.last_name = data.get('last_name')
        if 'email' in data:
            user.email = data.get('email')
        if 'phone' in data:
            user.phone = data.get('phone')
            farmer.phone = data.get('phone')
        if 'image' in data:
            file = request.files['image']
            if file.filename == '':
                return jsonify({'error': 'no file selected'})
            if not allowed_file(file.filename):
                return jsonify({'error': 'Invalid file format'})
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['USER_IMAGE_FOLDER'], filename)
            file.save(file_path)
            user.image_url = file_path
        db.session.commit()
        return jsonify({'message': 'user updated successfully',
                        'user': user
                        })
    elif user.role == 'buyer':
        if 'firt_name' in data:
            user.first_name = data.get('first_name')
        if 'email' in data:
            user.email = data.get('email')
        if 'image' in data:
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
        return jsonify({'message': 'user updated successfully',
                        'user': user
                        })

@app.route('/product/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get(id)
    if product:
        product_data = {
                'id': product.id,
                'name': product.name,
                'price': product.price,
                'quantity': product.quantity,
                'image_url': product.image_url
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

    categories = Category.query.get(category)
    if not categories:
        return jsonify({'error': 'no products from this category'})
    products = Product.query.filter_by(category_id=categories.id).all()
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
                    'image_url': product.image_url
                }
                for product in paginated_products
            ],
            'page': page,
            'per_page': per_page,
            'total_items': total_items,
            'total_pages': total_pages
        }
    return jsonify(response)

@app.route('/product/upload', methods=['POST'])
@jwt_required
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
    p_category = Category.query.get(category)
    if not p_category:
        new_category = Category(name=category)
        db.session.add(new_category)
        db.session.commit()
        p_category = Category.query.get(category)

    #Check if the file exists and is of the allowed type
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    if not allowed_file(file.filename):
        return jsonify({'error': 'Invalid file format'})

    #Securely save the file to the upload directory
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['PRODUCT_IMAGE_FOLDER'], filename)
    file.save(file_path)

    #Store the product details and image url in the database
    product = Product(name=name, price=price, quantity=quantity,
                      image_url=file_path, farmer_id=user.id,
                      category_id=p_category.id,
                      description=description)
    db.session.add(product)
    db.session.commit()

    return jsonify({'message': 'Product uploaded successfully'})
