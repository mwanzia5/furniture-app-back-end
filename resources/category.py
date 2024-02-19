from models import CategoryModel, db
from flask_restful import Resource, fields, marshal_with, reqparse, abort

# Define fields to be returned in the response
category_fields = {
    "id": fields.Integer,
    "name": fields.String
}

# Define a resource to handle requests for retrieving all categories
class CategoryList(Resource):
    @marshal_with(category_fields)
    def get(self):
        # Retrieve all categories from the database
        categories = CategoryModel.query.all()
        return categories

# Define a resource to handle requests for retrieving, updating, or deleting a specific category
class Category(Resource):
    def __init__(self):
        
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', type=str, help="This field cannot be blank.", required=True)

    @marshal_with(category_fields)
    def get(self, category_id):
        # Retrieve the category with the specified ID from the database
        category = CategoryModel.query.get(category_id)
        # If the category exists, return it
        if category:
            return category
        # If the category does not exist, abort the request with a 404 error
        else:
            abort(404, message="Category not found")

    @marshal_with(category_fields)
    def post(self):
        args = self.parser.parse_args()
        existing_category = CategoryModel.query.filter_by(name=args['name']).first()
        if existing_category:
            abort(400, message="Category already exists") 
        else:
            category = CategoryModel(**args)
            db.session.add(category)
            db.session.commit()
            return category, 201

    @marshal_with(category_fields)
    def put(self, category_id):
        # Retrieve the category with the specified ID from the database
        category = CategoryModel.query.get(category_id)
        # If the category does not exist, abort the request with a 404 error
        if not category:
            abort(404, message="Category not found")
        # Parse the incoming request data
        args = self.parser.parse_args()
        # Update the name of the category with the provided name
        category.name = args["name"]
        # Commit the changes to the database
        db.session.commit()
        # Return the updated category
        return category

    @marshal_with(category_fields)
    def delete(self, category_id):
        # Retrieve the category with the specified ID from the database
        category = CategoryModel.query.get(category_id)
        # If the category does not exist, abort the request with a 404 error
        if not category:
            abort(404, message="Category not found")
        # Delete the category from the database
        db.session.delete(category)
        # Commit the changes to the database
        db.session.commit()
        # Return an empty response with a 204 status code
        return "", 204