from flask import Request, request, render_template, send_file, redirect, url_for, flash, send_from_directory, flash
from werkzeug.utils import secure_filename

from covid import app
#from oildb import app, bcrypt, mail, dao
#from oildb.models import User, Analyzer, DataMeasurement, XrfData, ViscosityData, db, Asset, Email, Recipient, Version, XrfDataView
#from oildb.forms import RegistrationForm, LoginForm, UpdateAccountForm, RequestResetPasswordForm, ResetPasswordForm
#from oildb.dtos import XrfElementSet
#from oildb.domain import *

from flask_login import login_user, current_user, logout_user, login_required, fresh_login_required
from flask_mail import Message

import time
import json
import glob
import os
import csv
from datetime import datetime
import re
import base64

@app.route('/home')
def home():
    generate_graph()
    return render_template('index.html')


@app.route('/')
def index():
    return render_template('index.html')

