import flask
from marshmallow.fields import Email
from app import app
from flask import json, render_template, request, session, Response,jsonify,redirect,url_for,flash,make_response
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required,login_user,logout_user,current_user
from app.models import User,Student
from app.forms import forms

@app.route("/",methods=['GET','POST'])
@login_required
def index():
    return render_template('tution.html',current_user =current_user)

@app.route("/login",methods=['GET','POST'])
def login():
    form = forms.LoginForm()
    method = request.method

    if method == 'POST':
        user = User.User.query.filter_by(email=form.email.data).first()
        if user is not None and check_password_hash(user.password_hash, form.password.data):
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
@login_required
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

@app.route("/getUserLoginInfo",methods=['GET'])
@login_required
def getUsrLogin():
    
    get_student = Student.Student.query.filter_by(email=current_user.email)
    student_schema = Student.StudentSchema(many=True)
    student = student_schema.dump(get_student)

    return make_response(jsonify({"studentInfo":student}))

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

# @app.route("getRoute/<userId>",methods=['GET'])
# def getRole(userId):
#     user = User.User.query.filter_by(userName=userId)
#     return make_response(jsonify({"Roles": user.roles}),201)

@app.route("/getquare",methods=['GET'])
def getQuare():
    request.get_json()
    return jsonify({"data":2*2})
    
