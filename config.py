import os

SECRET_KEY = 'my_secret'
DEBUG = True
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'NewDB.db')