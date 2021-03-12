import flask
from app import app
from flask import json, render_template, request, session, Response,jsonify,redirect,url_for
from flask_login import login_required,login_user,logout_user

@app.route("/",methods=['GET','POST'])
@login_required
def index():
    return render_template('index.html')

from wtforms import Form, BooleanField, StringField, PasswordField, validators,SubmitField
from flask_wtf import FlaskForm
class loginForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    password = PasswordField('Password', [
        validators.DataRequired()
    ])
    submit = SubmitField('Log In')

from app import models
@app.route("/login",methods=['GET','POST'])
def login():
    form = loginForm(request.form)
    if form.is_submitted():
        # Login and validate the user.
        # user should be an instance of your `User` class
        # models.load_user(user)

        user = models.User()
        user.username = form.username
        user.password = form.password
        if user.username.data == "admin":
            if user.password.data == "123":
                login_user(user)
                return redirect(url_for("index"))
            else:
                return('Wrong pass')
        else:
            return('Login fail')
    return render_template('login.html', form=form)


@app.route("/about")
@login_required
def about():
    return "All about Flask"


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


