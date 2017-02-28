 #!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy
from main import app
import time
import pymysql
pymysql.install_as_MySQLdb()

from .administrator import Administrator
from  .wo import Wo

db = SQLAlchemy(app)


def set_wo_info(wo_info):
	wo = Wo(stu_name = wo_info['stu_name'],
		    stu_id = wo_info['stu_id'],
		    tel_number = wo_info['tel_number'],
		    ishandle = wo_info['ishandle'],
		    remark = wo_info['remark'],
		    problem_num =wo_info['problem_num'])
	wo.save()
	
def is_wo_exists(stu_id):
	wo_info = Wo.query.filter_by(stu_id = stu_id).first()
	if not  wo_info:
		return False
	else:
		return True

def is_admin_exists(admin_form):
	admin_info = Administrator.query.filter_by(admin_name = admin_form['admin_name']).first()
	if not admin_info:
		return False
	else:
		if admin_info['admin_passwd'] == admin_form['admin_passwd']:
			return True
		else:
			return False
		
		
		
		
		