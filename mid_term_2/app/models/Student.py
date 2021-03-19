from app.database import mysql_db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

class Student(mysql_db.Model):
    __tablename__ = 'students'
    id = mysql_db.Column(mysql_db.Integer, primary_key=True)
    studentId = mysql_db.Column(mysql_db.String(20), unique=True)
    fname = mysql_db.Column(mysql_db.String(20))
    phone = mysql_db.Column(mysql_db.String(20))
    email = mysql_db.Column(mysql_db.String(64))
    fee = mysql_db.Column(mysql_db.Float)
    
    def __init__(self, studentId, fname, phone="", email="", fee = 0):
        self.studentId = studentId
        self.fname = fname
        self.phone = phone
        self.email = email
        self.fee = fee

    def create(self):
        mysql_db.session.add(self)
        mysql_db.session.commit()
        return self

    def to_json(self):
        return {
            "fname":self.fname,
            "phone":self.phone,
            "email":self.email,
            "studentId":self.studentId
        }

    def __repr__(self):
        return '<Student %r, %r, %r, %r, %r, %r>' % (self.id, self.studentId, self.fname, self.phone, self.email, self.fee)

class StudentSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Student
        sqla_session = mysql_db.session

    id = fields.Number(dump_only=True)
    fname = fields.String(required=True)
    studentId = fields.String(required=True)
    phone = fields.String(required=False)
    email = fields.String(required=True)
    fee = fields.Number(required=True)