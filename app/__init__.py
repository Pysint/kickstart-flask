from celery import Celery
from flask import Flask
from flask_restful import Api, Resource
from flask_wtf.csrf import CsrfProtect
from app.functions_generic import make_celery
from flask_mongoengine import MongoEngine
from flask_login import LoginManager

#Initialize Flask Instance
app = Flask(__name__)
api = Api(app)

# Initialize Login manager
login_manager = LoginManager()
login_manager.init_app(app)

# Initialize DB and load models and views
from app.configs import variables
db = MongoEngine(app)
celery = make_celery(app)

# Import views
from app import views, models
