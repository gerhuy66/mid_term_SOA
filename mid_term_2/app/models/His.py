from app.database import mysql_db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

class His(mysql_db.Model):
    __tablename__ = 'history'
    id = mysql_db.Column(mysql_db.Integer, primary_key=True)
    studentId = mysql_db.Column(mysql_db.String(20))
    datetime = mysql_db.Column(mysql_db.String(20))
    amount = mysql_db.Column(mysql_db.Float)
    
    def __init__(self, studentId, datetime, amount = 0):
        self.studentId = studentId
        self.datetime = datetime
        self.amount = amount

    def create(self):
        mysql_db.session.add(self)
        mysql_db.session.commit()
        return self

    def __repr__(self):
        return '<His %r, %r, %r, %r>' % (self.id, self.studentId, self.datetime, self.amount)

class HisSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = His
        sqla_session = mysql_db.session

    id = fields.Number(dump_only=True)
    studentId = fields.String(required=True)
    datetime = fields.String(required=False)
    amount = fields.Number(required=True)