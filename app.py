from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api

from models import db

from resources.product import  ProductList, Product


app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



migrations=Migrate(app,db)
api=Api(app)


db.init_app(app)

api.add_resource(ProductList, '/product')
api.add_resource(Product, '/product', '/product/<int:product_id>')

if __name__ == '__main__':

    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5000)