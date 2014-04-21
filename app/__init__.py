from flask import Flask
from flask.ext.assets import Environment, Bundle
from flask_oauthlib.client import OAuth
from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from flask.ext.mail import Mail
from config import basedir
import os

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

UPLOAD_FOLDER = 'butts'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'jpeg', 'gif'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

app.config.from_object('config')

db = SQLAlchemy(app)


from app import views, models
