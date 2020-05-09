import os
import logging

from flask import Flask
from logging.handlers import RotatingFileHandler
from . import env

app_env = env.detect_environment()

# configure some details of the flask app object
app = Flask(__name__)
app.config['DEBUG'] = app_env.debug
app.config['SECRET_KEY'] = app_env.secret_key

# set logging format
formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# configure logging to a rotating files in ../data/logs
handler = RotatingFileHandler(app_env.logs_filename, maxBytes=100000, backupCount=1)
handler.setFormatter(formatter)
handler.setLevel(logging.DEBUG)
app.logger.addHandler(handler)

from covid import routes


