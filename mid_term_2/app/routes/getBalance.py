from app.models import User,Student,Role, Bank_Account
import flask
from app import app
from flask import json, render_template, request, session, Response,jsonify,redirect,url_for,flash,make_response

@app.route('/balance/<emails>',methods=['GET','POST'])
def getAccountBalance(emails):
    get_bln = User.User.query.filter(User.User.email == emails).first()
    bln = get_bln.balance
    return make_response(jsonify({"balance": bln}))