from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3 as sql
items = []
from models.item import ItemModel

class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument(
        'price', type = float, required= True, help = "This is necessary field"
    )
    parser.add_argument(
        'store_id', type = int, required= True, help = "This is necessary field"
    )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item is not None:
            return item.json()
        else:
            return {'message':'Item not found'},404

    def post(self,name):
        item = ItemModel.find_by_name(name)
        if item is not None:
            return {"message": f"The item with {name} already exist"}, 400

        data = Item.parser.parse_args()
        newitem = ItemModel(name, **data)
        try:
            newitem.save_to_db()
        except:
            return {"message": "Error in insertion"},500

        return newitem.json(),201

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
    
    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        if item is None:
            item = ItemModel(name, **data)
        else:
            item.price = data['price']
        item.save_to_db()
        return item.json()
        
class ItemList(Resource):
    def get(self):
        return {"item": [item.json() for item in ItemModel.query.all()]}
        #return {"item: list(map(lambda x.json():x , ItemModel.query.all()))"}