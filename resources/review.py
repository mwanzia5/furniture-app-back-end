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
    
    @marshal_with(response_field)
    def post(self):
        data = ReviewList.query.all()
class Review_id(Resource):
    reviews_parser = reqparse.RequestParser()
    reviews_parser.add_argument('text', required=True, help='Text is required')
    reviews_parser.add_argument('rating', required=True, help='Rating is required')

@marshal_with(reviews_fields)
def review_by_id(id):
    review = ReviewModel.query.filter_by(id=id).first()

    if request.method == 'GET':
        review_dict = review.to_dict()

        response = make_response(
            jsonify(review_dict),
            200
        )

        return response

    elif request.method == 'POST':
         new_review = ReviewModel(
            id=request.form.get("id"),
            user_id=request.form.get("user_id"),
            product_id=request.form.get("product-id"),
            text=request.form.get("text"),
            rating=request.form.get("rating")
        )

    db.session.add(new_review)
    db.session.commit()

    review_dict = new_review.to_dict()

    response = make_response(
            jsonify(review_dict),
            201
        )

    return response
