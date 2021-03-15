from logging import fatal
from flask_login import UserMixin
from app.database import mysql_db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, mysql_db.Model):
    __tablename__ = 'users'
    id = mysql_db.Column(mysql_db.Integer, primary_key = True)
    email = mysql_db.Column(mysql_db.String(64), unique=False, index=True)
    username = mysql_db.Column(mysql_db.String(64), unique=False, index=True)
    password_hash = mysql_db.Column(mysql_db.String(128))
    roles = mysql_db.Column(mysql_db.Integer)
    
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def create(self):
        mysql_db.session.add(self)
        mysql_db.session.commit()
        return self

    def __init__(self, username, email,password_hash,roles = 0):
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.roles = roles

    def __repr__(self):
        return '<User %r,%r,%r,%r>' % (self.username,self.email,self.username,self.password_hash)

    def verify(self,input_password):
        return self.password_hash == input_password

class UserSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = User
        sqla_session = mysql_db.session
    id = fields.Number(dump_only=True)
    email = fields.String(required=True)
    username = fields.String(required=False)
    password_hash = fields.String(required=True)
    roles = fields.Number(required=False)