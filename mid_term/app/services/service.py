from app.database import db

def testService():
    student_id = "51703096";
    conn = db.mysql.connect()
    cursor =conn.cursor()
    querry= "select * from student where s_id = %s"
    cursor.execute(querry,(student_id))
    return cursor.fetchone()