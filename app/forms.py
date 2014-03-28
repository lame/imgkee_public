from flask.ext.wtf import Form, fields, validators
from flask.ext.wtf import Required, Email, ValidationError, Length
from wtforms import TextField, BooleanField, TextAreaField
from models import User
# from wtforms.validators import Required, Length

class LoginForm(Form):
	username = fields.TextField('username', validators = [Required()])
	password = fields.PasswordField(validators=[Required()])
	remember_me = fields.BooleanField('remember_me', default = False)
	uniq = fields.BooleanField('uniq', default = False)

	def get_user(self):
		return db.session.query(User).filter_by(name=self.name.data).first()

class CreateAcctForm(Form):
	email = fields.TextField('email', validators = [Required()])
	username = fields.TextField('username', validators = [Required()])
	password1 = fields.TextField('password', validators = [Required()])
	password2 = fields.TextField('password', validators = [Required()])

	def validate(self):
		if not Form.validate(self):
			return False
		if self.username.data == self.original_username:
			return True
		user = User.query.filter_by(username = self.username.data).first()
		if user != None:
			self.username.errors.append('This email is already in use. Please choose another one.')
			return False
		return True
