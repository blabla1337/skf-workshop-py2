# -*- coding: utf-8 -*-
__version__ = '0.1'
from flask import Flask
import getpass

app = Flask('project')
app.config['SECRET_KEY'] = 'random'
app.config['username'] = getpass.getuser()
app.debug = True
from project.controllers import *
