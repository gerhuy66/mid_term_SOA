from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message
import re
from flask_otp import OTP
from app import app

class Config(Mail):
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = 'ibankingmtsoa@gmail.com'
    app.config['MAIL_PASSWORD'] = 'aA!123456'
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True


