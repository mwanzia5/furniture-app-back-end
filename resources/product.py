from flask_restful import Resource, reqparse, fields, marshal_with, abort, request

from models import db, ProductModel

product_fields = {
    "id":fields.Integer, 
    "title":fields.String,
    "description":fields.String,
    "price":fields.Float
}

class ProductList(Resource):
    @marshal_with(product_fields)
    def get(self):
        products = ProductModel.query.all()
        return products
    

class Product(Resource):
    #this function 
    def __init__(self):


        self.parser=reqparse.RequestParser()
        self.parser.add_argument('user_id', type=int, help='This field cannot be blank', required=True)
        self.parser.add_argument('title', type=str, help='This field cannot be blank', required=True)
        self.parser.add_argument('description', type=str, help='This field cannot be blank', required=True)
        self.parser.add_argument('price', type=float, help='This field cannot be blank', required=True)
        self.parser.add_argument('category_id', type=int, help='This field cannot be blank', required=True)

    @marshal_with(product_fields)
    def get(self, product_id):
        product = ProductModel.query.get(product_id)
        #cehcks if theres an existing product and returns it
        if product:
            return product
        #if product does not exist is aborts
        else:
            abort(404, message="Product not found")

    
    @marshal_with(product_fields)
    def post(self):
        args = self.parser.parse_args()
        #checks if the product already exists
        existing_product = ProductModel.query.filter_by(title=args['title']).first()
        if existing_product:
            abort(404, message="Product already exists")
        #if product does not exist, it creates a new product
        else:
            product=ProductModel(**args)
            db.session.add(product)
            db.session.commit()
            return product, 200
        
           

    @marshal_with(product_fields)
    def put(self, id):
        product = ProductModel.query.get(id)
        if not product:
           abort(404, message="Product not found")
        args = self.parser.parse_args()
        product.title = args["title"]
        product.description = args["description"]
        product.price = args["price"]
        db.session.commit()
        return product
        
    

  
    @marshal_with(product_fields)
    def delete(self, product_id):
        product = ProductModel.query.get(product_id)
        if not product:
            abort(404, message="Product not found")
        db.session.delete(product)
        db.session.commit()
        return {"result": "success"}
        


