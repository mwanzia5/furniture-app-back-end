from models import OrderModel,db
from flask_restful import Resource,fields,marshal,reqparse

order_fields = {
    "id": fields.Integer,
    "user_id": fields.Integer,
    "product_id": fields.Integer,
    "total_price": fields.Float,
    "status": fields.String,
    "order_at" : fields.DateTime  
}

class Order(Resource):
    order_parser = reqparse.RequestParser()
    order_parser.add_argument('total_price', required=True, help='Total price is required')
    order_parser.add_argument('status', required=True, help='Status is required')



    def get(self,id=None):
        if id:
            order = OrderModel.query.filter_by(id=id).first()
            if order == OrderModel:
                return {"message":"order not found"},404
            return marshal(order,order_fields)
        else:
            orders = OrderModel.query.all()
            return marshal(orders,order_fields)
    
    def post(self):
        data = Order.order_parser.parse_args()

        order = OrderModel(**data)


    
        db.session.add(order)
        db.session.commit()

        return {"message":"Order created successfully"}
        

    def patch(self,id):
        data = Order.order_parser.parse_args()
        order = OrderModel.query.get(id)

        if order:
            for key,value in data.items():
                setattr(order,key,value)
            try:
                db.session.commit()

                return {"message":"Order updated successfully"}
            except:
                return {"message":"Order unable to be updated"}
            
        else:
            return {"message":"Order not found"}

    def delete(self,id):
            
        order = OrderModel.query.get(id)
        if order:
            try:
                db.session.delete(order)
                db.session.commit()

                return {"message":"Order deleted"}
            except:
                return {"message":"Order unable to be deleted"}
        else:
            return {"message":"Order not found"}
        

   




