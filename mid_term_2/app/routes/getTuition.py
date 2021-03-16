import flask
from app import app
from flask import json, render_template, request, session, Response,jsonify,redirect,url_for,flash,make_response
from flask_login import login_required,login_user,logout_user,current_user
from app.models import User,Student
from app.forms import forms

@app.route('/getTuition/<studentId>', methods=['GET', 'POST'])
def getTuition(studentId):
    student = Student.Student.query.filter_by(studentId = studentId)
    student_schema = Student.StudentSchema(many=True)
    students = student_schema.dump(student)
    return make_response(jsonify({"student_fee": students[0]["fee"]}))
    

