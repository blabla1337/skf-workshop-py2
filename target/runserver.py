#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from project import app
from flask_cors import CORS

if __name__ == '__main__':
    cors = CORS(app, resources={r"/*": {"origins": "*"}})
    app.run(host='0.0.0.0')


