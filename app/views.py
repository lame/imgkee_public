from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm
from forms import LoginForm, CreateAcctForm
from models import User, ROLE_USER, ROLE_ADMIN
import binascii, hashlib, urllib, cStringIO

@app.route('/')
@app.route('/index')
@login_required
def index():
	return render_template ('index.html')

@app.route('/register' , methods=['GET','POST'])
def register():
	# # form = CreateAcctForm()
	# if request.method == 'POST':
	# 	user = User()
	# #	user.username = 
		return render_template('register.html')
	# user = User(request.form['username'] , request.form['password'],request.form['email'])
	# db.session.add(user)
	# db.session.commit()
	# flash('User successfully registered')
	# return redirect(url_for('login'))
 
@app.route("/login", methods=["GET", "POST"])
def login():
	if g.user is not None and g.user.is_authenticated():
		return redirect(url_for('index'))
	form = LoginForm()
	if form.validate_on_submit():
	# login and validate the user...
		user = User()
		db.session.add(user)
		db.session.commit()		
	remember_me = False
	if 'remember_me' in session:
		remember_me = session['remember_me']
		session.pop('remember_me', None)
	# login_user(user, remember = remember_me)
	flash("Logged in successfully.")
	# return redirect(url_for('index'))
	return render_template("login.html", form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index')) 

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')

@app.before_request
def before_request():
    g.user = current_user

@lm.user_loader
def load_user(id):
    return User.get(int(id))

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