from flask import Flask
from flask_migrate import Migrate
from models import db
from flask_restful import Api
from resources.category import Category, CategoryList
from resources.product import Product, Products
app = Flask(__name__)
api = Api(app)

# Configure database URI and disable track modifications
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize 
migrate = Migrate(app, db)

# Initialize database 
db.init_app(app)

api.add_resource(CategoryList, '/categorylist')
api.add_resource(Category, '/category', '/category/<int:category_id>')
api.add_resource(Products, '/products', )
api.add_resource(Product, '/product', '/product/<int:product_id>')
if __name__ == '__main__':
    
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5000)
