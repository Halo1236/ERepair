#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymysql
from flask_sqlalchemy import SQLAlchemy

from main import app

pymysql.install_as_MySQLdb()

db = SQLAlchemy(app)

from main.models.administrator import Administrator
from main.models.wo import Wo
from main.models.user import User

def get_wo_all(stu_id):
    wo_info = Wo.query.filter_by(stu_id=stu_id).all()
    if not wo_info:
        return None
    else:
        return wo_info

def set_wo_info(stu_id, tel_number, brand, problem, scheduled, remark):
    wo_mod = Wo(stu_id=stu_id,
                tel_number=tel_number,
                brand=brand,
                remark=remark,
                problem=problem,
                scheduled=scheduled)
    wo_mod.save()
    
def set_user_info(stu_id, stu_name):
    if not is_user_exists(stu_id, stu_name):
        user_mod = User(stu_id=stu_id, stu_name=stu_name)
        user_mod.save()
        return True
    return False


def is_wo_exists(stu_id):
    wo_info = Wo.query.filter_by(stu_id=stu_id).first()
    if not wo_info:
        return False
    else:
        return True


def is_admin_exists(admin_form):
    admin_info = Administrator.query.filter_by(
        admin_name=admin_form['admin_name']).first()
    if not admin_info:
        return False
    else:
        if admin_info['admin_passwd'] == admin_form['admin_passwd']:
            return True
        else:
            return False


def is_user_exists(stu_id, stu_name):
    if not (User.query.filter_by(
            stu_id=stu_id).first() or User.query.filter_by(
            stu_name=stu_name).first()):
        return False
    else:
        return True
