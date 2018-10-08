import hashlib
import random

from app import app, api, celery
from app.models import Users
from app.operations import User
from app.validators import Validate
from flask import Flask, request, g
from flask_login import (LoginManager, current_user, login_required,
                         login_user, logout_user)
from flask_restful import Api, Resource, reqparse


class APILogin(Resource):

    def __init__(self):
        self.args = reqparse.RequestParser()
        self.username = self.args.add_argument('username', location='json',
                                               required=True, help='Username')
        self.password = self.args.add_argument('password', location='json',
                                               required=True, help='Password')

    def post(self):
        args = self.args.parse_args()
        validate = Validate.login(args['username'], args['password'])
        if validate['result'] == 'success':
            login_user(validate['data'])
            validate = {"result": "success",
                        "message": "Succesfully logged in"}
            return validate

        else:
            return validate, 400


api.add_resource(APILogin, '/api/v1/login')


class APIUsers(Resource):
    decorators = [login_required]

    def __init__(self):
        self.args = reqparse.RequestParser()
        if request.method == "POST":
            username = self.args.add_argument('username', location='json',
                                              required=True, help='Username')
            password = self.args.add_argument('password', location='json',
                                              required=True, help='Password')
            email = self.args.add_argument('email', location='json',
                                           required=True, help='Username')

    def post(self):
        args = self.args.parse_args()
        operation = User().create(args['username'], args['password'],
                                  args['email'])
        return operation

    def get(self):
        users = []
        users_objects = Users.objects()
        for user in users_objects:
            user_object = {'id': str(user['id']), 'username': user['username'],
                           'email': user['email']}
            users.append(user_object)
        return users


api.add_resource(APIUsers, '/api/v1/users')


class APIUser(Resource):
    decorators = [login_required]

    def __init__(self):
        self.args = reqparse.RequestParser()
        if request.method == "POST":
            password = self.args.add_argument('password', location='json',
                                              required=False)
            email = self.args.add_argument('email', location='json',
                                           required=False)

    def get(self, user_id=None):
        if user_id is None:
            user_id = str(g.currentUser.id)
        get_user = User().get(user_id)
        return get_user

    def delete(self, user_id=None):
        if user_id is None:
            result = {"result": "failed", "message": "Requires user ID"}
        else:
            current_user = str(g.currentUser.id)
            validate_admin = Validate.admin(current_user)
            if validate_admin['result'] == "success":
                if user_id == current_user:
                    result = {"result": "failed",
                              "message": "Can't delete own user"}
                else:
                    result = User().delete(user_id)
            else:
                result = validate_admin

        return result

    def post(self, user_id):
        args = self.args.parse_args()


api.add_resource(APIUser, '/api/v1/user', '/api/v1/user/<string:user_id>')


class Logout(Resource):
    decorators = [login_required]

    def get(self):
        logout_user()
        return redirect(url_for('login'))


api.add_resource(Logout, '/api/v1/logout')
