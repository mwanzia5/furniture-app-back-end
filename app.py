from flask import Flask
from flask_migrate import Migrate
from models import db

app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


migrations=Migrate(app,db)


db.init_app(app)

if __name__ == '__main__':
    app.run(debug=True, port=5000)