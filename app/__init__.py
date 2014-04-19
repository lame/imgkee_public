from flask import Flask
from flask.ext.assets import Environment, Bundle
from flask_oauthlib.client import OAuth
from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from flask.ext.mail import Mail
from config import basedir
import sphinx_rtd_theme
import os

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif', 'bmp'])

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

app.config.from_object('config')

db = SQLAlchemy(app)


from app import views, models
