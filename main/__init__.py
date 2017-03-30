#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import logging
from logging.handlers import RotatingFileHandler

from flask import Flask

app = Flask(__name__, instance_relative_config=True)
# 加载配置
# app.config.from_object('config')
app.config.from_pyfile('config.py')
app.secret_key = app.config['SECRET_KEY']

# 记录日志
handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=1)
handler.setFormatter(
    logging.Formatter(
        datefmt='%Y-%m-%d %H:%M:%S',
        fmt='%(color)s[%(levelname)1.1s '
        '%(asctime)s %(module)s:%(lineno)d]%(end_color)s %(message)s'))

handler.setLevel(logging.WARNING)
app.logger.addHandler(handler)

from main import routes
