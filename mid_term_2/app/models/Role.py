from sqlalchemy.orm import relationship
from app.database import mysql_db
class Role(mysql_db.Model):
    __tablename__ = 'roles'
    id = mysql_db.Column(mysql_db.Integer, primary_key=True)
    name = mysql_db.Column(mysql_db.String(64), unique=True)
    role_value = mysql_db.Column(mysql_db.Integer)
    

    def __init__(self,name,role_value):
        self.name = name
        self.role_value = role_value

    def __repr__(self):
        return '<Role %r>' % self.name