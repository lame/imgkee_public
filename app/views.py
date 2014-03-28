from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm
from forms import LoginForm, RegistrationForm
from models import User, ROLE_USER, ROLE_ADMIN
import binascii, hashlib, urllib, cStringIO

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/')
@app.route('/index')
@login_required
def index():
	return render_template ('index.html', title = 'Home')

@app.route('/register' , methods=['GET','POST'])
def register():
	form = RegistrationForm(request.form)
	if form.validate_on_submit():
		print form;
		user = User()
		form.populate_obj(user)
		db.session.add(user)
		db.session.commit()
		login_user(user)
		return redirect(url_for('register.html'))
	return render_template('register.html', form = form, title = 'Register')
 
@app.route("/login", methods=["GET", "POST"])
def login():
	form = LoginForm(request.form)
	if form.validate_on_submit():
		user = form.get_user()
		login_user(user)
		flash("Logged in successfully.")
		return redirect(request.args.get("next") or url_for("index"))
	return render_template('login.html', form=form, title = 'Login')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index')) 

@app.route('/about')
def about():
	return render_template('about.html', title = 'About')

@app.route('/contact')
def contact():
	return render_template('contact.html', title = 'Contact')

@app.before_request
def before_request():
    g.user = current_user

# Read from a link
	# file = cStringIO.StringIO(urllib.urlopen(URL).read())
	# img = Image.open(file)

def dump():
	ff = open("cat.png", "rb")
	data = ff.read()
	ff.close()

	txt = binascii.hexlify(data)

	fw = open("cat.txt", "wb")
	fw.write(txt)
	fw.close()

def hash():
	ff = open("cat.txt", "rb")
	txt = ff.read()

	m = hashlib.sha512()
	m.update(txt)
	key = m.digest()

	print(key)