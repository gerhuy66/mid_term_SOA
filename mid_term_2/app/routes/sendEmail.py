import flask
from app import app
from flask import json, render_template, request, session, Response,jsonify,redirect,url_for,flash,make_response
from flask_login import login_required,login_user,logout_user,current_user
from app.models import User,Student
from flask_mail import Mail, Message
import pyotp
import datetime, time
from datetime import timedelta
from app.services import mailService
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
        email = request.json.get('email')
        subject = 'Mã OTP'

        otp = pyotp.TOTP('base32secret3232')
        time_otp = otp.now()
        
        session.permanent = True
        session['response'] = str(time_otp)
        session.permanent = True
        
        message = Message(subject, sender = 'ibankingmtsoa@gmail.com', recipients=[email])
        body = 'Mã OTP của bạn là: ' + str(time_otp)
        
        mailService.sendEmail(subject, email, body)

        return make_response(jsonify({"status":"send"}))

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