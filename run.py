#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from main import app

if __name__ == "__main__":
    app.debug = app.config['DEBUG']
    app.run(host = '0.0.0.0', port = 8083, threaded = True)