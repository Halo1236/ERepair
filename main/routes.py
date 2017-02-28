#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import render_template
from main import app

@app.route('/')
def index():
	return render_template('index.html')

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