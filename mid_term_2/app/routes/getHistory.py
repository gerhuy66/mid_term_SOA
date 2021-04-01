from app.models import His
import flask
from app import app
from flask import json, render_template, request, session, Response,jsonify,redirect,url_for,flash,make_response
from flask_login import login_required,login_user,logout_user,current_user
from app.models import Student,User
@app.route('/history/<student_id>',methods=['GET','POST'])
def getHistory(student_id):
    get_his = His.His.query.filter(His.His.studentId == student_id).all()
    his_schema = His.HisSchema(many=True)
    his = his_schema.dump(get_his)
    return make_response(jsonify({"History": his}))


from app.models import His
@app.route("/history")
@login_required
def history():

    return render_template("history.html")


@app.route("/getHistory",methods=['POST'])
@login_required
def gethis():
    # stu = Student.Student.query.filter_by(email=current_user.email).first()
    his_query = His.His.query.filter_by(payment_user=current_user.email)
    his_schema = His.HisSchema(many=True)
    his_data = his_schema.dump(his_query)
    return make_response(jsonify({"his":his_data}))

@app.route("/checkPayment/<paymentId>",methods=['GET'])
def checkPayment(paymentId):
    check_count = His.His.query.filter_by(payment_id=paymentId).count()
    if check_count == 0:
        return make_response(jsonify({"status":"200","paymentId":paymentId,"paymentStatus":"unpaid"}))
    else:
        return make_response(jsonify({"status":"200","paymentId":paymentId,"paymentStatus":"paid"}))
    
