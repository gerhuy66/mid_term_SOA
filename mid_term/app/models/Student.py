from app.database import mysql_db
class Student(mysql_db.Model):
    __tablename__ = 'students'
    id = mysql_db.Column(mysql_db.Integer, primary_key=True)
    fname = mysql_db.Column(mysql_db.String(20))
    phone = mysql_db.Column(mysql_db.String(20))
    email = mysql_db.Column(mysql_db.String(20))

    def __repr__(self):
        return '<Student %r>' % self.fname