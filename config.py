import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'very hard to guess'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024 #5 megabyte
    PRODUCT_IMAGE_FOLDER = '/AgriLink/product_imagess'
    USER_IMAGE_FOLDER = '/AgriLink/user_images'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                    'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
