''' from app.database import mysql_db
class Bank_Account(mysql_db.Model):
    __tablename__ = 'bank_accounts'
    id = mysql_db.Column(mysql_db.Integer, primary_key=True)
    student_id = mysql_db.Column(mysql_db.String(20))
    balance = mysql_db.Column(mysql_db.Integer)
    

    def create(self):
        mysql_db.session.add(self)
        mysql_db.session.commit()
        return self

    def __repr__(self):
        return '<Bank_Account %r>' % self.id '''