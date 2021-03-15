import flask
from app import app
from flask import json, render_template, request, session, Response,jsonify,redirect,url_for,flash,make_response
from flask_login import login_required,login_user,logout_user,current_user
from app.models import User,Student,Role

@app.route("/",methods=['GET','POST'])
@login_required
def index():
    return render_template('index.html',current_user =current_user)

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
    Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')

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

@app.route("/getUsers",methods=['GET'])
def getUsr():
    get_users = User.User.query.all()
    user_schema = User.UserSchema(many=True)
    users = user_schema.dump(get_users)
    return make_response(jsonify({"users": users}))

@app.route("/getStudents",methods=['GET'])
def getStudent():
    get_stus = Student.Student.query.all()
    student_schema = Student.StudentSchema(many=True)
    students = student_schema.dump(get_stus)
    return make_response(jsonify({"students": students}))

@app.route("/createUsers",methods=['POST'])
def createUsr():
    data = request.get_json()
    user_schema = User.UserSchema()
    user = user_schema.load(data)
    rs = user_schema.dump(user.create())
    return make_response(jsonify({"user": rs}),201)

@app.route("/createStudents",methods=['POST'])
def createStu():
    data = request.get_json()
    stu_schema = Student.StudentSchema()
    student = stu_schema.load(data)
    rs = stu_schema.dump(student.create())
    return make_response(jsonify({"student": rs}),201)

@app.route("getRoute/<userId>",methods=['GET'])
def getRole(userId):
    user = User.User.query.filter_by(userName=userId)
    return make_response(jsonify({"Roles": user.roles}),201)
    
