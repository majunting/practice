from flask import render_template, flash, redirect, url_for
from flask import request
from flask_login import current_user, login_user
from flask_login import login_required

from app.models import User
from app import app
from app.forms import LoginForm

from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index')
@login_required
def index():
	user = {'username': 'user1'}
	posts = [
		{
			'author': {'username': 'user2'},
			'body': 'Post 1'
		},
		{
			'author': {'username': 'user3'},
			'body': 'Post2'
		}
	]
	return render_template('index.html', title = 'home', posts = posts)
# 	return '''
# <html>
#     <head>
#         <title>Home Page - Microblog</title>
#     </head>
#     <body>
#         <h1>Hello, ''' + user['username'] + '''!</h1>
#     </body>
# </html>'''

@app.route('/login', methods = ['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username = form.username.data).first()
		if user is None or not user.check_password(form.password.data):
			flask('Invalid username or password')
			return redirect(url_for('login'))
		login_user(user, remember = form.remember_me.data)
		next_page = request.args.get('next')
		if not next_page or url_pase(next_page).netloc != '':
			next_page = url_for('index')
		# flash('Login requested for user {}, remember_me = {}'.format(
		# 	form.username.data, form.remember_me.data))
		return redirect(next_page)
	return render_template('login.html', title = 'Sign In', form = form)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))