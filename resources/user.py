import sqlite3 as sql
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type = str, required = True)
    parser.add_argument('password', type = str, required = True)

    def post(self):
        data = UserRegister.parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {"message":"the user already exists"}
        item = UserModel(**data)
        item.save_to_db()
        return {"message":"new user created successfully"},201
    