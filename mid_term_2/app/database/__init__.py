from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app import app
from flask_mail import Mail, Message

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost:3306/midterm_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

mysql_db = SQLAlchemy(app)

migrate = Migrate(app, mysql_db)