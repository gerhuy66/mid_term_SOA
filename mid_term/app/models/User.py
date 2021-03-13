from flask_login import UserMixin
from app.database import mysql_db

class User(UserMixin, mysql_db.Model):
    __tablename__ = 'users'
    id = mysql_db.Column(mysql_db.Integer, primary_key = True)
    email = mysql_db.Column(mysql_db.String(64), unique=True, index=True)
    username = mysql_db.Column(mysql_db.String(64), unique=True, index=True)
    password_hash = mysql_db.Column(mysql_db.String(128))
    roles = mysql_db.Column(mysql_db.Integer)
    
    def __init__(self, username, email,password_hash):
        self.username = username
        self.email = email
        self.password_hash = password_hash

    def __repr__(self):
        return '<User %r>' % self.username

    def verify(self,input_password):
        return self.password_hash == input_password