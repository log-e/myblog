from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from myblog import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    username = db.Column(db.String(20))
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20))
    time = db.Column(db.DateTime)
    content = db.Column(db.Text)
    #可以加入统计字数的函数比如def count啥的

