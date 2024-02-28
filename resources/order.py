
from flask import current_app
from flask_mail import Message
from flask_restful import Resource, fields, marshal, reqparse
from models import db, OrderModel, ProductModel, UserModel

from models import OrderModel, db
from flask_restful import Resource,fields,marshal,reqparse
from flask_jwt_extended import jwt_required,  current_user,get_jwt_identity


order_fields = {
    "id": fields.Integer,
    "user_id": fields.Integer,
    "product_id": fields.Integer,
    "total_price": fields.Float,
    "status": fields.String,
    "order_at": fields.DateTime
}

class Order(Resource):
    order_parser = reqparse.RequestParser()
    # order_parser.add_argument('total_price', required=True, help='Total price is required')
    # order_parser.add_argument('status', required=True, help='Status is required')
    # order_parser.add_argument('email', required=True, help='Email is required') 


    @jwt_required()
    def get(self,id=None):
        # if current_user['role'] != 'member':
        #     return { "message":"Unauthorized request"}

        if id:
            order = OrderModel.query.get(id)
            if order:
                return marshal(order, order_fields)
            else:
                return {"message": "Order not found"}, 404
        else:
            orders = OrderModel.query.all()

            return marshal(orders, order_fields)


            
    @jwt_required()

    def post(self):
        current_user = get_jwt_identity()
        order = OrderModel.query.get(id)
        user = UserModel.query.filter_by(id=current_user).first()
        email = user.email
        print("User role:", user.role)
        if user.role != 'member':
            return { "message":"Unauthorized request"}
        data = Order.order_parser.parse_args()
        data['user_id'] = order.user_id

        order = OrderModel(**data)


        db.session.add(order)
        db.session.commit()

        
        self.send_invoice(email, order)


        return {"message": "Order created successfully and invoice sent"}


    @jwt_required()
    def patch(self,id):
        if current_user['role'] != 'member':
            return { "message":"Unauthorized request"}

        data = Order.order_parser.parse_args()
        order = OrderModel.query.get(id)

        if order:
            for key, value in data.items():
                setattr(order, key, value)
            try:
                db.session.commit()
                return {"message": "Order updated successfully"}
            except:
                return {"message": "Order unable to be updated"}
        else:
            return {"message": "Order not found"}


    @jwt_required()
    def delete(self,id):
        if current_user['role'] != 'member':
            return { "message":"Unauthorized request"}

        order = OrderModel.query.get(id)
        if order:
            try:
                db.session.delete(order)
                db.session.commit()
                return {"message": "Order deleted"}
            except:
                return {"message": "Order unable to be deleted"}
        else:
            return {"message": "Order not found"}

    def send_invoice(self, email, order):
   
        user = UserModel.query.get(order.user_id)

        product = ProductModel.query.get(order.product_id)

        if user and product:
            msg = Message('Invoice for Your Order', recipients=[email])
            msg.body = f'Invoice Details:\n\n' \
                       f'Order ID: {order.id}\n' \
                       f'Total Price: ${order.total_price}\n' \
                       f'Status: {order.status}\n' \
                       f'Order Date: {order.order_at}\n' \
                       f'User Details:\n' \
                       f'   Username: {user.username}\n' \
                       f'   Email: {user.email}\n' \
                       f'Product Details:\n' \
                       f'   Product Name: {product.title}\n' \
                       f'   Description: {product.description}\n' \
                       f'   Price: ${product.price}\n' \
                   

            mail = current_app.extensions['mail'] 
            mail.send(msg)
        else:
            print("User or product not found for the given order, unable to send invoice.")





# from models import OrderModel,db
# from flask_restful import Resource,fields,marshal,reqparse

# order_fields = {
#     "id": fields.Integer,
#     "user_id": fields.Integer,
#     "product_id": fields.Integer,
#     "total_price": fields.Float,
#     "status": fields.String,
#     "order_at" : fields.DateTime  
# }

# class Order(Resource):
#     order_parser = reqparse.RequestParser()
#     order_parser.add_argument('total_price', required=True, help='Total price is required')
#     order_parser.add_argument('status', required=True, help='Status is required')



#     def get(self,id=None):
#         if id:
#             order = OrderModel.query.filter_by(id=id).first()
#             if order == OrderModel:
#                 return {"message":"order not found"},404
#             return marshal(order,order_fields)
#         else:
#             orders = OrderModel.query.all()
#             return marshal(orders,order_fields)
    
#     def post(self):
#         data = Order.order_parser.parse_args()

#         order = OrderModel(**data)


    
#         db.session.add(order)
#         db.session.commit()

#         return {"message":"Order created successfully"}
        

#     def patch(self,id):
#         data = Order.order_parser.parse_args()
#         order = OrderModel.query.get(id)

#         if order:
#             for key,value in data.items():
#                 setattr(order,key,value)
#             try:
#                 db.session.commit()

#                 return {"message":"Order updated successfully"}
#             except:
#                 return {"message":"Order unable to be updated"}
            
#         else:
#             return {"message":"Order not found"}

#     def delete(self,id):
            
#         order = OrderModel.query.get(id)
#         if order:
#             try:
#                 db.session.delete(order)
#                 db.session.commit()

#                 return {"message":"Order deleted"}
#             except:
#                 return {"message":"Order unable to be deleted"}
#         else:
#             return {"message":"Order not found"}
        

   




