from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm, ALLOWED_EXTENSIONS
from werkzeug.wsgi import SharedDataMiddleware
from forms import LoginForm, RegistrationForm
from models import User, ROLE_USER, ROLE_ADMIN
from werkzeug import secure_filename
import binascii, hashlib, urllib, cStringIO, os


@app.route('/create_acct/' , methods=['GET','POST'])
def create_acct():
	form = RegistrationForm(request.form)
	file = 0
	if form.validate_on_submit():
		print form
		file = request.files['img']
        if file and allowed_file(file.filename):
        	filename = secure_filename(file.filename)
        	file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        	mess = dump(file.filename)
        	hash_pass = hashify(mess)
		user = User()
		user.password = hash_pass
		form.populate_obj(user)
		db.session.add(user)
		db.session.commit()
		login_user(user)
		return redirect(url_for('index'))
	return render_template('register.html', title = "Create Account", form=form)

@app.route('/login/',methods=['GET', 'POST'])
def login():
	form = LoginForm(request.form)
	file = 0
	if form.validate_on_submit():
		file = request.files['img']
        if file and allowed_file(file.filename):
        	filename = secure_filename(file.filename)
        	file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        	mess = dump(file.filename)
        	hash_pass = hashify(mess)
		user = form.get_user()
		user.password = hash_pass
		if db.session.query(User).filter_by(name=user.name,password=user.password).first():
			if(login_user(user)):
				flash("Logged in successfully.")
				return redirect(request.args.get("next") or url_for("index"))
		else:
				flash("fuck ou butty")
				return redirect(request.args.get("next") or url_for("about"))	

	return render_template('login.html', title = "Login", form=form)

@app.route('/forgot_passwd')
def forgot_passwd():
	user = g.user
	return render_template ("forgot_passwd.html", title="Forgot Password")

@app.route('/')
@app.route('/index')
@login_required
def index():
	user = g.user
	return render_template ("index.html",
		title = "Home", 
		user = user)

@lm.user_loader
def load_user(id):
	return User.query.get(int(id))

@app.before_request
def before_request():
	g.user = current_user

@app.route('/logout/')
def logout():
	logout_user()
	return redirect(url_for('index'))

@app.route('/about/')
def about():
	return render_template('about.html', title = 'About')

@app.route('/contact/')
def contact():
	return render_template('contact.html', title = 'Contact')

@app.errorhandler(404)
def internal_error(error):
	return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500

def upload(request):
        form = RegistrationForm(request.POST)
        if form.image.data:
        	image_data = request.FILES[form.image.name].read()
        	open(os.path.join(UPLOAD_PATH, form.image.data), 'w').write(image_data)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
def dump(filename):
	ff = open('butts/'+filename, "rb")
	data = ff.read()
	ff.close()

	txt = binascii.hexlify(data)
	return txt

def hashify(hexdump):

	hexhash = hashlib.sha512(hexdump).hexdigest()


	return hexhash
