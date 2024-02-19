from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_number=db.Column(db.BigInteger,unique=True)
    role=db.Column(db.String(30))
    password = db.Column(db.String(64))
    created_at=db.Column(db.TIMESTAMP(),default=db.func.now())
    updated_at=db.Column(db.TIMESTAMP(),onupdate=db.func.now())
    products=db.relationship("ProductModel", backref="users",lazy=True) 
    reviews=db.relationship("ReviewModel", backref="users", lazy=True)
    orders=db.relationship("OrderModel",backref="users",lazy=True)
 
    
class ProductModel (db.Model):
    __tablename__="products"
    id=db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer,db.ForeignKey("users.id"))
    title=db.Column(db.String(80),nullable=False)
    description=db.Column(db.Text,nullable=False)
    price=db.Column(db.Float,nullable=False)
    reviews=db.relationship("ReviewModel",backref="products",lazy=True)
    category_id=db.Column(db.Integer,db.ForeignKey("categories.id"),nullable=False)
    orders=db.relationship("OrderModel",backref="products",lazy=True,)
   
    
class CategoryModel(db.Model):
    __tablename__="categories"   
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50),nullable=False)
    products=db.relationship("ProductModel",backref="categories",lazy=True)


class ReviewModel(db.Model):
    __tablename__="reviews"
    id=db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer,db.ForeignKey("users.id"))
    product_id=db.Column(db.Integer,db.ForeignKey("products.id"),nullable=False)
    text=db.Column(db.Text,nullable=False)
    rating=db.Column(db.Integer,nullable=False)
    
class OrderModel(db.Model):
    __tablename__="orders"
    id=db.Column(db.Integer,primary_key=True)  
    user_id=db.Column(db.Integer,db.ForeignKey("users.id"),nullable=False) 
    product_id=db.Column(db.Integer,db.ForeignKey("products.id"),nullable=False) 
    total_price=db.Column(db.Float,nullable=False)
    status=db.Column(db.String,nullable=False)
    payment_method=db.Column(db.String,nullable=False)
    order_at=db.Column(db.TIMESTAMP(),default=db.func.now())
    