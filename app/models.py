from app import db
# from flask.ext.admin.contrib.sqla import ModelView
from mixins import CRUDMixin
from flask.ext.login import UserMixin
from flask.ext.sqlalchemy import SQLAlchemy
from datetime import datetime

ROLE_USER = 0
ROLE_ADMIN = 1

class User(UserMixin, CRUDMixin, db.Model):
    id = db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String(20), unique=True , index=True)
    password = db.Column(db.String(200000))
    # email = db.Column(db.String(50),unique=True , index=True)
    # registered_on = db.Column(db.DateTime)

    role = db.Column(db.SmallInteger, default = ROLE_USER)
    db = db.relationship('Database', backref='user', lazy='dynamic')
 
    def __init__(self, name=None, password=None):
        self.name = name
        # self.email = email
        self.password = password

    def is_active(self):
        return True

    def get_id(self):
        return unicode(self.id)

    def is_admin(self):
        if self.role > 0:
            return True
        else:
            return False

    def __repr__(self):
        return '<User %r>' % (self.nickname)

class Database(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(255), unique = True)

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '%r' % (self.name)
