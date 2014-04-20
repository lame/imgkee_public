from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm, ALLOWED_EXTENSIONS, html_theme, html_theme_path
from werkzeug.wsgi import SharedDataMiddleware
from forms import LoginForm, RegistrationForm
from models import User, ROLE_USER, ROLE_ADMIN
import binascii, hashlib, urllib, cStringIO

UPLOAD_FOLDER = 'butts'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

@app.route('/create_acct/' , methods=['GET','POST'])
def create_acct():
	form = RegistrationForm(request.form)
	upload_file()
	if form.validate_on_submit():
		print form
		user = User()
		form.populate_obj(user)
		db.session.add(user)
		db.session.commit()
		login_user(user)
		return redirect(url_for('index'))
	return render_template('register.html', title = "Create Account", form=form)

@app.route('/login/',methods=['GET', 'POST'])
def login():
	form = LoginForm(request.form)
	if form.validate_on_submit():
		print "this is happening"
		user = form.get_user()
		login_user(user)
		flash("Logged in successfully.")
		return redirect(request.args.get("next") or url_for("index"))
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
