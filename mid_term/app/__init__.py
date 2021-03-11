from flask import Flask, json, render_template, request, session, Response,jsonify,redirect,url_for
from flask_login import LoginManager
app = Flask(__name__)

from app import models
from app.routes import testViews,views

app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    user = models.User()
    user.username = user_id
    return user