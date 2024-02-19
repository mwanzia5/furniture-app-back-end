from flask import Flask
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_restful import Api
from models import db,UserModel
from resources.category import Category,CategoryList
from resources.user import SignUpResource,LoginResource
from flask_jwt_extended import JWTManager,


app = Flask(__name__)


# Configure database URI and disable track modifications
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = "jwt-secret"

migrations=Migrate(app,db)


db.init_app(app)
api=Api(app)
bcrypt=Bcrypt(app)
jwt=JWTManager(app)

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return UserModel.query.filter_by(id=identity).one_or_none().to_json()

api.add_resource(SignUpResource, '/users', '/users/<int:id>')
api.add_resource(LoginResource, '/login')

api.add_resource(CategoryList, '/categorylist')
api.add_resource(Category, '/category', '/category/<int:category_id>')

if __name__ == '__main__':
    app.run(debug=True, port=5000)