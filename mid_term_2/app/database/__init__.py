from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app import app
from flask_mail import Mail, Message

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:Metrohuy1770@soa-db.cog53dp8vhfb.us-east-2.rds.amazonaws.com:3305/soadb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

mysql_db = SQLAlchemy(app)

migrate = Migrate(app, mysql_db)