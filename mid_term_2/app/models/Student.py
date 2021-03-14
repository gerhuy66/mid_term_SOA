from app.database import mysql_db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

class Student(mysql_db.Model):
    __tablename__ = 'students'
    id = mysql_db.Column(mysql_db.Integer, primary_key=True)
    studentId = mysql_db.Column(mysql_db.String(20))
    fname = mysql_db.Column(mysql_db.String(20))
    phone = mysql_db.Column(mysql_db.String(20))
    email = mysql_db.Column(mysql_db.String(20))
    
    def __init__(self,studentId,fname,phone="",email=""):
        self.studentId = studentId
        self.fname = fname
        self.phone = phone
        self.email = email

    def create(self):
        mysql_db.session.add(self)
        mysql_db.session.commit()
        return self

    def __repr__(self):
        return '<Student %r,%r,%r, %r, %r>' % (self.id,self.studentId,self.fname,self.phone,self.email)
        
class StudentSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Student
        sqla_session = mysql_db.session

    id = fields.Number(dump_only=True)
    fname = fields.String(required=True)
    studentId = fields.String(required=True)
    phone = fields.String(required=False)
    email = fields.String(required=True)