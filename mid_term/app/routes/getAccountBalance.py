from app import app
from app.services import service
from flask import Flask, json, render_template, request, session, Response ,jsonify 
from app.database import db
app = Flask(__name__)

@app.route("/balance",methods=['POST'])
def getAccountBalance():
    stId = request.args['stId']
    balance = service.getBalance
    rs = balance(db.mysql, stId)
    return jsontify(rs)
    