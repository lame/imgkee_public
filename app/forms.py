from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, TextAreaField
from wtforms.validators import Required, Length

class LoginForm(Form):
	username = TextField('username', validators = [Required()])
	password = TextField('password', validators = [Required()])
	# openid = TextField('openid', validators = [Required()])
	# remember_me = BooleanField('remember_me', default = False)

class CreateAcctForm(Form):
	username = TextField('username', validators = [Required()])
	password = TextField('password', validators = [Required()])

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
