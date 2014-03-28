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
    username = db.Column(db.String(20), unique=True , index=True)
    password = db.Column(db.String(20))
    email = db.Column(db.String(50),unique=True , index=True)
    registered_on = db.Column(db.DateTime)

    db = db.relationship('Database', backref='user', lazy='dynamic')
 
    def __init__(self , username = None ,password = None , email = None):
        self.username = username
        self.password = password
        self.email = email
        self.registered_on = datetime.utcnow()

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % (self.username)


class Database(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    username = db.Column(db.String(255), unique = True)

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '%r' % (self.username)
