from app.database import db

def testService():
    student_id = "51703096";
    conn = db.mysql.connect()
    cursor =conn.cursor()
    querry= "select * from student where s_id = %s"
    cursor.execute(querry,(student_id))
    return cursor.fetchone()

def getBalance(mysql, stuId):
    conn = mysql.connect()
    cursor = conn.cursor()
    querry = "select * from bank_account where bank_account.balance = %s"
    cursor.execute(querry,(stuId))
    return cursor.fetchone()