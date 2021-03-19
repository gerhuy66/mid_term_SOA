import flask
from app import app
from app import config
from flask import json, render_template, request, session, Response,jsonify,redirect,url_for,flash,make_response
from flask_login import login_required,login_user,logout_user,current_user
from app.models import User,Student
from flask_mail import Mail, Message
import pyotp
import datetime
from datetime import timedelta
from app import services
import random

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'ibankingmtsoa@gmail.com'
app.config['MAIL_PASSWORD'] = 'aA!123456'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['SECRET_KEY'] = 'xxxxxxxxx'


mail = Mail(app)

@app.route('/OTP', methods = ["GET", "POST"])
def OTP():
    if request.method == "POST":
        session['response'] = createOTP()
        email = request.form['email']
        subject = 'Mã OTP'

        session.permanent = True
        time = timedelta(seconds = 30)
        if 'response' in session:
            app.config['PERMANENT_SESSION_LIFETIME'] = time #minutes: set theo phút
        
        message = Message(subject, sender = 'ibankingmtsoa@gmail.com', recipients=[email])
        body = 'Mã OTP của bạn là: ' + session['response']
        services.mailService.sendEmail(subject, email, body)
        return render_template("enterOTP.html", email = email, time = time)
    return render_template('OTP.html')

@app.route('/otplogin', methods = ["GET", "POST"])
def account():
    otp_field = request.form['otp']
    if 'response' in session:
        s = session['response']
        session.pop('response', None)
        if s == otp_field:
            return 'OTP xác nhận thành công'
        else:
            msg = "Sai OTP. Nhập lại mail để nhận OTP"
            return render_template('OTP.html', msg = msg)
    else:
        msg = "OTP hết hạn. Nhập lại mail để nhận OTP"
        return render_template('OTP.html', msg = msg)

def createOTP():
    otp = pyotp.TOTP('base32secret3232',interval=1)
    return otp.now()
