from app import app
from flaskext.mysql import MySQL
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '1234'
app.config['MYSQL_DATABASE_DB'] = 'midterm_db'
app.config['MYSQL_DATABASE_Host'] = 'localhost'
mysql = MySQL()
mysql.init_app(app)