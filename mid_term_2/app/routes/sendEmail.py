import flask
from app import app
from app import config
from flask import json, render_template, request, session, Response,jsonify,redirect,url_for,flash,make_response
from flask_login import login_required,login_user,logout_user,current_user
from app.models import User,Student
from flask_mail import Mail, Message
import pyotp
import datetime, time
from datetime import timedelta
from app import services

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'ibankingmtsoa@gmail.com'
app.config['MAIL_PASSWORD'] = 'aA!123456'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['SECRET_KEY'] = 'xxxxxxxxx'
app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(minutes = 5)

mail = Mail(app)

@app.route('/OTP')
def OTP():
    return render_template('OTP.html')

otp = pyotp.TOTP('base32secret3232')


@app.route('/getOTP', methods=["GET","POST"])
def getOTP():
    if request.method == "POST":
        email = request.form['email']
        subject = 'Mã OTP'

        otp = pyotp.TOTP('base32secret3232')
        time_otp = otp.now()
        
        session.permanent = True
        session['response'] = str(time_otp)
        session.permanent = True
        
        message = Message(subject, sender = 'ibankingmtsoa@gmail.com', recipients=[email])
        body = 'Mã OTP của bạn là: ' + str(time_otp)
        
        services.mailService.sendEmail(subject, email, body)

        return render_template("enterOTP.html", email = email)

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