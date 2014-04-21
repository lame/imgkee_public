from flask.ext.wtf import Form, fields, validators
from flask.ext.wtf import Required, Email, ValidationError
from flask.ext.wtf.file import FileField,FileRequired, FileAllowed
from models import User
from app import db

def validate_login(form, field):
    user = form.get_user()
    
    if user is None:
        raise validators.ValidationError('Invalid user')

    # if user.consent is False:
    #     raise validators.ValidationError('Registration cannot be completed withouth consent')
    print get_pass(form)
    if user.password != get_pass(form):
        raise validators.ValidationError('Invalid password')

class LoginForm(Form):
    name = fields.TextField(validators=[Required()])
    img = fields.FileField('password')
    #password = fields.PasswordField(validators=[Required(), validate_login])

    def get_user(self):
        return db.session.query(User).filter_by(name=self.name.data).first()

    def get_pass(self):
        return db.session.query(User).filter_by(password=self.password.data).first()

class RegistrationForm(Form):
    name = fields.TextField('Username', validators=[Required()])
    img = fields.FileField('password', validators=[Required(), validate_login])

    
    # email = fields.TextField(validators=[Email(), Required()])
    #password = fields.PasswordField('New Password', [
    #    validators.Required(),
    #    validators.EqualTo('confirm', message='Passwords must match')
    #])
    #confirm = fields.PasswordField(validators=[Required()])
    #uniq = fields.BooleanField()


    def validate_name(self, field):
        if db.session.query(User).filter_by(name=self.name.data).count() > 0:
            raise validators.ValidationError('Duplicate name')

    def validate_email(self, field):
        if db.session.query(User).filter_by(email=self.email.data).count() > 0:
            raise validators.ValidationError('Duplicate email')