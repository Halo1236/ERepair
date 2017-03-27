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


def get_wo_all_by(stu_id):
    wo_info = Wo.query.filter_by(stu_id=stu_id).all()
    if not wo_info:
        return None
    else:
        return wo_info


def update_wo_handle(wo_id, wo_ishandle):
    wo_info = Wo.query.filter_by(id=wo_id).first()
    if not wo_info:
        return False
    else:
        wo_info.ishandle = wo_ishandle
        wo_info.update()
        return True


def update_wo_evaluation(wo_id, wo_evaluation):
    wo_info = Wo.query.filter_by(id=wo_id).first()
    if not wo_info:
        return False
    else:
        wo_info.evaluation = wo_evaluation
        wo_info.update()
        return True


def get_wo_all():
    wo_info = Wo.query.all()
    if not wo_info:
        return None
    else:
        return wo_info


def set_wo_info(
        stu_id,
        stu_name,
        tel_number,
        brand,
        problem,
        scheduled,
        remark):
    wo_mod = Wo(stu_id=stu_id,
                stu_name=stu_name,
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


def set_admin_info(admin_name, admin_passwd):
    admin_mod = Administrator(admin_name=admin_name, admin_passwd=admin_passwd)
    admin_mod.save()


def is_wo_exists(stu_id):
    wo_info = Wo.query.filter_by(stu_id=stu_id).first()
    if not wo_info:
        return False
    else:
        return True


def is_admin_exists(admin_name, admin_passwd):
    admin_info = Administrator.query.filter_by(
        admin_name=admin_name, admin_passwd=admin_passwd).first()
    if not admin_info:
        return False
    else:
        return True


def is_user_exists(stu_id, stu_name):
    if not (User.query.filter_by(
            stu_id=stu_id).first() or User.query.filter_by(
            stu_name=stu_name).first()):
        return False
    else:
        return True
