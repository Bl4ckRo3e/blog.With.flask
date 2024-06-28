from flask import Flask
from models import db
from rout import route


# setting the flask up
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Database.db'
app.config['SECRET_KEY'] = 'Hi Hitler'

# initial the database
db.init_app(app)
# creating the models 
with app.app_context():
    db.create_all()

# this is to add blue prints
app.register_blueprint(route, url_prefix='/')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
