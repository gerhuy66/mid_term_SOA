from app.models import His
import flask
from app import app
from flask import json, render_template, request, session, Response,jsonify,redirect,url_for,flash,make_response

@app.route('/history/<student_id>',methods=['GET','POST'])
def getHistory(student_id):
    get_his = His.His.query.filter(His.His.studentId == student_id).all()
    his_schema = His.HisSchema(many=True)
    his = his_schema.dump(get_his)
    return make_response(jsonify({"History": his}))