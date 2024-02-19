from flask_restful import Resource, reqparse,marshal_with,fields,abort,Api
from models import db, ReviewModel
from app import app

api=Api(app)
reviews_fields= {
    'id': fields.Integer,
    'user_id': fields.Integer,
    'product_id': fields.Integer,
    'text': fields.String,
    'rating': fields.Integer
}

class Review_list(Resource):
    @marshal_with(reviews_fields)
    def get(self):
        reviews=ReviewModel.query.all()
        return reviews


api.add_resource(Review_list, '/reviews') 
    # parser = reqparse.RequestParser()
    # parser.add_argument('rating', type=int,help="rating required", required=True)
    # parser.add_argument('text', type=str,help="text required" ,required=True)
   
    
    # def get(self):
    #     review_text = []
    #     for  review in ReviewModel.query.all():
    #         review_dict =  review.to_dict()
    #         review_text.append(review_dict)

    #     response = make_response(
    #         jsonify(review_dict),
    #         200
    #     )

    #     return response
    

    
    # def post(self):
    #     data = Review_list.parser.parse_args()
    #     new_review = ReviewModel(**data)

    #     db.session.add(new_review)
    #     db.session.commit()

    #     review_dict = new_review.to_dict()

    #     response = make_response(
    #         jsonify(review_dict),
    #         201
    #     )

    #     return response
    