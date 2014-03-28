import os
from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager, current_user
from config import basedir

app = Flask(__name__)

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

app.config.from_object('config')

db = SQLAlchemy(app)


from app import views, models
