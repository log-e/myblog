from myblog import db
from flask_login import mixins

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    username = db.Column(db.String(20))
    password = db.Column(db.String(128))

    def set_password(self, password):
        ...

    def check_password(self, password):
        ...

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20))
    datetime = db.Column(db.DateTime)
    content = db.Column(db.Text)

