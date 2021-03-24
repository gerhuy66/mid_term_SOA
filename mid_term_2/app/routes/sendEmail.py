import flask
from app import app
from flask import json, render_template, request, session, Response,jsonify,redirect,url_for,flash,make_response
from flask_login import login_required,login_user,logout_user,current_user
from app.models import User,Student
from flask_mail import Mail, Message
import pyotp
import datetime
from datetime import timedelta
from app.services import mailService
app.config['SECRET_KEY'] = 'xxxxxxxxx'


mail = Mail(app)

@app.route('/OTP', methods = ["GET", "POST"])
@login_required
def OTP():
    if request.method == "POST":
        sessNm = current_user.username+"_OTP"
        session[sessNm] = createOTP()
        email = request.json.get('email')
        subject = 'Mã OTP'

        session.permanent = True
        time = timedelta(minutes = 5)
        if sessNm in session:
            app.config['PERMANENT_SESSION_LIFETIME'] = time #minutes: set theo phút
        
        message = Message(subject, sender = 'ibankingmtsoa@gmail.com', recipients=[email])
        body = 'Mã OTP của bạn là: ' + session[sessNm]
        
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
    else:
        msg = "OTP hết hạn. Nhập lại mail để nhận OTP"
        return render_template('OTP.html', msg = msg)

def createOTP():
    otp = pyotp.TOTP('base32secret3232',interval=1)
    return otp.now()
