#！/usr/bin/env python3
#-*- coding: utf-8 -*-

from main.models import db

"""
用户数据模型
"""


class User(db.Model):
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8mb4'
    }

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    stu_id = db.Column(
        db.String(20),
        unique=True,
        nullable=False)
    stu_name = db.Column(db.String(20), unique=True, nullable=False)

    def __init__(self, stu_id, stu_name):
        self.stu_id = stu_id
        self.stu_name = stu_name

    def __repr__(self):
        return '<id %r>' % self.id

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def update(self):
        db.session.commit()
        return self
