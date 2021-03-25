from flask import request, render_template
from app import app
from werkzeug.security import generate_password_hash, check_password_hash
from app.forms import forms
from app.models import User,Student
import pyotp
import datetime, time

@app.route("/test/<password>",methods=['GET'])
def test2(password):
    password_hash = generate_password_hash(password)
    return password_hash
    

@app.route("/test/<studentId>", methods =['GET','POST'])
def test(studentId):
    ''' password = '123456A!'
    password1 = '123'
    password_hash = generate_password_hash(password)
    return password_hash '''

    ''' form = forms.LoginForm()
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
    return render_template('login.html', form=form) '''
    return studentId
