from flask_restful import Resource, reqparse, marshal_with, fields, abort
from models import db, ReviewModel

# Define fields for marshaling
review_fields = {
    'id': fields.Integer,
    'user_id': fields.Integer,
    'product_id': fields.Integer,
    'text': fields.String,
    'rating': fields.Integer
}

response_field = {
    "message": fields.String,
    "status": fields.String,
    "user": fields.Nested(review_fields)
}

# Initialize request parser outside of the class
reviews_parser = reqparse.RequestParser()
reviews_parser.add_argument('text', required=True, help='Text is required')
reviews_parser.add_argument('rating', required=True, type=int, help='Rating is required (1-5)')

class ReviewList(Resource):
    @marshal_with(review_fields)
    def get(self):
        reviews = ReviewModel.query.all()
        return reviews  
    
    @marshal_with(response_field)
    def post(self):
        args = reviews_parser.parse_args()
        
        # Validate rating (1-5)
        if not (1 <= args['rating'] <= 5):
            abort(400, message="Rating must be between 1 and 5")

        # Create a new review and add it to the database
        review = ReviewModel(**args)
        db.session.add(review)

        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            abort(500, message="Failed to create review: {}".format(str(e)))

        return {
            "message": "Review created successfully",
            "status": "success",
            "user": review
        }, 201

class Review_id(Resource):
    @marshal_with(review_fields)
    def get(self, review_id):
        review = ReviewModel.query.get(review_id)
        if not review:
            abort(404, message="Review not found")
        return review
