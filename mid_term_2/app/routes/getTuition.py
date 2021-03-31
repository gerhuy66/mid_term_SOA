import flask
from app import app
from flask import json, render_template, request, session, Response,jsonify,redirect,url_for,flash,make_response
from flask_login import login_required,login_user,logout_user,current_user
from app.models import User,Student,His
from app.forms import forms
from app.database import mysql_db
from datetime import date

@app.route('/getTuition/<studentId>', methods=['GET', 'POST'])
@login_required
def getTuition(studentId):
    student = Student.Student.query.filter_by(studentId = studentId)
    student_schema = Student.StudentSchema(many=True)
    students = student_schema.dump(student)
    return make_response(jsonify({"student_fee": students[0]["fee"]}))

@app.route('/chargeStudentFee', methods=['POST'])
@login_required
def chageFee():
    rq_data = request.json
    stdId = rq_data.get("stdId")
    fee = rq_data.get("fee")
    otp = rq_data.get("otp")
    valid = checkOTP(otp)
    if valid == "miss_otp":
        return make_response(jsonify({"status":"fail","message":"please get OTP"}))
    if valid == "incorrect":
        return make_response(jsonify({"status":"fail","message":"wrong OTP"}))
    stu_query = Student.Student.query.filter_by(studentId=stdId)
    stu = stu_query.first()
    stu_query.update(dict(fee=0))

    dateStr = date.today().strftime("%d/%m/%Y")
    his = His.His(stdId,dateStr,current_user.email,fee)
    mysql_db.session.add(his)

    usr_query = User.User.query.filter_by(email=current_user.email)
    usr = usr_query.first()
    newBalance =usr.balance - float(fee)
    if newBalance < 0:
        return make_response(jsonify({"status":"fail","message":"Not enough balance"}))
    usr_query.update(dict(balance=newBalance))
    mysql_db.session.commit()



    return make_response(jsonify({"status":"success","studetn_id":stdId,"amount":fee}))



def checkOTP(input_OTP):
    if current_user.username+"_OTP" in session:
        if input_OTP == session[current_user.username+"_OTP"]:
            return "correct"
        else:
            return "incorrect"
    else:
        return "miss_otp"

