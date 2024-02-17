from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from models import db, UserModel
from resources.user import SignUpResource
from resources.user import LoginResource

app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///data.db'
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

if __name__ == '__main__':
    app.run(debug=True, port=5555)