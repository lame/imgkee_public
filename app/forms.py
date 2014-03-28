from flask.ext.wtf import Form, fields, validators
from flask.ext.wtf import Required, Email, ValidationError, Length
from wtforms import TextField, BooleanField, TextAreaField
from models import User
# from wtforms.validators import Required, Length

def validate_login(form, field):
	user = form.get_user()

	if user is None:
		raise validators.ValidationError('Invalid user')

	if user.password != form.password.data:
		raise validators.ValidationError('Invalid password')

class LoginForm(Form):
	username = fields.TextField(validators = [Required()])
	password = fields.PasswordField(validators=[Required()])
	remember_me = fields.BooleanField(default = False)
	uniq = fields.BooleanField(default = False)

	def get_user(self):
		return db.session.query(User).filter_by(name=self.name.data).first()

class RegistrationForm(Form):
	email = fields.TextField(validators = [Required()])
	username = fields.TextField(validators = [Email()])
	password = fields.PasswordField('New Password', [ validators.Required(), validators.EqualTo('confirm', message='Passwords must match') ])
	confirm = fields.PasswordField(validators=[Required()])

	def validate_name(self, field):
		if db.session.query(User).filter_by(name=self.name.data).count() > 0:
			raise validators.ValidationError('Duplicate name')

	def validate_email(self, field):
		if db.session.query(User).filter_by(email=self.email.data).count() > 0:
			raise validators.ValidationError('Duplicate email')	