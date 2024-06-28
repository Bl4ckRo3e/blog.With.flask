from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# create the mapp of database
class category(db.Model):
    __tablename__ = 'Categories'
    id         = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name       = db.Column(db.String(50), unique=True, nullable=False)


class User(db.Model):
    __tablename__ = 'Users'
    id         = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name       = db.Column(db.String(50), unique=True, nullable=False)
    email      = db.Column(db.String(50), unique=True, nullable=False)
    code       = db.Column(db.Integer, nullable=False)
    mode       = db.Column(db.String(50), unique=True, nullable=False)


class Article(db.Model):
    __tablename__ = 'Articles'
    id         = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title      = db.Column(db.String(50), unique=True, nullable=False)
    content    = db.Column(db.String(255), nullable=False)
    image_data = db.Column(db.String(255), nullable=False)
    category   = db.Column(db.String(50), db.ForeignKey('Categories.name'))
    user_mode  = db.Column(db.String(50), nullable=False)
    active     = db.Column(db.String(5), nullable=False)
    count      = db.Column(db.Integer, nullable=False)
    writer     = db.Column(db.String(50), db.ForeignKey('Users.name'))


class Log(db.Model):
    __tablename__ = 'Logs'
    id         = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ip         = db.Column(db.String(50), nullable=False)
    time       = db.Column(db.String(50), nullable=False)
    work       = db.Column(db.String(50), nullable=False)

if __name__ == '__main__':
    print("Wrong File Run this is models")