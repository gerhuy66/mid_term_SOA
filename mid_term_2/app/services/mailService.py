from app import app
from flask_mail import Mail, Message

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'ibankingmtsoa@gmail.com'
app.config['MAIL_PASSWORD'] = 'aA!123456'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['SECRET_KEY'] = 'xxxxxxxxx'

mail = Mail(app)



def sendEmail(subject, email, content):
    message = Message(subject, sender = 'ibankingmtsoa@gmail.com', recipients=[email])
    message.body = content
    mail.send(message)
    return True
