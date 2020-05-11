from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3 as sql
items = []
from models.store import StoreModel

class Store(Resource):

    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store is not None:
            return store.json()
        else:
            return {'message':'Store not found'},404

    def post(self,name):
        store = StoreModel.find_by_name(name)
        if store is not None:
            return {"message": f"store item with {name} already exist"}, 400

        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {"message": "Error in insertion"},500

        return store.json(),201

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        return {'message':"Store Deleted"}
        
class StoreList(Resource):
    def get(self):
        return {"store": [store.json() for store in StoreModel.query.all()]}
        #return {"item: list(map(lambda x.json():x , ItemModel.query.all()))"}