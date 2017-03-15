#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from main.models import db

"""
管理员数据模型
"""


class Administrator(db.Model):

    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8mb4'
    }

    admin_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    admin_name = db.Column(
        db.String(20),
        unique=True,
        nullable=False)
    admin_passwd = db.Column(db.String(20), unique=True, nullable=False)

    def __init__(self, admin_name, admin_passwd):
        self.admin_name = admin_name
        self.admin_passwd = admin_passwd

    def __repr__(self):
        return '<admin_name %r>' % self.admin_name

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def update(self):
        db.session.commit()
        return self
