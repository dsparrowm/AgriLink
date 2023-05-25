"""This module creates the tables needed for agrilink
   using sql_alchemy models to map python classes to database tables
"""
from app import db
from datetime import datetime

class User(db.Model):
    """this class represents the user table"""
    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), index=True, unique=True)
    phone = db.Column(db.String(20), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.name)


class Farmer(db.Model):
    """This class represents the farmer table"""
    __tablename__ = "Farmer"
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String, nullable=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    phone = db.Column(db.String(40), nullable=True)

    def __repr__(self):
        return "<Farmer {}>".format(self.name)


class Category(db.Model):
    """this class contains columns for categorues of products"""
    __tablename__ = "Category"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return "Category {}".format(self.name)


class Pruduct(db.Model):
    """this class handles the products table"""
    __tablename__ = "Product"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(140))
    farmer_id = db.Column(db.Integer, db.ForeignKey('Farmer.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('Category.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    image_url = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return "Product {}".format(self.name)
