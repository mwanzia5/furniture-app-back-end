from flask import make_response,jsonify,request
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


class Review_id(Resource):
    reviews_parser = reqparse.RequestParser()
    reviews_parser.add_argument('text', required=True, help='Text is required')
    reviews_parser.add_argument('rating', required=True, help='Rating is required')

    @marshal_with(reviews_fields)
    def get(self, id):
        review = ReviewModel.query.get(id)
        return review

    @marshal_with(reviews_fields)
    def post(self, id):
        args = self.reviews_parser.parse_args()
        review = ReviewModel.query.filter_by(id=args['id']).first()

        if review == ReviewModel:
            abort(400, message="Review not found")
            
        db.session.add(review)
        db.session.commit()
        return review, 201