#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from flask import render_template, request, abort, jsonify, session, redirect, url_for, send_from_directory

from main.models import *



@app.route('/admin/index', methods=['GET', 'POST'])
@app.route('/admin/index/<handle>', methods=['GET', 'POST'])
def admin_index(handle=None):
    admin_name = session.get('admin_name', None)
    admin_passwd = session.get('admin_passwd', None)
    stu_id = request.args.get('stu_id', None)
    if request.method == 'GET':
        if admin_name and admin_passwd:
            if handle == 'ishandle':
                content = get_wo_all_by_ishandle(1)
            elif handle == 'nothandle':
                content = get_wo_all_by_ishandle(0)
            elif stu_id:
                content = get_wo_all_by_stuid(stu_id)
            else:
                content = get_wo_all()
            return render_template('admin_index.html', content=content)
        else:
            session.pop('admin_name', None)
            session.pop('admin_passwd', None)
            return redirect(url_for('admin_login'))
    else:
        id = request.form.get('id', '')
        wo_sn = request.form.get('wo_sn', '')
        admin_remark = request.form.get('admin_remark', '')
        print(id, wo_sn, admin_remark)
        if wo_sn and admin_remark and wo_sn and admin_name:
            if update_wo_by_id(id, wo_sn, admin_remark, admin_name):
                errmsg = 'ok'
            else:
                errmsg = '存储发送错误'
        else:
            errmsg = 'err_login'
        return jsonify({'errmsg': errmsg})


@app.route('/', methods=['GET', 'POST'])
def log_in():
    if request.method == 'POST':
        stu_id = request.form.get('userid', None)
        stu_name = request.form.get('username', None)
        session['userid'] = stu_id
        session['username'] = stu_name
        if set_user_info(stu_id, stu_name):
            errmsg = 'ok'
        else:
            errmsg = u'学号或者姓名格式不合法'
        return jsonify({'errmsg': errmsg})
    elif request.method == 'GET':
        return render_template('auth.html', page_title=u'E修哥工单系统',
                               page_info=u'请填写学号和姓名')
    else:
        abort(404)


@app.route('/index', methods=['GET'])
def check_login():
    stu_id = session.get('userid')
    stu_name = session.get('username')
    print(stu_id, stu_name)
    if stu_id and stu_name:
        if is_user_exists(stu_id, stu_name):
            return render_template('index.html', page_title=u'填写维修工单')
        else:
            abort(404)
    else:
        return redirect(url_for('log_out'))


@app.route('/index/result', methods=['POST'])
def index():
    if request.method == 'POST':
        stu_id = session.get('userid')
        stu_name = session.get('username')
        tel_number = request.form.get('tel_number', None)
        brand = request.form.get('brand', None)
        problem = request.form.get('problem', None)
        scheduled = request.form.get('scheduled', None)
        remark = request.form.get('remark', None)
        print(tel_number, brand, problem, scheduled, remark)
        if stu_id and stu_name and tel_number and brand and problem and scheduled and remark:
            set_wo_info(
                stu_id,
                stu_name,
                tel_number,
                brand,
                problem,
                scheduled,
                remark)
            errmsg = 'ok'
        else:
            errmsg = '数据存储发生错误'
        return jsonify({'errmsg': errmsg})
    else:
        abort(404)


@app.route('/index/succeed', methods=['GET', 'POST'])
def msg():
    return render_template('succeed.html')


@app.route('/index/history', methods=['GET', 'POST'])
def history():
    stu_id = session.get('userid')
    stu_name = session.get('username')
    if request.method == 'GET':
        if stu_id and stu_name:
            content = get_wo_all_by_stuid(stu_id)
            return render_template(
                'history.html',
                page_title='历史工单',
                page_info=stu_name + ',同学你好!',
                content=content)
        else:
            return redirect(url_for('log_out'))
    else:
        wo_id = request.form.get('wo_id', None)
        wo_ishandle = request.form.get('wo_ishandle', None)
        wo_evaluation = request.form.get('wo_evaluation', None)
        print(wo_id, wo_ishandle, wo_evaluation)
        if stu_name and stu_id:
            if wo_ishandle:
                if update_wo_handle(wo_id, wo_ishandle):
                    errmsg = 'ok'
                else:
                    errmsg = '存储发生错误'
            if wo_evaluation:
                if update_wo_evaluation(wo_id, wo_evaluation):
                    errmsg = 'ok'
                else:
                    errmsg = '存储发生错误'
        else:
            errmsg = 'err_login'
        return jsonify({'errmsg': errmsg})


@app.route('/logout', methods=['GET'])
def log_out():
    session.pop('userid', None)
    session.pop('username', None)
    return redirect(url_for('log_in'))


@app.route('/root.txt')
def robotstxt():
    return send_from_directory(app.static_folder, 'root.txt')


@app.errorhandler(404)
def page_not_found(error):
    app.logger.error('404', (error))
    return "page not found!", 404


@app.errorhandler(Exception)
def unhandled_exception(error):
    app.logger.error('Unhandled Exception:%s', (error))
    return "Error", 500
