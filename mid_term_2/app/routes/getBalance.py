from app.models import User,Student,Role, Bank_Account
import flask
from app import app
from flask import json, render_template, request, session, Response,jsonify,redirect,url_for,flash,make_response

@app.route("/balance",methods=['POST'])
def getAccountBalance():
    stId = request.args.get('stId')
    get_bln = Bank_Account.query.filter_by(Bank_Account.student_id == stId).first()
    bln = get_bln.balance
    return make_response(jsonify({"balance": bln}))