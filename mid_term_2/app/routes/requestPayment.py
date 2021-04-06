from app.models import User,Student,Role, Bank_Account, His
import flask
from app import app
from flask import json, render_template, request, session, Response,jsonify,redirect,url_for,flash,make_response
from app.database import mysql_db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date

@app.route('/requestpayment',methods=['GET','POST'])
def requestpayment():
    totalcost = request.json['totalcost']
    status = request.json['status']
    orderDatetime = request.json['orderDatetime']
    paymentUser = request.json['paymentUser']
    password = request.json['password']

    puser_email = User.User.query.filter(User.User.email == paymentUser)
    puser = puser_email.first()

    if puser is not None and check_password_hash(puser.password_hash, password):
        bauser = puser.balance
        new_balance = bauser - totalcost

        dateStr = date.today().strftime("%d/%m/%Y")
        payid = 'pm' + orderDatetime
        his = His.His(paymentUser, dateStr, paymentUser, payid, totalcost)
        mysql_db.session.add(his)

        if new_balance < 0:
            return make_response(jsonify({"status":"fail","message":"Not enough balance"}))

        puser_email.update(dict(balance=new_balance))
        mysql_db.session.commit()

        return make_response(jsonify({"paymentUser": paymentUser , "orderDatetime" : orderDatetime, "status" : "paid", "totalcost" : totalcost, "message" : "payment success"}))

    return make_response(jsonify({"status":"fail","message":"Username or Password invalid"}))
    
   