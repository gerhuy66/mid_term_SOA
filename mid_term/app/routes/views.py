import flask
from app import app
from flask import json, render_template, request, session, Response,jsonify,redirect,url_for,flash
from flask_login import login_required,login_user,logout_user,current_user

@app.route("/",methods=['GET','POST'])
@login_required
def index():
    return render_template('index.html')

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
    Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')

from app.models import User
@app.route("/login",methods=['GET','POST'])
def login():
    form = LoginForm()
    method = request.method
    if method == 'POST':
        user = User.User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify(form.password.data):
            login_user(user, form.remember_me.data)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('index')
            return redirect(next)
        flash('Invalid username or password.')
    return render_template('login.html', form=form)


@app.route("/about")
@login_required
def about():
    return "All about Flask"

@app.route("/tution")
def tutioion():
    return render_template("tution.html")

from app.services import service
@app.route("/test")
@login_required
def testStudent():
    test_service = service.testService
    rs = test_service()
    return jsonify({"data":rs})

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route("/userl")
def getUsrLogin():
    resp = {"result":200,"data":current_user.to_json()}
    return jsonify(resp)
#test
