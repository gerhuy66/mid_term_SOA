from app.database import mysql_db
class Tution(mysql_db.Model):
    __tablename__ = 'tutions'
    id = mysql_db.Column(mysql_db.Integer, primary_key=True)
    student_id = mysql_db.Column(mysql_db.String(20))
    fee = mysql_db.Column(mysql_db.Integer)

    def __repr__(self):
        return '<Tution %r>' % self.id