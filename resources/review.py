from flask_restful import Resource, reqparse,marshal_with,fields,abort
from models import db, ReviewModel


reviews_fields= {
    'id': fields.Integer,
    'user_id': fields.Integer,
    'product_id': fields.Integer,
    'text': fields.String,
    'rating': fields.Integer
}
response_field = {
    "message": fields.String,
    "status": fields.String,
    "user": fields.Nested(reviews_fields)
}


class ReviewList(Resource):
    reviews_parser = reqparse.RequestParser()
    reviews_parser.add_argument('text', required=True, help='Text is required')
    reviews_parser.add_argument('rating', required=True, help='Rating is required')


    @marshal_with(reviews_fields)
    def get(self):
        reviews = ReviewModel.query.all()
        return reviews
    
    @marshal_with(reviews_fields)
    def post(self):
        args = self.reviews_parser.parse_args()
    
        review = ReviewModel(**args)
        db.session.add(review)
        db.session.commit()
        return review, 201
    
class Review_id(Resource):
    reviews_parser = reqparse.RequestParser()
    reviews_parser.add_argument('text', required=True, help='Text is required')
    reviews_parser.add_argument('rating', required=True, help='Rating is required')

    @marshal_with(reviews_fields)
    def get(self,review_id):
       # Retrieve the product with the specified ID from the database
       review = ReviewModel.query.get(review_id)
       if review:
           return review
       else:
           abort(404, message="review not found")

    

