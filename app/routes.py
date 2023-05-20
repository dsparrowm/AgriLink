from flask import render_template, request
from app import app

@app.route('/', strict_slashes=False)
@app.route('/index', strict_slashes=False)
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET, POST'], strict_slashes=False)
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    return render_template('login.html')
