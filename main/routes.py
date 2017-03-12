#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import render_template,request,abort,jsonify,session,redirect,url_for

from main.models import *


@app.route('/',methods = ['GET','POST'])
def index():
	if request.method == 'POST':
		tel_number = request.form.get('tel_number','')
		brand = request.form.get('brand','')
		problem = request.form.get('problem','')
		remark = request.form.get('remark','')
		print(tel_number,brand)
		#set_wo(stu_id,stu_name,tel_number,brand,problem,remark)
		return jsonify({'errmsg': 'ok' })
	elif request.method == 'GET':
		return render_template('index.html',page_title = u'E修哥工单系统',
		                                    page_info = u'详细填写信息')
	else:
		abort(404)

@app.route('/login',methods = ['GET','POST'])
def log_in():
	if request.method == 'POST':
		stu_id = request.form.get('userid','')
		stu_name = request.form.get('username','')
		session['userid'] = stu_id
		session['username'] = stu_name
		if stu_id and stu_name:
			set_user_info(stu_id,stu_name)
			errmsg = 'ok'
		else:
			errmsg = u'学号或者姓名格式不合法'
		return jsonify({'errmsg':errmsg})
	elif request.method == 'GET':
		return render_template('auth.html',page_title = u'E修哥工单系统',
		                               page_info = u'请填写学号和姓名')
	else:
		abort(404)

@app.route('/<stu_id>/result',methods = ['GET'])
def wo_result(stu_id=None):
	if is_wo_exists(stu_id):
		return jsonify({'errmsg': 'ok'})
	else:
		return jsonify({'errmsg': '提交工单失败'})


@app.route('/login/result',methods = ['POST'])
def check_login():
	stu_id = session.get('userid')
	stu_name = session.get('username')
	if stu_id and stu_name:
		if is_user_exists(stu_id):
			return render_template('index.html',page_title = u'填写维修工单',
			                                    page_info = u'请保证信息的正确性，不要留空')
		else:
			abort(404)
	else:
		return redirect(url_for('login'))
		

@app.errorhandler(404)
def page_not_found(error):
	app.logger.error('404', (error))
	return "page not found!", 404


@app.errorhandler(Exception)
def unhandled_exception(error):
	app.logger.error('Unhandled Exception: %s', (error))
	return "Error", 500