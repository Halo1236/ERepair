#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import render_template,request,abort,jsonify

from main import app


@app.route('/',methods = ['GET','POST'])
def index():
	if request.method == 'POST':
		stu_name = request.form.get('stu_name','')
		stu_id = request.form.get('stu_id','')
		tel_number = request.form.get('tel_number','')
		brand = request.form.get('brand','')
		problem = request.form.get('problem','')
		remark = request.form.get('remark','')
		#set_wo(stu_id,stu_name,tel_number,brand,problem,remark)
		return jsonify({'errmsg': 'ok' })
	elif request.method == 'GET':
		return render_template('index.html',page_title = u'E修哥工单系统',
		                                    page_info = u'详细填写信息')
	else:
		abort(404)
	
@app.route('/login',methods = ['GET'])
def log_in():
	return render_template('auth.html',page_title = u'E修哥工单系统',
		                               page_info = u'请填写学号和姓名')

# @app.route('/<stu_id>/result',methods = ['GET'])
# def wo_result(stu_id=None):
# 	if is_wo_exists(stu_id):
# 		return jsonify({'errmsg': 'ok'})
# 	else:
# 		return jsonify({'errmsg': '提交工单失败'})


@app.route('/login')
def login():
	return render_template('login.html')

@app.errorhandler(404)
def page_not_found(error):
	app.logger.error('404', (error))
	return "page not found!", 404


@app.errorhandler(Exception)
def unhandled_exception(error):
	app.logger.error('Unhandled Exception: %s', (error))
	return "Error", 500