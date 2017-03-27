#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime

from main.models import db

"""
工单数据模型
"""


class Wo(db.Model):

    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8mb4'
    }

    '''
	id: 记录编号
	stu_id: 学号
	stu_name: 姓名
	tel_number: 手机号码
	brand: 电脑品牌
	ishandle: 是否处理（0未处理，1已处理）
	problem: 问题
	scheduled: 预约时间
	sn码
	admin_id: 维修人员编号
	evaluation: 维修评价(1-5分)
	remark: 备注
	regtime: 提交时间
	'''
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    stu_id = db.Column(db.String(20), nullable=False)
    stu_name = db.Column(db.String(20), nullable=False)
    tel_number = db.Column(db.String(20), nullable=False)
    brand = db.Column(db.String(20), nullable=False)
    ishandle = db.Column(db.Integer, default=0, nullable=False)
    problem = db.Column(db.String(20), nullable=False)
    scheduled = db.Column(db.String(20), nullable=False)
    admin_id = db.Column(db.String(20), nullable=True)
    sn = db.Column(db.String(20), nullable=True)
    evaluation = db.Column(db.Integer, default=0, nullable=False)
    remark = db.Column(db.String(200), nullable=True)
    regtime = db.Column(db.DateTime, default=datetime.now, nullable=False)

    def __init__(
            self,
            stu_id,
            stu_name,
            tel_number,
            problem,
            brand,
            scheduled,
            remark):
        self.stu_id = stu_id
        self.stu_name = stu_name
        self.tel_number = tel_number
        self.remark = remark
        self.problem = problem
        self.brand = brand
        self.scheduled = scheduled

    def __repr__(self):
        return '<stu_id %r>' % self.stu_id

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return self

    def update(self):
        db.session.commit()
        return self
