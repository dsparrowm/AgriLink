"""This module contains routes and view functions for imteracting
with the fromtend
"""
from flask import request, jsonify
from app import app, db
from app.models import User, Farmer, Category, Product, Order
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
    """
        Login endpoint that receives a POST request with the user's email and password. 
        It returns a JSON object with the message 'Login successful', an access token, and the user's ID 
        if the email and password are valid. If they are invalid, it returns a JSON object with the message 
        'Invalid email or password' and a 401 status code. 

        Parameters:
        None

        Returns:
            A tuple in the form of a JSON object with keys 'message', 'token', and 'user_id' for a successful login 
            or a JSON object with key 'message' and a 401 status code for an unsuccessful login.

    Example:
    {
        'message': 'Login successful',
        'token': 'example_token',
        'user_id': 1
    }
    """
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
    """
        Registers a new user with the provided information in the request form data. 
        If the user is successfully registered, a farmer or buyer object is also created
        depending on the role provided in the form data. 

        Parameters:
        None

        Returns:
            A JSON response containing a message indicating whether the registration was successful 
            or if the user already exists. HTTP status code 200 is returned if registration is successful, 
            and 403 if the user already exists.
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
    """
	    Route that returns the user information. Uses the JWT token to retrieve the current user's info
        from the database.

	    :return: A JSON object with the user's id, first name, last name, email, phone, role, and
        image URL.
	"""
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
    """
        Updates the user information of the specified user.

        Args:
            id (int): The user ID to update.

        Returns:
            json: A JSON object containing a message indicating whether the update was successful or not.

        Raises:
            HTTPException: If authorization fails or user is not found.

    """
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
            user.image_url = filename
        db.session.commit()   
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
            user.image_url = filename
    
        db.session.commit()
        return jsonify({'message': 'user updated successfully'})

@app.route('/product/<int:id>', methods=['GET'])
def get_product(id):
    """
        Returns a JSON representation of a product with the given id.
    
        Parameters:
        id (int): The id of the product to retrieve.
    
        Returns:
            If a product with the given id exists, returns a JSON representation of the product,
            including its id, name, price, quantity, image url, category name, category id, and description.
            If no product is found, 
            returns a JSON object with an error message.
    """
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
    """
        Retrieves a paginated list of products based on a category.

        :return: A JSON object with a paginated list of products according to the parameters
                passed. The object has the following keys: 'products', 'page', 'per_page', 
                'total_items', and 'total_pages'.
        :rtype: JSON
    """
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
    """
	    Update the product with the given ID. Requires the user to be authenticated and
	    authorized to update the specified product. The product can be updated with a new
	    name, price, quantity, category, description, or image. If the image is updated,
	    it must be a valid file format and saved to the product image folder. Returns a JSON
	    response indicating success or failure in updating the product.

	    :param id: The ID of the product to be updated.
	    :return: A JSON response indicating success or failure in updating the product.
	"""
    current_user = get_jwt_identity()
    if current_user != id:
        return jsonify({'error': 'Unauthorized'})
    user = User.query.get(current_user)
    if not user:
        return jsonify({'error': 'user not found'})
    product = Product.query.get(id)
    if not product:
        return jsonify({'error': 'product not found'})
    if 'name' in request.form:
        name = request.form['name']
        product.name = name
    if 'price' in request.form:
        price = request.form['price']
        product.price = price
    if 'quantity' in request.form:
        quantity = request.form['quantity']
        product.quantity = quantity
    if 'category' in request.form:
        category = request.form['category']
        req = Category.query.filter_by(name=category).first()
        if not req:
            return jsonify({'error': 'Category does not exist'})
        product.category_id = req.id
    if 'description' in request.form:
        description = request.form['description']
        product.description = description
    if 'image' in request.files:
        file = request.files['image']
        #check that the image exists and file format is correct
        if file.filename == '':
            return jsonify({'error': 'no file selected'})
        if not allowed_file(file.filename):
            return jsonify({'error': 'Invalid file format'})
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['PRODUCT_IMAGE_FOLDER'], filename)
        if product.image_url != filename:
            file.save(file_path)
            product.image_url = filename

    db.session.commit()
    return jsonify({'message': 'product updated successfully'})

@app.route('/product/upload', methods=['POST'])
@jwt_required()
def add_product():
    """
	    Adds a new product to the database, given the product details and image file.
	
	    Args:
	        None.
	
	    Returns:
	        A JSON object containing a message indicating whether the product was 
	        uploaded successfully or not, along with the name, category, and price 
	        of the product if successful, or an error message if unsuccessful.
	"""
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
    """
        Retrieves a paginated list of products belonging to a user who is authenticated 
        and authorized as a farmer. The products are retrieved from the database and 
        paginated according to the request parameters 'page' and 'per_page'. The retrieved 
        products along with pagination details such as total number of pages and total 
        number of items are returned as a JSON response. 

        Returns:
            A JSON response containing a paginated list of products, pagination details such 
            as total number of pages and total number of items.
    """
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

    products = db.session.query(Product, Category).join(Category).all()
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
                    'category': Category.name
                }
                for product, Category in paginated_products
            ],
            'page': page,
            'per_page': per_page,
            'total_items': total_items,
            'total_pages': total_pages
        }
    return jsonify(response)
@app.route('/product/<int:id>/farmer', methods=['GET'])
def get_product_farmer_details(id):
    """
        Returns the details of the farmer who sold the product with the given ID.
    
        Args:
            id (int): The ID of the product to get farmer details for.
    
        Returns:
            A JSON object containing the following keys:
            - id (int): The ID of the farmer.
            - first_name (str): The first name of the farmer.
            - last_name (str): The last name of the farmer.
            - phone (str): The phone number of the farmer.
            - location (str): The location of the farmer.
            If the product is not found, a JSON object containing an error message.
    """
    product = Product.query.get(id)
    if not product:
        return jsonify({'error': 'Product not found'})
    farmer = Farmer.query.get(product.farmer_id)
    user = User.query.filter_by(id=farmer.id).first()
    return jsonify({'id': user.id,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'phone': user.phone,
                    'location': farmer.location
                })

@app.route('/user/product/order', methods=['POST'])
@jwt_required()
def completed_order():
    """
        This function is a Flask endpoint that handles completed orders. It accepts a POST request
        to /user/product/order with a JSON body containing the product_id and requires
        a valid JWT token for authorization. It retrieves the current user's identity, the product_id
        from the request's JSON body, and the User, Product, and Farmer objects associated with the
        current user and product_id. If the product is not found, it returns a JSON error message.
        Otherwise, it creates an Order object and adds it to the database, then returns a JSON success
        message. This function does not take any parameters and returns a JSON response.
    """
    current_user = get_jwt_identity()
    data = request.get_json()
    product_id = data.get('product_id')
    user = User.query.get(current_user)
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'error': 'Product not found'})
    farmer = Farmer.query.filter_by(user_id=product.farmer_id).first()
    order = Order(product_id=product.id,
                  buyer_id=current_user,
                  farmer_id=farmer.user_id,
                  amount=product.price
                )
    db.session.add(order)
    db.session.commit()
    return jsonify({'message': 'order entered successfully'})

@app.route('/user/<int:id>/balance', methods=['GET'])
@jwt_required()
def farmer_balance_info(id):
    """
        Returns the balance information of a farmer with the given ID. 

        :param id: int representing the ID of the farmer.
        :type id: int

        :return: A JSON object containing the balance of the farmer.
    """
    current_user = get_jwt_identity()
    if current_user != id:
        return jsonify({'error': 'Unauthorized user'})
    orders = Order.query.filter_by(farmer_id=id).all()
    if not orders:
        return jsonify({'balance': 0})
    balance = 0
    for order in orders:
        balance += order.amount
    return jsonify({'balance': balance})

@app.route('/user/orders', methods=['GET'])
@jwt_required()
def user_orders():
    """ Returns all the orders for that user """
    current_user = get_jwt_identity()
    user = User.query.get(current_user)
    orders = db.session.query(Product, Order).join(Order).all()
    if user.role == 'farmer':      
        response = {
            'Transactions': [
                {
                    'order_id': order.id,
                    'createad_at': order.created_at,
                    'amount': order.amount,
                    'status': order.status,
                    'product_name': product.name,
                    'buyer_id': order.buyer_id
                }
                for product, order in orders
            ]
        }
        return jsonify(response)
    elif user.role == 'buyer':
        response = {
            'Transactions': [
                {
                    'order_id': order.id,
                    'createad_at': order.created_at,
                    'amount': order.amount,
                    'status': order.status,
                    'product_name': product.name,
                    'farmer_id': order.farmer_id
                }
                for product, order in orders
            ]
        }
        return jsonify(response)
    
@app.route('/user/sales', methods=['GET'])
@jwt_required()
def sales_summary():
    """
        Returns the sales summary of a user. If the user's role is "farmer",
        it returns their total sales, total orders, and total products. Otherwise, it returns
        an error message. 
        :return: JSON object containing total_sales (int), total_orders (int), and total_products (int) 
        or an error message (str).
    """
    current_user = get_jwt_identity()
    user = User.query.get(current_user)
    if user.role == 'farmer':
        total_sales = 0
        orders = Order.query.filter_by(farmer_id=user.id).all()
        for order in orders:
            total_sales += order.amount
        farmer_orders = Order.query.filter_by(farmer_id=user.id).all()
        total_orders = len(farmer_orders)
        farmer_products = Product.query.filter_by(farmer_id=user.id).all()
        total_products = len(farmer_products)
        return jsonify({'total_sales': total_sales,
                        'total_orders': total_orders,
                        'total_products': total_products
                    })
    else:
        return jsonify({'error': 'Unauthorized user'})

@app.route('/user/product/order/confirmation', methods=['Post'])
@jwt_required()
def confirm_order():
    current_user = get_jwt_identity()
    data = request.get_json()
    product_id = data.get('id')
    order = Order.query.filter_by(buyer_id=current_user).first()
    if not order:
        return jsonify({'error': 'No order made for that product'})
    order.status = 'confirmed'
    db.session.commit()
    return jsonify({'message': 'Order confirmed'})