from app import app
from app.api_generic import *
from flask import Flask, abort, g, make_response, render_template, request
from flask_login import (LoginManager, current_user, login_required,
                         login_user, logout_user)

from flask_wtf.csrf import CSRFProtect

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
currentUser = ""

# CSRF Protection
csrf = CSRFProtect(app)
csrf.init_app(app)


@login_manager.user_loader
def load_user(id):
    return Users.objects.get(username=id)


@app.before_request
def before_request():
    g.currentUser = current_user


@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')
