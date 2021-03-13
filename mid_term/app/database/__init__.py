from flask_sqlalchemy import SQLAlchemy

from app import app
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost:3306/midterm_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
mysql_db = SQLAlchemy(app)

